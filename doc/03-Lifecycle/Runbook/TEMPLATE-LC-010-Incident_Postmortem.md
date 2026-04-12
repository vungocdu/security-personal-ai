# Incident Postmortem Report

**MERCURY SOLUTIONS**
**Software Engineering Excellence**

---

## DOCUMENT CONTROL

| Field                          | Value                                           |
| ------------------------------ | ----------------------------------------------- |
| **Document ID**                | POSTMORTEM-[YYYY]-[NNN]                         |
| **Template Version**           | 1.0                                             |
| **Document Version**           | [e.g., 1.0]                                     |
| **Incident ID**                | INC-[YYYY]-[NNN]                                |
| **Incident Date**              | [YYYY-MM-DD HH:MM TZ]                           |
| **Report Date**                | [YYYY-MM-DD]                                    |
| **Document Status**            | [Draft / Under Review / Final]                  |
| **Classification**             | [Public / Internal / Confidential / Restricted] |
| **Owner (Incident Commander)** | [Name]                                          |
| **Prepared By**                | [Name, Role]                                    |
| **Approved By**                | [Name, Role]                                    |
| **Approval Date**              | [YYYY-MM-DD]                                    |
| **Next Review Date**           | [YYYY-MM-DD]                                    |
| **AI-Assisted**                | [ ] Yes - Tool: **\_\_\_** [ ] No               |

---

## ISO STANDARDS COMPLIANCE

**This template satisfies:**

- ✓ ISO/IEC 12207:2017 - Clause 6.4.11 (Maintenance) & 6.4.12 (Operation)
- ✓ ISO/IEC 15288:2023 - Clause 6.4.8 (Disposal Process) & 6.4.7 (Maintenance)
- ✓ ISO/IEC 27001:2022 - Annex A 5.24-5.28 (Incident Management)
- ✓ ISO 9001:2015 - Clause 10.2 (Nonconformity and Corrective Action)

**Traceability to:**

- TEMPLATE-LC-009-Operational_Runbook.md
- TEMPLATE-LC-008-SLO_SLI_Plan.md
- QM-001 Section 10.2

---

## EXECUTIVE SUMMARY

**Incident ID**: INC-[YYYY]-[NNN]
**Severity**: [P1-Critical / P2-High / P3-Medium / P4-Low]
**Duration**: [X] hours [Y] minutes (from detection to resolution)
**Impact**: [Brief description of business impact]
**Root Cause**: [One-sentence summary of root cause]
**Status**: [Resolved / Ongoing / Monitoring]

**Key Metrics**:

- **Time to Detect (TTD)**: [X] minutes
- **Time to Respond (TTR)**: [X] minutes
- **Time to Resolve (TTR)**: [X] hours [Y] minutes
- **Mean Time to Recovery (MTTR)**: [X] hours [Y] minutes
- **Users Affected**: [N] users ([X]% of user base)
- **Financial Impact**: [Estimated $X or N/A]

**One-Line Summary**: [Concise statement for management dashboards]

---

## 1. INCIDENT OVERVIEW

### 1.1 Incident Classification

| Attribute            | Value                                                                                                 |
| -------------------- | ----------------------------------------------------------------------------------------------------- |
| **Incident ID**      | INC-[YYYY]-[NNN]                                                                                      |
| **Title**            | [Descriptive title of the incident]                                                                   |
| **Severity**         | [P1-Critical / P2-High / P3-Medium / P4-Low]                                                          |
| **Category**         | [System Outage / Performance Degradation / Security Breach / Data Loss / Integration Failure / Other] |
| **Service Affected** | [Service/Component Name]                                                                              |
| **Environment**      | [Production / Staging / Other]                                                                        |
| **Detection Method** | [Automated Monitoring / User Report / Internal Discovery]                                             |
| **ISO Mapping**      | ISO 27001:5.24 (Incident planning), ISO 12207:6.4.12 (Operation)                                      |

### 1.2 Timeline Summary

