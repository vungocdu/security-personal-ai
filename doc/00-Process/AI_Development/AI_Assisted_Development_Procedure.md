# AI-Assisted Development Procedure

**MERCURY SOLUTIONS**
**Software Engineering Excellence**

---

## DOCUMENT CONTROL

| Field                | Value                             |
| -------------------- | --------------------------------- |
| **Document ID**      | PROC-AI-001                       |
| **Template Version** | 1.0                               |
| **Document Version** | [e.g., 1.0]                       |
| **Owner**            | AI Integration Specialist         |
| **Document Status**  | Approved                          |
| **Classification**   | Internal                          |
| **Creation Date**    | [YYYY-MM-DD]                      |
| **Last Updated**     | 2025-10-24                        |
| **Approved By**      | [Name, Role]                      |
| **Approval Date**    | [YYYY-MM-DD]                      |
| **Next Review Date** | [YYYY-MM-DD]                      |
| **AI-Assisted**      | [ ] Yes - Tool: **\_\_\_** [ ] No |

---

## 1. PURPOSE

This procedure defines the processes and controls for using AI agents in software development activities to ensure quality, traceability, and compliance with ISO standards.

---

## 2. SCOPE

### 2.1 Applicability

This procedure applies to all development activities involving AI assistance, including:

- Requirements analysis and SRS generation
- Architecture and design documentation
- Code generation and implementation
- Test case generation and execution
- Documentation creation and maintenance
- Code review and quality assurance

### 2.2 Out of Scope

- Manual development activities without AI assistance (covered by standard SDLC procedures)
- AI model development or training (separate ML lifecycle procedures)

---

## 3. NORMATIVE REFERENCES

- ISO/IEC 12207:2017 - Software life cycle processes
- ISO/IEC 25010:2011 - Systems and software quality models
- ISO/IEC 23894:2023 - Guidance on AI risk management
- Mercury Solution Quality Manual (PROC-ISO-001)

---

## 4. DEFINITIONS

### 4.1 AI Agent

An artificial intelligence system capable of performing software development tasks with varying degrees of autonomy, including code generation, documentation, testing, and analysis.

### 4.2 AI-Generated Artifact

Any work product (code, documentation, tests, designs) created primarily by an AI agent, subject to human review and approval.

### 4.3 Human-in-the-Loop (HITL)

A process model where AI agents perform tasks with mandatory human oversight, review, and approval at defined checkpoints.

### 4.4 AI Prompt Engineering

The practice of crafting effective instructions and context for AI agents to produce desired outputs that meet quality and compliance requirements.

---

## 5. ROLES AND RESPONSIBILITIES

### 5.1 AI Integration Specialist

**Responsibilities**:

- Define and maintain AI-assisted workflows
- Establish AI agent quality criteria
- Provide AI tool training to development teams
- Monitor AI-generated artifact quality metrics
- Investigate AI-related incidents or quality issues
- Maintain AI agent documentation and configuration

**Competence Requirements**:

- Understanding of AI capabilities and limitations
- Software development expertise
- Knowledge of ISO software engineering standards
- Risk management proficiency

### 5.2 Developer (Human)

**Responsibilities**:

- Configure and prompt AI agents appropriately
- Review all AI-generated outputs for correctness, security, and compliance
- Approve or reject AI-generated artifacts
- Document AI assistance in commit messages and audit trails
- Report AI quality issues or limitations
- Maintain responsibility for final work products

**Competence Requirements**:

- Software development proficiency in relevant domains
- Understanding of AI assistance capabilities and risks
- Code review and quality assessment skills
- ISO standards awareness

### 5.3 Quality Assurance Specialist

**Responsibilities**:

- Audit AI-assisted development processes
- Verify compliance with quality standards
- Monitor AI-generated artifact metrics
- Validate human review effectiveness
- Recommend process improvements

**Competence Requirements**:

- Quality management expertise
- ISO standards knowledge
- Understanding of AI technologies
- Audit and assessment skills

