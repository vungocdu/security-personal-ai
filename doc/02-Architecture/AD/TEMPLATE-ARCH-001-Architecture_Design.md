# Architecture Design Template (ISO/IEC/IEEE 42010)

**Document ID:** ARCH-[PROJECT]-[SYSTEM]-[YYYY]-[NNN]  
**Template Version:** 1.0.0  
**Standard Alignment:** ISO/IEC/IEEE 42010, ISO/IEC 12207:2017 (6.4.4), ISO/IEC 15288:2023 (6.4.4), ISO/IEC/IEEE 29148:2018, ISO/IEC 27001:2022, PDPA (Singapore)

---

## Document Control

| Field                     | Value                                                |
| ------------------------- | ---------------------------------------------------- |
| **Project**               | [Enter project/programme name]                       |
| **System / Component**    | [Enter system/component name]                        |
| **Document Version**      | [e.g., 0.1 Draft]                                    |
| **Status**                | [Draft / In Review / Approved / Baseline]            |
| **Classification**        | [Public / Internal / Confidential / Restricted]      |
| **Author**                | [Name, Role]                                         |
| **Architect / Tech Lead** | [Name]                                               |
| **Contributors**          | [Optional list; include AI agent ID if applicable]   |
| **Creation Date**         | [YYYY-MM-DD]                                         |
| **Last Updated**          | [YYYY-MM-DD]                                         |
| **Approved By**           | [Name, Role]                                         |
| **Approval Date**         | [YYYY-MM-DD]                                         |
| **Next Review Date**      | [YYYY-MM-DD]                                         |
| **AI-Assisted**           | [ ] Yes — Tool: **\_\_\_\_** [ ] No (Human authored) |

---

## ISO Traceability

| ISO Clause / Control                                | Addressed In    | Evidence / Notes                          |
| --------------------------------------------------- | --------------- | ----------------------------------------- |
| ISO/IEC 12207:2017 §6.4.4 (Architecture Definition) | Entire document | Architecture activities and outputs       |
| ISO/IEC/IEEE 42010 §5 (Architecture Description)    | Sections 1–6    | Stakeholders, concerns, viewpoints, views |
| ISO/IEC/IEEE 29148 §9 (Traceability)                | §3, §12         | Requirement mapping + risk links          |
| ISO/IEC 27001:2022 Annex A (Security)               | §7, §8          | Security measures, RBAC, data protection  |
| PDPA (Singapore)                                    | §7.4, §8.4      | PII controls, data subject rights         |

---

## Instructions for Use

**Purpose:** Capture the architecture description required for planning, implementation, verification, and compliance audits.

**When to Create:** After the SRS is baselined and before significant implementation work begins (per PROC-SDLC-001 §6.4), update whenever major architectural changes occur.

**How to Complete:**

1. Populate Document Control, ISO Traceability, and References before drafting technical sections.
2. Cover stakeholder concerns and rationale for decisions (ISO/IEC/IEEE 42010).
3. Ensure every requirement traced in §3 has corresponding architectural treatment or rationale.
4. Link to supporting artefacts (ADRs, diagrams, API specs, data models) instead of duplicating content.
5. Mark AI-generated sections and confirm human review (PROC-AI-001).
6. Run Architecture Review checklist prior to approval (PROC-SDLC-001 §6.4.6).

**Quality Gate Checklist:**