| Event                                   | Date/Time (TZ)     | Duration from Start |
| --------------------------------------- | ------------------ | ------------------- |
| **Incident Start** (Issue began)        | [YYYY-MM-DD HH:MM] | T+0                 |
| **Detection** (First alert/report)      | [YYYY-MM-DD HH:MM] | T+[X]m              |
| **Response** (Team engaged)             | [YYYY-MM-DD HH:MM] | T+[X]m              |
| **Diagnosis** (Root cause identified)   | [YYYY-MM-DD HH:MM] | T+[X]m              |
| **Mitigation** (Temporary fix applied)  | [YYYY-MM-DD HH:MM] | T+[X]m              |
| **Resolution** (Permanent fix deployed) | [YYYY-MM-DD HH:MM] | T+[X]h [Y]m         |
| **Validation** (System verified stable) | [YYYY-MM-DD HH:MM] | T+[X]h [Y]m         |
| **Incident Closed**                     | [YYYY-MM-DD HH:MM] | T+[X]h [Y]m         |

**Total Incident Duration**: [X] hours [Y] minutes

### 1.3 Impact Assessment

**Business Impact**:

- **Service Availability**: [X]% downtime for [Y] hours
- **Users Affected**: [N] users ([X]% of total users)
- **Transactions Lost**: [N] transactions (estimated value: $[X])
- **Revenue Impact**: Estimated $[X] in lost revenue
- **Reputation Impact**: [High/Medium/Low] - [Brief description]
- **Compliance Impact**: [Any regulatory/SLA violations]

**Technical Impact**:

- **Systems Affected**: [List affected systems/services]
- **Data Integrity**: [No impact / Data loss: X records / Data corruption: description]
- **Performance Degradation**: [Response time increased by X%, throughput reduced by Y%]
- **Dependencies**: [Cascading failures in dependent systems]

**Customer Communication**:

- **Status Page Updated**: [Yes/No] at [Time]
- **Customer Notifications**: [Number] customers notified via [email/SMS/in-app]
- **Support Tickets**: [N] tickets opened, [M] resolved

---

## 2. DETAILED TIMELINE

### 2.1 Chronological Event Log

| Time (TZ) | Event               | Actor/System    | Action Taken | Result/Observation |
| --------- | ------------------- | --------------- | ------------ | ------------------ |
| [HH:MM]   | [Event description] | [Person/System] | [Action]     | [Outcome]          |
| [HH:MM]   | [Event description] | [Person/System] | [Action]     | [Outcome]          |
| [HH:MM]   | [Event description] | [Person/System] | [Action]     | [Outcome]          |

**Example**:
| Time | Event | Actor | Action | Result |
|------|-------|-------|--------|--------|
| 14:23 | Database connection pool exhausted | Monitoring | Prometheus alert triggered | Slack notification sent to #alerts |
| 14:25 | Incident acknowledged | John Doe (On-call) | Investigated metrics dashboard | Identified 95% connection pool utilization |
| 14:30 | Mitigation attempted | John Doe | Increased connection pool size | Partial relief, error rate dropped to 20% |
| 14:45 | Root cause identified | Jane Smith (DBA) | Analyzed slow query logs | Found long-running queries blocking connections |
| 15:00 | Permanent fix deployed | Jane Smith | Optimized query, added index | Error rate dropped to <1%, system stable |
| 15:30 | Validation complete | John Doe | Monitored for 30 minutes | No recurrence, metrics normal |
| 15:35 | Incident closed | John Doe | Updated status page | Incident resolved, monitoring continues |

### 2.2 Communication Log

| Time    | Channel                   | Audience   | Message              | Sender |
| ------- | ------------------------- | ---------- | -------------------- | ------ |
| [HH:MM] | [Slack/Email/Status Page] | [Audience] | [Summary of message] | [Name] |

---

## 3. ROOT CAUSE ANALYSIS

### 3.1 Root Cause

**Primary Root Cause**:
[Detailed explanation of the fundamental reason the incident occurred. Use the "5 Whys" method if applicable.]

**Contributing Factors**:

1. [Factor 1 - e.g., Insufficient monitoring coverage]
2. [Factor 2 - e.g., Lack of rate limiting]
3. [Factor 3 - e.g., Inadequate capacity planning]

### 3.2 Five Whys Analysis (if applicable)

1. **Why did [incident] occur?**
   [Answer]

2. **Why [answer to question 1]?**
   [Answer]

3. **Why [answer to question 2]?**
   [Answer]

4. **Why [answer to question 3]?**
   [Answer]

5. **Why [answer to question 4]?**
   [Answer - Root Cause]

### 3.3 Technical Details

**System State Before Incident**:

- [Description of normal operating state]
- [Relevant metrics: CPU, memory, connections, etc.]

**Trigger Event**:

- [What specifically triggered the incident]
- [Was it gradual degradation or sudden failure?]