---

## 6. PROCESS DESCRIPTION

### 6.1 AI Agent Selection and Configuration

#### 6.1.1 Agent Selection Criteria

Before using an AI agent for development tasks, verify:

| Criterion            | Requirement                                                   | Verification Method                             |
| -------------------- | ------------------------------------------------------------- | ----------------------------------------------- |
| **Capability Match** | Agent capabilities align with task requirements               | Review agent documentation, conduct pilot tests |
| **Security**         | Agent does not expose sensitive data externally               | Security assessment, terms of service review    |
| **Reliability**      | Consistent output quality for similar inputs                  | Historical performance data, benchmarking       |
| **Traceability**     | Agent interactions can be logged and audited                  | Test logging capabilities                       |
| **Compliance**       | Agent usage aligns with licensing and regulatory requirements | Legal review                                    |

#### 6.1.2 Configuration Management

- AI agent configurations (model version, parameters, prompts) shall be documented and version-controlled
- Configuration changes require approval by AI Integration Specialist
- Configuration baselines maintained for each project phase

### 6.2 AI-Assisted Requirements Engineering

#### 6.2.1 Requirements Elicitation

AI agents may assist with:

- Stakeholder interview analysis
- Requirements extraction from documentation
- Use case generation
- User story creation

**Controls**:

- All AI-generated requirements must be reviewed and validated by qualified requirements engineer
- Stakeholders must confirm requirements accuracy
- Ambiguous or uncertain AI outputs flagged for human clarification

#### 6.2.2 SRS Generation

Process:

1. Developer provides AI agent with project context, stakeholder inputs, and SRS template
2. AI agent generates draft SRS sections
3. Developer reviews for completeness, accuracy, consistency, and testability
4. Iterations performed until quality criteria met
5. Requirements engineer performs final approval
6. SRS marked with AI assistance notation in document header

**Quality Criteria**:

- All requirements follow SMART principles (Specific, Measurable, Achievable, Relevant, Time-bound)
- Requirements traceability to source documents established
- No ambiguous terms (see AI Agent Document Authoring Guide, Section 8)
- Acceptance criteria defined for all functional requirements

#### 6.2.3 Traceability Matrix Update

- AI agents may assist in populating traceability matrices
- Human verification required for all traceability links
- Bidirectional traceability validated during reviews

### 6.3 AI-Assisted Architecture and Design

#### 6.3.1 Architecture Decision Records (ADRs)

AI agents may assist with:

- Identifying architectural concerns
- Researching solution options
- Drafting ADR content
- Evaluating trade-offs

**Controls**:

- Architect must validate all architectural decisions
- ADRs must include explicit approval signature
- Alternative solutions must be genuinely considered (not just AI-generated lists)

#### 6.3.2 API Design

Process:

1. Developer provides API requirements and design principles to AI agent
2. AI agent generates OpenAPI specification draft
3. Developer reviews for consistency, security, and best practices
4. API design review conducted with stakeholders
5. Approved specification becomes source of truth for implementation

**Quality Criteria**:

- OpenAPI specification validates successfully
- Security controls defined (authentication, authorization, rate limiting)
- Error handling standardized
- Versioning strategy documented
- Examples provided for all endpoints

#### 6.3.3 Data Modeling

AI-assisted data modeling requires:

- Validation of entity relationships and cardinalities
- Review of normalization and performance considerations
- Security classification of all data fields
- Verification of compliance with data retention policies

### 6.4 AI-Assisted Code Implementation

#### 6.4.1 Code Generation

**Permitted Uses**:

- Boilerplate code generation (models, DTOs, interfaces)
- Standard algorithm implementation
- Unit test scaffolding
- API client/server stub generation
- Database migration scripts

**Prohibited Without Enhanced Review**:

- Security-critical functions (authentication, authorization, encryption)
- Payment processing logic
- Personal data handling
- Complex business rule implementation

**Process**:

1. Developer provides AI agent with clear specifications including:
   - Functional requirements (REQ-\*)
   - Design constraints
   - Coding standards
   - Security requirements
   - Test requirements
2. AI agent generates code
3. Developer performs mandatory code review (see 6.4.2)
4. Code integrated into codebase with commit message indicating AI assistance
5. Automated tests executed
6. Human verification of test results

#### 6.4.2 Mandatory Code Review Checklist

For all AI-generated code, developer must verify:

- [ ] **Correctness**: Code implements specified requirements accurately
- [ ] **Security**: No security vulnerabilities (SQL injection, XSS, authentication bypass, etc.)
- [ ] **Performance**: No obvious performance anti-patterns (N+1 queries, memory leaks, inefficient algorithms)
- [ ] **Error Handling**: Appropriate exception handling and logging
- [ ] **Coding Standards**: Complies with project coding conventions
- [ ] **Maintainability**: Code is readable and well-structured
- [ ] **Testing**: Adequate test coverage exists
- [ ] **Dependencies**: No unnecessary or insecure dependencies introduced
- [ ] **Documentation**: Code comments appropriate and accurate
- [ ] **Licensing**: No copyright or licensing issues

**Escalation**: If any criterion fails, code must be corrected before integration. Repeated failures reported to AI Integration Specialist for process improvement.

#### 6.4.3 AI-Assisted Code Review

AI agents may assist human reviewers by:

- Identifying potential bugs or anti-patterns
- Checking coding standard compliance
- Suggesting improvements

**Controls**:

- AI suggestions are advisory only; human reviewer makes final decisions
- Human reviewer must independently assess code quality
- AI review does not replace human peer review

### 6.5 AI-Assisted Testing

#### 6.5.1 Test Case Generation

AI agents may generate:

- Unit test cases
- Integration test scenarios
- Test data
- Edge case identification

**Quality Criteria**:

- Test cases achieve minimum code coverage targets (unit: 80%, integration: 70%)
- Edge cases and error conditions adequately covered
- Test assertions are meaningful (not just "no exception thrown")
- Test data includes both valid and invalid inputs

#### 6.5.2 Test Execution

- AI-generated tests executed via standard CI/CD pipelines
- Test results reviewed by qualified personnel
- Failures investigated and root-caused by humans
- Test effectiveness monitored via defect detection metrics

### 6.6 AI-Assisted Documentation

#### 6.6.1 Technical Documentation

AI agents may assist with:

- API documentation generation from code
- User manual drafting
- Architecture diagram descriptions
- Code comment generation

**Controls**:

- All documentation reviewed for accuracy and completeness
- Technical accuracy verified by subject matter expert
- Documentation tested with actual users when applicable
- Version controlled with code

#### 6.6.2 Audit Documentation

For ISO compliance documentation:

- AI-generated content clearly marked
- Human reviewer identified in document approval section
- Compliance with ISO documentation requirements verified
- Audit trail of AI assistance maintained

---

## 7. QUALITY CONTROLS

### 7.1 AI Output Quality Metrics

| Metric                              | Target            | Measurement Method                                | Frequency   |
| ----------------------------------- | ----------------- | ------------------------------------------------- | ----------- |
| AI-Generated Code Acceptance Rate   | >70%              | (Approved commits / Total AI commits) × 100       | Monthly     |
| AI-Generated Test Effectiveness     | >80%              | (Defects found by AI tests / Total defects) × 100 | Per release |
| AI-Generated Documentation Accuracy | >95%              | (Accurate sections / Total sections) × 100        | Quarterly   |
| Human Review Cycle Time             | <2 hours (median) | Time from AI generation to approval               | Weekly      |
| AI-Related Defects                  | <5% of total      | Defects attributed to AI generation errors        | Monthly     |

### 7.2 Review Effectiveness Monitoring

- Random sampling of approved AI-generated artifacts for secondary review
- Defects traced to AI generation vs. human review failures
- Reviewer competence assessed based on defect escape rates

