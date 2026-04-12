# ADR-XXXX: <Decision Title>

**Document Purpose:** Capture architecture decisions per ISO/IEC/IEEE 42010 & ISO/IEC 12207 (Architecture Definition) ensuring traceability to requirements (ISO/IEC/IEEE 29148) and security controls (ISO/IEC 27001).

---

## 0. Decision Metadata

| Field                         | Value                                                    |
| ----------------------------- | -------------------------------------------------------- |
| **Decision Owner**            | [Name, Role]                                             |
| **Authors / Contributors**    | [Names; include AI agent IDs if applicable]              |
| **Date Raised**               | [YYYY-MM-DD]                                             |
| **Status**                    | Proposed / Accepted / Rejected / Superseded / Deprecated |
| **Supersedes / Related ADRs** | [ADR-XXX, if any]                                        |
| **Review Cadence**            | [e.g., Annual, On major release]                         |
| **Next Review Date**          | [YYYY-MM-DD]                                             |
| **Linked Artefacts**          | [AD section, SRS requirement IDs, Jira ticket]           |

---

## 1. Context & Problem Statement

- **Business / Technical drivers:**  
  [Summarize goals, constraints, SLA, compliance obligations.]
- **Requirements Impacted:**
  - FR-XXX-###
  - NFR-YYY-###
  - SEC-ZZZ-### (ISO 27001/PDPA)
- **Current Pain Points / Gaps:**  
  [What limitations exist without this decision?]

---

## 2. Decision Drivers

List the criteria influencing the decision (weight or priority optional).

| Driver  | Description                              | Priority (H/M/L) |
| ------- | ---------------------------------------- | ---------------- |
| Example | Meet P95 latency < 400 ms (NFR-PERF-001) | High             |
|         | Align with existing team skillset        | Medium           |
|         | Minimize vendor lock-in                  | Low              |

---

## 3. Considered Options

### 3.1 Option A — `<Name>`

- **Description:**  
  [Outline architecture/pattern/tool]
- **Pros:**
  - [Advantage 1]
  - [Advantage 2]
- **Cons / Risks:**
  - [Risk 1]
  - [Risk 2]
- **Compliance Impact:**  
  [How does it align with ISO controls, PDPA, etc.]

### 3.2 Option B — `<Name>`

[Repeat block for each option considered (min. two options per ISO 42010 guidance)]

---

## 4. Decision

- **Chosen Option:** `<Option Name>`
- **Rationale:**  
  [Explain why, referencing decision drivers and evidence.]
- **Scope:**  
  [Components/services/environments impacted]
- **Assumptions:**
  - [Assumption 1]
  - [Assumption 2]

---

## 5. Consequences

| Category              | Positive  | Negative / Mitigation   |
| --------------------- | --------- | ----------------------- |
| Technical             | [Benefit] | [Drawback + mitigation] |
| Operational           |           |                         |
| Security / Compliance |           |                         |
| Cost                  |           |                         |

**Follow-up Actions:**

- [ ] Update Architecture Description (§X.X).
- [ ] Adjust Data Model / API contracts.
- [ ] Schedule security review / pen test.
- [ ] Communicate to stakeholders (Product, QA, Ops).

---

## 6. Implementation Notes

- **Work Breakdown / Milestones:**  
  [Epics, tickets, feature flags, rollout plan]
- **Testing Implications:**  
  [Unit/integration tests, contract tests, load tests]
- **Migration / Rollback Strategy:**  
  [Expand-contract, blue/green, data migration plan]

---

## 7. Compliance & Traceability Checklist

- [ ] Linked SRS requirement IDs updated (ISO/IEC/IEEE 29148).
- [ ] AD sections reference this ADR (ISO/IEC 42010).
- [ ] Data retention / classification implications assessed.
- [ ] Security controls mapped to ISO/IEC 27001 Annex A.
- [ ] Risk Register updated if new residual risks introduced.

---

## 8. Review & Approval

| Role                  | Name | Decision / Sign-off   | Date | Notes |
| --------------------- | ---- | --------------------- | ---- | ----- |
| Architect / Tech Lead |      | Approve / Reject      |      |       |
| Product Owner         |      | Approve / Acknowledge |      |       |
| Security Officer      |      | Concur / Review       |      |       |
| DevOps Lead           |      | Inform / Concur       |      |       |

---

**Change Log**

| Version | Date         | Author | Summary       |
| ------- | ------------ | ------ | ------------- |
| 0.1     | [YYYY-MM-DD] | [Name] | Initial draft |
| 1.0     | [YYYY-MM-DD] | [Name] | Accepted      |
