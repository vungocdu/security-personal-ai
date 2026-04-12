# Operational Runbook

**MERCURY SOLUTIONS**
**Software Engineering Excellence**

---

## DOCUMENT CONTROL

| Field                | Value                                           |
| -------------------- | ----------------------------------------------- |
| **Document ID**      | RUNBOOK-[SERVICE]-[YYYY]-[NNN]                  |
| **Template Version** | 1.0                                             |
| **Document Version** | [e.g., 1.0]                                     |
| **Service / System** | [Enter Service Name]                            |
| **Document Status**  | [Draft / Active / Retired]                      |
| **Classification**   | [Public / Internal / Confidential / Restricted] |
| **Author**           | [Name, Role]                                    |
| **Creation Date**    | [YYYY-MM-DD]                                    |
| **Last Updated**     | [YYYY-MM-DD]                                    |
| **Approved By**      | [Name, Role]                                    |
| **Approval Date**    | [YYYY-MM-DD]                                    |
| **Next Review Date** | [YYYY-MM-DD]                                    |
| **AI-Assisted**      | [ ] Yes - Tool: **\_\_\_** [ ] No               |

---

## ISO STANDARDS COMPLIANCE

**This template satisfies:**

- ✓ ISO/IEC 12207:2017 - Clause 6.4.12 (Operation Process) & 6.4.11 (Maintenance Process)
- ✓ ISO/IEC 15288:2023 - Clause 6.4.7 (Maintenance Process)
- ✓ ISO/IEC 27001:2022 - Annex A 5.29-5.30 (ICT Readiness & Continuity)
- ✓ ISO 9001:2015 - Clause 8.5 (Production and Service Provision)

**Traceability to:**

- TEMPLATE-LC-008-SLO_SLI_Plan.md
- TEMPLATE-LC-010-Incident_Postmortem.md
- TEMPLATE-LC-007-Go_Live_Checklist.md

---

## 1. SYSTEM OVERVIEW

| Attribute                | Details                              |
| ------------------------ | ------------------------------------ |
| **Service Description**  | `[Brief summary of service purpose]` |
| **Business Owner**       | `[Name, Department]`                 |
| **Technical Owner**      | `[Primary SRE/Dev Lead]`             |
| **Environments Covered** | `[Prod / Staging / QA]`              |
| **SLAs / SLOs**          | `[Link to relevant targets]`         |

**Architecture Summary:**  
`[Provide diagram link or high-level description of major components.]`

---

## 2. SERVICE INVENTORY & OWNERSHIP

| Component                | Description | Repository / Location | Owner | On-Call Group |
| ------------------------ | ----------- | --------------------- | ----- | ------------- |
| API Service              |             |                       |       |               |
| Web Frontend             |             |                       |       |               |
| Database                 |             |                       |       |               |
| Background Jobs          |             |                       |       |               |
| Third-Party Integrations |             |                       |       |               |

---

## 3. ON-CALL PROCEDURES

- **Primary On-Call Schedule:** `[Link to roster or PagerDuty schedule]`
- **Secondary / Escalation:** `[Contact details]`
- **Shift Handoff Checklist:**
  1. Review open incidents and follow-up actions.
  2. Confirm alert suppression windows.
  3. Validate upcoming change deployments.

- **Communication Channels:** `[Slack #channel, Teams, bridge numbers]`

---

## 4. MONITORING & ALERTING

| Metric / Indicator | Threshold / Condition  | Dashboard | Alert Destination | Notes |
| ------------------ | ---------------------- | --------- | ----------------- | ----- |
| Availability       | < 99.9% rolling 30 min | [Link]    | PagerDuty         |       |
| Latency P95        | > 300 ms               | [Link]    | Slack #ops        |       |
| Error Rate         | > 1%                   | [Link]    | PagerDuty         |       |
| Queue Depth        | > 1000 messages        | [Link]    | Email Ops         |       |

- **Log Locations:** `[Centralized logging index / query examples]`
- **Tracing:** `[How to access distributed traces, e.g., Jaeger search instructions]`

---

## 5. INCIDENT RESPONSE PLAYBOOK

1. Acknowledge alert via `[tool]`.
2. Assess impact; determine severity using `[severity matrix reference]`.
3. Create or update incident ticket `[INC-YYYY-NNN]` and notify stakeholders.
4. Execute relevant runbook section (see Section 6).
5. Provide updates every `[frequency]` minutes to communication channel.
6. When resolved, capture timeline and actions for postmortem.

**Incident Command Roles:** `[Define Incident Commander, Communications, Operations, SME]`

---

## 6. COMMON ISSUES & TROUBLESHOOTING

