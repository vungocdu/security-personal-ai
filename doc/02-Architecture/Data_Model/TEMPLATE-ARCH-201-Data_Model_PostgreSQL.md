# Data Model Template — PostgreSQL

**Document ID:** DM-PG-[PROJECT]-[SUBSYSTEM]-[YYYY]-[NNN]  
**Template Version:** 1.0.0  
**Related Standards:** ISO/IEC/IEEE 42010, ISO/IEC 12207:2017 §6.4.4, ISO/IEC/IEEE 29148, ISO/IEC 27001:2022, ISO/IEC 27701, PDPA (Singapore)

---

## Document Control

| Field                        | Value                                   |
| ---------------------------- | --------------------------------------- |
| **System / Component**       | [e.g., ActiveSG Ticketing]              |
| **Data Domains**             | [e.g., User, Facility, Ticket, Audit]   |
| **Document Version**         | [0.1 Draft]                             |
| **Status**                   | Draft / In Review / Approved / Baseline |
| **Classification**           | Internal / Confidential / Restricted    |
| **Author**                   | [Name, Role]                            |
| **Data Architect / Steward** | [Name]                                  |
| **Reviewers**                | [Security, QA, Product, DevOps]         |
| **Creation Date**            | [YYYY-MM-DD]                            |
| **Last Updated**             | [YYYY-MM-DD]                            |
| **Approved By**              | [Name, Role]                            |
| **Approval Date**            | [YYYY-MM-DD]                            |
| **Next Review Date**         | [YYYY-MM-DD]                            |
| **AI-Assisted**              | [ ] Yes — Tool: **\_\_** [ ] No         |

---

## ISO Traceability

| Clause / Control           | Addressed In | Evidence                   |
| -------------------------- | ------------ | -------------------------- |
| ISO/IEC 12207:2017 §6.4.4  | §§3–6        | Logical + physical outputs |
| ISO/IEC/IEEE 29148 §9      | §§2, 7       | Requirements mapping       |
| ISO/IEC 27001:2022 Annex A | §§4, 6       | Classification, security   |
| PDPA                       | §§4.3, 6.2   | PII handling, retention    |

---

## 1. Stakeholders & Responsibilities

| Stakeholder           | Role | Responsibilities                | RACI | Review Status |
| --------------------- | ---- | ------------------------------- | ---- | ------------- |
| Data Architect        |      | Logical + physical design       | R/A  |               |
| Tech Lead             |      | Implementation oversight        | C    |               |
| DBA / DevOps          |      | Deployment, backups, monitoring | R    |               |
| Security Officer      |      | Classification, encryption      | C    |               |
| Product Owner         |      | Data usage compliance           | I    |               |
| DPO / Privacy Officer |      | PDPA requests                   | C    |               |

---

## 2. Requirements Traceability

| Requirement ID | Description      | Data Entity / Field             | Verification             |
| -------------- | ---------------- | ------------------------------- | ------------------------ |
| FR-XXX-001     | [Requirement]    | `ticket.title`, `ticket.status` | API & DB tests           |
| NFR-SEC-002    | Encrypt PII      | `user.email`, `user.phone`      | Encryption configuration |
| REG-PDPA-005   | Right to erasure | `ticket.deleted_at`, purge job  | Retention logs           |

---

## 3. Data Domains & Business Context

| Domain        | Description                        | Owner    | Dependent Processes |
| ------------- | ---------------------------------- | -------- | ------------------- |
| Ticketing     | Manage incidents / work orders     | Ops      | SLA dashboards      |
| Identity      | Authentication / RBAC              | Security | Access control      |
| Observability | Logs & metrics (relational subset) | DevOps   | Audits              |

---

## 4. Logical Data Model

### 4.1 Entity Relationship Overview

```
Facility 1 ── * Ticket * ── 1 User (creator/assignee)
Ticket 1 ── * Comment
```

### 4.2 Entity Catalogue

