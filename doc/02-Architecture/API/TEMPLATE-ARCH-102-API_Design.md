# API Design Template (ISO/IEC/IEEE 42010 & 29148)

**Document ID:** API-[DOMAIN]-[SERVICE]-[YYYY]-[NNN]  
**Template Version:** 1.0.0  
**Related Standards:** ISO/IEC/IEEE 42010 (Architecture Description), ISO/IEC 12207:2017 §6.4.4 (Architecture Definition), ISO/IEC/IEEE 29148:2018 (Requirements), ISO/IEC 27001:2022 (Security), ISO/IEC 25010 (Quality), PDPA (Singapore)

---

## Document Control

| Field                | Value                                         |
| -------------------- | --------------------------------------------- |
| **Service / Module** | [e.g., Actiwell Ticketing API]                |
| **API Type**         | REST / GraphQL / gRPC / Async Events          |
| **Document Version** | [e.g., 0.1 Draft]                             |
| **Status**           | Draft / In Review / Approved / Baseline       |
| **Classification**   | Public / Internal / Confidential / Restricted |
| **Author**           | [Name, Role]                                  |
| **Reviewers**        | [Architect, Security, QA, Product]            |
| **Creation Date**    | [YYYY-MM-DD]                                  |
| **Last Updated**     | [YYYY-MM-DD]                                  |
| **Approved By**      | [Name, Role]                                  |
| **Approval Date**    | [YYYY-MM-DD]                                  |
| **Next Review Date** | [YYYY-MM-DD]                                  |
| **AI-Assisted**      | [ ] Yes — Tool: **\_\_** [ ] No               |

---

## ISO Traceability Matrix

| Clause / Control                                    | Addressed In    | Evidence                        |
| --------------------------------------------------- | --------------- | ------------------------------- |
| ISO/IEC/IEEE 42010 §5 (Viewpoints/Concerns)         | §4–§8           | Context & endpoint design       |
| ISO/IEC 12207:2017 §6.4.4 (Architecture Definition) | Entire document | API architecture outputs        |
| ISO/IEC/IEEE 29148 §9 (Requirements)                | §3, §7, §9      | Requirement ↔ contract mapping |
| ISO/IEC 27001:2022 Annex A (Security)               | §8              | Security & privacy controls     |
| ISO/IEC 25010 (Quality)                             | §9              | Non-functional attributes       |

---

## Instructions for Authors

1. Populate Document Control & ISO Traceability before drafting technical sections.
2. Start from agreed SRS/AD artefacts; every API behaviour must map back to requirements (PROC-SDLC-001).
3. Use **shall/should/may** statements for requirements (ISO/IEC/IEEE 29148).
4. Identify AI-generated content and confirm human review (PROC-AI-001).
5. Ensure compliance with company API guidelines (naming, versioning, security).
6. Update this design upon major change or version increment; archive superseded versions.

> **Checklist:**
>
> - [ ] Stakeholders and RACI defined
> - [ ] Endpoint catalogue, schemas, validation rules complete
> - [ ] Error codes standardized
> - [ ] Security, rate limits, logging documented
> - [ ] NFR targets measurable and test plan linked
> - [ ] Compliance/privacy obligations covered
> - [ ] Change log & approvals signed

---

## Table of Contents