| Scenario           | Symptoms     | Diagnostic Steps                          | Resolution                         | Reference |
| ------------------ | ------------ | ----------------------------------------- | ---------------------------------- | --------- |
| High error rate    | 5xx spikes   | Check logs, inspect recent deployments    | Rollback release / scale services  | [Link]    |
| Database latency   | Slow queries | Review DB metrics, analyze slow query log | Optimize query / add index / scale | [Link]    |
| Third-party outage | API timeouts | Validate status page, switch to fallback  | Enable feature flag fallback       | [Link]    |

> Update this section with lessons learned from incidents or postmortems.

---

## 7. ROUTINE OPERATIONS

- **Daily:** `[Health checks, log review]`
- **Weekly:** `[Patch updates, capacity review]`
- **Monthly:** `[Failover drills, metrics review meeting]`
- **Quarterly:** `[Runbook review, AWS/Azure/GCP cost optimization review]`

| Task | Description | Owner | Frequency | Evidence |
| ---- | ----------- | ----- | --------- | -------- |
|      |             |       |           |          |

---

## 8. RECOVERY PROCEDURES

| Recovery Scenario   | Trigger                  | Recovery Steps                       | RTO     | RPO      | Validation            |
| ------------------- | ------------------------ | ------------------------------------ | ------- | -------- | --------------------- |
| Full service outage | Severity 1 incident      | `[Step-by-step instructions]`        | `[hrs]` | `[mins]` | `[Smoke test script]` |
| Database corruption | Data integrity alerts    | Restore backup `[ID]`, replay logs   | `[hrs]` | `[mins]` | `[Validation query]`  |
| Region failure      | Cloud region unavailable | Initiate DR failover to region `[X]` | `[hrs]` | `[mins]` | `[Checklist]`         |

---

## 9. ESCALATION PATH

| Severity | Conditions                      | Escalation Contacts     | Response Time | Notes                  |
| -------- | ------------------------------- | ----------------------- | ------------- | ---------------------- |
| Sev 1    | Complete outage, data loss risk | Incident Commander, CTO | 15 minutes    | Launch incident bridge |
| Sev 2    | Partial degradation             | On-call + Product Owner | 30 minutes    | Notify stakeholders    |
| Sev 3    | Minor impact                    | On-call                 | 4 hours       | Track via ticket       |

---

## 10. CONTACTS & RESOURCES

| Role             | Name | Contact | Backup | Notes |
| ---------------- | ---- | ------- | ------ | ----- |
| Service Owner    |      |         |        |       |
| Operations Lead  |      |         |        |       |
| Security Officer |      |         |        |       |
| Product Owner    |      |         |        |       |
| Vendor Support   |      |         |        |       |

- **Reference Links:** `[Confluence, dashboards, repositories, vendor portals]`

---

## 11. CHANGE HISTORY

| Version | Date         | Description     | Prepared By | Approved By |
| ------- | ------------ | --------------- | ----------- | ----------- |
| 1.0     | [YYYY-MM-DD] | Initial release | [Name]      | [Name]      |
| 1.1     |              |                 |             |             |

---

## 1. SYSTEM OVERVIEW

### 1.1 Service Description

**Service Name**: [Name]
**Purpose**: [What the service does and why it exists]
**Criticality**: [Critical / High / Medium / Low]
**SLA**: [Availability target, e.g., 99.9% uptime]

**Business Impact**:

- [Impact statement 1 - e.g., Processes customer payments]
- [Impact statement 2 - e.g., Revenue-critical service]
- [Impact statement 3 - e.g., Regulatory compliance requirement]

### 1.2 Architecture Overview

**High-Level Architecture**:
[Insert architecture diagram or reference to architecture documentation]

**Components**:
| Component | Technology | Purpose | Criticality |
|-----------|------------|---------|-------------|
| [Component 1] | [Tech stack] | [Purpose] | [Critical/High/Medium/Low] |
| [Component 2] | [Tech stack] | [Purpose] | [Critical/High/Medium/Low] |
| [Component 3] | [Tech stack] | [Purpose] | [Critical/High/Medium/Low] |

**Example**:
| Component | Technology | Purpose | Criticality |
|-----------|------------|---------|-------------|
| API Gateway | Kong | Request routing, authentication | Critical |
| Application Server | Node.js (Express) | Business logic | Critical |
| Database | PostgreSQL 15 | Data persistence | Critical |
| Cache Layer | Redis 7 | Session storage, caching | High |
| Message Queue | RabbitMQ | Async processing | High |
| Object Storage | AWS S3 | File storage | Medium |

### 1.3 Dependencies

**Upstream Dependencies** (services we depend on):
| Service | Provider | Impact if Unavailable | Fallback/Mitigation |
|---------|----------|----------------------|---------------------|
| [Service 1] | [Internal/External] | [Impact] | [Mitigation] |
| [Service 2] | [Internal/External] | [Impact] | [Mitigation] |

