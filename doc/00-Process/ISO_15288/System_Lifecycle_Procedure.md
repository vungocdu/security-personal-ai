# System Lifecycle Procedure (ISO/IEC 15288:2023)

**Document ID**: PROC-SLC-001  
**Owner**: Systems Engineering Lead  
**Version**: 1.0  
**Status**: Approved  
**Last Updated**: 2025-10-24  
**Standards**: ISO/IEC 15288:2023, ISO/IEC 12207:2017, ISO/IEC/IEEE 42010, ISO/IEC 27001:2022  
**Related Documents**: ISO/IEC 12207 SDLC Procedure, Quality Manual (QM-001), ISMS-001, TEMPLATE-ARCH-001-Architecture_Design.md

---

## 1. Purpose

Define Mercury Solution's system lifecycle process in alignment with ISO/IEC 15288:2023, ensuring system-of-systems coordination, traceability to requirements, and governance across technical and management processes.

---

## 2. Scope

### 2.1 Applicability

This procedure applies to:

- Solutions integrating multiple software/hardware services
- Cross-domain initiatives (e.g., Ticketing + CDP + Revenue Management)
- Systems involving external partners/vendors
- AI-enabled subsystems requiring coordinated governance

### 2.2 Processes Covered (ISO/IEC 15288 Clause 6.1–6.4)

- Agreement Processes (Acquisition, Supply)
- Organizational Project-Enabling Processes
- Technical Management Processes
- Technical Processes (Business Analysis through Disposal)

---

## 3. Normative References

| Reference          | Title                           |
| ------------------ | ------------------------------- |
| ISO/IEC 15288:2023 | System life cycle processes     |
| ISO/IEC 12207:2017 | Software life cycle processes   |
| ISO/IEC/IEEE 42010 | Architecture description        |
| ISO/IEC/IEEE 29148 | Requirements engineering        |
| ISO/IEC 27001:2022 | Information security management |
| ISO/IEC 27701:2019 | Privacy information management  |

---

## 4. Roles & Responsibilities

| Role                     | Responsibilities                                           | Key Artefacts                                                                      |
| ------------------------ | ---------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Systems Engineering Lead | Own lifecycle tailoring, integration strategy              | TEMPLATE-ARCH-001-Architecture_Design.md                                           |
| Program Manager          | Coordinate multi-project schedule, risk, vendor engagement | TEMPLATE-ARCH-501-Risk_Register.md, Compliance_Matrix_ISO.md                       |
| Architecture Board       | Approve system architecture, interface contracts           | TEMPLATE-ARCH-101-Architecture_Decision_Record.md, TEMPLATE-ARCH-102-API_Design.md |
| Data Protection Officer  | Validate privacy & retention controls                      | TEMPLATE-ARCH-301-Data_Retention_Matrix.md                                         |
| Security Lead            | Threat modelling, security controls, incident readiness    | TEMPLATE-ARCH-401-Security_Privacy_Plan.md                                         |
| Vendor Manager           | Acquisition, partner governance, contract SLAs             | Agreement plan (Section 6.1)                                                       |
| Quality Manager          | Lifecycle quality metrics, audits                          | QM-001, Compliance_Matrix_ISO.md                                                   |

---

## 5. Lifecycle Tailoring Overview

### 5.1 Stage Gates

1. **Concept Approval** – Business case, stakeholder map, preliminary risk register
2. **Architecture Baseline** – Approved system architecture & ADRs, security/privacy plans
3. **Integration Readiness** – Interface contracts, data models, test strategy complete
4. **Operational Readiness** – Deployment plan, SLO/SLI, incident runbooks, retention jobs validated
5. **Lifecycle Reviews** – Periodic validation of risk/residual, compliance evidence, disposal planning

### 5.2 Artefact Checklist per Gate

- Concept: Business goals, stakeholder needs, high-level risk entries
- Architecture: TEMPLATE-ARCH-001, TEMPLATE-ARCH-101, TEMPLATE-ARCH-102, data model templates
- Integration: Contract specs, RBAC matrix, security/privacy plan updates, retention matrix approval
- Operation: Deployment & runbook templates, observability plans, incident postmortem template readiness
- Lifecycle: Disposal strategy, knowledge transfer records, archival per retention matrix

---

## 6. Process Activities (ISO/IEC 15288 Clauses)

### 6.1 Agreement Processes (Acquisition & Supply)

- **Outputs**: Vendor assessment, SoW, SLA tracking sheet
- **Artefacts**: Procurement checklist, change impact assessment
- **Controls**: Vendor risk entries in TEMPLATE-ARCH-501-Risk_Register.md