1. [Purpose & Scope](#1-purpose--scope)
2. [Definitions & References](#2-definitions--references)
3. [Stakeholders, Roles & RACI](#3-stakeholders-roles--raci)
4. [System Context & Dependencies](#4-system-context--dependencies)
5. [Resource Model & Domain Overview](#5-resource-model--domain-overview)
6. [Endpoint Catalogue & Contracts](#6-endpoint-catalogue--contracts)
7. [Business Rules & Validation](#7-business-rules--validation)
8. [Security & Privacy Controls](#8-security--privacy-controls)
9. [Non-Functional Requirements](#9-non-functional-requirements)
10. [Error Handling & Status Codes](#10-error-handling--status-codes)
11. [Rate Limiting, Quotas & Idempotency](#11-rate-limiting-quotas--idempotency)
12. [Observability & Operational Logging](#12-observability--operational-logging)
13. [Lifecycle Management & Versioning](#13-lifecycle-management--versioning)
14. [Testing & Verification Plan](#14-testing--verification-plan)
15. [Compliance & Data Protection Checklist](#15-compliance--data-protection-checklist)
16. [Change Log](#16-change-log)
17. [Approvals](#17-approvals)

---

## 1. Purpose & Scope

### 1.1 Purpose _(Required)_

> **Author Guidance:** Describe the business outcome and boundary of the API without diving into implementation. Answer “What value does this API deliver and for whom?”

### 1.2 Scope _(Required)_

- **In Scope:** [Endpoints/functions included, systems touched]
- **Out of Scope:** [Deferred features, exclusions]
- **Assumptions:** [Technology, availability, data sources]

### 1.3 Objectives & Success Metrics

- [Objective 1, e.g., Reduce ticket resolution time by 20%]
- [KPIs / SLAs]
- [Compliance objectives (e.g., PDPA lawful basis)]

---

## 2. Definitions & References

| Term                    | Definition                               |
| ----------------------- | ---------------------------------------- |
| Resource                | REST resource accessible via URI         |
| Idempotency Key         | Header used to deduplicate POST requests |
| [Domain-specific terms] |                                          |

| Reference                | Location                                | Notes              |
| ------------------------ | --------------------------------------- | ------------------ |
| SRS                      | `/01-Requirements/...`                  | Requirement source |
| Architecture Description | `/02-Architecture/AD/...`               | Context/views      |
| ADR Index                | `/02-Architecture/ADR/...`              | Decision history   |
| Data Model               | `/02-Architecture/Data_Model/...`       | Entities & schema  |
| Security & Privacy Plan  | `/02-Architecture/Security_Privacy/...` | Controls           |

---

## 3. Stakeholders, Roles & RACI

| Stakeholder        | Role | Responsibilities | RACI (R/A/C/I) | Review Status |
| ------------------ | ---- | ---------------- | -------------- | ------------- |
| Product Owner      |      |                  |                |               |
| Solution Architect |      |                  |                |               |
| Backend Engineer   |      |                  |                |               |
| QA Lead            |      |                  |                |               |
| Security Officer   |      |                  |                |               |
| DevOps             |      |                  |                |               |
| AI Agent (if used) |      |                  |                |               |

---

## 4. System Context & Dependencies

### 4.1 Context Diagram

[Insert C4 Level 1 diagram or describe external systems/channels.]

### 4.2 Integrations & Upstream/Downstream Services

| System     | Interaction Type          | Direction | Protocol  | Notes |
| ---------- | ------------------------- | --------- | --------- | ----- |
| [System A] | Authoritative data source | Inbound   | REST/gRPC |       |
| [System B] | Notification service      | Outbound  | Webhook   |       |

### 4.3 Constraints

- Regulatory (PDPA/GDPR, sector-specific)
- Technical (runtime limits, existing infrastructure)
- Operational (support hours, SLAs)

---

## 5. Resource Model & Domain Overview

### 5.1 Domain Summary

Describe primary resources (e.g., Ticket, Facility, Equipment) and relationships.

### 5.2 Resource Relationships Diagram

[ERD/C4 Container or textual depiction.]

### 5.3 Field Dictionary (High-level)

| Resource | Field | Description       | Type | PII? | Notes |
| -------- | ----- | ----------------- | ---- | ---- | ----- |
| Ticket   | id    | Unique identifier | UUID | No   |       |

---

## 6. Endpoint Catalogue & Contracts

### 6.1 Endpoint Summary

| Endpoint          | Method | Purpose      | Auth   | RBAC                           | Request Schema       | Response Schema    |
| ----------------- | ------ | ------------ | ------ | ------------------------------ | -------------------- | ------------------ |
| `/api/v1/tickets` | GET    | List tickets | Bearer | `hq_staff`, `manager`, `staff` | `ListTicketsRequest` | `TicketCollection` |

### 6.2 Detailed Endpoint Specification

#### 6.2.1 `GET /api/v1/tickets`

- **Description:** [Functional description]
- **Query Parameters:**
  - `status` (enum: created, in_progress, resolved, closed)
  - `page`, `limit`, `sort`
- **Request Example:**

```http
GET /api/v1/tickets?status=created&page=1&limit=20 HTTP/1.1
Authorization: Bearer <token>
```

- **Response Example:**

```json
{
  "data": [ { "id": "uuid", "title": "...", ... } ],
  "page": 1,
  "limit": 20,
  "total": 120
}
```

- **Behaviour / Rules:**
  - Must filter by `facilityId` unless role `hq_staff`.
  - Returns masked PII for non-HQ roles.
- **Performance Budget:** P95 latency < 400 ms @ 100 RPS.

_(Repeat for each endpoint.)_

### 6.3 Payload Schemas

| Schema                | Description                 | Required Fields             | Optional Fields                          | Validation Notes                              |
| --------------------- | --------------------------- | --------------------------- | ---------------------------------------- | --------------------------------------------- |
| `CreateTicketRequest` | Payload for ticket creation | `title`, `facilityId`       | `description`, `priority`, `equipmentId` | `title` length 3–120, `facilityId` must exist |
| `TicketResource`      | Response representation     | `id`, `status`, `createdAt` | ...                                      | Mask fields per RBAC                          |

Include JSON Schema / OpenAPI snippet if available.

---

## 7. Business Rules & Validation

| Rule ID   | Statement                                             | Applies To           | Enforcement                          | Source Requirement |
| --------- | ----------------------------------------------------- | -------------------- | ------------------------------------ | ------------------ |
| BR-TK-001 | Ticket priority `urgent` requires `hq_staff` approval | POST `/tickets`      | Service layer check + workflow state | SRS FR-TK-010      |
| VAL-002   | `description` max length 2000 chars                   | Create/Update ticket | JSON schema validation               | UX guideline       |

---

## 8. Security & Privacy Controls

### 8.1 Authentication

- Method: [Supabase Auth / OIDC / etc]
- Token TTL, refresh policy, MFA requirements.

### 8.2 Authorization & RBAC

- Roles: `hq_staff`, `manager`, `staff`, `technician`, `anonymous`
- Field-level masking, facility scoping.
- Reference: `Security_Privacy/RBAC_Matrix_By_Endpoint.md`.

### 8.3 Data Protection

- PII fields: [List; encryption, masking strategies]
- Logging policy: redact tokens, PII allowlist.

### 8.4 Threat Model Summary

- Main threats: [Credential stuffing, injection, etc]
- Mitigations: [Rate limiting, schema validation, WAF]

### 8.5 Compliance Notes

- PDPA lawful basis: [Consent / Contract / Legitimate Interest]
- Data subject requests: [Endpoints/process]
- Security testing cadence: [SAST per PR, DAST quarterly, pen test annually]

---

## 9. Non-Functional Requirements

| Attribute                       | Target                           | Measurement Method              | Architecture Strategy              |
| ------------------------------- | -------------------------------- | ------------------------------- | ---------------------------------- |
| Performance                     | P95 < 400 ms @ 100 RPS           | k6 load test                    | DB indexing, caching, pagination   |
| Availability                    | ≥ 99.5% monthly uptime           | SLO dashboard                   | Vercel + Supabase HA               |
| Scalability                     | Support 5x baseline load         | Load test & autoscaling metrics | Stateless functions, queue offload |
| Maintainability                 | Lint/typecheck 100%, ADR updates | CI results                      | Contract-first, modular services   |
| Observability                   | 100% endpoints w/ requestId logs | Log audit                       | Structured logging, tracing        |
| Accessibility (if UI endpoints) | WCAG 2.1 AA                      | Accessibility audit             | UI linting, semantic HTML          |

---

## 10. Error Handling & Status Codes

### 10.1 Standard Error Envelope

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "title is required",
    "details": [{ "field": "title", "issue": "required" }],
    "requestId": "uuid"
  }
}
```

### 10.2 Error Catalogue

| Code                  | HTTP Status | Description           | Retryable?          | Logged As | Mitigation      |
| --------------------- | ----------- | --------------------- | ------------------- | --------- | --------------- |
| `AUTH_INVALID_TOKEN`  | 401         | Token missing/invalid | No                  | Warn      | Prompt re-auth  |
| `RATE_LIMIT_EXCEEDED` | 429         | Throttling triggered  | Yes (after backoff) | Info      | Increase quota? |

---

## 11. Rate Limiting, Quotas & Idempotency

| Endpoint                 | Limit            | Dimension     | Idempotency                       | Notes                  |
| ------------------------ | ---------------- | ------------- | --------------------------------- | ---------------------- |
| `/api/v1/auth/login`     | 5 req/min/IP     | IP + username | Not required                      | Block 10 min on exceed |
| `/api/v1/tickets` (POST) | 60 req/min/token | Token         | `Idempotency-Key` header required | Store key 24h          |

Include retry policy, exponential backoff instructions, detection of quota breaches.

---

## 12. Observability & Operational Logging

| Aspect   | Approach                                            | Tooling / Owner                        |
| -------- | --------------------------------------------------- | -------------------------------------- |
| Logging  | JSON logs with `requestId`, `actorId`, `facilityId` | Logflare/BigQuery, retention 12 months |
| Metrics  | Latency, error rate, rate-limit hits                | Prometheus/Datadog dashboards          |
| Tracing  | Distributed tracing via OpenTelemetry               | Vercel / Supabase integration          |
| Alerting | 5xx > 2% for 5 min, auth failures spike             | PagerDuty, Ops rotation                |

---

## 13. Lifecycle Management & Versioning

- **Versioning Scheme:** Path-based (`/api/v1`), semantic versioning for schema.
- **Backward Compatibility Policy:** Additive changes allowed; breaking changes require `/v2` with deprecation notice (≥90 days).
- **Deprecation Process:** Sunset header, documentation updates, stakeholder notification.
- **Change Control:** ADR required for breaking changes; update traceability matrix.

---

## 14. Testing & Verification Plan

| Test Type             | Scope                 | Tooling           | Owner            | Status             |
| --------------------- | --------------------- | ----------------- | ---------------- | ------------------ |
| Unit Tests            | Handler/service logic | Jest/Vitest       | Backend Engineer | Planned            |
| Contract Tests        | OpenAPI validation    | Prism / Dredd     | QA               | Required           |
| Performance Tests     | Critical endpoints    | k6                | DevOps           | Scheduled          |
| Security Tests        | SAST, DAST, pen test  | CodeQL, OWASP ZAP | Security         | Cadence documented |
| Monitoring Validation | Logs/alerts working   | Synthetic checks  | SRE              | Quarterly          |

Include acceptance criteria for readiness to release (e.g., 0 high severity issues).

---

## 15. Compliance & Data Protection Checklist

- [ ] PII fields catalogued and masked as needed.
- [ ] Data retention automation documented (link to matrix).
- [ ] DPIA / PIA completed (if required).
- [ ] Vendor assessments completed (if using third-party services).
- [ ] Access controls reviewed with Security.
- [ ] API documentation published (developer portal / internal wiki).
- [ ] Service-level agreements agreed with stakeholders.

---

## 16. Change Log

| Version | Date         | Author | Summary           |
| ------- | ------------ | ------ | ----------------- |
| 0.1     | [YYYY-MM-DD] | [Name] | Initial draft     |
| 1.0     | [YYYY-MM-DD] | [Name] | Approved baseline |

---

## 17. Approvals

| Role                            | Name | Signature | Date |
| ------------------------------- | ---- | --------- | ---- |
| Architect / Tech Lead (Approve) |      |           |      |
| Product Owner (Approve)         |      |           |      |
| Security Officer (Concur)       |      |           |      |
| QA Lead (Concur)                |      |           |      |
| DevOps Lead (Concur)            |      |           |      |

---

**Distribution:** Store in `/02-Architecture/API/` and link from Architecture Description, SRS traceability matrix, and developer portal. Update upon major release or when compliance/architecture checkpoints demand.