- [ ] Stakeholders and concerns identified.
- [ ] Architecture views cover context, containers, components, deployment.
- [ ] ADRs documented for all significant decisions.
- [ ] Security, privacy, data retention controls described.
- [ ] Operations (CI/CD, observability, DR) summarized.
- [ ] Traceability & risks mapped to requirements and controls.
- [ ] Document reviewed/approved by Architect and Security Officer.

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Introduction](#2-introduction)
3. [Requirements Traceability](#3-requirements-traceability)
4. [Stakeholders & Concerns](#4-stakeholders--concerns)
5. [Constraints & Architectural Principles](#5-constraints--architectural-principles)
6. [Architecture Viewpoints & Views](#6-architecture-viewpoints--views)
7. [Architecture Decisions](#7-architecture-decisions)
8. [Data Architecture](#8-data-architecture)
9. [Security & Privacy Architecture](#9-security--privacy-architecture)
10. [Quality Attributes & Non-Functional Requirements](#10-quality-attributes--non-functional-requirements)
11. [Operational Considerations](#11-operational-considerations)
12. [Risks & Mitigations](#12-risks--mitigations)
13. [Compliance & Verification Plan](#13-compliance--verification-plan)
14. [Appendices](#14-appendices)
15. [Approvals](#15-approvals)

---

## 1. Executive Summary

**Solution Overview:**  
[Brief overview of the architecture, business goals, and deployment model]

**Highlights / Key Changes:**

- [Key decision or pattern #1]
- [Key decision or pattern #2]

**Compliance Status:**

- Architecture Review: [Scheduled / Complete — date & outcome]
- Security Review: [Scheduled / Complete]
- Traceability: [Complete / Pending items]

---

## 2. Introduction

### 2.1 Purpose

[Describe why this architecture description exists and how it will be used.]

### 2.2 Scope

- **In Scope:** [List modules, integrations, deployment regions, etc.]
- **Out of Scope:** [List deferred or excluded elements]

### 2.3 References

| Document            | ID / Location                           | Description                       |
| ------------------- | --------------------------------------- | --------------------------------- |
| SRS                 | `/01-Requirements/SRS/...`              | System Requirements Specification |
| Traceability Matrix | `/01-Requirements/...`                  | Requirements ↔ Design mapping    |
| ADR Index           | `/02-Architecture/ADR/...`              | Architecture decision records     |
| API Design          | `/02-Architecture/API/...`              | API contracts/reference           |
| Data Model          | `/02-Architecture/Data_Model/...`       | Logical/physical data model       |
| Security Plan       | `/02-Architecture/Security_Privacy/...` | Security & privacy controls       |
| Deployment Plan     | `/03-Lifecycle/...`                     | Operational runbooks              |

---

## 3. Requirements Traceability (ISO/IEC/IEEE 29148)

| Requirement ID | Description                        | Architectural Response (Section / View) | Verification Method      |
| -------------- | ---------------------------------- | --------------------------------------- | ------------------------ |
| FR-XXX-001     | [Functional requirement statement] | [e.g., §6.3 Component View]             | [Test plan / inspection] |
| NFR-YYY-002    | [Non-functional requirement]       | [e.g., §10 Quality Attributes]          | [Monitoring / load test] |
| SEC-ZZZ-003    | [Security requirement]             | [e.g., §9 Security Architecture]        | [Pen test / audit]       |

**Notes:** Identify unmet requirements and provide rationale or remediation plan.

---

## 4. Stakeholders & Concerns (ISO/IEC/IEEE 42010)

| Stakeholder      | Role / Interest            | Key Concerns                | Contact / Review Status |
| ---------------- | -------------------------- | --------------------------- | ----------------------- |
| Product Owner    | Business outcomes          | Time-to-market, cost, SLA   | [Name, review date]     |
| Tech Lead        | Implementation feasibility | Modularity, maintainability |                         |
| Security Officer | Compliance & risk          | Threat mitigation, PDPA     |                         |
| Operations       | Deployment & support       | Observability, rollback     |                         |
| [Add others]     |                            |                             |                         |

---

## 5. Constraints & Architectural Principles

### 5.1 Constraints

| Constraint ID | Category   | Description                                | Source              |
| ------------- | ---------- | ------------------------------------------ | ------------------- |
| CON-ARCH-001  | Technical  | [e.g., Must use existing Supabase cluster] | [Policy / decision] |
| CON-ARCH-002  | Regulatory | [e.g., PDPA compliance requirements]       | [Law / regulation]  |

### 5.2 Architectural Principles

| Principle           | Description          | Implications                  |
| ------------------- | -------------------- | ----------------------------- |
| Contract-first APIs | [Describe principle] | [Impact on processes/tooling] |
| Least privilege     |                      |                               |

---

## 6. Architecture Viewpoints & Views

### 6.1 Viewpoint Catalogue

| Viewpoint                               | Purpose                                        | Stakeholder Concerns    | View(s) Provided |
| --------------------------------------- | ---------------------------------------------- | ----------------------- | ---------------- |
| Context                                 | Show system boundaries and external actors     | Product Owner, Security | §6.2             |
| Container                               | Identify deployable units and responsibilities | Tech Lead, DevOps       | §6.3             |
| Component                               | Detail service/module interactions             | Developers, QA          | §6.4             |
| Deployment                              | Describe runtime topology                      | DevOps                  | §6.5             |
| Sequence / Runtime                      | Illustrate critical scenarios                  | QA, Ops                 | §6.6             |
| [Optional: Data Flow, Capability, etc.] |                                                |                         |                  |

### 6.2 Context View

[Embed C4 diagram or describe external systems, trust boundaries, user personas.]

### 6.3 Container View

[Describe major containers (applications, services, data stores), technology stack, interconnections.]

### 6.4 Component View

[Detail internal modules/components, service responsibilities, patterns (e.g., hexagonal, CQRS).]

### 6.5 Deployment View

[Outline environments (dev/stg/prod), hosting platform, scaling, region/zone topology, connectivity, network policies.]

### 6.6 Runtime / Sequence Views

[Provide key sequences (e.g., create ticket, login, report generation) highlighting synchronous/asynchronous flows and key security controls.]

### 6.7 Cross-cutting Concerns

- **Observability:** [Logging, tracing, metrics strategy]
- **Configuration Management:** [Feature flags, secrets handling, configuration sources]
- **Error Handling / Resilience:** [Retry policies, circuit breakers, fallback mechanisms]

---

## 7. Architecture Decisions (ADR Summary)

| ADR ID               | Decision             | Status                             | Rationale                         | Implications                       |
| -------------------- | -------------------- | ---------------------------------- | --------------------------------- | ---------------------------------- |
| ADR-0001             | [Decision statement] | [Proposed / Accepted / Superseded] | [Summary of drivers/alternatives] | [Impacts on design, team, tooling] |
| [Add rows as needed] |                      |                                    |                                   |                                    |

[Link to detailed ADR files. Include open decisions / pending evaluations.]

---

## 8. Data Architecture

### 8.1 Data Domains & Ownership

| Domain            | Owner  | Systems of Record    | Notes |
| ----------------- | ------ | -------------------- | ----- |
| [e.g., Ticketing] | [Team] | [Database / service] |       |

### 8.2 Logical & Physical Models

- **Logical model summary:** [Reference to ERD or data model doc]
- **Physical storage:** [Databases, schemas, partitioning strategies]
- **Integration flows:** [ETL, CDC, events; include diagrams if applicable]

### 8.3 Data Classification & Retention

| Entity   | Classification            | Retention Policy   | Control Reference               |
| -------- | ------------------------- | ------------------ | ------------------------------- |
| [Entity] | [Internal / Confidential] | [Policy, timeline] | [Link to Data Retention Matrix] |

### 8.4 Data Quality & Governance

[Describe validation rules, stewardship, reconciliation, lineage tracking.]

---

## 9. Security & Privacy Architecture

### 9.1 Threat Model Summary

- **Primary threats:** [List top STRIDE categories]
- **Attack surfaces:** [APIs, UIs, data stores, integrations]
- **Risk posture:** [Residual risk status]

### 9.2 Authentication & Authorization

| Area               | Design                               | Control Reference       |
| ------------------ | ------------------------------------ | ----------------------- |
| Identity Provider  | [e.g., Supabase Auth, OIDC provider] | [Link to Security Plan] |
| Session Management | [Cookies, JWT TTL, refresh policy]   |                         |
| RBAC / ABAC        | [Roles, scopes, field-level masking] | [Link to RBAC matrix]   |

### 9.3 Data Protection

| Layer             | Control                            | Notes |
| ----------------- | ---------------------------------- | ----- |
| In transit        | [TLS version, certificate pinning] |       |
| At rest           | [Encryption, key management]       |       |
| Data minimization | [PII masking, pseudonymization]    |       |

### 9.4 Logging, Monitoring, & Incident Response

[Summarize observability controls, alert thresholds, runbook references.]

### 9.5 Compliance & Privacy

- **PDPA handling:** [Data subject request process, consent, lawful basis]
- **Security Testing:** [SAST/DAST cadence, pen test schedule]
- **Vulnerability Management:** [Ticket SLAs, reporting]

---

## 10. Quality Attributes & Non-Functional Requirements

| Attribute       | Target / KPI                           | Architecture Strategies  | Verification         |
| --------------- | -------------------------------------- | ------------------------ | -------------------- |
| Performance     | [e.g., P95 latency < 400 ms @ 100 RPS] | [Caching, async jobs]    | [Load testing plan]  |
| Availability    | [e.g., ≥ 99.5% monthly]                | [Multi-region, failover] | [SLO/SLA monitoring] |
| Scalability     |                                        |                          |                      |
| Maintainability |                                        |                          |                      |
| Reliability     |                                        |                          |                      |
| Accessibility   |                                        |                          |                      |
| Observability   |                                        |                          |                      |

---

## 11. Operational Considerations

### 11.1 Environments

| Environment | URL / Identifier | Purpose           | Differences |
| ----------- | ---------------- | ----------------- | ----------- |
| Dev         |                  | Developer testing |             |
| Staging     |                  | Pre-production QA |             |
| Production  |                  | Customer-facing   |             |

### 11.2 CI/CD & Release Management

- **Pipeline stages:** [Lint → Test → Build → Deploy]
- **Migration strategy:** [Expand/contract, manual approval]
- **Rollback plan:** [Feature flag, revert deploy, DB restore]

### 11.3 Observability & SRE

- **Logging:** [Platform, retention]
- **Metrics:** [Key indicators, dashboards]
- **Alerts:** [Thresholds, paging policy]

### 11.4 Business Continuity & DR

- **Backup cadence:** [Daily/weekly, retention]
- **Recovery Time Objective (RTO):** [Value]
- **Recovery Point Objective (RPO):** [Value]
- **Failover process:** [Manual / automated, reference runbook]

---

## 12. Risks & Mitigations

| Risk ID  | Description      | Likelihood | Impact  | Mitigation / Control | Residual Status       |
| -------- | ---------------- | ---------- | ------- | -------------------- | --------------------- |
| RISK-### | [Risk statement] | [L/M/H]    | [L/M/H] | [Mitigation actions] | [Monitoring / Active] |

[Reference the central Risk Register; ensure new risks logged if not already tracked.]

---

## 13. Compliance & Verification Plan

| Compliance Item                    | Responsible Party | Evidence Required               | Review Cadence           |
| ---------------------------------- | ----------------- | ------------------------------- | ------------------------ |
| Architecture Review Board approval | Architect         | Approved minutes, checklist     | Per major release        |
| Security sign-off                  | Security Officer  | Threat model, pen test report   | Annually or major change |
| Data retention validation          | DPO, DevOps       | Retention job logs, audit trail | Quarterly                |
| ADR currency                       | Tech Lead         | ADR index review                | Quarterly                |

---

## 14. Appendices

- **Appendix A:** Diagram exports (context, container, component, deployment)
- **Appendix B:** API endpoint catalogue / schemas
- **Appendix C:** Data dictionary excerpts
- **Appendix D:** Change log (history of updates to this document)

> **Change Log Example**
>
> | Version | Date       | Author | Summary       |
> | ------- | ---------- | ------ | ------------- |
> | 0.1.0   | 2025-10-31 | [Name] | Initial draft |

---

## 15. Approvals

| Role                            | Name | Signature | Date |
| ------------------------------- | ---- | --------- | ---- |
| Product Owner (Approve)         |      |           |      |
| Tech Lead / Architect (Approve) |      |           |      |
| Security Officer (Concur)       |      |           |      |
| DevOps Lead (Concur)            |      |           |      |
| Quality Manager (Informed)      |      |           |      |

---

**Distribution:** Store the approved version in the project knowledge base and link within the traceability matrix. Update relevant runbooks and checklists upon approval.