**Downstream Dependencies** (services that depend on us):
| Service | Owner | Impact if We're Unavailable |
|---------|-------|----------------------------|
| [Service 1] | [Team] | [Impact] |
| [Service 2] | [Team] | [Impact] |

### 1.4 Operational Characteristics

| Characteristic                     | Target          | Current    |
| ---------------------------------- | --------------- | ---------- |
| **Availability**                   | 99.9% (monthly) | [Actual %] |
| **Response Time (P95)**            | < 500ms         | [Actual]   |
| **Throughput**                     | 1000 req/sec    | [Actual]   |
| **Error Rate**                     | < 0.1%          | [Actual %] |
| **RTO** (Recovery Time Objective)  | 1 hour          | -          |
| **RPO** (Recovery Point Objective) | 5 minutes       | -          |

---

## 2. SERVICES AND OWNERSHIP

### 2.1 RACI Matrix

| Activity                     | Responsible         | Accountable      | Consulted           | Informed   |
| ---------------------------- | ------------------- | ---------------- | ------------------- | ---------- |
| **Incident Response**        | On-call Engineer    | Operations Lead  | Dev Team            | Management |
| **Routine Maintenance**      | Operations Engineer | Operations Lead  | -                   | Dev Team   |
| **Deployments**              | DevOps Engineer     | Release Manager  | Dev Lead, QA        | Operations |
| **Monitoring Configuration** | SRE                 | Operations Lead  | Dev Team            | -          |
| **Capacity Planning**        | SRE                 | Operations Lead  | Architect           | Finance    |
| **Security Patching**        | Operations Engineer | Security Officer | Dev Team            | Management |
| **Backup Verification**      | Operations Engineer | Operations Lead  | DBA                 | Audit Team |
| **Performance Tuning**       | SRE                 | Operations Lead  | Architect, Dev Team | -          |

### 2.2 Team Contacts

| Role                             | Name     | Email   | Phone       | Slack     | Backup        |
| -------------------------------- | -------- | ------- | ----------- | --------- | ------------- |
| **Operations Lead**              | [Name]   | [email] | [phone]     | @[handle] | [Backup name] |
| **On-Call Engineer (Primary)**   | Rotation | -       | [PagerDuty] | #oncall   | -             |
| **On-Call Engineer (Secondary)** | Rotation | -       | [PagerDuty] | #oncall   | -             |
| **Development Lead**             | [Name]   | [email] | [phone]     | @[handle] | [Backup name] |
| **DBA**                          | [Name]   | [email] | [phone]     | @[handle] | [Backup name] |
| **Security Officer**             | [Name]   | [email] | [phone]     | @[handle] | [Backup name] |

**On-Call Schedule**: [Link to PagerDuty/Opsgenie schedule]

---

## 3. ON-CALL PROCEDURES

### 3.1 On-Call Responsibilities

**Primary On-Call**:

- Acknowledge alerts within 5 minutes (SLA: 100%)
- Begin incident response within 15 minutes
- Triage and resolve P3/P4 incidents independently
- Escalate P1/P2 incidents to secondary on-call if needed
- Update incident status in [incident management tool]
- Document incident response in postmortem

**Secondary On-Call**:

- Available for escalation from primary
- Take over for P1/P2 incidents
- Coordinate with development team if needed
- Serve as backup if primary is unavailable

### 3.2 On-Call Rotation

**Schedule**: [Weekly / Bi-weekly]
**Handoff Time**: [Day/Time]
**Handoff Procedure**:

1. Review open incidents and ongoing issues
2. Check scheduled maintenance windows
3. Review recent deployments and changes
4. Review monitoring dashboards for anomalies
5. Confirm PagerDuty/Opsgenie access working
6. Update team on any known issues

**Handoff Checklist**:

- [ ] Review incident log from past week
- [ ] Check for upcoming maintenance windows
- [ ] Verify access to all monitoring tools
- [ ] Confirm contact information is up to date
- [ ] Review any system changes from past week
- [ ] Check error budget status

### 3.3 On-Call Tools and Access

**Required Tools**:

- [ ] PagerDuty/Opsgenie (alerting)
- [ ] [Monitoring tool] (Datadog/Grafana/Prometheus)
- [ ] [Log aggregation] (Splunk/ELK/CloudWatch)
- [ ] [Incident management] (Jira/ServiceNow)
- [ ] VPN access (if remote)
- [ ] AWS/Azure/GCP console access
- [ ] Database client (read-only access)
- [ ] Slack / communication channels

**Access Verification**:
Run this checklist during handoff to verify all tools accessible:

```bash
# Verify access to key systems
ping [monitoring-dashboard-url]
ssh [jump-host] "echo OK"
psql -h [db-host] -U readonly -c "SELECT 1"
```

---

## 4. MONITORING AND ALERTING

### 4.1 Monitoring Dashboard

**Primary Dashboard**: [Link to main monitoring dashboard]

**Key Metrics to Watch**:
| Metric | Normal Range | Warning Threshold | Critical Threshold | Alert Channel |
|--------|--------------|-------------------|-------------------|---------------|
| CPU Usage | 0-60% | >75% for 5 min | >90% for 2 min | Slack + Page |
| Memory Usage | 0-70% | >80% for 5 min | >90% for 2 min | Slack + Page |
| Response Time (P95) | <500ms | >800ms for 3 min | >1500ms for 2 min | Page |
| Error Rate | <0.1% | >1% for 2 min | >5% for 1 min | Page |
| Request Rate | 100-2000/sec | >2500/sec | >3000/sec | Slack |
| Database Connections | 0-80% | >85% | >95% | Page |
| Disk Usage | 0-70% | >80% | >90% | Slack + Page |
| Queue Depth | 0-1000 | >5000 | >10000 | Slack |

### 4.2 Alert Definitions

**P1 - Critical** (Page immediately, 15-minute response SLA):

- Service down (availability <95% for 5 minutes)
- Error rate >10% for 2 minutes
- Data loss detected
- Security breach detected

**P2 - High** (Page immediately, 1-hour resolution SLA):

- Performance degradation (P95 >1500ms for 5 minutes)
- Database connection pool >95%
- Disk usage >90%
- Dependency failure affecting core functionality

**P3 - Medium** (Slack alert, next business day resolution):

- Warning thresholds exceeded
- Non-critical dependency failure
- Minor performance degradation

**P4 - Low** (Email notification):

- Info-level events
- Scheduled maintenance reminders

### 4.3 Alert Response Procedure

**When Alert Fires**:

1. **Acknowledge** alert in PagerDuty/Opsgenie (within 5 minutes)
2. **Assess** impact using monitoring dashboards
3. **Notify** team in #incidents Slack channel
4. **Investigate** using troubleshooting guides (Section 6)
5. **Mitigate** or escalate (Section 9)
6. **Document** actions in incident ticket
7. **Resolve** and verify system stability
8. **Postmortem** if P1/P2 incident (use TEMPLATE-LC-010-Incident_Postmortem.md)

---

## 5. INCIDENT RESPONSE

### 5.1 Incident Severity Levels

| Severity          | Definition                                          | Examples                                  | Response Time     | Resolution Time |
| ----------------- | --------------------------------------------------- | ----------------------------------------- | ----------------- | --------------- |
| **P1 - Critical** | Complete service outage, data loss, security breach | Service down, database crash, data breach | 15 minutes        | 1 hour          |
| **P2 - High**     | Major functionality degraded, workaround exists     | Performance degradation, partial outage   | 1 hour            | 4 hours         |
| **P3 - Medium**   | Minor functionality impaired, no user impact        | Non-critical feature broken, warnings     | 4 hours           | 1 business day  |
| **P4 - Low**      | Cosmetic issues, informational                      | UI typo, deprecation warnings             | Next business day | 1 week          |

### 5.2 Incident Response Process

**Phase 1: Detection and Acknowledgement** (0-5 minutes)

1. Alert fires or user reports issue
2. On-call engineer acknowledges alert
3. Create incident ticket in [incident management system]
4. Post initial status in #incidents Slack channel

**Phase 2: Assessment and Triage** (5-15 minutes)

1. Check monitoring dashboards
2. Determine severity (P1/P2/P3/P4)
3. Assess scope of impact (% users affected, services impacted)
4. Decide: Can I handle this or escalate?

**Phase 3: Investigation and Diagnosis** (15 minutes - X hours)

1. Follow relevant troubleshooting guide (Section 6)
2. Check recent changes (deployments, config changes)
3. Analyze logs and metrics
4. Identify root cause or initiate escalation

**Phase 4: Mitigation and Resolution**

1. Apply fix (rollback, restart, config change, etc.)
2. Verify fix resolves issue
3. Monitor for 15-30 minutes for stability
4. Update incident status

**Phase 5: Post-Incident**

1. Close incident ticket
2. Update status page / notify users
3. Schedule postmortem meeting (P1/P2 only)
4. Create postmortem document (use TEMPLATE-LC-010-Incident_Postmortem.md)
5. Identify and track corrective actions

### 5.3 Incident Communication

**Internal Communication**:

- **#incidents Slack channel**: Real-time updates
- **Incident ticket**: Detailed investigation notes
- **Management**: Notify for P1/P2 incidents via email/Slack within 30 minutes

**External Communication** (if customer-facing):