| Entity     | Description     | Key Attributes                            | Relationships                             | Notes            |
| ---------- | --------------- | ----------------------------------------- | ----------------------------------------- | ---------------- |
| Facility   | Tenant boundary | `id`, `name`, `tenant_code`               | Has many `Ticket`, `Equipment`            |                  |
| Ticket     | Work item       | `id`, `facility_id`, `status`, `priority` | Belongs to `Facility`, has many `Comment` | Soft delete      |
| User       | Actor           | `id`, `email`, `role`, `facility_id`      | Has many `Ticket`, `Comment`              | PII              |
| Comment    | Thread entry    | `id`, `ticket_id`, `author_id`            | Belongs to `Ticket` & `User`              | Visibility flags |
| AuditEvent | Change log      | `id`, `entity_type`, `payload`            | Optional `ticket_id`                      | Append-only      |

### 4.3 Attribute Dictionary

| Entity | Attribute    | Type                                               | Nullable | Default   | PII | Description        |
| ------ | ------------ | -------------------------------------------------- | -------- | --------- | --- | ------------------ |
| Ticket | `status`     | Enum (`created`,`in_progress`,`resolved`,`closed`) | No       | `created` | No  | Workflow state     |
| Ticket | `deleted_at` | `timestamptz`                                      | Yes      | NULL      | No  | Soft delete marker |
| User   | `email`      | `citext`                                           | No       | —         | Yes | Unique login       |

---

## 5. Physical Design — PostgreSQL

### 5.1 Schema Overview

| Table                | Purpose          | Primary Key | Partitioning                                                               | Notes               |
| -------------------- | ---------------- | ----------- | -------------------------------------------------------------------------- | ------------------- |
| `public.facility`    | Tenant boundary  | `id uuid`   | Optional by tenant                                                         |                     |
| `public.user`        | Identity         | `id uuid`   | None                                                                       | Use `citext`        |
| `public.ticket`      | Work items       | `id uuid`   | Optional by month (`PARTITION BY RANGE (date_trunc('month', created_at))`) | Soft delete         |
| `public.comment`     | Ticket threads   | `id uuid`   | Inherits ticket partition                                                  | `ON DELETE CASCADE` |
| `public.audit_event` | Lifecycle events | `id uuid`   | Partition by month                                                         | Append-only         |

### 5.2 DDL Template

```sql
CREATE TABLE public.ticket (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  facility_id uuid NOT NULL REFERENCES public.facility(id),
  creator_id uuid NOT NULL REFERENCES public."user"(id),
  assignee_id uuid REFERENCES public."user"(id),
  title text NOT NULL CHECK (char_length(title) BETWEEN 3 AND 120),
  description text,
  status text NOT NULL CHECK (status IN ('created','in_progress','resolved','closed')),
  priority text NOT NULL CHECK (priority IN ('low','medium','high','urgent')),
  sla_due_at timestamptz,
  closed_at timestamptz,
  deleted_at timestamptz,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now()
);
```

### 5.3 Constraints & Indexing

| Table         | Constraint / Index                                     | Purpose                  |
| ------------- | ------------------------------------------------------ | ------------------------ |
| `ticket`      | `FOREIGN KEY (facility_id)`                            | Enforce tenant ownership |
| `ticket`      | `idx_ticket_facility_status` (`facility_id`, `status`) | Filter dashboards        |
| `ticket`      | `idx_ticket_created_at_desc` (`created_at DESC`)       | Recent ticket queries    |
| `comment`     | `FOREIGN KEY (ticket_id) ON DELETE CASCADE`            | Cascade cleanup          |
| `audit_event` | `CHECK (jsonb_typeof(payload) = 'object')`             | Validate JSON            |

### 5.4 Performance & Storage Notes

- Prefer UUID v7 or ULID for write locality when supported.
- Enable `pgbouncer` in transaction mode for serverless workloads.
- Use partial index for open tickets (`WHERE status != 'closed'`).
- Configure autovacuum thresholds for high-churn tables (tickets/comments).
- Document tablespace usage if deviating from defaults.

### 5.5 Security Features

- Row Level Security (RLS) policy per facility (example below).
- Use `SECURITY DEFINER` functions sparingly; document justification.

```sql
ALTER TABLE public.ticket ENABLE ROW LEVEL SECURITY;
CREATE POLICY ticket_facility_scope ON public.ticket
  USING (facility_id = current_setting('app.current_facility')::uuid OR current_setting('app.role') = 'hq_staff');
```

---

## 6. Security, Privacy & Compliance

### 6.1 Classification & Access

