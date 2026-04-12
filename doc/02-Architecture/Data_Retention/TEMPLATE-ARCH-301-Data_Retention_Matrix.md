# Data Retention Matrix Template

**Document ID:** RET-[PROJECT]-[DATA-DOMAIN]-[YYYY]-[NNN]  
**Template Version:** 1.0.0  
**Standards Alignment:** ISO/IEC 27001:2022 Annex A 5.34 (Information deletion), ISO/IEC/IEEE 42010, ISO/IEC 27701, PDPA/GDPR (as applicable)

---

## Document Control

| Field                  | Value                                   |
| ---------------------- | --------------------------------------- |
| **System / Component** | [System name]                           |
| **Prepared By**        | [Name, Role]                            |
| **Reviewed By**        | [Security Lead, DPO, Legal]             |
| **Document Version**   | [e.g., 0.1 Draft]                       |
| **Status**             | Draft / In Review / Approved / Baseline |
| **Classification**     | Internal / Confidential / Restricted    |
| **Creation Date**      | [YYYY-MM-DD]                            |
| **Last Updated**       | [YYYY-MM-DD]                            |
| **Approval Date**      | [YYYY-MM-DD]                            |
| **Next Review Date**   | [YYYY-MM-DD]                            |
| **AI-Assisted**        | [ ] Yes — Tool: **\_\_** [ ] No         |

---

## 1. Instructions for Use

1. Identify every data entity (tables, collections, files, logs, exports) stored or processed by the system.
2. For each entity, determine legal basis, retention period, storage location, encryption, responsible roles, and deletion process.
3. Note automation (jobs, scripts) enforcing retention and evidence required for audits.
4. Review with Security, DPO/Privacy, and Product to confirm lawful basis and business needs.
5. Update this matrix whenever data categories or regulations change; archive previous versions.
6. Ensure retention controls are referenced in the Security & Privacy Plan and operational runbooks.

**Quality Checklist**

- [ ] All data entities (structured & unstructured) listed.
- [ ] Legal basis documented per regulation/policy.
- [ ] Retention periods measurable and justified.
- [ ] Responsible roles and deletion workflow defined.
- [ ] Automation, evidence, and review cadence captured.
- [ ] Links to supporting SOPs/runbooks provided.
- [ ] Approved by Security + DPO/Privacy.

---

## 2. Data Retention Table

| Data Entity           | PII / Sensitivity        | Legal Basis / Purpose             | Retention Period              | Storage Location     | Encryption                        | Authorized Roles    | Deletion / Anonymization Process         | Evidence / Automation               |
| --------------------- | ------------------------ | --------------------------------- | ----------------------------- | -------------------- | --------------------------------- | ------------------- | ---------------------------------------- | ----------------------------------- |
| [e.g., `users` table] | Yes (name, email, phone) | Contract fulfilment; PDPA consent | 36 months after last activity | [Database / storage] | [Encryption at rest / in transit] | [Roles with access] | [Soft delete + purge job / manual steps] | [Job logs, tickets, audit evidence] |
| [Entity 2]            |                          |                                   |                               |                      |                                   |                     |                                          |                                     |
| [Entity 3]            |                          |                                   |                               |                      |                                   |                     |                                          |                                     |

_Add additional rows as needed._

---

## 3. Automation & Monitoring

| Control                           | Description                                           | Owner          | Frequency     | Evidence Location              |
| --------------------------------- | ----------------------------------------------------- | -------------- | ------------- | ------------------------------ |
| Retention job (`retention:prune`) | [Describe script/cron enforcing retention]            | [DevOps]       | [Monthly]     | [Link to logs/report]          |
| Backup rotation                   | [Snapshots auto-rotated every X days]                 | [DevOps/SRE]   | [Daily]       | [Backup dashboard link]        |
| Export expiry                     | [Mechanism deleting PDPA/GDPR exports after delivery] | [DPO/Security] | [Per request] | [Ticket link / automation log] |
| Access review                     | [Quarterly review of storage access]                  | [Security]     | [Quarterly]   | [Review report location]       |

---

## 4. Compliance Mapping

| Regulation / Policy             | Clause                                            | Implementation Evidence |
| ------------------------------- | ------------------------------------------------- | ----------------------- |
| ISO/IEC 27001:2022 Annex A 5.34 | Information deletion implemented via [jobs/SOP]   | [Evidence reference]    |
| PDPA (Singapore)                | Purpose limitation & retention obligations        | [Procedure reference]   |
| GDPR Article 17 (if applicable) | Right to erasure supported via [endpoint/runbook] | [Ticketing workflow]    |
| Corporate Policy [ID]           | Data retention standard                           | [Policy link]           |

---

## 5. Review & Audit Log

| Date         | Reviewer | Summary          | Actions / Tickets |
| ------------ | -------- | ---------------- | ----------------- |
| [YYYY-MM-DD] | [Name]   | [Review outcome] | [Links]           |
|              |          |                  |                   |

---

## 6. Approvals

| Role                                    | Name | Signature | Date |
| --------------------------------------- | ---- | --------- | ---- |
| Security Lead (Approve)                 |      |           |      |
| DPO / Privacy Officer (Approve)         |      |           |      |
| Product Owner / Business Owner (Concur) |      |           |      |
| DevOps Lead (Concur)                    |      |           |      |

---

**Distribution:** Store approved version under `/02-Architecture/Data_Retention/` and reference from Security & Privacy Plan, operational runbooks, and audit packets. Update change log when revisions occur.
