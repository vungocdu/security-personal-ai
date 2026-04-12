# Software Development Lifecycle Procedure

**Document ID**: PROC-SDLC-001
**Owner**: Development Team Lead
**Version**: 1.0
**Status**: Approved
**Last Updated**: 2025-10-24
**Standard**: ISO/IEC 12207:2017
**Related**: QM-001, PROC-AI-001, ISO/IEC 15288:2023

---

## 1. PURPOSE

This procedure defines the software development lifecycle (SDLC) process for Mercury Solution, aligned with ISO/IEC 12207:2017 software life cycle processes and adapted for AI-assisted development practices.

---

## 2. SCOPE

### 2.1 Applicability

This procedure applies to all software development projects at Mercury Solution, including:

- New product development
- Major feature enhancements
- System integrations
- Microservices development
- AI-assisted and traditional development

### 2.2 Process Coverage

This procedure addresses ISO/IEC 12207:2017 Technical Processes:

- 6.4.1 Business or Mission Analysis
- 6.4.2 Stakeholder Needs and Requirements Definition
- 6.4.3 System/Software Requirements Definition
- 6.4.4 Architecture Definition
- 6.4.5 Design Definition
- 6.4.6 System Analysis
- 6.4.7 Implementation
- 6.4.8 Integration
- 6.4.9 Verification
- 6.4.10 Transition (Deployment)
- 6.4.11 Validation
- 6.4.12 Operation
- 6.4.13 Maintenance

---

## 3. NORMATIVE REFERENCES

- ISO/IEC 12207:2017 - Systems and software engineering — Software life cycle processes
- ISO/IEC 15288:2023 - Systems and software engineering — System life cycle processes
- ISO/IEC/IEEE 29148:2018 - Systems and software engineering — Life cycle processes — Requirements engineering
- ISO/IEC 25010:2011 - Systems and software Quality Requirements and Evaluation (SQuaRE)
- ISO/IEC 27001:2022 - Information security management
- Mercury Solution Quality Manual (QM-001)
- AI-Assisted Development Procedure (PROC-AI-001)

---

## 4. DEFINITIONS

### 4.1 Software Development Lifecycle (SDLC)

The framework defining the process for planning, creating, testing, deploying, and maintaining software systems from conception through retirement.

### 4.2 Iteration

A time-boxed development cycle (typically 1-4 weeks) in which a planned set of requirements is implemented, integrated, tested, and potentially deployed.

### 4.3 Baseline

An approved version of a work product that serves as the basis for further development and can be changed only through formal change control procedures.

### 4.4 Traceability

The ability to relate work products bidirectionally (e.g., requirements to design to code to tests).

### 4.5 Verification

Confirmation through objective evidence that specified requirements have been fulfilled (building it right).

### 4.6 Validation

Confirmation through objective evidence that requirements for a specific intended use are fulfilled (building the right thing).

---

## 5. ROLES AND RESPONSIBILITIES

| Role                             | Responsibilities                                                         | Deliverables                                                  |
| -------------------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------- |
| **Product Owner**                | Define business objectives, prioritize requirements, accept deliverables | Product vision, prioritized backlog                           |
| **Project Manager**              | Plan, monitor, control project; manage risks and stakeholders            | Project plan, status reports, risk register                   |
| **Requirements Engineer**        | Elicit, analyze, document, validate requirements                         | SRS, traceability matrix                                      |
| **Architect**                    | Define system architecture, make technical decisions                     | AD, ADRs, architecture diagrams                               |
| **Developer**                    | Design, implement, unit test software                                    | Code, unit tests, LLD                                         |
| **QA Specialist**                | Verify and validate software quality                                     | Test plans, test cases, test reports                          |
| **DevOps Engineer**              | Build CI/CD pipelines, manage deployments                                | CI/CD configuration, deployment scripts                       |
| **Information Security Officer** | Define security requirements, review designs/code                        | Security requirements, threat models, security review reports |
| **AI Integration Specialist**    | Oversee AI-assisted development quality                                  | AI quality metrics, process guidance                          |

**RACI Matrix**: See `/03-Lifecycle/Runbook/RACI_Matrix.md` for detailed assignments.

---

## 6. SDLC PHASES AND ACTIVITIES

### 6.1 Phase 1: Business and Mission Analysis (ISO 12207:6.4.1)

#### 6.1.1 Purpose

Understand the business problem or opportunity, identify stakeholders, and establish the business case.

#### 6.1.2 Activities

| Activity                        | Description                                              | Inputs                               | Outputs                | Responsible       |
| ------------------------------- | -------------------------------------------------------- | ------------------------------------ | ---------------------- | ----------------- |
| **Identify Stakeholders**       | Identify all parties with interest or influence          | Market analysis, org chart           | Stakeholder list       | Product Owner, PM |
| **Understand Business Context** | Analyze business environment, constraints, opportunities | Business strategy, market trends     | Context analysis       | Product Owner     |
| **Define Business Objectives**  | Articulate what the organization wants to achieve        | Stakeholder needs, strategic goals   | Business objectives    | Product Owner     |
| **Establish Business Case**     | Justify investment in software solution                  | Cost estimates, benefits analysis    | Business case document | Product Owner, PM |
| **Identify Constraints**        | Document technical, budget, schedule, regulatory limits  | Organizational policies, regulations | Constraints list       | PM, Architect     |

#### 6.1.3 Outputs

- Stakeholder list with roles and interests
- Business objectives statement
- Business case (problem, solution approach, benefits, costs, timeline)
- Constraints and assumptions

#### 6.1.4 Approval Criteria

- Stakeholders identified and confirmed
- Business objectives align with organizational strategy
- Business case approved by sponsoring executive
- Constraints documented and acknowledged

---

### 6.2 Phase 2: Stakeholder Needs and Requirements (ISO 12207:6.4.2)

#### 6.2.1 Purpose

Elicit, analyze, and document stakeholder needs and convert into stakeholder requirements.

#### 6.2.2 Activities

