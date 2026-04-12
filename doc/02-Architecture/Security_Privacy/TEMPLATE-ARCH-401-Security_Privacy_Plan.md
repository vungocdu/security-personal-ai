# Security & Privacy Plan Template

**Document ID:** SEC-[PROJECT]-[SYSTEM]-[YYYY]-[NNN]  
**Template Version:** 1.0.0  
**Standards Alignment:** ISO/IEC 27001:2022, ISO/IEC 27002, ISO/IEC 12207/15288 (Security & Operation), ISO/IEC 27701, PDPA/GDPR (as applicable)

---

## Document Control

| Field                  | Value                                   |
| ---------------------- | --------------------------------------- |
| **System / Component** | [System name]                           |
| **Prepared By**        | [Security lead / Architect]             |
| **Reviewed By**        | [DPO, DevOps Lead, Product Owner]       |
| **Document Version**   | [0.1 Draft]                             |
| **Status**             | Draft / In Review / Approved / Baseline |
| **Classification**     | Internal / Confidential / Restricted    |
| **Creation Date**      | [YYYY-MM-DD]                            |
| **Last Updated**       | [YYYY-MM-DD]                            |
| **Approval Date**      | [YYYY-MM-DD]                            |
| **Next Review Date**   | [YYYY-MM-DD]                            |
| **AI-Assisted**        | [ ] Yes — Tool: **\_\_** [ ] No         |

---

## 1. Threat Model Summary

| Asset / Surface     | Primary Threats (STRIDE)   | Existing Controls   | Gaps / Action Items |
| ------------------- | -------------------------- | ------------------- | ------------------- |
| [e.g., API Gateway] | [Spoofing, tampering, DoS] | [Controls in place] | [Remediation plan]  |
| [Data store]        |                            |                     |                     |

**Abuse / Misuse Cases:**

1. [Scenario – e.g., credential stuffing] → [Mitigation]
2. [Scenario] → [Mitigation]

---

## 2. Authentication & Authorization

| Area                   | Policy / Design                                       | Evidence / Reference                          |
| ---------------------- | ----------------------------------------------------- | --------------------------------------------- |
| Authentication Methods | [OIDC, SSO, Supabase Auth, JWT TTL, MFA requirements] | [Link to documentation]                       |
| Session Management     | [Cookie settings, token rotation, logout process]     |                                               |
| Authorization Model    | [RBAC/ABAC roles & scopes]                            | `Security_Privacy/RBAC_Matrix_By_Endpoint.md` |
| Secrets Management     | [Secret store, rotation cadence, ownership]           | [Runbook link]                                |
| Administrative Access  | [Break-glass, dual control]                           |                                               |

---

## 3. Data Protection (PII, Encryption, Masking)

| Control                | Implementation                                                                                                     | Verification / Owner             |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------ | -------------------------------- |
| PII Inventory          | [Link to PII map, tagging approach]                                                                                | [Review cadence]                 |
| Encryption In Transit  | [TLS version, certificate management]                                                                              | [SSL scans / monitoring]         |
| Encryption At Rest     | [Database/storage encryption, key management]                                                                      | [Attestation / audit]            |
| Data Minimization      | [Field-level masking, data redaction]                                                                              | [Automated tests, manual review] |
| Tokenization / Masking | [Sensitive field treatment]                                                                                        | [Testing / monitoring]           |
| Data Retention         | Reference `/02-Architecture/Data_Retention/TEMPLATE-ARCH-301-Data_Retention_Matrix.md` and project-specific matrix | [Retention job evidence]         |
| Backups & Recovery     | [Backup cadence, storage, restore testing]                                                                         | [Runbook results]                |

---

## 4. Audit & Logging

| Topic               | Details                                                         |
| ------------------- | --------------------------------------------------------------- |
| Log Scope           | [Events captured: auth, privilege changes, data access, errors] |
| Log Format          | [Structured JSON, correlation IDs, PII policy]                  |
| Storage & Retention | [Log platform, retention period, access controls]               |
| Monitoring & Alerts | [Use cases, thresholds, escalation path]                        |
| Audit Trail         | [Entities tracked, change history, export capabilities]         |
| Review Cadence      | [Weekly ops review, quarterly security review]                  |

---

## 5. Vulnerability & Patch Management

| Activity                        | Cadence                   | Tooling               | Owner               | Notes |
| ------------------------------- | ------------------------- | --------------------- | ------------------- | ----- |
| Dependency Scanning             | [Per CI run / weekly]     | [Dependency scanner]  | [Tech Lead]         |       |
| SAST                            | [Per PR]                  | [Tool]                | [Security]          |       |
| DAST                            | [Quarterly / release]     | [Tool]                | [Security]          |       |
| Penetration Testing             | [Annually / major change] | [Vendor / internal]   | [Security Lead]     |       |
| Infrastructure Hardening Review | [Semi-annual]             | [Checklist]           | [DevOps + Security] |       |
| Patch Management                | [Monthly]                 | [Process description] | [DevOps]            |       |
| Incident Response Drill         | [Semi-annual]             | [Runbook reference]   | [DevOps + Product]  |       |

Remediation Workflow: [Describe discovery → ticketing → fix → verification → closure].

---

## 6. Compliance & Evidence Checklist

- [ ] RBAC matrix approved (link).
- [ ] Data retention automation documented (link).
- [ ] Vulnerability scan & pen test reports stored (location).
- [ ] Incident response contacts verified (date).
- [ ] Quarterly access reviews logged (link).
- [ ] DPIA/PIA completed (link).
- [ ] Encryption configuration documented (link).

**Owner:** [Security Lead]; **Review Frequency:** [Quarterly].

---

## 7. Residual Risks & Exceptions

| Risk ID        | Description   | Mitigation / Acceptance            | Owner   | Review Date  |
| -------------- | ------------- | ---------------------------------- | ------- | ------------ |
| [RISK-SEC-001] | [Risk detail] | [Accepted / Mitigated via control] | [Owner] | [YYYY-MM-DD] |

---

## 8. Approvals

| Role                            | Name | Signature | Date |
| ------------------------------- | ---- | --------- | ---- |
| Security Lead (Approve)         |      |           |      |
| DPO / Privacy Officer (Approve) |      |           |      |
| Tech Lead / Architect (Concur)  |      |           |      |
| DevOps Lead (Concur)            |      |           |      |
| Product Owner (Informed)        |      |           |      |

---

**Distribution:** Store approved plan in `/02-Architecture/Security_Privacy/`, link from Architecture Description, Risk Register, and operational runbooks. Update after major architectural or regulatory changes.