### 7.3 Continuous Improvement

- AI agent performance trends analyzed quarterly
- Low-performing agents replaced or retrained
- Human review process refined based on effectiveness data
- Lessons learned from AI-related incidents documented

---

## 8. RISK MANAGEMENT

### 8.1 Identified Risks

| Risk ID     | Description                                  | Likelihood | Impact   | Mitigation                                         |
| ----------- | -------------------------------------------- | ---------- | -------- | -------------------------------------------------- |
| RISK-AI-001 | AI generates insecure code                   | Medium     | High     | Mandatory security-focused code review; SAST tools |
| RISK-AI-002 | Over-reliance on AI reduces human competence | Medium     | High     | Regular training; rotation of AI vs. manual tasks  |
| RISK-AI-003 | AI introduces licensing violations           | Low        | High     | License scanning tools; code origin verification   |
| RISK-AI-004 | AI generates non-compliant code              | Medium     | Medium   | Compliance checklists; automated linting           |
| RISK-AI-005 | Data leakage through AI prompts              | Low        | Critical | Prompt sanitization; approved AI services only     |
| RISK-AI-006 | AI hallucinates requirements/features        | Medium     | Medium   | Traceability validation; stakeholder confirmation  |

### 8.2 Risk Treatment

- All High and Critical risks require documented mitigation controls
- Risk treatment effectiveness verified during internal audits
- Residual risks accepted by project management
- New risks identified through incident analysis

---

## 9. TRACEABILITY AND AUDIT TRAIL

### 9.1 Required Records

For each AI-assisted development activity, maintain:

1. **AI Agent Identification**
   - Tool name and version
   - Configuration parameters
   - Prompt/instruction provided

2. **Input Context**
   - Requirements or specifications provided to AI
   - Constraints and design decisions

3. **Output Artifacts**
   - AI-generated work product
   - Version and timestamp

4. **Review Records**
   - Reviewer identity
   - Review date and time
   - Review findings and decisions
   - Approval status

5. **Modifications**
   - Changes made to AI output during review
   - Rationale for changes

### 9.2 Commit Message Format

For AI-assisted commits:

```
<type>(<scope>): <description>

AI-Assisted: [Tool Name/Version]
Human Reviewer: [Reviewer Name]
Requirements: [REQ-ID1, REQ-ID2]

<detailed description>
```

Example:

```
feat(auth): implement JWT token validation

AI-Assisted: Claude Code 4.5 (Sonnet)
Human Reviewer: John Doe
Requirements: REQ-AUTH-003, REQ-AUTH-005

Implemented JWT validation middleware with role-based access control.
AI-generated base implementation; human modifications for project-specific
error handling and logging standards.
```

### 9.3 Audit Log Requirements

- All AI interactions logged with timestamp, user, input, output
- Logs retained for minimum 3 years
- Log access restricted to authorized personnel
- Logs available for compliance audits

---

## 10. TRAINING AND COMPETENCE

### 10.1 Required Training

| Personnel                 | Training Topic                   | Duration | Frequency  |
| ------------------------- | -------------------------------- | -------- | ---------- |
| All Developers            | AI-Assisted Development Overview | 2 hours  | Onboarding |
| All Developers            | AI Code Review Best Practices    | 4 hours  | Annual     |
| AI Integration Specialist | Advanced AI Engineering          | 16 hours | Annual     |
| QA Specialists            | Auditing AI-Assisted Processes   | 4 hours  | Annual     |

### 10.2 Competence Assessment

- Developers assessed via code review quality metrics
- AI Integration Specialists evaluated on process improvement contributions
- QA Specialists assessed through audit effectiveness

---

## 11. INCIDENT MANAGEMENT

### 11.1 AI-Related Incident Types

- Security vulnerability introduced by AI-generated code
- Data leakage through AI prompts
- AI-generated code causing production defect
- License compliance violation from AI code
- Incorrect AI-generated requirements leading to rework