| Activity                            | Description                                                           | Inputs                                   | Outputs                           | Responsible                          |
| ----------------------------------- | --------------------------------------------------------------------- | ---------------------------------------- | --------------------------------- | ------------------------------------ |
| **Stakeholder Needs Elicitation**   | Gather needs through interviews, workshops, surveys                   | Stakeholder list, business objectives    | Raw stakeholder needs             | Requirements Engineer, Product Owner |
| **Needs Analysis**                  | Analyze, prioritize, and resolve conflicts                            | Stakeholder needs                        | Analyzed and prioritized needs    | Requirements Engineer                |
| **Define Stakeholder Requirements** | Transform needs into formal requirements                              | Analyzed needs                           | Stakeholder requirements document | Requirements Engineer                |
| **Define User Stories (Agile)**     | Create user stories with acceptance criteria                          | Stakeholder requirements                 | User story backlog                | Product Owner, Requirements Engineer |
| **Identify NFRs**                   | Elicit non-functional requirements (performance, security, usability) | Stakeholder needs, NFR criteria template | NFR list                          | Requirements Engineer, Architect     |

#### 6.2.3 AI Assistance

AI agents may assist with:

- Transcribing and summarizing interview notes
- Identifying implicit requirements
- Generating draft user stories
- Suggesting NFR categories

**Controls**: All AI-generated requirements validated by Requirements Engineer and confirmed with stakeholders (per PROC-AI-001).

#### 6.2.4 Outputs

- Stakeholder Requirements Document (or User Story Backlog)
- Non-Functional Requirements list
- Acceptance criteria for each requirement
- Initial traceability matrix

#### 6.2.5 Approval Criteria

- Requirements approved by key stakeholders
- Acceptance criteria defined for all functional requirements
- NFRs include measurable targets
- Requirements are unambiguous and testable

**Quality Gate**: Requirements Review meeting with stakeholders.

---

### 6.3 Phase 3: System/Software Requirements Definition (ISO 12207:6.4.3)

#### 6.3.1 Purpose

Transform stakeholder requirements into detailed software requirements specification (SRS) that developers can implement.

#### 6.3.2 Activities

| Activity                             | Description                                             | Inputs                                         | Outputs                                   | Responsible                           |
| ------------------------------------ | ------------------------------------------------------- | ---------------------------------------------- | ----------------------------------------- | ------------------------------------- |
| **Analyze Stakeholder Requirements** | Decompose and refine into software requirements         | Stakeholder requirements                       | Detailed software requirements            | Requirements Engineer                 |
| **Define Functional Requirements**   | Specify system behavior in detail                       | Stakeholder requirements, use cases            | Functional requirements (SRS Section 4.1) | Requirements Engineer                 |
| **Define Interface Requirements**    | Specify user, system, hardware, software interfaces     | Stakeholder requirements, architecture context | Interface requirements (SRS Section 4.3)  | Requirements Engineer, Architect      |
| **Define Data Requirements**         | Specify data models, retention, security classification | Stakeholder requirements, compliance needs     | Data requirements (SRS Section 4.4)       | Requirements Engineer, Data Architect |
| **Refine NFRs**                      | Specify performance, security, reliability targets      | Stakeholder NFRs, NFR criteria                 | Detailed NFRs (SRS Section 4.2)           | Requirements Engineer, Architect      |
| **Establish Traceability**           | Link software requirements to stakeholder requirements  | All requirements                               | Updated traceability matrix               | Requirements Engineer                 |

#### 6.3.3 AI Assistance

AI agents may assist with:

- Generating SRS sections from templates and input
- Populating traceability matrix
- Checking for completeness and ambiguity
- Suggesting test scenarios

**Controls**: Human review of all AI-generated content; compliance with SRS template; stakeholder validation (per PROC-AI-001).

#### 6.3.4 Template

Use: `/01-Requirements/SRS/01_MS_SRS_Template.md`

#### 6.3.5 Outputs

- Software Requirements Specification (SRS)
- Updated Traceability Matrix (`/01-Requirements/Traceability_Matrix.md`)
- Data classification matrix
- Interface specifications

#### 6.3.6 Approval Criteria

- SRS complete per template
- All requirements have unique IDs (REQ-AREA-NNN)
- Traceability to stakeholder requirements established
- NFRs measurable (metrics, targets, measurement methods defined)
- Approved by Requirements Engineer and reviewed by Architect

**Quality Gate**: SRS Review meeting.

---

### 6.4 Phase 4: Architecture Definition (ISO 12207:6.4.4)

#### 6.4.1 Purpose

Define the high-level system architecture that satisfies requirements and supports design, implementation, and evolution.

#### 6.4.2 Activities

| Activity                           | Description                                                                      | Inputs                                          | Outputs                                        | Responsible                 |
| ---------------------------------- | -------------------------------------------------------------------------------- | ----------------------------------------------- | ---------------------------------------------- | --------------------------- |
| **Define Architecture Viewpoints** | Determine architectural views needed (context, container, component, deployment) | SRS, stakeholder concerns                       | Architecture viewpoints list                   | Architect                   |
| **Create Architecture Views**      | Develop diagrams and descriptions for each viewpoint                             | SRS, patterns, constraints                      | Architecture diagrams (C4, UML)                | Architect                   |
| **Make Architecture Decisions**    | Evaluate alternatives and make key technical decisions                           | Requirements, constraints, technology landscape | Architecture Decision Records (ADRs)           | Architect, Tech Lead        |
| **Define Component Architecture**  | Decompose system into modules/services                                           | Architecture views, SRS                         | Component diagrams, responsibility assignments | Architect                   |
| **Design Data Architecture**       | Define data storage, flow, integration                                           | Data requirements, scalability needs            | Data architecture diagram, data model          | Architect, Data Architect   |
| **Define API Strategy**            | Design API contracts between components                                          | Component architecture, interface requirements  | API design document, OpenAPI specs (initial)   | Architect, API Designer     |
| **Security Architecture**          | Define security controls, threat mitigations                                     | Security requirements, threat model             | Security architecture, RBAC model              | Architect, Security Officer |

#### 6.4.3 AI Assistance

AI agents may assist with:

- Researching architecture patterns
- Drafting ADR content
- Generating initial API specifications
- Identifying architectural risks

**Controls**: Architect validates all decisions; alternatives genuinely evaluated; ADRs formally approved (per PROC-AI-001).

#### 6.4.4 Templates and Guides

- `/02-Architecture/AD/TEMPLATE-ARCH-001-Architecture_Design.md`
- `/02-Architecture/ADR/TEMPLATE-ARCH-101-Architecture_Decision_Record.md`
- `/02-Architecture/API/TEMPLATE-ARCH-102-API_Design.md`
- `/02-Architecture/Data_Model/` (PostgreSQL/MySQL/MongoDB templates)

#### 6.4.5 Outputs

- Architecture Description (AD) document
- Architecture Decision Records (ADRs) for key decisions
- Component/service diagrams
- Data architecture diagrams
- Initial API specifications (OpenAPI)
- Security architecture
- Deployment architecture

#### 6.4.6 Approval Criteria

- Architecture addresses all significant requirements
- ADRs document rationale for key decisions
- Architecture reviewed by stakeholders and development team
- Security architecture reviewed by Security Officer
- Traceability from requirements to architectural elements established

**Quality Gate**: Architecture Review meeting.

---

### 6.5 Phase 5: Design Definition (ISO 12207:6.4.5)

#### 6.5.1 Purpose

Define detailed design of software components sufficient for implementation.

#### 6.5.2 Activities

| Activity                      | Description                                         | Inputs                                 | Outputs                                | Responsible                 |
| ----------------------------- | --------------------------------------------------- | -------------------------------------- | -------------------------------------- | --------------------------- |
| **Detailed Component Design** | Design internal structure, classes, modules         | Architecture, SRS                      | Low-Level Design (LLD)                 | Developer, Architect        |
| **Database Design**           | Design physical database schema, indexes            | Data architecture, data requirements   | Database schema, migration scripts     | Data Architect, Developer   |
| **API Detailed Design**       | Finalize API contracts (endpoints, schemas, errors) | API architecture, SRS                  | OpenAPI specifications                 | API Designer, Developer     |
| **UI/UX Design**              | Design user interfaces and interactions             | User requirements, usability standards | Wireframes, mockups, UI specifications | UX Designer                 |
| **Algorithm Design**          | Design complex algorithms and calculations          | Functional requirements                | Algorithm specifications, pseudocode   | Developer                   |
| **Security Design**           | Design security controls for each component         | Security requirements, threat model    | Security design specifications         | Developer, Security Officer |
| **Design Verification**       | Review designs for correctness, completeness        | All design artifacts                   | Design review records                  | Architect, Peer Reviewers   |

#### 6.5.3 AI Assistance

AI agents may assist with:

- Generating LLD sections
- Drafting OpenAPI specifications
- Creating database schemas
- Suggesting design patterns

**Controls**: Designs reviewed by qualified personnel; security-critical designs reviewed by Security Officer; API specs validated against standards (per PROC-AI-001).

#### 6.5.4 Templates

- `/05-LLD/Module_Template/TEMPLATE-LLD-001-Module_Design.md`
- `/02-Architecture/API/OpenAPI_Guide.md`
- `/02-Architecture/Data_Model/` → `TEMPLATE-ARCH-201/202/203` (PostgreSQL/MySQL/MongoDB)

#### 6.5.5 Outputs

- Low-Level Design (LLD) documents
- Database schemas and ER diagrams
- Final OpenAPI specifications
- UI mockups/wireframes
- Algorithm specifications
- Design review records

#### 6.5.6 Approval Criteria

- LLD provides sufficient detail for implementation
- Database design normalized, indexed, and secure
- APIs follow RESTful/GraphQL best practices
- UI designs meet accessibility standards (WCAG)
- Designs traceable to requirements
- Design review completed with no open major issues

**Quality Gate**: Design Review meeting.

---

### 6.6 Phase 6: Implementation (ISO 12207:6.4.7)

#### 6.6.1 Purpose

Produce software units from design specifications through coding and unit testing.

#### 6.6.2 Activities

| Activity                  | Description                                            | Inputs                          | Outputs                        | Responsible           |
| ------------------------- | ------------------------------------------------------ | ------------------------------- | ------------------------------ | --------------------- |
| **Environment Setup**     | Configure development environment, tools, dependencies | Technology stack, tool list     | Configured dev environment     | Developer, DevOps     |
| **Code Implementation**   | Write source code per design                           | LLD, API specs, database schema | Source code                    | Developer             |
| **Unit Test Development** | Create unit tests for each code unit                   | Code, requirements              | Unit tests                     | Developer             |
| **Code Review**           | Peer review of code for quality, security, standards   | Code, coding standards          | Code review comments, approval | Peer Developers       |
| **Static Analysis**       | Run automated code quality and security scans          | Code                            | Static analysis reports        | Developer (automated) |
| **Unit Test Execution**   | Run unit tests and verify coverage                     | Code, unit tests                | Test results, coverage reports | Developer             |
| **Code Commit**           | Commit approved code to version control                | Reviewed code, passing tests    | Git commits                    | Developer             |

#### 6.6.3 AI Assistance

AI agents may assist with:

- Code generation (boilerplate, standard patterns)
- Unit test generation
- Code review (as supplement to human review)
- Documentation generation

**Controls**: Mandatory human code review; security-sensitive code requires enhanced review; AI assistance identified in commits (per PROC-AI-001 Section 6.4).

#### 6.6.4 Coding Standards

- Language-specific style guides (e.g., PEP 8 for Python, ESLint for JavaScript)
- Project-specific conventions (see `/04-Supporting/Naming_Repo_Conventions.md`)
- Security coding standards (OWASP guidelines)
- Accessibility standards (WCAG 2.1 Level AA)

#### 6.6.5 Code Review Checklist

Reviewers must verify (see PROC-AI-001 Section 6.4.2):

- Correctness
- Security
- Performance
- Error handling
- Coding standards
- Maintainability
- Testing adequacy
- Dependencies
- Documentation

#### 6.6.6 Outputs