| Table                | Classification | PII   | Access Roles               | Controls                      |
| -------------------- | -------------- | ----- | -------------------------- | ----------------------------- |
| `public.user`        | Confidential   | Yes   | `hq_staff`, DPO            | Field masking, audited access |
| `public.ticket`      | Confidential   | Maybe | `hq_staff`, facility roles | RLS, field-level masking      |
| `public.audit_event` | Internal       | No    | Security, DevOps           | Append-only, tamper detection |

### 6.2 Encryption & Key Management

- At rest: Managed Postgres TDE (e.g., Supabase/AWS RDS).
- In transit: Enforce `sslmode=require`.
- Keys stored in [KMS provider]; rotation policy [quarterly/annual].

### 6.3 PDPA Considerations

- Export endpoints: `/api/user/data-export` referencing tables.
- Deletion: set `deleted_at`, schedule purge job within [X] days.
- Audit: log accessor role + requestId; store evidence for 36 months.

---

## 7. Data Retention & Lifecycle

| Entity       | Retention Policy           | Archive                   | Deletion Method                                   | Evidence    |
| ------------ | -------------------------- | ------------------------- | ------------------------------------------------- | ----------- |
| Tickets      | 24 months post-closure     | Cold storage (S3/Glacier) | `retention:prune` job (hard delete after archive) | Job log     |
| Users        | 36 months after inactivity | Primary DB (flag)         | Soft delete + secure purge                        | Jira ticket |
| Audit Events | 36 months                  | Log warehouse             | Partition drop + backup archive                   | Ops report  |

Reference `TEMPLATE-ARCH-301-Data_Retention` (if available) or actual matrix.

---

## 8. Migration, Versioning & Deployment

| Topic          | Practice                                                             |
| -------------- | -------------------------------------------------------------------- |
| Versioning     | Semantic (`2025.10.31-01`), stored in migration table                |
| Tooling        | Prisma Migrate / Flyway / Liquibase                                  |
| Change Pattern | Expand → backfill → contract; avoid destructive `ALTER` without plan |
| Blue/Green     | Use shadow DB for migration verification when zero downtime required |
| Rollback       | Snapshot (cloud), down migration scripts, feature flags              |
| Approvals      | DBA + Security sign-off for PII schema changes                       |

---

## 9. Data Quality & Testing

| Test                   | Scope                      | Tooling                    | Frequency    | Owner    |
| ---------------------- | -------------------------- | -------------------------- | ------------ | -------- |
| Schema lint            | Naming, types, constraints | Prisma validate / SQLFluff | CI           | Backend  |
| Referential integrity  | FK consistency             | Integration tests          | CI + nightly | DBA      |
| RLS tests              | Facility scoping           | Automated tests (pgTAP)    | CI           | Security |
| Performance regression | Slow query detection       | pgBadger / EXPLAIN plans   | Quarterly    | DevOps   |
| Backup restore drill   | Recovery validation        | Restore to staging         | Semi-annual  | DevOps   |

---

## 10. Operational Considerations

| Topic             | Notes                                                             |
| ----------------- | ----------------------------------------------------------------- |
| Monitoring        | Track connections, replication lag, locks, buffer cache hit ratio |
| Alerting          | Threshold for slow queries, disk usage, replication delays        |
| Maintenance       | `VACUUM ANALYZE` schedule, reindex plan, partition pruning        |
| High Availability | Multi-AZ, failover drills, RTO/RPO targets                        |
| Runbooks          | Link to backup/restore, incident response, schema change SOP      |

---

## 11. Risks & Mitigations

| Risk ID     | Description                                    | Likelihood | Impact | Mitigation                                                                | Residual   |
| ----------- | ---------------------------------------------- | ---------- | ------ | ------------------------------------------------------------------------- | ---------- |
| RISK-PG-001 | Long-running migration locks table             | Medium     | High   | Use `ALTER TABLE ... NOT VALID`, lock during low traffic, test on staging | Monitoring |
| RISK-PG-002 | RLS misconfiguration exposes other tenant data | Low        | High   | Automated RLS tests, security review                                      | Monitoring |
| RISK-PG-003 | Autovacuum lag causing bloat                   | Medium     | Medium | Tune autovacuum, monitor `pg_stat_activity`                               | Active     |

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

**Distribution:** Store in `/02-Architecture/Data_Model/` and link from Architecture Description, API design, retention matrix, and runbooks. Update upon schema change or compliance review.
