# Risk Register Template

**Document ID:** RISK-[PROJECT]-[SYSTEM]-[YYYY]-[NNN]  
**Template Version:** 1.0.0  
**Standards Alignment:** ISO/IEC 27001:2022 (Risk Management), ISO/IEC 12207/15288 (Project Risk), ISO 31000

---

## Document Control

| Field                  | Value                                             |
| ---------------------- | ------------------------------------------------- |
| **System / Component** | [System name]                                     |
| **Prepared By**        | [Risk owner / Project Manager]                    |
| **Reviewed By**        | [Architecture Lead, Security Lead, Product Owner] |
| **Document Version**   | [0.1 Draft]                                       |
| **Status**             | Draft / In Review / Approved / Baseline           |
| **Classification**     | Internal / Confidential / Restricted              |
| **Creation Date**      | [YYYY-MM-DD]                                      |
| **Last Updated**       | [YYYY-MM-DD]                                      |
| **Approval Date**      | [YYYY-MM-DD]                                      |
| **Next Review Date**   | [YYYY-MM-DD]                                      |
| **AI-Assisted**        | [ ] Yes — Tool: **\_\_** [ ] No                   |

---

## Instructions for Use

1. Identify risks across people, process, technology, vendors, compliance, and operations.
2. Assess likelihood & impact (use consistent scale L/M/H or numeric).
3. Document mitigation/controls and residual status (Active, Monitoring, Closed, Accepted).
4. Link to evidence (tickets, ADRs, runbooks) for auditability.
5. Review at least quarterly or when major changes occur.
6. Escalate High residual risks to leadership per governance policy.

**Quality Checklist**

- [ ] Risk descriptions are clear and actionable.
- [ ] Likelihood/impact scored consistently.
- [ ] Owners assigned and aware.
- [ ] Mitigation plans documented with timelines.
- [ ] Residual status tracked; accepted risks approved.
- [ ] Evidence links provided.
- [ ] Review cadence and next steps recorded.

---

## 1. Risk Log

| Risk ID  | Description                                 | Likelihood | Impact | Owner           | Mitigation / Controls                          | Residual Status | Target Resolution / Review | Evidence       |
| -------- | ------------------------------------------- | ---------- | ------ | --------------- | ---------------------------------------------- | --------------- | -------------------------- | -------------- |
| RISK-001 | [e.g., Key staff attrition delays delivery] | Medium     | High   | Product Manager | Cross-training, documentation, succession plan | Monitoring      | [YYYY-MM-DD]               | [Link to plan] |
| RISK-002 |                                             |            |        |                 |                                                |                 |                            |                |
| RISK-003 |                                             |            |        |                 |                                                |                 |                            |                |

_Add rows as necessary._

---

## 2. Risk Heat Map (Optional)

| Impact \ Likelihood | Low             | Medium | High |
| ------------------- | --------------- | ------ | ---- |
| **High Impact**     | [List risk IDs] |        |      |
| **Medium Impact**   |                 |        |      |
| **Low Impact**      |                 |        |      |

---

## 3. Mitigation Plan Tracking

| Risk ID  | Action Item                             | Owner   | Due Date     | Status      | Notes                 |
| -------- | --------------------------------------- | ------- | ------------ | ----------- | --------------------- |
| RISK-001 | [e.g., Complete cross-training for Ops] | [Owner] | [YYYY-MM-DD] | In Progress | [Link to task/ticket] |
|          |                                         |         |              |             |                       |

---

## 4. Accepted Risks & Rationale

| Risk ID  | Reason for Acceptance                     | Approval      | Expiry / Revisit Date | Monitoring Approach |
| -------- | ----------------------------------------- | ------------- | --------------------- | ------------------- |
| RISK-00A | [e.g., Third-party SLA for minor service] | [Name / Role] | [YYYY-MM-DD]          | [Metric / alert]    |

---

## 5. Review & Audit Log

| Date         | Participants | Summary    | Decisions / Actions   |
| ------------ | ------------ | ---------- | --------------------- |
| [YYYY-MM-DD] | [Names]      | [Findings] | [Next steps, tickets] |
|              |              |            |                       |

---

## 6. Approvals

| Role                          | Name | Signature | Date |
| ----------------------------- | ---- | --------- | ---- |
| Architecture Lead (Approve)   |      |           |      |
| Security Lead (Concur)        |      |           |      |
| Product Owner (Concur)        |      |           |      |
| Project Manager (Responsible) |      |           |      |
| Executive Sponsor (Informed)  |      |           |      |

---

**Distribution:** Store in `/02-Architecture/` and link from Architecture Description, Compliance Matrix, and Security & Privacy Plan. Update after risk workshops or major releases.