- **Status page**: Update within 15 minutes of P1, 1 hour of P2
- **Email**: Notify affected customers (per customer communication plan)
- **Support team**: Brief support team to handle customer inquiries

**Communication Template**:

```
[P1/P2/P3] [Service Name] - [Brief Description]

Status: [Investigating / Identified / Monitoring / Resolved]

Impact: [% users affected, functionality impacted]

Update: [What we know, what we're doing]

Next Update: [Timeframe]
```

---

## 6. COMMON ISSUES AND TROUBLESHOOTING

### 6.1 Troubleshooting Guide Template

For each common issue, provide:

- **Symptoms**: How to recognize the issue
- **Likely Causes**: Most common root causes
- **Diagnostic Steps**: How to confirm the cause
- **Resolution**: Step-by-step fix
- **Prevention**: How to prevent recurrence

---

### 6.2 High CPU Usage

**Symptoms**:

- CPU usage >80% sustained
- Slow response times
- Timeout errors

**Likely Causes**:

- Runaway process
- Traffic spike
- Inefficient queries
- Resource leak

**Diagnostic Steps**:

```bash
# Check CPU usage by process
top -o %CPU

# Check application logs for errors
tail -f /var/log/[app]/app.log

# Check request rate
curl [metrics-endpoint] | grep request_rate
```

**Resolution**:

1. If traffic spike: Check if legitimate, consider scaling
2. If runaway process: Identify and kill process
   ```bash
   kill -9 [PID]
   systemctl restart [service-name]
   ```
3. If inefficient queries: Identify slow queries, add to optimization backlog
4. If resource leak: Restart service, create bug ticket

**Prevention**:

- Set up autoscaling based on CPU threshold
- Implement request rate limiting
- Regular performance profiling

---

### 6.3 High Memory Usage

**Symptoms**:

- Memory usage >80%
- OOM (Out of Memory) errors
- Application crashes

**Likely Causes**:

- Memory leak
- Large dataset processing
- Insufficient capacity

**Diagnostic Steps**:

```bash
# Check memory usage
free -m
ps aux --sort=-%mem | head

# Check for memory leaks (if Node.js)
node --inspect [app.js]
# Then use Chrome DevTools heap profiler
```

**Resolution**:

1. Restart service to free memory (temporary)
   ```bash
   systemctl restart [service-name]
   ```
2. If memory leak: Create bug ticket, investigate with profiler
3. If capacity issue: Scale up instance size

**Prevention**:

- Set up memory alerts at 80%
- Regular memory leak testing
- Implement memory limits per process

---

### 6.4 Database Connection Pool Exhausted

**Symptoms**:

- "Too many connections" errors
- Connection timeout errors
- Unable to query database

**Likely Causes**:

- Connection leaks (not closing connections)
- Slow queries holding connections
- Traffic spike exceeding pool size
- Database overload

**Diagnostic Steps**:

```bash
# Check current connections
psql -c "SELECT count(*) FROM pg_stat_activity;"

# Check slow queries
psql -c "SELECT pid, now() - query_start AS duration, query
         FROM pg_stat_activity
         WHERE state != 'idle'
         ORDER BY duration DESC
         LIMIT 10;"

# Check connection pool metrics
curl [app-metrics-endpoint] | grep db_connections
```

**Resolution**:

1. Kill long-running queries:
   ```sql
   SELECT pg_terminate_backend(pid)
   FROM pg_stat_activity
   WHERE state != 'idle' AND now() - query_start > interval '5 minutes';
   ```
2. Increase connection pool size (temporary):
   - Update application config: `MAX_CONNECTIONS=200`
   - Restart application
3. Restart application to release leaked connections
4. If database overload: Consider read replicas or caching

**Prevention**:

- Implement connection timeouts
- Add monitoring for connection pool usage
- Optimize slow queries
- Use connection pooler (pgBouncer)

---

### 6.5 High Error Rate

**Symptoms**:

- Error rate >1%
- 500-series HTTP errors
- Application errors in logs

**Likely Causes**:

- Bad deployment
- Dependency failure
- Database issues
- Resource exhaustion

**Diagnostic Steps**:

```bash
# Check error logs
tail -f /var/log/[app]/error.log

# Check recent deployments
git log --oneline -10

# Check dependency health
curl [dependency-health-endpoint]

# Check error breakdown by type
grep "ERROR" /var/log/[app]/app.log | awk '{print $5}' | sort | uniq -c | sort -rn
```

**Resolution**:

1. If bad deployment: Rollback immediately
   ```bash
   # Rollback to previous version
   [deployment-tool] rollback
   ```
2. If dependency failure: Check dependency status, implement circuit breaker
3. If database issues: See database troubleshooting section
4. If resource exhaustion: Scale up or restart