### 11.2 Incident Response

1. Immediate containment (code rollback, access restriction)
2. Impact assessment
3. Root cause analysis (AI prompt, review failure, tool limitation)
4. Corrective action implementation
5. Preventive measures deployment
6. Incident report documentation
7. Lessons learned sharing

### 11.3 Escalation Criteria

Escalate to AI Integration Specialist if:

- Incident severity is High or Critical
- Incident involves potential compliance violation
- Incident indicates systemic AI tool issue
- Multiple similar incidents occur (>3 in one month)

---

## 12. COMPLIANCE VERIFICATION

### 12.1 Internal Audit Checklist

Auditors shall verify:

- [ ] AI agent configurations are documented and approved
- [ ] Developers have completed required AI training
- [ ] Random sample of AI-generated code includes mandatory review evidence
- [ ] Commit messages properly identify AI assistance
- [ ] Quality metrics are within target ranges
- [ ] Identified risks have documented mitigation controls
- [ ] AI-related incidents are properly documented and resolved
- [ ] Audit logs are complete and accessible

### 12.2 Audit Frequency

- Quarterly for projects heavily using AI assistance (>50% of commits)
- Semi-annually for moderate AI usage (20-50% of commits)
- Annually for low AI usage (<20% of commits)

---

## 13. CONTINUOUS IMPROVEMENT

### 13.1 Process Metrics Review

- Monthly review of AI quality metrics by AI Integration Specialist
- Quarterly trend analysis and improvement planning
- Annual process effectiveness review

### 13.2 Improvement Triggers

- Metrics falling below targets for 2 consecutive periods
- Audit findings (major or critical non-conformities)
- New AI capabilities becoming available
- Regulatory or standard updates
- Lessons learned from incidents

### 13.3 Process Change Management

- Proposed changes reviewed by Quality Manager
- Impact assessment performed
- Changes approved by process owner
- Training updated and delivered
- Changes communicated to all affected personnel
- Effectiveness of changes monitored

---

## 14. APPENDICES

### Appendix A: AI Agent Approved List

| Tool Name      | Version    | Approved Uses          | Restrictions         | Approval Date | Review Date |
| -------------- | ---------- | ---------------------- | -------------------- | ------------- | ----------- |
| Claude Code    | 4.5        | Code gen, docs, review | No PII in prompts    | 2025-10-24    | 2026-01-24  |
| GitHub Copilot | Enterprise | Code completion        | Enterprise plan only | 2025-10-24    | 2026-01-24  |

### Appendix B: AI Prompt Engineering Guidelines

**Effective Prompt Structure**:

1. Role definition: "You are an expert [domain] developer..."
2. Context: Provide relevant requirements, constraints, standards
3. Task: Clear, specific instruction
4. Output format: Specify desired structure (code, docs, tests)
5. Quality criteria: Mention standards, security, performance requirements
6. Examples (if applicable): Show desired output pattern

**Prompt Security**:

- Never include credentials, API keys, or secrets
- Sanitize customer data before including in prompts
- Use placeholder data for examples
- Review prompts for sensitive information disclosure

### Appendix C: Code Review Checklist (Detailed)

See separate document: `/03-Lifecycle/Test/AI_Code_Review_Checklist.md`

### Appendix D: AI-Related Risk Register

See: `/02-Architecture/TEMPLATE-ARCH-501-Risk_Register.md` (AI-specific risks)

---

## 15. REVISION HISTORY

| Version | Date       | Author                    | Changes                                                                                  |
| ------- | ---------- | ------------------------- | ---------------------------------------------------------------------------------------- |
| 1.0     | 2025-10-24 | AI Integration Specialist | Initial release - comprehensive AI-assisted development procedure aligned with ISO 12207 |

---

**Document End**

**Approval**:

- AI Integration Specialist: ********\_******** Date: ****\_****
- Quality Manager: ********\_******** Date: ****\_****
- Development Team Lead: ********\_******** Date: ****\_****
