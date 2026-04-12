# Naming & Repository Conventions

**MERCURY SOLUTIONS**  
**Software Engineering Excellence**

---

## DOCUMENT CONTROL

| Field                | Value                                     |
| -------------------- | ----------------------------------------- |
| **Document ID**      | CONV-REPO-001                             |
| **Template Version** | 1.1                                       |
| **Document Version** | [e.g., 1.1]                               |
| **Owner**            | Mercury Solutions Architecture Council    |
| **Co-Owners**        | DevOps Lead, Quality Manager              |
| **Document Status**  | [Draft / In Review / Approved / Baseline] |
| **Classification**   | Internal                                  |
| **Creation Date**    | 2024-10-10                                |
| **Last Updated**     | [YYYY-MM-DD]                              |
| **Approved By**      | [Name, Role]                              |
| **Approval Date**    | [YYYY-MM-DD]                              |
| **Next Review Date** | [YYYY-MM-DD]                              |
| **AI-Assisted**      | [ ] Yes - Tool: **\_\_\_** [ ] No         |

---

## ISO STANDARDS COMPLIANCE

**This document supports adherence to:**

- ✓ ISO/IEC/IEEE 12207:2017 — Clause 6.3 (Project Management) & 6.4 (Technical Processes)
- ✓ ISO/IEC 15288:2023 — Clause 6.3.2 (Configuration Management)
- ✓ ISO/IEC/IEEE 42010:2022 — Architecture description consistency
- ✓ ISO 9001:2015 — Clause 8.5 (Production and Service Provision)
- ✓ ISO/IEC 27001:2022 — Annex A 5.15 (Access Control to Source Code)

**Traceability references:**

- TEMPLATE-LC-004-Configuration_Management.md
- TEMPLATE-LC-001-CI_CD_Strategy.md
- TEMPLATE-LC-011-Test_Plan_VnV.md

---

## 1. PURPOSE & SCOPE

### 1.1 Purpose

Establish consistent naming, structural, and governance practices for Mercury Solutions repositories to improve maintainability, onboarding, and ISO audit readiness.

### 1.2 Scope

- **In Scope:** Monorepo layout, package/app naming, branch/tag conventions, commit messages, documentation identifiers.
- **Out of Scope:** Third-party system naming policies, customer-specific repository rules (governed by project agreements).

### 1.3 Guiding Principles

- Clarity over brevity; names must communicate domain intent.
- Names remain stable once baselined (change requires review via TEMPLATE-LC-002-Change_Impact_Assessment.md).
- Prefixes align to Mercury product codes and module taxonomy.

---

## 2. REPOSITORY STRUCTURE & NAMING

### 2.1 Repository Naming

| Asset              | Pattern               | Example                     | Notes                                   |
| ------------------ | --------------------- | --------------------------- | --------------------------------------- |
| Monorepo           | `mercury-{domain}`    | `mercury-services-monorepo` | Lowercase, hyphen-separated             |
| Standalone service | `{product}-{service}` | `minova-doc-service`        | Avoid abbreviations unless standardised |
| Documentation repo | `{product}-docs`      | `minova-platform-docs`      | Mirrors directory layout below          |

### 2.2 Directory Layout (Monorepo)

```
repo-root/
├─ docs/                         # ISO-aligned documentation (see ISO_Doc_Kit)
├─ apps/                         # Deployable applications (web, mobile, service)
│  └─ {app-name}/
├─ packages/                     # Shared libraries, SDKs, design systems
│  ├─ core/
│  ├─ data/
│  └─ ui/
├─ services/                     # Backend services (Go, Node, Python)
│  └─ {service-name}/
├─ infra/                        # Infrastructure-as-code (Terraform, Pulumi)
├─ scripts/                      # DX tools, migrations
└─ tools/                        # Internal CLI and automation
```

---

## 3. MODULE & ARTIFACT TAXONOMY

### 3.1 Module Codes