- Source code (version-controlled)
- Unit tests
- Code review records
- Static analysis reports
- Unit test results and coverage reports
- Commit messages with traceability (REQ-IDs)

#### 6.6.7 Approval Criteria

- Code implements requirements correctly
- Unit test coverage ≥80% (configurable by project)
- Code review approved by at least one peer
- Static analysis: no critical issues, major issues resolved or waived
- Coding standards compliance verified
- Security scan: no high/critical vulnerabilities

**Quality Gate**: Automated CI pipeline checks + human code review approval.

---

### 6.7 Phase 7: Integration (ISO 12207:6.4.8)

#### 6.7.1 Purpose

Combine software units and components into a complete system per the architecture and integration strategy.

#### 6.7.2 Activities

| Activity                        | Description                                         | Inputs                                    | Outputs                    | Responsible              |
| ------------------------------- | --------------------------------------------------- | ----------------------------------------- | -------------------------- | ------------------------ |
| **Define Integration Strategy** | Plan order and approach for integration             | Architecture, dependencies                | Integration plan           | Architect, DevOps        |
| **Integration Build**           | Assemble components into builds                     | Source code, dependencies                 | Integrated builds          | DevOps (CI/CD)           |
| **Integration Testing**         | Test interfaces and interactions between components | Integrated builds, integration test cases | Integration test results   | QA Specialist, Developer |
| **API Contract Testing**        | Verify API contracts are honored                    | OpenAPI specs, service implementations    | Contract test results      | QA Specialist, DevOps    |
| **Database Integration**        | Integrate with databases, run migrations            | Database schema, migration scripts        | Integrated database        | Developer, DBA           |
| **Environment Configuration**   | Configure integration/staging environments          | Deployment architecture, config specs     | Configured environments    | DevOps                   |
| **Issue Resolution**            | Fix integration defects                             | Integration test failures                 | Fixed code, retest results | Developer                |

#### 6.7.3 Integration Strategies

- **Continuous Integration**: Code integrated multiple times daily via automated pipelines
- **Incremental Integration**: Components integrated in stages per dependency order
- **Big Bang (avoid)**: All components integrated at once (high risk, not recommended)

#### 6.7.4 Outputs

- Integrated software builds
- Integration test plans and results
- API contract test results
- Environment configuration documentation
- Integration issue logs and resolutions

#### 6.7.5 Approval Criteria

- All planned components integrated successfully
- Integration tests pass (target: 100%)
- API contract tests pass (target: 100%)
- No critical or high-severity integration defects
- Environment configuration validated

**Quality Gate**: Integration Test Pass Rate ≥95%.

---

### 6.8 Phase 8: Verification (ISO 12207:6.4.9)

#### 6.8.1 Purpose

Confirm that software work products correctly reflect specified requirements (building it right).

#### 6.8.2 Activities

| Activity                      | Description                                                | Inputs                                    | Outputs                            | Responsible              |
| ----------------------------- | ---------------------------------------------------------- | ----------------------------------------- | ---------------------------------- | ------------------------ |
| **Test Planning**             | Define test strategy, scope, resources                     | SRS, test plan template                   | Test plan                          | QA Lead                  |
| **Test Case Design**          | Create detailed test cases                                 | SRS, design docs                          | Test cases                         | QA Specialist            |
| **Test Environment Setup**    | Prepare test environments and data                         | Environment specs, test data requirements | Test environments                  | DevOps, QA               |
| **Test Execution**            | Execute functional, integration, system tests              | Test cases, integrated software           | Test results                       | QA Specialist            |
| **Regression Testing**        | Re-test after changes to ensure no new defects             | Previous test cases, changed software     | Regression test results            | QA Specialist            |
| **Performance Testing**       | Verify NFRs (performance, scalability)                     | Performance requirements, test tools      | Performance test results           | QA Specialist, DevOps    |
| **Security Testing**          | Identify vulnerabilities (SAST, DAST, penetration testing) | Security requirements, application        | Security test results              | Security Officer, QA     |
| **Defect Management**         | Log, track, retest defects                                 | Test failures                             | Defect reports, resolution records | QA Specialist, Developer |
| **Traceability Verification** | Ensure all requirements tested                             | Traceability matrix, test results         | Verified traceability              | QA Lead                  |

#### 6.8.3 Types of Testing

| Test Type         | Purpose                                           | Responsibility        | Entry Criteria         | Exit Criteria                      |
| ----------------- | ------------------------------------------------- | --------------------- | ---------------------- | ---------------------------------- |
| **Unit**          | Verify individual code units                      | Developer             | Code complete          | ≥80% coverage, all tests pass      |
| **Integration**   | Verify component interactions                     | QA + Developer        | Integration complete   | ≥95% pass rate                     |
| **System**        | Verify system as a whole                          | QA Specialist         | Integration tests pass | All critical paths tested and pass |
| **Regression**    | Ensure changes don't break existing functionality | QA Specialist         | Code changes committed | Existing tests still pass          |
| **Performance**   | Verify NFRs (response time, throughput)           | QA + DevOps           | Test environment ready | Meets NFR targets                  |
| **Security**      | Identify vulnerabilities                          | Security Officer + QA | Code complete          | No high/critical vulnerabilities   |
| **Usability**     | Verify user experience                            | QA + UX               | UI implemented         | Meets usability criteria           |
| **Accessibility** | Verify WCAG compliance                            | QA                    | UI implemented         | WCAG 2.1 AA compliance             |

#### 6.8.4 AI Assistance

AI agents may assist with:

- Test case generation
- Test data creation
- Automated test scripting
- Test results analysis

**Controls**: Test effectiveness validated (defects found vs. escaped); human review of test adequacy; critical functionality tested manually (per PROC-AI-001).

#### 6.8.5 Templates

- `/03-Lifecycle/Test/TEMPLATE-LC-011-Test_Plan_VnV.md`
- `/03-Lifecycle/Test/Test_Case_Template.md`
- `/03-Lifecycle/Test/Test_Report_Template.md`

#### 6.8.6 Outputs

