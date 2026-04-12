# Data Model Template — MySQL

**Document ID:** DM-MYSQL-[PROJECT]-[SUBSYSTEM]-[YYYY]-[NNN]  
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

| Clause / Control          | Addressed In | Evidence                  |
| ------------------------- | ------------ | ------------------------- |
| ISO/IEC 12207:2017 §6.4.4 | §§3–6        | Logical + physical design |
| ISO/IEC/IEEE 29148 §9     | §§2, 7       | Requirements mapping      |
| ISO/IEC 27001 Annex A     | §§4, 6       | Classification / security |
| PDPA                      | §§4.3, 6.3   | PII handling, retention   |

---

## 1. Stakeholders & Responsibilities

| Stakeholder      | Role | Responsibilities           | RACI | Review Status |
| ---------------- | ---- | -------------------------- | ---- | ------------- |
| Data Architect   |      | Logical/physical design    | R/A  |               |
| Tech Lead        |      | Implementation oversight   | C    |               |
| DBA / DevOps     |      | Schema deployment, backups | R    |               |
| Security Officer |      | Data protection review     | C    |               |
| Product Owner    |      | Consent, lawful basis      | I    |               |
| DPO              |      | PDPA compliance            | C    |               |

---

## 2. Requirements Traceability

| Requirement ID | Description          | Data Entity / Field             | Verification       |
| -------------- | -------------------- | ------------------------------- | ------------------ |
| FR-XXX-001     | [Requirement]        | `ticket.title`, `ticket.status` | Integration tests  |
| NFR-PERF-004   | Query < 200 ms       | `idx_ticket_facility_status`    | k6 / SQL profiling |
| SEC-LOG-007    | Audit logs immutable | `audit_event` table             | Logging checks     |

---

## 3. Data Domains & Business Context

| Domain                  | Description          | Owner    | Dependencies     |
| ----------------------- | -------------------- | -------- | ---------------- |
| Ticketing               | Maintenance workflow | Ops      | Reporting, SLA   |
| Identity                | Users & roles        | Security | RBAC             |
| Billing (if applicable) | Payments             | Finance  | External gateway |

---

## 4. Logical Data Model

### 4.1 Entity Overview

| Entity   | Description     | Key Attributes                            | Relationships                             | Notes                        |
| -------- | --------------- | ----------------------------------------- | ----------------------------------------- | ---------------------------- |
| Facility | Tenant boundary | `id`, `name`, `tenant_code`               | Has many `Ticket`, `Equipment`            |                              |
| Ticket   | Work order      | `id`, `facility_id`, `status`, `priority` | Belongs to `Facility`, has many `Comment` | Soft delete via `deleted_at` |
| User     | System actor    | `id`, `email`, `role`, `facility_id`      | Has many `Ticket`, `Comment`              | PII                          |
| Comment  | Ticket note     | `id`, `ticket_id`, `author_id`            | Belongs to `Ticket`                       | Visibility control           |

### 4.2 Attribute Dictionary

| Entity | Attribute    | Type                                              | Nullable | Default           | PII | Description       |
| ------ | ------------ | ------------------------------------------------- | -------- | ----------------- | --- | ----------------- |
| Ticket | `status`     | ENUM('created','in_progress','resolved','closed') | No       | 'created'         | No  | Workflow state    |
| Ticket | `created_at` | DATETIME                                          | No       | CURRENT_TIMESTAMP | No  | UTC stored        |
| User   | `email`      | VARCHAR(254)                                      | No       | —                 | Yes | Unique with index |

---

## 5. Physical Design — MySQL (InnoDB)

### 5.1 Engine & Config

- Engine: InnoDB for ACID compliance.
- Character set: `utf8mb4` with `unicode_ci` collation.
- Enable `innodb_file_per_table`, `innodb_flush_log_at_trx_commit=1`.
- Use `READ-COMMITTED` isolation (default) unless business requires `REPEATABLE-READ`.

### 5.2 Schema & DDL Template