### 6.2 Organizational Project-Enabling Processes

- Portfolio alignment with Quality Manual (QM-001) and Compliance Matrix
- Infrastructure management with TEMPLATE-LC-004-Configuration_Management.md
- Knowledge management via documented templates & ADRs

### 6.3 Technical Management Processes

- Project planning: Integrated roadmap, dependency matrix
- Risk management: Trace risks to mitigation tasks, maintain evidence in risk register template
- Configuration management: Versioned templates, ADR change log, template usage mapped in traceability matrix
- Measurement: Service KPIs, SLO/SLI, retention job success rate, security drill outcomes

### 6.4 Technical Processes

| Clause | Process                      | Key Activities                                      | Artefacts                                                                |
| ------ | ---------------------------- | --------------------------------------------------- | ------------------------------------------------------------------------ |
| 6.4.1  | Business or Mission Analysis | Scenario modelling, stakeholder needs               | Business case, stakeholder map                                           |
| 6.4.2  | Stakeholder Requirements     | Consolidate SRS entries, align across subsystems    | SRS templates, traceability matrix                                       |
| 6.4.3  | System Requirements          | Harmonise functional/non-functional requirements    | SRS + NFR criteria                                                       |
| 6.4.4  | Architecture Definition      | Produce system architecture, interface, data models | TEMPLATE-ARCH-001, 102, 201/202/203                                      |
| 6.4.5  | Design Definition            | Detailed subsystem LLDs, interface design           | LLD templates, ADRs                                                      |
| 6.4.6  | System Analysis              | Trade-off studies, simulation results               | ADR rationale, risk updates                                              |
| 6.4.7  | Implementation               | Coordination of subsystem builds                    | Dev checklists, CI/CD plan                                               |
| 6.4.8  | Integration                  | Integration strategy across services                | Integration plan, contract tests                                         |
| 6.4.9  | Verification                 | Cross-subsystem verification plan                   | TEMPLATE-LC-011-Test_Plan_VnV.md, contract test results                  |
| 6.4.10 | Transition                   | Deployment runbooks, go-live proofs                 | TEMPLATE-LC-005-Deployment_Plan.md, TEMPLATE-LC-007-Go_Live_Checklist.md |
| 6.4.11 | Operation                    | SLO monitoring, incident response                   | TEMPLATE-LC-008-SLO_SLI_Plan.md, Runbook templates                       |
| 6.4.12 | Maintenance                  | Change management, backlog triage                   | Change impact assessments                                                |
| 6.4.13 | Disposal                     | Data archival/disposal per retention template       | Disposal checklist, retention reports                                    |

---

## 7. Tailoring & Compliance Guidance

- Tailor lifecycle stages using PROC-SDLC-001 and this procedure; document tailoring decisions in ADRs.
- Maintain mapping in Compliance_Matrix_ISO.md for audit readiness.
- Ensure all templates (architecture, security, retention, risk) are baselined before release milestones.
- Record deviations and approvals in the risk register and governance meeting minutes.

---

## 8. Evidence & Review Cadence

| Review Type               | Frequency                 | Participants                               | Artefacts Reviewed              |
| ------------------------- | ------------------------- | ------------------------------------------ | ------------------------------- |
| Lifecycle Gate Review     | At each stage             | Architecture Board, Product, Security, DPO | Alignment to artefact checklist |
| Risk Review               | Quarterly                 | Program Manager, Security, DPO             | TEMPLATE-ARCH-501 risk entries  |
| Security & Privacy Review | Quarterly or major change | Security Lead, DPO                         | TEMPLATE-ARCH-401, RBAC matrix  |
| Data Retention Audit      | Quarterly                 | DevOps, Security, DPO                      | TEMPLATE-ARCH-301 evidence logs |

---

## 9. Records & Archives

- Approved templates stored under `/02-Architecture/` tree with versioning.
- Governance meeting notes archived in project collaboration space with links to artefacts.
- Evidence of compliance (retention jobs, security drills, risk reviews) stored under `/security/` or `/compliance/` repositories.
- Disposal records maintained per retention matrix requirements.

---

## 10. Approvals

| Role                     | Name | Signature | Date |
| ------------------------ | ---- | --------- | ---- |
| Systems Engineering Lead |      |           |      |
| Program Manager          |      |           |      |
| Architecture Lead        |      |           |      |
| Security Lead            |      |           |      |
| Quality Manager          |      |           |      |
| DPO / Privacy Officer    |      |           |      |

---

**Distribution:** Publish in knowledge base, reference in Compliance Matrix and SDLC procedure, and brief project teams during kickoff. Update following governance changes or regulatory updates.
