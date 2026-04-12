# Data Model Template — MongoDB

**Document ID:** DM-MONGO-[PROJECT]-[SUBSYSTEM]-[YYYY]-[NNN]  
**Template Version:** 1.0.0  
**Related Standards:** ISO/IEC/IEEE 42010, ISO/IEC 12207:2017 §6.4.4, ISO/IEC/IEEE 29148, ISO/IEC 27001:2022, ISO/IEC 27701, PDPA

---

## Document Control

| Field                  | Value                                   |
| ---------------------- | --------------------------------------- |
| **System / Component** | [System name]                           |
| **Data Domains**       | [Domain list]                           |
| **Document Version**   | [0.1 Draft]                             |
| **Status**             | Draft / In Review / Approved / Baseline |
| **Classification**     | Internal / Confidential / Restricted    |
| **Author**             | [Name, Role]                            |
| **Data Steward**       | [Name]                                  |
| **Reviewers**          | [Security, QA, DevOps, Product]         |
| **Creation Date**      | [YYYY-MM-DD]                            |
| **Last Updated**       | [YYYY-MM-DD]                            |
| **Approved By**        | [Name, Role]                            |
| **Approval Date**      | [YYYY-MM-DD]                            |
| **Next Review Date**   | [YYYY-MM-DD]                            |
| **AI-Assisted**        | [ ] Yes — Tool: **\_\_** [ ] No         |

---

## ISO Traceability

| Clause / Control          | Addressed In | Evidence                          |
| ------------------------- | ------------ | --------------------------------- |
| ISO/IEC 12207:2017 §6.4.4 | §§3–6        | Logical & physical design         |
| ISO/IEC/IEEE 29148 §9     | §§2, 7       | Requirement ↔ data mapping       |
| ISO/IEC 27001 Annex A     | §§4, 6       | Classification, security controls |
| PDPA                      | §§4.3, 6.3   | PII handling, retention           |

---

## 1. Stakeholders & Responsibilities

| Stakeholder      | Role | Responsibilities               | RACI | Review Status |
| ---------------- | ---- | ------------------------------ | ---- | ------------- |
| Data Architect   |      | Document schema design         | R/A  |               |
| Tech Lead        |      | Service integration oversight  | C    |               |
| DevOps / DBA     |      | Cluster configuration, backups | R    |               |
| Security Officer |      | Access control review          | C    |               |
| Product Owner    |      | Data usage, consent            | I    |               |
| DPO              |      | PDPA compliance                | C    |               |

---

## 2. Requirements Traceability

| Requirement ID | Description        | Collection / Field                     | Verification    |
| -------------- | ------------------ | -------------------------------------- | --------------- |
| FR-XXX-001     | [Requirement]      | `tickets.status`, `tickets.facilityId` | API tests       |
| NFR-PERF-005   | Query < 150 ms     | `tickets` index plan                   | Profiling       |
| SEC-AUD-010    | Audit immutability | `auditEvents` TTL                      | Security review |

---

## 3. Data Domains & Business Context

| Domain    | Description                              | Owner    | Notes                      |
| --------- | ---------------------------------------- | -------- | -------------------------- |
| Ticketing | Denormalised view for analytics / search | Ops      | Sourced from relational DB |
| Audit     | Immutable event log                      | Security | Stored only in MongoDB     |
| Telemetry | High-volume events                       | DevOps   | Optional                   |

---

## 4. Logical Data Model

### 4.1 Aggregates & Relationships

| Aggregate       | Description                                       | References                  | Notes                             |
| --------------- | ------------------------------------------------- | --------------------------- | --------------------------------- |
| TicketAggregate | Ticket with embedded comments & facility snapshot | `facilityId`, `assignee.id` | Denormalised for read performance |
| AuditEvent      | Immutable change log                              | `ticketId`, `actorId`       | TTL optional                      |

### 4.2 Document Schema (JSON)