- Test plan
- Test cases mapped to requirements
- Test execution results
- Defect reports
- Test coverage reports
- Performance test results
- Security scan reports
- Traceability verification records

#### 6.8.7 Approval Criteria

- Test plan approved by QA Lead and Project Manager
- All requirements have associated test cases
- Test execution: pass rate ≥95% (critical tests: 100%)
- No open critical or high defects
- NFR targets met (performance, security)
- Traceability verified: all REQ-IDs tested

**Quality Gate**: Verification Complete - ready for validation.

---

### 6.9 Phase 9: Transition/Deployment (ISO 12207:6.4.10)

#### 6.9.1 Purpose

Install software into production environment and enable users to operate the system.

#### 6.9.2 Activities

| Activity                        | Description                                          | Inputs                                      | Outputs                              | Responsible            |
| ------------------------------- | ---------------------------------------------------- | ------------------------------------------- | ------------------------------------ | ---------------------- |
| **Deployment Planning**         | Plan deployment strategy, schedule, rollback         | Deployment architecture, release scope      | Deployment plan                      | DevOps, PM             |
| **Pre-Deployment Checklist**    | Verify readiness for deployment                      | Go-live checklist, test results             | Checklist completion record          | PM, QA Lead            |
| **Production Environment Prep** | Configure production environment, secrets, databases | Environment specs, configuration            | Configured production environment    | DevOps                 |
| **Database Migration**          | Execute database changes in production               | Migration scripts, backup                   | Migrated database                    | DBA, DevOps            |
| **Software Deployment**         | Deploy software to production                        | Deployment artifacts (containers, binaries) | Deployed software                    | DevOps                 |
| **Smoke Testing**               | Verify basic functionality post-deployment           | Smoke test cases                            | Smoke test results                   | QA Specialist          |
| **User Training**               | Train users on new/changed functionality             | User manuals, training materials            | Trained users, training records      | Product Owner, Trainer |
| **Documentation Handover**      | Provide operational documentation                    | User manual, admin manual, runbooks         | Documentation in accessible location | Tech Writer, Developer |
| **Go-Live Approval**            | Formal approval to make system available             | Smoke test results, checklist               | Go-live approval record              | PM, Product Owner      |
| **Post-Deployment Monitoring**  | Monitor system health and performance                | Monitoring dashboards, logs                 | Monitoring reports                   | DevOps, Support        |

#### 6.9.3 Deployment Strategies

| Strategy       | Description                                           | Risk   | Use Case                                     |
| -------------- | ----------------------------------------------------- | ------ | -------------------------------------------- |
| **Blue/Green** | Deploy to green environment, switch traffic from blue | Low    | Zero-downtime deployments                    |
| **Canary**     | Gradually shift traffic to new version                | Low    | High-risk changes, gradual rollout           |
| **Rolling**    | Update instances incrementally                        | Medium | Stateless services                           |
| **Big Bang**   | Deploy all at once                                    | High   | Small changes, scheduled downtime acceptable |

#### 6.9.4 Rollback Plan

Every deployment must include:

- Rollback decision criteria (e.g., >5% error rate)
- Rollback procedure (step-by-step)
- Rollback testing (verify rollback works in staging)
- Rollback authority (who can authorize)

#### 6.9.5 Templates

- `/03-Lifecycle/Deployment/TEMPLATE-LC-005-Deployment_Plan.md`
- `/03-Lifecycle/GoLive/TEMPLATE-LC-007-Go_Live_Checklist.md`
- `/04-Supporting/User_Manual.md`
- `/04-Supporting/Admin_Manual.md`

#### 6.9.6 Outputs

- Deployment plan with rollback procedure
- Completed go-live checklist
- Smoke test results
- User training records
- Operational documentation (user manual, admin manual, runbooks)
- Go-live approval
- Post-deployment monitoring reports

#### 6.9.7 Approval Criteria

- All go-live checklist items complete
- Smoke tests pass (100%)
- Rollback plan tested and approved
- User training completed (if applicable)
- Documentation complete and accessible
- Monitoring and alerting configured
- Formal go-live approval obtained

**Quality Gate**: Go-Live Approval.

---

### 6.10 Phase 10: Validation (ISO 12207:6.4.11)

#### 6.10.1 Purpose

Confirm that the software meets stakeholder needs and fulfills its intended use in the operational environment (building the right thing).

#### 6.10.2 Activities

| Activity                          | Description                                | Inputs                                    | Outputs                  | Responsible                 |
| --------------------------------- | ------------------------------------------ | ----------------------------------------- | ------------------------ | --------------------------- |
| **User Acceptance Testing (UAT)** | Users test software in realistic scenarios | UAT test cases, production/staging system | UAT results              | Users, QA Facilitator       |
| **Operational Testing**           | Verify system operates in real environment | Production system, operational scenarios  | Operational test results | Operations team             |
| **Stakeholder Review**            | Stakeholders confirm system meets needs    | Deployed system, acceptance criteria      | Acceptance sign-off      | Product Owner, Stakeholders |
| **Collect User Feedback**         | Gather feedback from actual use            | Operational system, user surveys          | User feedback reports    | Product Owner, Support      |
| **Defect Resolution (if needed)** | Fix issues identified in validation        | Validation defects                        | Fixed software, retest   | Developer, QA               |

#### 6.10.3 Validation vs. Verification

| Aspect         | Verification             | Validation                                          |
| -------------- | ------------------------ | --------------------------------------------------- |
| Question       | Did we build it right?   | Did we build the right thing?                       |
| Focus          | Requirements conformance | Stakeholder needs fulfillment                       |
| Timing         | Throughout development   | Near end of development, in operational environment |
| Responsibility | QA team                  | Users/Stakeholders                                  |

#### 6.10.4 Outputs

- UAT test results
- Operational test results
- Stakeholder acceptance records
- User feedback reports
- Validation defect reports and resolutions

#### 6.10.5 Approval Criteria

- UAT pass rate ≥95%
- Stakeholders formally accept the system
- No critical usability or functionality issues
- User feedback generally positive

**Quality Gate**: Formal Stakeholder Acceptance.

---