| Code  | Domain        | Description                               |
| ----- | ------------- | ----------------------------------------- |
| `CRM` | Customer      | Customer accounts, profiles, segmentation |
| `BKG` | Booking       | Scheduling, reservations, occupancy       |
| `PAY` | Payment       | Billing, invoicing, settlements           |
| `OPS` | Operations    | Back-office workflows, automations        |
| `OBS` | Observability | Monitoring, telemetry, reporting          |
| `SEC` | Security      | IAM, audit, compliance controls           |
| `AI`  | AI Enablement | Models, prompts, inference services       |

> Extend via Change Impact Assessment; maintain register in `/02-Architecture/Data_Model/Module_Catalog.md`.

### 3.2 Requirement & Artifact IDs

| Type                       | Pattern               | Example                      | Notes                             |
| -------------------------- | --------------------- | ---------------------------- | --------------------------------- |
| Functional Requirement     | `{MOD}-FR-###`        | `CRM-FR-015`                 | Sequential per module             |
| Non-functional Requirement | `{MOD}-NFR-###`       | `OBS-NFR-004`                | Link to SLO/SLA                   |
| Use Case                   | `{MOD}-UC-###`        | `PAY-UC-002`                 | Align with BPMN/sequence diagrams |
| ADR                        | `ADR-{####}-{slug}`   | `ADR-0032-event-sourcing.md` | 4-digit zero-padded               |
| API                        | `{MOD}-API-###`       | `AI-API-006`                 | Documented in OpenAPI             |
| Database Object            | `{MOD}_{object_name}` | `pay_transactions`           | snake_case for persistence        |

---

## 4. SOURCE NAMING CONVENTIONS

### 4.1 TypeScript / JavaScript

| Element    | Convention         | Example                 | Notes                        |
| ---------- | ------------------ | ----------------------- | ---------------------------- |
| Variables  | `camelCase`        | `customerId`, `isValid` | Avoid abbreviations          |
| Functions  | `camelCase`        | `createInvoice()`       | Verb + noun                  |
| Classes    | `PascalCase`       | `InvoiceService`        | One class per file           |
| Components | `PascalCase.tsx`   | `BookingSummary.tsx`    | Co-locate styles/tests       |
| Hooks      | `use{Name}.ts`     | `useSessions.ts`        | Export default hook          |
| Constants  | `UPPER_SNAKE_CASE` | `MAX_BOOKINGS_PER_DAY`  | Reserve for immutable config |

### 4.2 Go

| Element    | Convention  | Example                       | Notes                   |
| ---------- | ----------- | ----------------------------- | ----------------------- |
| Packages   | lowercase   | `audit`, `reporting`          | No underscores          |
| Files      | lowercase   | `handler.go`, `repository.go` | Group by responsibility |
| Interfaces | `CamelCase` | `Notifier`, `Repository`      | No `I` prefix           |
| Structs    | `CamelCase` | `PaymentRequest`              | Exported if shared      |
| Constants  | `CamelCase` | `MaxRetries`                  | Use `const` block       |

### 4.3 Database

| Element    | Convention                   | Example                          | Notes                                |
| ---------- | ---------------------------- | -------------------------------- | ------------------------------------ |
| Tables     | `snake_case`                 | `customer_profiles`              | Plural nouns                         |
| Columns    | `snake_case`                 | `created_at`, `status_code`      | Use `_id` suffix for FKs             |
| Indexes    | `idx_{table}_{column}`       | `idx_customer_profiles_email`    | Unique indexes prefixed with `uidx_` |
| Migrations | `YYYYMMDDHHMM_{description}` | `20250115_add_customer_segments` | UTC timestamps                       |

---

## 5. GIT GOVERNANCE

### 5.1 Branch Taxonomy

| Branch      | Pattern                      | Example                       | Purpose                     |
| ----------- | ---------------------------- | ----------------------------- | --------------------------- |
| Mainline    | `main`                       | `main`                        | Production-ready baseline   |
| Development | `develop`                    | `develop`                     | Optional integration branch |
| Feature     | `feature/{MOD}-{short-slug}` | `feature/CRM-customer-export` | New functionality           |
| Bugfix      | `bugfix/{MOD}-{issue}`       | `bugfix/PAY-incorrect-total`  | Non-hotfix defect           |
| Hotfix      | `hotfix/{issue}`             | `hotfix/log4j-remediation`    | Urgent production fix       |
| Release     | `release/v{major}.{minor}`   | `release/v2.3`                | Stabilisation prior to tag  |