```json
{
  "_id": "ObjectId",
  "ticketId": "uuid",
  "facility": {
    "id": "uuid",
    "name": "string"
  },
  "status": "created|in_progress|resolved|closed",
  "priority": "low|medium|high|urgent",
  "assignee": {
    "id": "uuid",
    "role": "technician"
  },
  "description": "string",
  "comments": [
    {
      "commentId": "uuid",
      "authorId": "uuid",
      "body": "string",
      "visibility": "internal|external",
      "createdAt": "ISO-8601"
    }
  ],
  "attachments": [
    {
      "type": "image|file",
      "url": "string",
      "checksum": "sha256"
    }
  ],
  "createdAt": "ISO-8601",
  "updatedAt": "ISO-8601",
  "metadata": {
    "source": "api|import",
    "tags": ["string"]
  }
}
```

### 4.3 Field Dictionary

| Field             | Type          | Required | PII   | Description                  |
| ----------------- | ------------- | -------- | ----- | ---------------------------- |
| `ticketId`        | UUID          | Yes      | No    | Foreign key to relational ID |
| `facility.name`   | String        | Yes      | No    | Snapshot for quick reads     |
| `assignee`        | Object        | Optional | Yes   | Mask for unauthorised roles  |
| `comments[].body` | String        | Yes      | Maybe | Sanitize for sensitive info  |
| `metadata.tags`   | Array<String> | Optional | No    | Search filters               |

---

## 5. Physical Design — MongoDB

### 5.1 Collections & Sharding

| Collection               | Purpose                                   | Shard Key                          | TTL                      | Notes                             |
| ------------------------ | ----------------------------------------- | ---------------------------------- | ------------------------ | --------------------------------- |
| `tickets`                | Read-optimised aggregate                  | `{ facilityId: 1, createdAt: -1 }` | No                       | Consider zone sharding per region |
| `auditEvents`            | Immutable event log                       | `{ ticketId: 1, createdAt: 1 }`    | Optional via `expiresAt` | Use majority write concern        |
| `attachments` (optional) | Metadata for large files stored elsewhere | `{ ticketId: 1 }`                  | No                       | Store binary in S3/GridFS         |

### 5.2 Index Strategy

| Collection    | Index                                         | Purpose                 |
| ------------- | --------------------------------------------- | ----------------------- |
| `tickets`     | `{ ticketId: 1 }` unique                      | Sync with relational ID |
| `tickets`     | `{ facilityId: 1, status: 1, createdAt: -1 }` | Dashboard queries       |
| `tickets`     | `{ "comments.commentId": 1 }` sparse          | Locate comment quickly  |
| `auditEvents` | `{ ticketId: 1, createdAt: 1 }`               | Timeline queries        |
| `auditEvents` | TTL on `expiresAt`                            | Automated retention     |

### 5.3 Data Consistency

- Use change streams or CDC to keep MongoDB in sync with relational source.
- Ensure idempotent upserts using `ticketId`.
- For multi-document updates, use transactions or compensating logic.
- Document eventual consistency expectations for consuming services.

### 5.4 Storage & Performance

- Limit document size (<16MB). Move large arrays to child collections if necessary.
- Use schema validation (JSON Schema) to enforce structure.

```javascript
db.createCollection('tickets', {
  validator: {
    $jsonSchema: {
      bsonType: 'object',
      required: ['ticketId', 'facility', 'status', 'createdAt'],
      properties: {
        ticketId: { bsonType: 'string', pattern: '^[0-9a-fA-F-]{36}$' },
        status: { enum: ['created', 'in_progress', 'resolved', 'closed'] },
        priority: { enum: ['low', 'medium', 'high', 'urgent'] },
      },
    },
  },
});
```

- Configure WiredTiger compression (zstd) if supported.
- Monitor working set vs RAM; scale cluster or add indexes accordingly.

### 5.5 Security Controls

- Authentication: SCRAM-SHA-256 with x.509 if available.
- Authorization: Role-based (read/write separated); use least privilege.
- Network: VPC peering / IP whitelist; disable public access.
- Encryption: Enable at-rest encryption; require TLS 1.2+.
- Auditing: Enable audit events for auth and data access.

---

## 6. Security, Privacy & Compliance

### 6.1 Classification & Access

| Collection    | Classification | PII   | Access Roles                | Notes                      |
| ------------- | -------------- | ----- | --------------------------- | -------------------------- |
| `tickets`     | Confidential   | Maybe | `hq_staff`, facility scoped | Field masking for comments |
| `auditEvents` | Internal       | No    | Security, DevOps            | Immutable                  |
| `attachments` | Confidential   | Maybe | Controlled via signed URL   | Store outside DB if large  |