### 6.11 Phase 11: Operation (ISO 12207:6.4.12)

#### 6.11.1 Purpose

Operate the software system to deliver its intended service, monitor performance, and provide user support.

#### 6.11.2 Activities

| Activity                     | Description                                      | Inputs                              | Outputs                               | Responsible          |
| ---------------------------- | ------------------------------------------------ | ----------------------------------- | ------------------------------------- | -------------------- |
| **System Monitoring**        | Monitor uptime, performance, errors              | Monitoring tools, SLO targets       | Monitoring dashboards, alerts         | Operations team      |
| **Incident Management**      | Respond to and resolve incidents                 | Incident reports, runbooks          | Incident resolution records           | Support team, DevOps |
| **User Support**             | Provide help desk and technical support          | User inquiries, knowledge base      | Support tickets resolved              | Support team         |
| **Performance Optimization** | Tune system for better performance               | Performance metrics, profiling data | Optimization implementations          | Developer, DevOps    |
| **Backup and Recovery**      | Execute backup schedules, test recovery          | Backup plan, backup tools           | Backup records, recovery test results | Operations team      |
| **SLA Monitoring**           | Track and report against SLAs                    | SLA definitions, actual performance | SLA reports                           | Operations Manager   |
| **Log Analysis**             | Analyze logs for issues, trends, security events | Application logs, security logs     | Log analysis reports                  | Operations, Security |

#### 6.11.3 Key Operational Metrics

| Metric                          | Target                 | Measurement         | Frequency    |
| ------------------------------- | ---------------------- | ------------------- | ------------ |
| **Availability**                | ≥99.9%                 | Uptime monitoring   | Real-time    |
| **Response Time (P95)**         | <500ms                 | APM tools           | Real-time    |
| **Error Rate**                  | <0.1%                  | Log analysis        | Real-time    |
| **MTTD (Mean Time to Detect)**  | <5 minutes             | Incident timestamps | Per incident |
| **MTTR (Mean Time to Resolve)** | <1 hour (P2 incidents) | Incident timestamps | Per incident |

#### 6.11.4 Templates

- `/03-Lifecycle/Runbook/TEMPLATE-LC-009-Operational_Runbook.md`
- `/03-Lifecycle/Runbook/TEMPLATE-LC-010-Incident_Postmortem.md`
- `/03-Lifecycle/Observability/TEMPLATE-LC-008-SLO_SLI_Plan.md`

#### 6.11.5 Outputs

- Monitoring dashboards
- Incident reports and resolutions
- Support ticket logs
- Performance reports
- SLA compliance reports
- Backup and recovery records
- Postmortem reports (for major incidents)

#### 6.11.6 Escalation

- **P1 (Critical)**: System down, major functionality broken → Immediate escalation, all hands
- **P2 (High)**: Significant functionality impaired → 1-hour response SLA
- **P3 (Medium)**: Minor functionality issue → 4-hour response SLA
- **P4 (Low)**: Cosmetic or low-impact → Next business day

---

### 6.12 Phase 12: Maintenance (ISO 12207:6.4.13)

#### 6.12.1 Purpose

Modify software to correct defects, improve performance, adapt to changed environments, or add new features.

#### 6.12.2 Types of Maintenance

| Type           | Description                            | Examples                             | Process                                                              |
| -------------- | -------------------------------------- | ------------------------------------ | -------------------------------------------------------------------- |
| **Corrective** | Fix defects                            | Bug fixes                            | Defect → Analysis → Fix → Test → Deploy                              |
| **Adaptive**   | Adapt to environment changes           | OS upgrade, API version change       | Change request → Impact analysis → Implementation → Test → Deploy    |
| **Perfective** | Improve performance or maintainability | Refactoring, optimization            | Enhancement request → Planning → Implementation → Test → Deploy      |
| **Preventive** | Prevent future problems                | Security patches, dependency updates | Proactive identification → Planning → Implementation → Test → Deploy |

#### 6.12.3 Activities

| Activity                       | Description                                       | Inputs                              | Outputs                    | Responsible                     |
| ------------------------------ | ------------------------------------------------- | ----------------------------------- | -------------------------- | ------------------------------- |
| **Change Request Management**  | Receive, evaluate, prioritize change requests     | Change requests, impact assessments | Approved change backlog    | Product Owner, Change Board     |
| **Impact Analysis**            | Assess impact of change                           | Change request, current system      | Impact assessment document | Architect, Developer            |
| **Maintenance Implementation** | Implement change per SDLC                         | Change request, design              | Modified software          | Developer (follows Phases 6-10) |
| **Regression Testing**         | Ensure changes don't break existing functionality | Test suite, modified software       | Regression test results    | QA Specialist                   |
| **Documentation Updates**      | Update docs to reflect changes                    | Modified software, previous docs    | Updated documentation      | Developer, Tech Writer          |
| **Release Management**         | Package and deploy maintenance release            | Tested software, release notes      | Deployed release           | DevOps                          |

#### 6.12.4 Maintenance Process Flow

1. Change request submitted
2. Impact analysis performed
3. Change approved/rejected/deferred
4. If approved: prioritize and schedule
5. Implement change following SDLC phases (6.5-6.10)
6. Test thoroughly including regression
7. Update documentation
8. Deploy via standard deployment process
9. Monitor post-deployment

#### 6.12.5 Templates

- `/03-Lifecycle/ChangeMgmt/TEMPLATE-LC-002-Change_Impact_Assessment.md`
- `/03-Lifecycle/ChangeMgmt/TEMPLATE-LC-003-Release_Notes.md`

#### 6.12.6 Outputs

- Change impact assessments
- Modified software
- Test results (including regression)
- Updated documentation
- Release notes

#### 6.12.7 Approval Criteria

- Impact assessment complete and approved
- Changes tested and verified
- Regression tests pass
- Documentation updated
- Release notes prepared
- Deployment approved

**Quality Gate**: Change approval before implementation; Release approval before deployment.

---

## 7. PROCESS TAILORING

### 7.1 Tailoring Principles

This SDLC may be tailored based on:

- Project size and complexity
- Risk level
- Customer requirements
- Regulatory constraints
- Team experience

### 7.2 Tailoring Approval

Tailoring proposals:

1. Documented with justification
2. Reviewed by Quality Manager
3. Approved by Project Manager and Development Lead
4. Communicated to team
5. Recorded in project plan

### 7.3 Minimum Requirements (Non-Tailorable)

- Requirements must be documented and traceable
- Code must be reviewed
- Testing must be performed
- Deployments must be planned
- Quality gates must be passed
- Records must be maintained

---

## 8. AGILE/ITERATIVE ADAPTATION

### 8.1 Mapping SDLC to Agile

Mercury Solution commonly uses Agile methodologies (Scrum, Kanban). The SDLC phases map to Agile as follows:

| SDLC Phase               | Agile Mapping                            |
| ------------------------ | ---------------------------------------- |
| Business Analysis        | Product Vision, Roadmap                  |
| Stakeholder Requirements | User Stories, Acceptance Criteria        |
| Software Requirements    | Refined User Stories, Definition of Done |
| Architecture             | Initial Sprint(s), ongoing refinement    |
| Design                   | Sprint Planning, Story breakdown         |
| Implementation           | Sprint execution                         |
| Integration              | Continuous Integration (daily)           |
| Verification             | Sprint testing, Definition of Done       |
| Transition               | Sprint Review, Release to production     |
| Validation               | Sprint Review, Stakeholder feedback      |
| Operation                | Production monitoring, Support           |
| Maintenance              | Backlog grooming, subsequent sprints     |

### 8.2 Agile Quality Gates

Quality maintained through:

- **Definition of Ready**: User stories ready for sprint
- **Definition of Done**: Code complete, reviewed, tested, documented, deployed
- **Sprint Review**: Demo to stakeholders (validation)
- **Sprint Retrospective**: Process improvement
- **Automated CI/CD**: Continuous verification

### 8.3 Documentation in Agile

- Living documentation (code as documentation, up-to-date wikis)
- Just-in-time documentation (create when needed)
- Lightweight but compliant (templates followed, but concise)

---

## 9. TRACEABILITY REQUIREMENTS

### 9.1 Mandatory Traceability Links

| From                     | To                             | Purpose                                    |
| ------------------------ | ------------------------------ | ------------------------------------------ |
| Business Objectives      | Stakeholder Requirements       | Ensure requirements support business goals |
| Stakeholder Requirements | Software Requirements (REQ-\*) | Ensure completeness                        |
| Software Requirements    | Design (AD, LLD)               | Ensure all requirements designed           |
| Software Requirements    | Test Cases (TEST-\*)           | Ensure all requirements tested             |
| Software Requirements    | Code Commits                   | Ensure all requirements implemented        |
| Test Cases               | Test Results                   | Demonstrate testing performed              |
| Defects                  | Code Changes                   | Track defect resolutions                   |

### 9.2 Traceability Verification

- Verified during phase gate reviews
- Automated tools used where possible
- Traceability matrix maintained (see `/01-Requirements/Traceability_Matrix.md`)

---

## 10. QUALITY GATES

### 10.1 Gate Criteria Summary

| Phase                        | Gate                   | Entry Criteria                            | Exit Criteria                                      |
| ---------------------------- | ---------------------- | ----------------------------------------- | -------------------------------------------------- |
| **Stakeholder Requirements** | Requirements Review    | Business case approved                    | Requirements approved by stakeholders              |
| **Software Requirements**    | SRS Review             | Stakeholder requirements approved         | SRS complete, reviewed, approved                   |
| **Architecture**             | Architecture Review    | SRS approved                              | Architecture approved, ADRs documented             |
| **Design**                   | Design Review          | Architecture approved                     | Designs complete, reviewed, traceable              |
| **Implementation**           | Code Review + CI       | Design approved                           | Code reviewed, tests pass, static analysis clean   |
| **Integration**              | Integration Tests      | Code committed                            | Integration tests ≥95% pass                        |
| **Verification**             | Test Completion        | Integration complete                      | Test plan executed, ≥95% pass, no critical defects |
| **Deployment**               | Go-Live Approval       | Verification complete, checklist complete | Smoke tests pass, approval obtained                |
| **Validation**               | Stakeholder Acceptance | System in production                      | UAT pass, stakeholder sign-off                     |

### 10.2 Gate Authorities

| Gate                   | Approver(s)                                        |
| ---------------------- | -------------------------------------------------- |
| Requirements Review    | Product Owner, Key Stakeholders                    |
| SRS Review             | Requirements Engineer, Architect                   |
| Architecture Review    | Architect, Development Lead, Security Officer      |
| Design Review          | Architect, Peer Reviewers                          |
| Code Review            | Peer Developer(s)                                  |
| Integration Tests      | QA Lead                                            |
| Test Completion        | QA Lead, Project Manager                           |
| Go-Live Approval       | Project Manager, Product Owner, Operations Manager |
| Stakeholder Acceptance | Product Owner, Key Stakeholders                    |

---

## 11. RECORDS AND EVIDENCE

### 11.1 Required Records Per Phase

| Phase             | Records                                                | Retention                   |
| ----------------- | ------------------------------------------------------ | --------------------------- |
| Business Analysis | Stakeholder list, business case, context analysis      | 3 years post-project        |
| Requirements      | SRS, traceability matrix, review minutes               | Project lifetime + 3 years  |
| Architecture      | AD, ADRs, architecture diagrams, review minutes        | Project lifetime + 3 years  |
| Design            | LLD, database schema, API specs, review records        | Project lifetime + 3 years  |
| Implementation    | Source code, code review records, test results         | Permanent (code repository) |
| Integration       | Integration test results, issue logs                   | 3 years                     |
| Verification      | Test plans, test cases, test results, defect reports   | Project lifetime + 3 years  |
| Deployment        | Deployment plans, go-live checklists, approval records | Project lifetime + 3 years  |
| Validation        | UAT results, acceptance records                        | Project lifetime + 3 years  |
| Operation         | Incident reports, SLA reports, monitoring dashboards   | 3 years                     |
| Maintenance       | Change requests, impact assessments, release notes     | Project lifetime + 3 years  |