### 5.2 Commit Messages (Conventional Commits)

```
<type>(<module>): <imperative sentence>

Body (wrap at 100 chars)

Refs: <issue/ticket ids>
AI-Assisted: <Tool/Prompt/Validation>
```

**Types:** `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `perf`, `build`, `revert`.  
**Module Scope:** Use module code (e.g., `feat(CRM): ...`).

### 5.3 Tagging

| Scenario       | Pattern                                | Example           | Notes                 |
| -------------- | -------------------------------------- | ----------------- | --------------------- |
| Stable release | `v{major}.{minor}.{patch}`             | `v2.3.1`          | Semantic versioning   |
| Pre-release    | `v{major}.{minor}.{patch}-{stage}.{n}` | `v2.3.0-rc.1`     | `alpha`, `beta`, `rc` |
| Hotfix         | `v{major}.{minor}.{patch}-hotfix.{n}`  | `v2.3.1-hotfix.1` | Link to Change record |

---

## 6. DOCUMENTATION NAMING

| Document              | Pattern                            | Example                     | Notes                            |
| --------------------- | ---------------------------------- | --------------------------- | -------------------------------- |
| Software Requirements | `SRS-{Product}-{Module}-v{X.Y}.md` | `SRS-Minova-CRM-v1.0.md`    | Stored under `/01-Requirements/` |
| Architecture Design   | `MS_AD_{Product}_{Module}.md`      | `MS_AD_Minova_CRM.md`       | `/02-Architecture/AD/`           |
| Low-Level Design      | `LLD-{Module}-{Component}.md`      | `LLD-CRM-AddressService.md` | `/05-LLD/Module_Template/`       |
| Test Plan             | `TEST-{Module}-{Scope}.md`         | `TEST-CRM-UAT.md`           | `/03-Lifecycle/Test/`            |
| Runbook               | `RUNBOOK-{Service}.md`             | `RUNBOOK-CRM-Service.md`    | `/03-Lifecycle/Runbook/`         |

> Ensure each document header references template version and AI involvement.

---

## 7. ENVIRONMENT & CONFIGURATION

- Environment files use lowercase with environment suffix: `.env.local`, `.env.staging`, `.env.production`.
- Environment variable naming: `{SERVICE}_{SETTING}` (server-side) and `NEXT_PUBLIC_{SETTING}` (client-side).
- Configuration baselines documented in TEMPLATE-LC-004-Configuration_Management.md.

---

## 8. QUALITY GATES

### 8.1 Pre-Commit Checklist

- [ ] Formatting (Prettier, gofmt, black, etc.)
- [ ] Linting (ESLint, golangci-lint, etc.)
- [ ] Type / Static Analysis (TypeScript, mypy)
- [ ] Unit tests
- [ ] Secrets scanning
- [ ] Commit conforms to convention

### 8.2 Pre-Merge Requirements

- [ ] CI pipeline success (build, test, security scans)
- [ ] Code coverage ≥ 80% (or project target)
- [ ] Change Impact Assessment approved for cross-team changes
- [ ] Documentation updated (README, docs, OpenAPI)
- [ ] Regression test evidence attached for high-risk modules

---

## 9. GOVERNANCE & CHANGE MANAGEMENT

- Changes to naming conventions require:
  1. Proposal ADR describing rationale.
  2. Impact analysis via TEMPLATE-LC-002-Change_Impact_Assessment.md.
  3. Approval by Architecture Council and Quality Manager.
  4. Update this document, Directory_Overview.md, and Document_Index.md.

- Maintain historical versions in Git; do not delete retired conventions—mark as deprecated.

---

## 10. CHANGE HISTORY

| Version | Date         | Description                                                  | Author               | Approved By |
| ------- | ------------ | ------------------------------------------------------------ | -------------------- | ----------- |
| 1.0     | 2024-01-27   | Initial release aligned with ActiveSG monorepo conventions   | Architecture Council | CTO         |
| 1.1     | [YYYY-MM-DD] | Mercury-wide standardisation; ISO document control alignment | [Name]               | [Name]      |