**Failure Mode**:

- [How the system failed: crash, hang, data corruption, etc.]
- [Error messages, stack traces, logs]

**Why Existing Controls Failed**:

- [Why monitoring didn't catch it earlier]
- [Why alarms didn't fire or were ignored]
- [Why redundancy/failover didn't work]

---

## 4. RESPONSE EVALUATION

### 4.1 What Went Well

- [Positive aspect 1 - e.g., Monitoring detected the issue quickly]
- [Positive aspect 2 - e.g., Team responded within SLA]
- [Positive aspect 3 - e.g., Communication was timely and effective]

### 4.2 What Went Poorly

- [Issue 1 - e.g., Diagnosis took longer than expected due to insufficient logging]
- [Issue 2 - e.g., Rollback procedure was not documented]
- [Issue 3 - e.g., Customer communication was delayed]

### 4.3 Where We Got Lucky

- [Lucky factor 1 - e.g., Incident occurred during low-traffic period]
- [Lucky factor 2 - e.g., Senior engineer was available to assist]
- [Lucky factor 3 - e.g., No data loss despite database crash]

---

## 5. MITIGATION AND RESOLUTION

### 5.1 Immediate Mitigation (Temporary Fix)

**Actions Taken**:

1. [Action 1 - e.g., Increased connection pool size from 100 to 200]
2. [Action 2 - e.g., Restarted affected service instances]
3. [Action 3 - e.g., Redirected traffic to secondary region]

**Effectiveness**: [Describe how effective the mitigation was]

**Risks Introduced**: [Any new risks or technical debt created by the mitigation]

### 5.2 Permanent Resolution

**Root Fix**:

- **Solution**: [Description of permanent fix]
- **Implementation**: [How it was implemented]
- **Validation**: [How it was tested before deployment]
- **Deployment Time**: [When it was deployed]

**Verification**:

- [How resolution was verified - e.g., metrics, testing, monitoring]
- [Evidence of stability - e.g., 24 hours with no recurrence]

---

## 6. CORRECTIVE ACTIONS

### 6.1 Action Items

| ID     | Action                                  | Owner  | Due Date     | Priority          | Status                      | ISO Mapping      |
| ------ | --------------------------------------- | ------ | ------------ | ----------------- | --------------------------- | ---------------- |
| CA-001 | [Specific action to prevent recurrence] | [Name] | [YYYY-MM-DD] | [High/Medium/Low] | [Open/In Progress/Complete] | ISO 9001:10.2    |
| CA-002 | [Specific action to improve detection]  | [Name] | [YYYY-MM-DD] | [High/Medium/Low] | [Open/In Progress/Complete] | ISO 27001:5.26   |
| CA-003 | [Specific action to improve response]   | [Name] | [YYYY-MM-DD] | [High/Medium/Low] | [Open/In Progress/Complete] | ISO 12207:6.4.12 |

**Example**:
| ID | Action | Owner | Due Date | Priority | Status |
|----|--------|-------|----------|----------|--------|
| CA-001 | Add connection pool monitoring with alerts at 80% utilization | DevOps Lead | 2025-11-15 | High | In Progress |
| CA-002 | Optimize top 10 slowest queries identified in analysis | DBA | 2025-11-20 | High | Open |
| CA-003 | Implement query timeout of 30 seconds | Backend Lead | 2025-11-10 | High | Complete |
| CA-004 | Document runbook for connection pool exhaustion | Tech Writer | 2025-11-25 | Medium | Open |
| CA-005 | Conduct tabletop exercise for similar incidents | Incident Manager | 2025-12-01 | Medium | Open |

### 6.2 Prevention Measures

**Technical Improvements**:

- [Improvement 1 - e.g., Implement circuit breakers]
- [Improvement 2 - e.g., Add query performance monitoring]
- [Improvement 3 - e.g., Increase database capacity]

**Process Improvements**:

- [Improvement 1 - e.g., Update runbook with new scenario]
- [Improvement 2 - e.g., Add pre-deployment checklist item]
- [Improvement 3 - e.g., Enhance monitoring coverage]

**Training/Documentation**:

- [Improvement 1 - e.g., Train on-call engineers on new monitoring]
- [Improvement 2 - e.g., Update troubleshooting guide]
- [Improvement 3 - e.g., Document new escalation procedure]

### 6.3 Long-Term Strategic Actions

- [Strategic action 1 - e.g., Migrate to autoscaling architecture]
- [Strategic action 2 - e.g., Implement chaos engineering practices]
- [Strategic action 3 - e.g., Adopt SRE principles across team]

---

## 7. LESSONS LEARNED

### 7.1 Key Takeaways

1. **[Lesson 1]**: [Description and implications]
2. **[Lesson 2]**: [Description and implications]
3. **[Lesson 3]**: [Description and implications]

**Example**:

1. **Monitoring Gaps**: We lacked monitoring on connection pool utilization, which delayed detection.
2. **Runbook Insufficiency**: Runbooks didn't cover this scenario, slowing diagnosis.
3. **Capacity Planning**: Database connection pool sizing was based on outdated assumptions about query patterns.

### 7.2 Process Gaps Identified

| Gap     | Impact   | Recommended Change |
| ------- | -------- | ------------------ |
| [Gap 1] | [Impact] | [Recommendation]   |

**Example**:
| Gap | Impact | Recommendation |
|-----|--------|----------------|
| No automated scaling for connection pools | Manual intervention required, delaying resolution | Implement autoscaling based on metrics |
| Insufficient query performance testing in staging | Slow queries only discovered in production | Add performance regression testing to CI/CD |
| No documented runbook for connection pool issues | Team had to troubleshoot from scratch | Create runbook for common database issues |

### 7.3 Blameless Culture Statement

This postmortem is conducted in accordance with our blameless culture principles. The purpose is to learn from the incident and improve our systems and processes, not to assign blame to individuals. All team members are encouraged to contribute openly to foster continuous improvement.

---

## 8. METRICS AND SLO IMPACT

### 8.1 SLI/SLO Performance

| SLI/SLO                | Target   | Actual During Incident | Impact            |
| ---------------------- | -------- | ---------------------- | ----------------- |
| Availability (monthly) | 99.9%    | [X]%                   | [Missed/On track] |
| Error Rate             | < 0.1%   | [X]%                   | [Missed/On track] |
| Response Time P95      | < 500ms  | [X]ms                  | [Missed/On track] |
| MTTR                   | < 1 hour | [X] hours              | [Missed/Met]      |

**Error Budget Consumption**:

- **Budget Consumed**: [X]% of monthly error budget
- **Budget Remaining**: [Y]%
- **Projected End-of-Month Status**: [On track / At risk / Exceeded]

### 8.2 Incident Response Metrics

| Metric                | Target        | Actual      | Met?     |
| --------------------- | ------------- | ----------- | -------- |
| Time to Detect (TTD)  | < 5 minutes   | [X] minutes | [Yes/No] |
| Time to Acknowledge   | < 5 minutes   | [X] minutes | [Yes/No] |
| Time to Respond (TTR) | < 15 minutes  | [X] minutes | [Yes/No] |
| Time to Mitigate      | < 30 minutes  | [X] minutes | [Yes/No] |
| Time to Resolve (TTR) | < 1 hour (P1) | [X] hours   | [Yes/No] |

---

## 9. CUSTOMER COMMUNICATION

### 9.1 External Communication

**Status Page Updates**:
| Time | Status | Message |
|------|--------|---------|
| [HH:MM] | Investigating | [Message text] |
| [HH:MM] | Identified | [Message text] |
| [HH:MM] | Monitoring | [Message text] |
| [HH:MM] | Resolved | [Message text] |

**Customer Notifications**:

- **Email Sent**: [Yes/No] to [N] customers at [Time]
- **In-App Notification**: [Yes/No]
- **Support Ticket Updates**: [N] tickets updated

**Post-Incident Communication**:

- **Customer-Facing Postmortem**: [Yes/No] - Published at [URL]
- **Executive Summary Sent**: [Yes/No] - To [stakeholder list]

### 9.2 Internal Communication

**Stakeholders Informed**:

- [Executive Team]: Notified at [Time] via [Channel]
- [Product Team]: Notified at [Time] via [Channel]
- [Customer Success]: Notified at [Time] via [Channel]

---

## 10. COMPLIANCE AND AUDIT

### 10.1 Regulatory Impact

**Data Protection**:

- **PII Exposed**: [Yes/No] - [If yes, describe extent and notification obligations]
- **GDPR Notification Required**: [Yes/No] - [Status]
- **Data Breach Reporting**: [Yes/No] - [Status]

**Service Level Agreements**:

- **SLA Breached**: [Yes/No] - [Which SLAs]
- **Customer Credits Due**: [Yes/No] - [Estimated $X]
- **Contractual Notifications**: [Yes/No] - [Completed on YYYY-MM-DD]

**ISO Compliance**:

- **ISO 27001 Incident Reporting**: [Completed per Clause 5.26]
- **ISO 9001 Nonconformity Record**: [Created per Clause 10.2]
- **ISO 12207 Operational Record**: [Updated per Clause 6.4.12]

### 10.2 Audit Trail

**Evidence Preserved**:

- [ ] System logs (location: [path/URL])
- [ ] Monitoring dashboards (screenshots saved)
- [ ] Communication records (Slack exports)
- [ ] Configuration changes (Git commits)
- [ ] Database query logs
- [ ] Network traffic captures (if applicable)

**Retention Period**: [X] years per [Data Retention Policy]

---

## 11. REVIEW AND APPROVAL

### 11.1 Postmortem Meeting

**Meeting Date**: [YYYY-MM-DD]
**Attendees**: [List of participants]
**Facilitator**: [Name]

**Agenda**:

1. Incident overview
2. Timeline walkthrough
3. Root cause discussion
4. Action items review
5. Lessons learned
6. Q&A

**Meeting Notes**: [Link to meeting notes or summary]

### 11.2 Approval and Sign-Off

| Role                   | Name   | Signature          | Date         |
| ---------------------- | ------ | ------------------ | ------------ |
| **Incident Commander** | [Name] | ********\_******** | **\_\_\_\_** |
| **Technical Lead**     | [Name] | ********\_******** | **\_\_\_\_** |
| **Operations Manager** | [Name] | ********\_******** | **\_\_\_\_** |
| **Quality Manager**    | [Name] | ********\_******** | **\_\_\_\_** |

### 11.3 Distribution

This postmortem has been distributed to:

- [ ] Engineering Team
- [ ] Operations Team
- [ ] Product Management
- [ ] Executive Leadership
- [ ] Quality/Compliance Team
- [ ] Customers (if customer-facing version created)

---

## 12. FOLLOW-UP

### 12.1 Action Item Tracking

**Next Review Date**: [YYYY-MM-DD] (30 days from incident)

**Tracking Location**: [Jira epic / GitHub project / etc.]

**Review Cadence**: Weekly until all high-priority actions complete

### 12.2 Effectiveness Verification

**Verification Method**:

- [ ] Conduct tabletop exercise simulating similar incident
- [ ] Monitor metrics for [X] weeks to ensure no recurrence
- [ ] Review action item completion status
- [ ] Validate runbook updates with on-call team

**Success Criteria**:

- All high-priority corrective actions completed within [X] weeks
- No recurrence of similar incident within [X] months
- Improved incident response metrics (TTD, TTR, MTTR)

---

## 13. APPENDICES

### Appendix A: Supporting Evidence

**Logs**:

- [Link to relevant log files or excerpts]

**Metrics/Dashboards**:

- [Screenshot or link to monitoring dashboards during incident]

**Configuration**:

- [Relevant configuration files or changes]

**Code/Scripts**:

- [Any relevant code snippets or deployment scripts]

### Appendix B: Related Incidents

| Incident ID | Date         | Similarity         | Outcome                                 |
| ----------- | ------------ | ------------------ | --------------------------------------- |
| [INC-ID]    | [YYYY-MM-DD] | [How it's related] | [Was it prevented by previous actions?] |

### Appendix C: Technical Details

[Any additional technical information, diagrams, architecture views, or data that supports the analysis]

### Appendix D: References

- [Runbook: Link]
- [Architecture Diagram: Link]
- [Monitoring Dashboard: Link]
- [Related Postmortems: Links]
- [ISO 27001 Incident Management Procedure]
- [ISO 9001 Corrective Action Procedure]

---

## 14. REVISION HISTORY

| Version | Date         | Author               | Changes                   |
| ------- | ------------ | -------------------- | ------------------------- |
| 1.0     | [YYYY-MM-DD] | [Incident Commander] | Initial postmortem report |

---

**Document End**

**Status**: [Draft/Under Review/Final]
**Next Review**: [YYYY-MM-DD + 30 days]
**Related Documents**: Runbook, Incident Response Plan, SLO/SLI Definitions, ISMS-001, QM-001
**Classification**: [Internal / Confidential / Customer-Facing]