### 11.2 Record Storage

- Code and technical artifacts: Git repositories (GitHub, GitLab, etc.)
- Documents: Document management system, Git
- Project management: Jira, Azure DevOps, etc.
- Test results: Test management tools, CI/CD systems

---

## 12. TOOLS AND AUTOMATION

### 12.1 Recommended Tools

| Purpose            | Tools (Examples)                                 |
| ------------------ | ------------------------------------------------ |
| Version Control    | Git (GitHub, GitLab, Bitbucket)                  |
| CI/CD              | GitHub Actions, GitLab CI, Jenkins, Azure DevOps |
| Project Management | Jira, Azure DevOps, Linear                       |
| Requirements       | Jira, Confluence, Markdown in Git                |
| Design/Modeling    | draw.io, Lucidchart, Mermaid, PlantUML           |
| API Design         | Swagger/OpenAPI Editor, Postman                  |
| Code Quality       | SonarQube, ESLint, Pylint                        |
| Security Scanning  | Snyk, OWASP ZAP, Burp Suite                      |
| Testing            | Jest, PyTest, Selenium, Cypress, JMeter          |
| Monitoring         | Prometheus, Grafana, Datadog, New Relic          |
| AI Assistance      | Claude Code, GitHub Copilot (per PROC-AI-001)    |

### 12.2 Automation Priorities

1. Continuous Integration (automated builds and tests)
2. Static code analysis
3. Security scanning
4. Test execution
5. Deployment pipelines
6. Monitoring and alerting

---

## 13. CONTINUOUS IMPROVEMENT

### 13.1 Process Metrics

| Metric                          | Target            | Purpose             |
| ------------------------------- | ----------------- | ------------------- |
| Cycle Time (Idea to Production) | <30 days (median) | Measure efficiency  |
| Deployment Frequency            | >1 per week       | Measure agility     |
| Change Failure Rate             | <5%               | Measure quality     |
| Mean Time to Recovery (MTTR)    | <1 hour           | Measure resilience  |
| Requirements Traceability       | 100%              | Ensure completeness |
| Code Review Coverage            | 100%              | Ensure quality      |

### 13.2 Process Review

SDLC procedure reviewed:

- Annually by Development Lead and Quality Manager
- After major projects (lessons learned)
- Following audit findings
- When technology/tools change significantly

### 13.3 Improvement Sources

- Retrospectives (Agile teams)
- Audit findings
- Metrics trends
- Industry best practices
- Technology advancements (including AI)

---

## 14. COMPLIANCE AND AUDITING

### 14.1 Compliance Verification

Compliance with this procedure verified through:

- Internal audits (quarterly sampling)
- Peer reviews
- Automated checks (CI/CD gates)
- Management reviews

### 14.2 Non-Conformance Handling

Non-conformances addressed per QM-001 Section 10.2:

1. Identify and record
2. Immediate correction
3. Root cause analysis (if major)
4. Corrective action
5. Verification of effectiveness

---

## 15. TRAINING AND COMPETENCE

### 15.1 Required Training

| Role                      | Training                                    | Frequency                   |
| ------------------------- | ------------------------------------------- | --------------------------- |
| All Development Personnel | SDLC Overview (this procedure)              | Onboarding + annual refresh |
| Developers                | ISO 12207 concepts, AI-assisted development | Onboarding                  |
| Architects                | Architecture practices, ADR process         | Onboarding                  |
| QA Specialists            | Testing methodologies, tools                | Onboarding + as needed      |
| DevOps                    | CI/CD, deployment, monitoring               | Onboarding + as needed      |

### 15.2 Competence Verification

- Observation of work products (code, documents, tests)
- Peer feedback
- Audit findings
- Defect metrics

---

## 16. APPENDICES

### Appendix A: SDLC Process Flow Diagram

See separate diagram: `/00-Process/ISO_12207/SDLC_Process_Flow.svg`

### Appendix B: Phase Inputs/Outputs Matrix

See separate spreadsheet: `/00-Process/ISO_12207/SDLC_IO_Matrix.xlsx`

### Appendix C: Compliance Mapping to ISO 12207

| ISO 12207:2017 Clause                    | Mercury Solution Implementation | Evidence                               |
| ---------------------------------------- | ------------------------------- | -------------------------------------- |
| 6.4.1 Business or Mission Analysis       | Section 6.1                     | Business case documents                |
| 6.4.2 Stakeholder Needs and Requirements | Section 6.2                     | Stakeholder requirements, user stories |
| 6.4.3 System/Software Requirements       | Section 6.3                     | SRS documents                          |
| 6.4.4 Architecture Definition            | Section 6.4                     | AD, ADRs                               |
| 6.4.5 Design Definition                  | Section 6.5                     | LLD, API specs, database schema        |
| 6.4.7 Implementation                     | Section 6.6                     | Source code, code reviews              |
| 6.4.8 Integration                        | Section 6.7                     | Integration test results               |
| 6.4.9 Verification                       | Section 6.8                     | Test plans, test results               |
| 6.4.10 Transition                        | Section 6.9                     | Deployment plans, go-live records      |
| 6.4.11 Validation                        | Section 6.10                    | UAT results, acceptance records        |
| 6.4.12 Operation                         | Section 6.11                    | Incident reports, SLA reports          |
| 6.4.13 Maintenance                       | Section 6.12                    | Change requests, release notes         |

---

## 17. REVISION HISTORY

| Version | Date       | Author                | Changes                                                                                                           |
| ------- | ---------- | --------------------- | ----------------------------------------------------------------------------------------------------------------- |
| 1.0     | 2025-10-24 | Development Team Lead | Initial release - Complete SDLC procedure aligned with ISO/IEC 12207:2017 and adapted for AI-assisted development |

---

**Document End**

**Approval**:

- Development Team Lead: ********\_******** Date: ****\_****
- Quality Manager: ********\_******** Date: ****\_****
- Architect: ********\_******** Date: ****\_****

**Next Review Date**: 2026-10-24