**Prevention**:

- Implement canary deployments
- Add health checks for all dependencies
- Set up error rate alerts

---

### 6.6 Service Unresponsive / Down

**Symptoms**:

- Health check failing
- 502/503/504 errors
- No logs being generated

**Likely Causes**:

- Process crash
- Infinite loop/deadlock
- Network issue
- Load balancer misconfiguration

**Diagnostic Steps**:

```bash
# Check if process is running
ps aux | grep [process-name]
systemctl status [service-name]

# Check service logs
journalctl -u [service-name] -n 100

# Check network connectivity
ping [service-host]
curl -v http://[service-host]:[port]/health

# Check load balancer
aws elbv2 describe-target-health --target-group-arn [arn]
```

**Resolution**:

1. Restart service:
   ```bash
   systemctl restart [service-name]
   # OR
   docker restart [container-id]
   # OR
   kubectl rollout restart deployment/[deployment-name]
   ```
2. If restart fails: Check logs for startup errors
3. If network issue: Check security groups, firewall rules
4. If deadlock: Force kill and restart
   ```bash
   kill -9 [PID]
   systemctl start [service-name]
   ```

**Prevention**:

- Implement health checks with auto-restart
- Set up liveness and readiness probes (Kubernetes)
- Monitor process uptime

---

## 7. ROUTINE OPERATIONS

### 7.1 Daily Tasks

**Morning Checks** (15 minutes):

- [ ] Review overnight alerts and incidents
- [ ] Check system health dashboard
- [ ] Verify backup completion status
- [ ] Review error rate trends
- [ ] Check disk space usage
- [ ] Review application logs for anomalies

**End-of-Day** (10 minutes):

- [ ] Update incident log
- [ ] Hand off any open issues to next shift
- [ ] Check scheduled maintenance for next day

### 7.2 Weekly Tasks

**System Maintenance**:

- [ ] Review and archive old logs (every Monday)
- [ ] Check for security patches and updates (every Tuesday)
- [ ] Verify backup restoration tests (every Wednesday)
- [ ] Review capacity and performance trends (every Thursday)
- [ ] Clean up old data/files per retention policy (every Friday)

**Procedure**:

```bash
# Archive old logs (retain 30 days)
find /var/log/[app]/ -name "*.log" -mtime +30 -exec gzip {} \;
find /var/log/[app]/ -name "*.log.gz" -mtime +90 -delete

# Check for security updates
apt update && apt list --upgradable | grep -i security

# Test backup restoration (weekly)
./scripts/restore_backup_test.sh
```

### 7.3 Monthly Tasks

**Capacity Planning Review**:

- [ ] Analyze resource utilization trends
- [ ] Project capacity needs for next 3 months
- [ ] Review and update capacity plan

**Security Review**:

- [ ] Review access logs for anomalies
- [ ] Audit user access and permissions
- [ ] Rotate secrets and API keys
- [ ] Review security scan results

**Procedure**:

```bash
# Rotate database password (monthly)
./scripts/rotate_db_password.sh

# Rotate API keys
./scripts/rotate_api_keys.sh

# Audit user access
aws iam get-account-authorization-details > access_audit_$(date +%Y%m%d).json
```

### 7.4 Quarterly Tasks

- [ ] Disaster recovery drill (test full recovery process)
- [ ] Review and update runbook
- [ ] Conduct tabletop incident response exercise
- [ ] Review SLA/SLO performance and adjust targets
- [ ] Update architecture diagrams

---

## 8. RECOVERY PROCEDURES

### 8.1 Backup and Recovery Objectives

**RTO (Recovery Time Objective)**: [1 hour]
**RPO (Recovery Point Objective)**: [5 minutes]

**Backup Schedule**:
| Backup Type | Frequency | Retention | Location |
|-------------|-----------|-----------|----------|
| Database Full Backup | Daily at 2 AM UTC | 30 days | S3 bucket: [bucket-name] |
| Database Incremental | Every 15 minutes | 7 days | S3 bucket: [bucket-name] |
| Application Config | On every change | 90 days | Git repository |
| System Snapshots | Weekly | 4 weeks | AWS/Azure snapshots |

### 8.2 Database Recovery

**Scenario**: Database corruption or data loss

**Prerequisites**:

- Access to backup storage (S3/Azure Blob)
- Database administrative credentials
- Backup restoration scripts

**Procedure**:

1. **Assess the situation**:

   ```bash
   # Check database status
   psql -c "SELECT pg_is_in_recovery();"

   # Determine recovery point
   psql -c "SELECT pg_last_wal_replay_lsn();"
   ```

2. **Identify latest backup**:

   ```bash
   aws s3 ls s3://[backup-bucket]/db-backups/ --recursive | sort | tail -10
   ```

