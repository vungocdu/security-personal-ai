# Go-Live Readiness Checklist

**MERCURY SOLUTIONS**
**Software Engineering Excellence**

---

## DOCUMENT CONTROL

| Field                 | Value                                           |
| --------------------- | ----------------------------------------------- |
| **Document ID**       | GO-LIVE-[PROJECT]-[YYYY]-[NNN]                  |
| **Template Version**  | 1.0                                             |
| **Document Version**  | [e.g., 1.0]                                     |
| **Project / Release** | [Enter Project Name]                            |
| **Deployment Date**   | [YYYY-MM-DD]                                    |
| **Document Status**   | [Draft / In Review / Approved / Baseline]       |
| **Classification**    | [Public / Internal / Confidential / Restricted] |
| **Author**            | [Name, Role]                                    |
| **Creation Date**     | [YYYY-MM-DD]                                    |
| **Last Updated**      | [YYYY-MM-DD]                                    |
| **Approved By**       | [Name, Role]                                    |
| **Approval Date**     | [YYYY-MM-DD]                                    |
| **Next Review Date**  | [YYYY-MM-DD]                                    |
| **AI-Assisted**       | [ ] Yes - Tool: **\_\_\_** [ ] No               |

---

## ISO STANDARDS COMPLIANCE

**This template satisfies:**

- ✓ ISO/IEC 12207:2017 - Clause 6.4.10 (Transition Process)
- ✓ ISO/IEC 15288:2023 - Clause 6.3.8 (Quality Assurance Process)
- ✓ ISO/IEC 27001:2022 - Annex A 5.30 (ICT Readiness for Business Continuity)
- ✓ ISO 9001:2015 - Clause 8.6 (Release of Products and Services)

**Traceability to:**

- TEMPLATE-LC-005-Deployment_Plan.md
- TEMPLATE-LC-006-Deployment_Readiness_Assessment.md
- TEMPLATE-LC-009-Operational_Runbook.md

---

## 1. PRE-GO-LIVE VALIDATION

| #   | Checklist Item                                                  | Owner                | Status | Evidence |
| --- | --------------------------------------------------------------- | -------------------- | ------ | -------- |
| 1   | Requirements coverage confirmed (BRD/SRS traceability)          | Business Analyst     | [ ]    |          |
| 2   | QA sign-off received; all critical defects resolved             | QA Lead              | [ ]    |          |
| 3   | Performance benchmarks met in staging                           | Performance Engineer | [ ]    |          |
| 4   | Security assessment completed; residual risk accepted           | Security Lead        | [ ]    |          |
| 5   | Data migration rehearsed and validated                          | DBA                  | [ ]    |          |
| 6   | Backups completed and verified                                  | DBA                  | [ ]    |          |
| 7   | Monitoring dashboards configured and alert thresholds validated | SRE Lead             | [ ]    |          |
| 8   | Runbooks updated and reviewed                                   | Operations Lead      | [ ]    |          |

---

## 2. BUSINESS & SUPPORT READINESS

| #   | Checklist Item                                     | Owner               | Status | Evidence |
| --- | -------------------------------------------------- | ------------------- | ------ | -------- |
| 9   | Support teams briefed and knowledge base updated   | Support Manager     | [ ]    |          |
| 10  | Customer communication plan approved and scheduled | Communications Lead | [ ]    |          |
| 11  | On-call schedule updated with contact details      | Service Owner       | [ ]    |          |
| 12  | SLA/SLO updates communicated to stakeholders       | Product Owner       | [ ]    |          |
| 13  | Incident response bridge and channels prepared     | Incident Manager    | [ ]    |          |

---

## 3. TECHNICAL CUTOVER PREP

| #   | Checklist Item                                         | Owner            | Status | Evidence |
| --- | ------------------------------------------------------ | ---------------- | ------ | -------- |
| 14  | Deployment pipeline dry-run completed                  | DevOps Lead      | [ ]    |          |
| 15  | Feature flags configured and default states validated  | Dev Lead         | [ ]    |          |
| 16  | Rollback plan rehearsed or tabletop exercise completed | Release Manager  | [ ]    |          |
| 17  | Dependency services confirmed available and notified   | Integration Lead | [ ]    |          |
| 18  | Capacity and scaling parameters reviewed               | SRE Lead         | [ ]    |          |

---

## 4. GO-LIVE APPROVAL

| Role                  | Name | Decision     | Date | Notes |
| --------------------- | ---- | ------------ | ---- | ----- |
| Release Manager       |      | [Go / No-Go] |      |       |
| Product Owner         |      | [Go / No-Go] |      |       |
| Operations Lead       |      | [Go / No-Go] |      |       |
| Security Lead         |      | [Go / No-Go] |      |       |
| Customer Success Lead |      | [Go / No-Go] |      |       |

---

## 5. POST-GO-LIVE FOLLOW-UP

- Confirm deployment outcome communicated to stakeholders.
- Monitor key metrics for `[duration]` and log findings.
- Schedule post-go-live review no later than `[YYYY-MM-DD]`.
- Update change record with final status and lessons learned.

---

## 6. CHANGE HISTORY

| Version | Date         | Description     | Prepared By | Approved By |
| ------- | ------------ | --------------- | ----------- | ----------- |
| 1.0     | [YYYY-MM-DD] | Initial release | [Name]      | [Name]      |
| 1.1     |              |                 |             |             |