```sql
CREATE TABLE ticket (
  id BINARY(16) PRIMARY KEY,
  facility_id BINARY(16) NOT NULL,
  creator_id BINARY(16) NOT NULL,
  assignee_id BINARY(16),
  title VARCHAR(120) NOT NULL,
  description TEXT,
  status ENUM('created','in_progress','resolved','closed') NOT NULL DEFAULT 'created',
  priority ENUM('low','medium','high','urgent') NOT NULL DEFAULT 'medium',
  sla_due_at DATETIME,
  closed_at DATETIME,
  deleted_at DATETIME,
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  CONSTRAINT fk_ticket_facility FOREIGN KEY (facility_id) REFERENCES facility(id),
  CONSTRAINT fk_ticket_creator FOREIGN KEY (creator_id) REFERENCES user(id),
  CONSTRAINT fk_ticket_assignee FOREIGN KEY (assignee_id) REFERENCES user(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

> **ID Strategy:** Store UUIDs as `BINARY(16)` for compact indexes; convert to/from text in application layer.

### 5.3 Indexing & Partitioning

| Table     | Index                                                          | Purpose           | Notes               |
| --------- | -------------------------------------------------------------- | ----------------- | ------------------- |
| `ticket`  | `idx_ticket_facility_status (facility_id, status, created_at)` | Dashboard filters | Covering index      |
| `ticket`  | `idx_ticket_deleted_at`                                        | Retention jobs    | Filter soft-deleted |
| `user`    | `idx_user_email` UNIQUE                                        | Login lookups     | Case-insensitive    |
| `comment` | `idx_comment_ticket_created`                                   | Comment ordering  | Include created_at  |

Partitioning options:

- Range partition by month on `created_at` for high-volume workloads.
- Alternatively, hash partition by `facility_id` for tenant isolation.

### 5.4 Performance & Storage Notes

- Normalize text columns; avoid `TEXT` unless necessary (prefer `VARCHAR`).
- Use generated columns for JSON search (if storing metadata).
- Monitor slow query log; set threshold (e.g., 200 ms).
- Configure read replicas for analytics; document replication lag tolerance.

### 5.5 Security Controls

- User accounts: enforce `REQUIRE SSL`.
- Grant least privilege per environment (app user vs migration user).
- Mask PII via views when exposing to BI tools.
- Enable MySQL Enterprise Audit or use proxy layer for logging.

---

## 6. Security, Privacy & Compliance

### 6.1 Classification & Access

| Table         | Classification | PII   | Access Roles                                 | Notes                           |
| ------------- | -------------- | ----- | -------------------------------------------- | ------------------------------- |
| `user`        | Confidential   | Yes   | `hq_staff`, DPO                              | Mask via view/procedure         |
| `ticket`      | Confidential   | Maybe | `hq_staff`, `manager`, `staff`, `technician` | Facility-level filtering in app |
| `audit_event` | Internal       | No    | Security, DevOps                             | Append-only                     |

### 6.2 Encryption & Key Management

- At rest: MySQL TDE (if available) or disk encryption.
- In transit: TLS (verify server cert).
- Secret storage: Vault/KMS; rotate quarterly or per policy.

### 6.3 PDPA Requirements

- Consent tracking stored in `user_consent` table (if applicable).
- Data export: stored procedures generating CSV/JSON; log requests.
- Deletion: soft delete + asynchronous purge within [X] days; ensure cascading to related tables.

---

## 7. Data Retention & Lifecycle

| Entity       | Retention Policy        | Archive           | Deletion Method                   | Evidence    |
| ------------ | ----------------------- | ----------------- | --------------------------------- | ----------- |
| Tickets      | 24 months after closure | Cold archive (S3) | Archive table + purge job         | Job runbook |
| Users        | 36 months inactivity    | Primary DB (flag) | Soft delete + secure purge script | Jira task   |
| Audit Events | 36 months               | Log service       | Drop partitions older than window | Ops report  |

---

## 8. Migration, Versioning & Deployment

| Topic            | Approach                                                                       |
| ---------------- | ------------------------------------------------------------------------------ |
| Versioning       | Timestamped SQL (`20251031_add_ticket_status.sql`)                             |
| Tooling          | Flyway/Liquibase/Prisma (SQL mode)                                             |
| Change Pattern   | Expand/contract; avoid `ALTER TABLE` column type changes without downtime plan |
| Zero Downtime    | Use `pt-online-schema-change` or gh-ost for large tables                       |
| Rollback         | Full backup + inverse migration script                                         |
| Release Sequence | 1) Schema migration 2) App deploy 3) Smoke tests                               |

---

## 9. Data Quality & Testing

| Test                   | Scope                       | Tooling                  | Frequency    | Owner     |
| ---------------------- | --------------------------- | ------------------------ | ------------ | --------- |
| Schema lint            | Naming, charset, collation  | SQLFluff, custom scripts | CI           | Backend   |
| FK integrity           | Constraint checks           | Integration tests        | CI + nightly | DBA       |
| Data profiling         | PII leakage, null anomalies | dbt / Great Expectations | Monthly      | Data team |
| Performance regression | Query benchmark             | sysbench / EXPLAIN       | Quarterly    | DevOps    |
| Backup restore         | Recovery validation         | Restore replica          | Semi-annual  | DevOps    |

---

## 10. Operational Considerations

| Topic             | Notes                                                    |
| ----------------- | -------------------------------------------------------- |
| Monitoring        | Track QPS, replication lag, deadlocks, temp table usage  |
| Alerting          | Slow query log volume, disk usage, connection saturation |
| Maintenance       | Analyze tables, optimize, partition housekeeping         |
| High Availability | Master + replica, failover procedure, RTO/RPO targets    |
| Runbooks          | Backup/restore, schema change SOP, incident response     |

---

## 11. Risks & Mitigations

| Risk ID     | Description                               | Likelihood | Impact | Mitigation                                             | Residual   |
| ----------- | ----------------------------------------- | ---------- | ------ | ------------------------------------------------------ | ---------- |
| RISK-MY-001 | Schema change causes lock/downtime        | Medium     | High   | Use online schema tooling, schedule maintenance window | Monitoring |
| RISK-MY-002 | Collation mismatch leading to query drift | Low        | Medium | Enforce `utf8mb4_unicode_ci` via migrations            | Closed     |
| RISK-MY-003 | Replica lag impacts reads                 | Medium     | Medium | Monitor lag, use read-after-write routing              | Active     |

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

**Distribution:** Store in `/02-Architecture/Data_Model/` and reference in Architecture Description, API design, retention matrix, and runbooks. Update when schema or policy changes occur.\*\*\* End Patch