3. **Stop application** (to prevent writes during recovery):

   ```bash
   systemctl stop [app-service]
   ```

4. **Restore from backup**:

   ```bash
   # Download backup
   aws s3 cp s3://[backup-bucket]/db-backups/[backup-file].tar.gz /tmp/

   # Extract backup
   tar -xzf /tmp/[backup-file].tar.gz -C /tmp/db-restore

   # Restore database
   pg_restore -h [db-host] -U postgres -d [db-name] -c /tmp/db-restore/backup.dump
   ```

5. **Verify restoration**:

   ```sql
   -- Check row counts in critical tables
   SELECT 'users' AS table_name, COUNT(*) FROM users
   UNION ALL
   SELECT 'orders', COUNT(*) FROM orders;

   -- Verify latest data timestamp
   SELECT MAX(created_at) FROM orders;
   ```

6. **Restart application**:

   ```bash
   systemctl start [app-service]
   ```

7. **Monitor for errors**:
   ```bash
   tail -f /var/log/[app]/app.log
   ```

**Expected Duration**: 30-60 minutes (depending on database size)

### 8.3 Application Recovery

**Scenario**: Application failure requiring redeployment

**Procedure**:

1. **Rollback to last known good version**:

   ```bash
   # If using Docker
   docker pull [registry]/[app]:[previous-tag]
   docker stop [app-container]
   docker rm [app-container]
   docker run -d --name [app-container] [registry]/[app]:[previous-tag]

   # If using Kubernetes
   kubectl rollout undo deployment/[app-name]

   # If using traditional deployment
   git checkout [previous-commit-hash]
   ./deploy.sh
   ```

2. **Verify health**:

   ```bash
   curl http://localhost:[port]/health
   ```

3. **Monitor logs**:
   ```bash
   docker logs -f [app-container]
   # OR
   kubectl logs -f deployment/[app-name]
   ```

**Expected Duration**: 5-15 minutes

### 8.4 Full System Recovery (Disaster Recovery)

**Scenario**: Complete infrastructure failure (region outage, data center loss)

**Prerequisites**:

- Secondary region/data center configured
- DNS failover mechanism
- Cross-region backups

**Procedure**:

1. **Activate disaster recovery plan**:
   - Notify management and stakeholders
   - Assemble recovery team
   - Declare disaster recovery mode

2. **Failover to secondary region**:

   ```bash
   # Update DNS to point to DR site
   aws route53 change-resource-record-sets --hosted-zone-id [zone-id] \
     --change-batch file://failover-dns.json

   # OR manually update DNS records
   ```

3. **Provision infrastructure in DR site** (if not pre-provisioned):

   ```bash
   # Deploy infrastructure as code
   terraform apply -var-file=dr-site.tfvars
   ```

4. **Restore data from backups**:
   - Follow database recovery procedure (Section 8.2)
   - Restore application state from backups

5. **Deploy application**:

   ```bash
   ./deploy.sh --environment=dr-production
   ```

6. **Verify functionality**:
   - Test critical user journeys
   - Verify data consistency
   - Check integration with dependencies

7. **Update status page**:
   - Notify users of failover
   - Provide updates on service restoration

8. **Post-recovery**:
   - Monitor for 24 hours
   - Document lessons learned
   - Plan return to primary site

**Expected Duration**: 2-4 hours

---

## 9. ESCALATION PROCEDURES

### 9.1 Escalation Matrix

| Incident Severity | Response Time     | Initial Contact | Escalation After                    | Final Escalation               |
| ----------------- | ----------------- | --------------- | ----------------------------------- | ------------------------------ |
| **P1 - Critical** | 15 minutes        | Primary On-Call | 30 minutes → Secondary On-Call      | 1 hour → Dev Lead + Management |
| **P2 - High**     | 1 hour            | Primary On-Call | 2 hours → Secondary On-Call         | 4 hours → Dev Lead             |
| **P3 - Medium**   | 4 hours           | Primary On-Call | Next business day → Operations Lead | -                              |
| **P4 - Low**      | Next business day | Primary On-Call | 3 business days → Operations Lead   | -                              |

### 9.2 When to Escalate

**Escalate to Secondary On-Call**:

- Unable to diagnose issue within 30 minutes (P1) or 2 hours (P2)
- Issue requires expertise beyond your skill level
- Multiple simultaneous incidents
- Primary on-call unavailable

**Escalate to Development Team**:

- Application code bug identified
- Database schema issue
- Architectural problem
- Requires code change to resolve

**Escalate to Management**:

- P1 incident exceeding 1 hour
- Data breach or security incident
- SLA violation likely
- Customer escalation
- Major financial impact

### 9.3 Escalation Procedure