### 6.2 PDPA Handling

- Data export: use aggregation pipeline filtered by requester ID.
- Deletion: mark `deleted` flag + remove from search indexes; purge from Mongo within [X] days.
- Consent: store consent metadata outside aggregated doc to avoid repeated updates.

---

## 7. Data Retention & Lifecycle

| Collection    | Retention Policy       | Automation                          | Evidence         |
| ------------- | ---------------------- | ----------------------------------- | ---------------- |
| `tickets`     | 24 months post-closure | Batch job removes archive copies    | Job logs         |
| `auditEvents` | 36 months              | TTL index on `expiresAt`            | Atlas TTL report |
| `attachments` | 12 months              | Delete via storage lifecycle policy | Storage report   |

---

## 8. Migration, Versioning & Deployment

| Topic             | Approach                                                                           |
| ----------------- | ---------------------------------------------------------------------------------- |
| Versioning        | Semantic tags stored in `schemaVersions` collection                                |
| Migration Tooling | Mongock / custom scripts / Prisma (Mongo)                                          |
| Deployment        | Blue/green clusters or rolling upgrades; ensure driver compatibility               |
| Backfills         | Use bulk operations with batches + retry logic                                     |
| Rollback          | Maintain previous schema compatibility; keep old readers until migration validated |
| Change Governance | Review by Data Architect + Security for PII adjustments                            |

---

## 9. Data Quality & Testing

| Test                  | Scope                               | Tooling                | Frequency   | Owner    |
| --------------------- | ----------------------------------- | ---------------------- | ----------- | -------- |
| Schema validation     | JSON schema enforcement             | Integration tests      | CI          | Backend  |
| Consistency check     | Compare counts vs relational source | Scheduled job          | Daily       | Data Ops |
| Performance profiling | Query latency, index stats          | Atlas profiler         | Monthly     | DevOps   |
| Security audit        | Role permissions, TLS status        | Scripts / Atlas report | Quarterly   | Security |
| Backup restore        | Snapshot + restore to staging       | Atlas backup           | Semi-annual | DevOps   |

---

## 10. Operational Considerations

| Topic      | Notes                                                             |
| ---------- | ----------------------------------------------------------------- |
| Monitoring | Use Atlas / Ops Manager metrics (ops/sec, memory, connections)    |
| Alerting   | Trigger on replication lag, disk usage, slow ops, auth failures   |
| Scaling    | Enable auto-scaling or document manual process; track working set |
| Backup     | Continuous snapshots; test restore time vs RTO                    |
| Runbooks   | Change streams outage, index rebuild, region failover             |

---

## 11. Risks & Mitigations

| Risk ID        | Description                                     | Likelihood | Impact | Mitigation                         | Residual   |
| -------------- | ----------------------------------------------- | ---------- | ------ | ---------------------------------- | ---------- |
| RISK-MONGO-001 | Document size exceeds 16MB                      | Medium     | High   | Monitor doc size, split aggregates | Monitoring |
| RISK-MONGO-002 | Change stream lag causes stale reads            | Medium     | Medium | Alert on lag, add retries          | Active     |
| RISK-MONGO-003 | Missing schema validation allows malformed data | Low        | High   | Enforce validator, automated tests | Closed     |

---

## 12. Change Log

| Version | Date         | Author | Summary           |
| ------- | ------------ | ------ | ----------------- |
| 0.1     | [YYYY-MM-DD] | [Name] | Initial draft     |
| 1.0     | [YYYY-MM-DD] | [Name] | Approved baseline |

---

## 13. Approvals

| Role                           | Name | Signature | Date |
| ------------------------------ | ---- | --------- | ---- |
| Data Architect (Approve)       |      |           |      |
| Tech Lead (Concur)             |      |           |      |
| Security Officer (Concur)      |      |           |      |
| DevOps Lead (Concur)           |      |           |      |
| Product Owner / DPO (Informed) |      |           |      |

---

**Distribution:** Store in `/02-Architecture/Data_Model/` and reference in Architecture Description, API design, retention matrix, and runbooks. Update when schema or platform changes occur.\*\*\* End Patch
