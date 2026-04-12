# Change Impact Assessment

**MERCURY SOLUTIONS**
**Software Engineering Excellence**

---

## DOCUMENT CONTROL

| Field                | Value                                           |
| -------------------- | ----------------------------------------------- |
| **Document ID**      | CIA-[PROJECT]-[YYYY]-[NNN]                      |
| **Template Version** | 1.0                                             |
| **Document Version** | [e.g., 1.0]                                     |
| **Change ID**        | [CHG-YYYY-NNN]                                  |
| **Requester**        | [Name, Role]                                    |
| **Document Status**  | [Draft / In Review / Approved / Baseline]       |
| **Classification**   | [Public / Internal / Confidential / Restricted] |
| **Creation Date**    | [YYYY-MM-DD]                                    |
| **Last Updated**     | [YYYY-MM-DD]                                    |
| **Approved By**      | [Name, Role]                                    |
| **Approval Date**    | [YYYY-MM-DD]                                    |
| **Next Review Date** | [YYYY-MM-DD]                                    |
| **AI-Assisted**      | [ ] Yes - Tool: **\_\_\_** [ ] No               |

---

## ISO STANDARDS COMPLIANCE

**This template satisfies:**

- ✓ ISO/IEC 12207:2017 - Clause 6.3.5 (Configuration Management Process)
- ✓ ISO/IEC 15288:2023 - Clause 6.3.5 (Configuration Management Process)
- ✓ ISO/IEC 27001:2022 - Annex A 8.32 (Change Management)
- ✓ ISO 9001:2015 - Clause 8.5.6 (Control of Changes)

**Traceability to:**

- TEMPLATE-LC-004-Configuration_Management.md
- TEMPLATE-LC-005-Deployment_Plan.md
- QM-001 Section 7.5 (Documented Information)

---

## 1. CHANGE SUMMARY

| Field                              | Details                                                  |
| ---------------------------------- | -------------------------------------------------------- |
| **Title**                          | [Enter change title]                                     |
| **Business Driver**                | [Customer request / Incident / Compliance / Enhancement] |
| **Change Category**                | [Standard / Normal / Emergency]                          |
| **Implementation Window**          | [YYYY-MM-DD HH:MM - time zone]                           |
| **Related Tickets / References**   | [Jira/Linear IDs, Incident IDs]                          |
| **Services / Components Affected** | [List impacted services]                                 |

> **Guidance:** Provide a concise description of why the change is required and the intended business or technical outcome.

---

## 2. SCOPE & AFFECTED ARTIFACTS

- **Requirements:** [Link to REQ IDs, BRD sections]
- **Design & Architecture:** [ADRs, Architecture docs]
- **Code Modules / Repos:** [Repositories, packages, modules]
- **Infrastructure / Configuration:** [Terraform modules, Helm charts, environment variables]
- **Data Assets:** [Databases, schemas, PII classification]
- **Operational Assets:** [Runbooks, SOPs, monitoring dashboards]

---

## 3. IMPACT ASSESSMENT

| Dimension               | None | Low | Medium | High | Notes / Evidence |
| ----------------------- | ---- | --- | ------ | ---- | ---------------- |
| Scope                   | [ ]  | [ ] | [ ]    | [ ]  |                  |
| Schedule                | [ ]  | [ ] | [ ]    | [ ]  |                  |
| Cost / Effort           | [ ]  | [ ] | [ ]    | [ ]  |                  |
| Service Availability    | [ ]  | [ ] | [ ]    | [ ]  |                  |
| Quality                 | [ ]  | [ ] | [ ]    | [ ]  |                  |
| Security & Privacy      | [ ]  | [ ] | [ ]    | [ ]  |                  |
| Regulatory / Compliance | [ ]  | [ ] | [ ]    | [ ]  |                  |
| Dependencies            | [ ]  | [ ] | [ ]    | [ ]  |                  |

**Risk Statement:** `[If <condition>, then <impact>, caused by <source>.]`

**Mitigations:** `[List controls, compensating measures, or defer decisions.]`

---

## 4. VALIDATION & TEST STRATEGY

| Test Type                    | Entry Criteria | Exit Criteria | Owner | Evidence |
| ---------------------------- | -------------- | ------------- | ----- | -------- |
| Unit Tests                   |                |               |       |          |
| Integration / Contract Tests |                |               |       |          |
| Performance / Load           |                |               |       |          |
| Security Testing             |                |               |       |          |
| User Acceptance              |                |               |       |          |

- **Test Environment:** [Dev / QA / Staging]
- **Data Requirements:** [Synthetic / Masked / Production copy]
- **Automation Coverage:** [Percentage or scope statement]

---

## 5. IMPLEMENTATION PLAN

1. `[Step-by-step execution tasks with owners and estimated durations]`
2. `[Include validation checkpoints and decision gates]`
3. `[Confirm release communication plan and stakeholder notifications]`

**Deployment Method:** [Canary / Blue-Green / Rolling / Manual]  
**Automation Pipeline:** [Link to pipeline job or workflow]  
**Pre-Deployment Checklist:** [Reference TEMPLATE-LC-005-Deployment_Plan.md]

---

## 6. ROLLBACK & CONTINGENCY

- **Rollback Trigger:** `[Define measurable condition for rollback]`
- **Rollback Procedure:** `[Enumerate commands, scripts, or restore actions]`
- **Data Recovery Plan:** `[Backups, restore points, verification steps]`
- **Communication Plan:** `[Notify stakeholders, incident management invocation]`

---

## 7. APPROVALS

| Role                | Name | Decision              | Date | Notes |
| ------------------- | ---- | --------------------- | ---- | ----- |
| Change Manager      |      | [Approved / Rejected] |      |       |
| Service Owner       |      | [Approved / Rejected] |      |       |
| QA Lead             |      | [Approved / Rejected] |      |       |
| Security Lead / DPO |      | [Approved / Rejected] |      |       |
| Release Manager     |      | [Approved / Rejected] |      |       |

---

## 8. CHANGE LOG

| Version | Date         | Description     | Prepared By | Notes |
| ------- | ------------ | --------------- | ----------- | ----- |
| 1.0     | [YYYY-MM-DD] | Initial release | [Name]      |       |
| 1.1     |              |                 |             |       |