1. **Prepare escalation information**:
   - Incident ID and severity
   - Summary of issue and impact
   - Steps already taken
   - Current system state
   - Why escalation is needed

2. **Initiate escalation**:
   - Page next level (PagerDuty/Opsgenie)
   - Post in #incidents Slack channel
   - Send email to escalation contact
   - Update incident ticket with escalation

3. **Handoff**:
   - Brief escalation contact (5-minute sync call)
   - Share incident ticket and relevant logs
   - Continue to assist as needed
   - Document handoff in incident ticket

---

## 10. CONTACTS AND RESOURCES

### 10.1 Team Contacts

See Section 2.2 for detailed contact information.

**After-Hours Escalation**:

- **Primary On-Call**: [PagerDuty phone number]
- **Secondary On-Call**: [PagerDuty phone number]
- **Development Lead (Emergency)**: [Phone number]
- **Operations Manager (Emergency)**: [Phone number]

### 10.2 External Contacts

**Vendors and Service Providers**:
| Provider | Service | Support Contact | Account ID |
|----------|---------|-----------------|------------|
| AWS | Cloud Infrastructure | [support email/phone] | [account-id] |
| Datadog | Monitoring | [support email] | [org-id] |
| PagerDuty | Alerting | [support email] | [account-id] |

### 10.3 Key Resources

**Documentation**:

- Architecture Diagram: [Link]
- API Documentation: [Link]
- Deployment Guide: [Link]
- Configuration Management: [Link]
- Incident Postmortem Archive: [Link]

**Tools and Dashboards**:

- Primary Monitoring Dashboard: [Link]
- Log Aggregation: [Link]
- Incident Management: [Link]
- Status Page: [Link]
- On-Call Schedule: [Link]

**Code Repositories**:

- Application Code: [Git URL]
- Infrastructure as Code: [Git URL]
- Runbooks and Scripts: [Git URL]

---

## 11. RUNBOOK MAINTENANCE

### 11.1 Review Schedule

**Quarterly Review**:

- Verify all procedures are current
- Update contact information
- Validate escalation procedures
- Test recovery procedures

**After Major Incidents**:

- Update troubleshooting guides with new learnings
- Add new common issues
- Refine recovery procedures

**After Significant Changes**:

- Architecture changes
- Technology stack updates
- Team reorganization
- Process changes

### 11.2 Feedback and Improvement

**Provide Feedback**:

- Create Jira ticket: [Project]-RUNBOOK-[Issue]
- Submit pull request with changes
- Discuss in #operations Slack channel

**Runbook Maintainer**: [Operations Lead Name]
**Last Reviewed**: [YYYY-MM-DD]
**Next Review**: [YYYY-MM-DD]

---

## 12. APPENDICES

### Appendix A: Command Reference

**Common Commands**:

```bash
# Check service status
systemctl status [service-name]

# Restart service
systemctl restart [service-name]

# View logs
journalctl -u [service-name] -n 100 --follow

# Check disk space
df -h

# Check memory
free -m

# Check network
netstat -tuln

# Database connection
psql -h [host] -U [user] -d [database]

# Deploy application
./scripts/deploy.sh [environment]

# Rollback deployment
./scripts/rollback.sh [version]
```

### Appendix B: Configuration Files

**Location**: `/etc/[app-name]/`

**Key Configuration Files**:

- `app.conf` - Application settings
- `database.conf` - Database connection
- `logging.conf` - Log configuration
- `monitoring.conf` - Monitoring settings

### Appendix C: Glossary

- **RTO**: Recovery Time Objective - Maximum acceptable downtime
- **RPO**: Recovery Point Objective - Maximum acceptable data loss
- **SLA**: Service Level Agreement - Contractual uptime commitment
- **SLO**: Service Level Objective - Internal performance target
- **SLI**: Service Level Indicator - Measured metric
- **MTTR**: Mean Time To Recovery - Average time to resolve incidents
- **TTD**: Time To Detect - Time from incident start to detection
- **P1/P2/P3/P4**: Incident priority levels

---

## 13. REVISION HISTORY

| Version | Date         | Author            | Changes                                                                                   |
| ------- | ------------ | ----------------- | ----------------------------------------------------------------------------------------- |
| 1.0     | [YYYY-MM-DD] | [Operations Lead] | Initial comprehensive runbook template aligned with ISO/IEC 12207:2017 and ISO 27001:2022 |

---

**Document End**

**Status**: [Draft/Active/Retired]
**Next Review**: [YYYY-MM-DD]
**Related Documents**: TEMPLATE-LC-010-Incident_Postmortem.md, TEMPLATE-LC-008-SLO_SLI_Plan.md, TEMPLATE-LC-005-Deployment_Plan.md, DR_Backup_Plan.md
**Classification**: Internal - Operations Team
