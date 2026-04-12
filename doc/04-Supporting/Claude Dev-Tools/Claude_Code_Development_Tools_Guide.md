# Claude Code Development Tools Guide

**MERCURY SOLUTIONS**
**AI-Powered Development Excellence**

---

## DOCUMENT CONTROL

| Field                | Value                                            |
| -------------------- | ------------------------------------------------ |
| **Document ID**      | SUPP-DEV-001                                     |
| **Title**            | Claude Code Development Tools Guide              |
| **Owner**            | AI Integration Specialist                        |
| **Version**          | 1.0                                              |
| **Status**           | Approved                                         |
| **Classification**   | Internal                                         |
| **Creation Date**    | 2025-10-24                                       |
| **Last Updated**     | 2025-10-24                                       |
| **Approved By**      | Development Team Lead, AI Integration Specialist |
| **Approval Date**    | 2025-10-24                                       |
| **Next Review Date** | 2026-01-24                                       |
| **Related**          | PROC-AI-001, PROC-SDLC-001, QM-001, ISMS-001     |
| **AI-Assisted**      | [X] Yes - Tool: Claude Code 4.5 [ ] No           |

---

## 1. PURPOSE AND SCOPE

### 1.1 Purpose

This guide provides comprehensive instructions for using Claude Code and associated development tools in accordance with Mercury Solution's ISO-compliant software development lifecycle (SDLC). It ensures developers leverage AI assistance effectively while maintaining quality, security, and compliance standards.

### 1.2 Scope

**Covers**:

- Claude Code CLI tool setup and configuration
- Model Context Protocol (MCP) server integration
- AI-assisted development workflows
- Quality assurance and code review processes
- Security and compliance considerations
- Troubleshooting and best practices

**Does Not Cover**:

- General AI development procedures (see PROC-AI-001)
- SDLC processes (see PROC-SDLC-001)
- Non-Claude AI tools (separate documentation)

### 1.3 Intended Audience

- Software Developers
- DevOps Engineers
- QA/Test Engineers
- Technical Leads
- AI Integration Specialists

---

## 2. NORMATIVE REFERENCES

- ISO/IEC 12207:2017 - Software life cycle processes
- ISO/IEC 25010:2011 - Systems and software quality models
- PROC-AI-001 - AI-Assisted Development Procedure
- PROC-SDLC-001 - Software Development Lifecycle Procedure
- QM-001 - Quality Management System Manual
- ISMS-001 - Information Security Management System Manual

---

## 3. TOOL OVERVIEW

### 3.1 Claude Code

Claude Code is an AI-powered command-line development assistant that provides:

| Capability          | Description                                      | Use Cases                                                     |
| ------------------- | ------------------------------------------------ | ------------------------------------------------------------- |
| **Code Generation** | Generate code from natural language descriptions | Feature implementation, boilerplate generation, API endpoints |
| **Code Analysis**   | Understand and explain existing codebases        | Code reviews, documentation, refactoring                      |
| **Testing**         | Generate and execute tests                       | Unit tests, integration tests, test data generation           |
| **Documentation**   | Create and update technical documentation        | API docs, README files, architecture documents                |
| **Debugging**       | Identify and fix issues                          | Error investigation, performance optimization                 |
| **Refactoring**     | Improve code structure and quality               | Technical debt reduction, pattern implementation              |

### 3.2 Model Context Protocol (MCP)

MCP enables Claude Code to interact with external tools and services:

- **Database Connections**: Query and analyze database schemas
- **API Integration**: Test and document APIs
- **File System Operations**: Advanced file manipulation
- **Custom Tools**: Project-specific integrations

### 3.3 Supported Models

- **Claude Sonnet 4.5**: Primary model for development tasks (recommended)
- **Claude Opus**: For complex architectural decisions
- **Claude Haiku**: For quick, simple tasks

---

## 4. INSTALLATION AND SETUP

### 4.1 Prerequisites

#### System Requirements

- **Operating System**: Linux, macOS, or Windows (WSL2)
- **Node.js**: Version 18.0 or higher
- **npm**: Version 8.0 or higher
- **Git**: Version 2.30 or higher
- **Memory**: Minimum 8GB RAM (16GB recommended)
- **Storage**: 500MB free space for tool installation

#### Access Requirements

- Anthropic API key (stored securely in environment variables)
- Network access to Anthropic API endpoints
- Repository access credentials

### 4.2 Installation Steps

#### Step 1: Install Claude Code CLI

```bash
# Install globally via npm
npm install -g @anthropic-ai/claude-code

# Verify installation
claude-code --version
```

#### Step 2: Configure API Access

```bash
# Set API key (NEVER commit this to version control)
export ANTHROPIC_API_KEY="your-api-key-here"

# Add to your shell profile for persistence
echo 'export ANTHROPIC_API_KEY="your-api-key-here"' >> ~/.bashrc
# or ~/.zshrc for zsh users

# Verify configuration
claude-code auth status
```

#### Step 3: Initialize Project

```bash
# Navigate to your project directory
cd /path/to/your/project

# Initialize Claude Code configuration
claude-code init

# This creates .claude/ directory with:
# - .claude/config.json (project settings)
# - .claude/CLAUDE.md (project-specific instructions)
# - .claude/commands/ (custom slash commands)
```

#### Step 4: Configure Project Settings

Edit `.claude/config.json`:

```json
{
  "model": "claude-sonnet-4.5",
  "maxTokens": 8096,
  "temperature": 0.7,
  "safety": {
    "sandboxMode": true,
    "requireApproval": ["file_write", "bash_exec", "network_request"]
  },
  "logging": {
    "enabled": true,
    "level": "info",
    "path": ".claude/logs/"
  },
  "compliance": {
    "commitFormat": "conventional",
    "requireAITag": true,
    "codeReviewRequired": true
  }
}
```

### 4.3 Security Configuration

#### API Key Management

**CRITICAL SECURITY REQUIREMENTS**:

- ✅ Store API keys in environment variables or secure vaults (e.g., AWS Secrets Manager)
- ✅ Add `.env` files to `.gitignore`
- ✅ Rotate API keys quarterly
- ✅ Use separate keys for dev/staging/production environments
- ❌ NEVER commit API keys to version control
- ❌ NEVER share API keys via email or chat
- ❌ NEVER use production keys in development environments

#### Sandbox Mode

Always enable sandbox mode in development:

```json
{
  "safety": {
    "sandboxMode": true,
    "allowedOperations": ["read", "analyze"],
    "restrictedPaths": ["/etc/", "~/.ssh/", "*.env", "*credentials*"]
  }
}
```

### 4.4 Integration with Version Control

#### .gitignore Configuration

```gitignore
# Claude Code
.claude/logs/
.claude/cache/
.claude/.session
.claude/*.secret

# API Keys
.env
.env.local
*.key
*credentials*
```

#### Git Hooks Setup

```bash
# Pre-commit hook to verify AI assistance tags
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/bash
# Verify AI-assisted commits include required metadata
git diff --cached --name-only | while read file; do
    if git diff --cached "$file" | grep -q "AI-Assisted:"; then
        echo "✅ AI assistance properly documented"
    fi
done
EOF

chmod +x .git/hooks/pre-commit
```

---

## 5. CLAUDE CODE WORKFLOWS

### 5.1 Feature Development Workflow

#### Phase 1: Requirements Analysis

```bash
# Start Claude Code session
claude-code

# Analyze requirements document
> Read docs/01-Requirements/SRS/SRS-<Feature>.md

# Ask Claude to explain requirements
> Summarize the functional requirements for <Feature> and identify any ambiguities

# Generate traceability matrix entries
> Generate traceability matrix rows for requirements REQ-<AREA>-NNN through REQ-<AREA>-MMM
```

#### Phase 2: Architecture and Design

```bash
# Generate Architecture Decision Record
> Create ADR for <decision topic> following template TEMPLATE-ARCH-101-Architecture_Decision_Record.md

# Design API endpoints
> Design REST API for <feature> following OpenAPI 3.0 specification and project conventions

# Create data model
> Design PostgreSQL schema for <feature> with proper constraints, indexes, and relationships
```

#### Phase 3: Implementation

```bash
# Generate code structure
> Create directory structure and boilerplate for <feature> following project conventions

# Implement feature
> Implement <feature-name> according to REQ-<AREA>-NNN with unit tests

# Generate tests
> Create unit tests for <module> with minimum 80% code coverage
```

#### Phase 4: Code Review

```bash
# Self-review with Claude
> Review the code in src/<path> for security vulnerabilities, performance issues, and code quality

# Generate review checklist
> Create code review checklist for this feature based on PROC-AI-001 Section 6.4.2
```

#### Phase 5: Documentation

```bash
# Generate API documentation
> Update OpenAPI specification for new endpoints in <feature>

# Create user documentation
> Write user guide section for <feature> following project documentation standards

# Update README
> Update project README with new <feature> setup instructions
```

### 5.2 Bug Fix Workflow

#### Step 1: Investigation

```bash
# Analyze error logs
> Analyze the error in logs/<logfile> and identify root cause

# Search for related code
> Find all code locations related to <error-message>

# Check test coverage
> Analyze test coverage for <affected-module> and identify gaps
```

#### Step 2: Fix Implementation

```bash
# Generate fix
> Fix the bug in src/<path> where <description-of-issue>

# Add regression test
> Create regression test for bug <BUG-ID> to prevent future occurrences

# Verify fix
> Run tests related to <module> and verify all pass
```

#### Step 3: Documentation

```bash
# Update changelog
> Add bug fix entry to CHANGELOG.md for issue <BUG-ID>

# Create postmortem (if critical)
> Create incident postmortem for critical bug <BUG-ID> following template TEMPLATE-LC-010-Incident_Postmortem.md
```

### 5.3 Refactoring Workflow

#### Step 1: Analysis

```bash
# Identify code smells
> Analyze src/<path> for code smells and anti-patterns

# Plan refactoring
> Create refactoring plan for <module> with step-by-step approach
```

#### Step 2: Execution

```bash
# Execute refactoring
> Refactor <module> to improve <quality-attribute> while maintaining backward compatibility

# Update tests
> Update and add tests to verify refactoring hasn't changed behavior
```

#### Step 3: Verification

```bash
# Run full test suite
> Run all tests and report results

# Performance comparison
> Compare performance metrics before and after refactoring
```

### 5.4 Code Review Workflow

#### As Reviewer

```bash
# Review pull request
> Review PR #<number> for code quality, security, and compliance with standards

# Generate review comments
> Create structured code review feedback for src/<path> with severity ratings

# Verify test coverage
> Verify test coverage for changes in PR #<number> meets minimum 80% threshold
```

#### As Author Responding to Review

```bash
# Address review comments
> Address code review comment about <issue> in src/<path>

# Update based on feedback
> Implement suggested improvements from code review while maintaining functionality
```

---

## 6. MCP SERVER INTEGRATION

### 6.1 Overview

Model Context Protocol (MCP) servers extend Claude Code's capabilities with project-specific tools and integrations.

### 6.2 Available MCP Servers

#### Mercury Solution MCP Servers

Located in `/mcp-server/services/`:

| Service              | Purpose                         | Capabilities                                                |
| -------------------- | ------------------------------- | ----------------------------------------------------------- |
| **document**         | ISO documentation management    | Template generation, compliance checking, document indexing |
| **pms/pms-core**     | Property Management System core | Database operations, business logic, API testing            |
| **pms/revenue**      | Revenue management              | Pricing calculations, forecast analysis, reporting          |
| **pms/ota**          | OTA calculator                  | Rate calculations, commission tracking, parity checking     |
| **pms/database-ops** | Database operations             | Schema management, migration execution, data validation     |
| **pms/analytics**    | Analytics and reporting         | Data queries, report generation, metrics calculation        |
| **pms/integration**  | External integrations           | Channex, Beds24, payment gateway testing                    |

### 6.3 MCP Server Configuration

#### Configuration File: `.claude/mcp.json`

```json
{
  "mcpServers": {
    "document": {
      "command": "node",
      "args": ["/path/to/mcp-server/services/document/server.js"],
      "env": {
        "DOC_ROOT": "/path/to/ISO_Doc_Kit"
      },
      "autoStart": true,
      "capabilities": [
        "document.template.generate",
        "document.compliance.check",
        "document.index.search"
      ]
    },
    "pms-core": {
      "command": "node",
      "args": ["/path/to/mcp-server/services/pms/pms-core/server.js"],
      "env": {
        "DATABASE_URL": "${PMS_DATABASE_URL}",
        "ENVIRONMENT": "development"
      },
      "autoStart": false,
      "capabilities": ["database.query", "database.schema", "api.test"]
    }
  }
}
```

### 6.4 Using MCP Servers

#### Document Service Examples

```bash
# Generate SRS document from template
> Generate SRS document for feature <Feature-Name> using template TEMPLATE-REQ-002-Software_Requirements_Specification.md

# Check compliance with ISO standards
> Check document <path> for compliance with ISO/IEC 29148 requirements

# Search documentation index
> Search ISO documentation for all references to "data retention"
```

#### PMS Core Service Examples

```bash
# Query database schema
> Show me the schema for table reservations including all constraints and relationships

# Test API endpoint
> Test API endpoint POST /api/v1/reservations with sample data and verify response

# Validate business logic
> Validate pricing calculation logic for equipment type <type> against requirements REQ-PMS-123
```

#### Database Operations Examples

```bash
# Generate migration
> Create database migration to add field <field-name> to table <table-name> with appropriate constraints

# Validate data integrity
> Validate referential integrity for all foreign keys in schema pms_production

# Generate seed data
> Generate realistic test data for tables: reservations, guests, payments
```

### 6.5 Custom MCP Server Development

#### Creating Project-Specific MCP Servers

**Directory Structure**:

```
mcp-server/services/<your-service>/
├── server.js          # Main MCP server implementation
├── handlers/          # Request handlers
├── config/            # Configuration files
├── tests/             # Unit and integration tests
├── README.md          # Service documentation
└── package.json       # Dependencies
```

**Basic MCP Server Template** (`server.js`):

```javascript
const { MCPServer } = require('@anthropic-ai/mcp-sdk');

class CustomMCPServer extends MCPServer {
  constructor() {
    super('custom-service', '1.0.0');

    // Register capabilities
    this.registerCapability(
      'custom.action',
      this.handleCustomAction.bind(this)
    );
  }

  async handleCustomAction(params) {
    // Validate inputs per PROC-AI-001 Section 8
    if (!params.requiredField) {
      return {
        error: 'Missing required field',
        code: 'VALIDATION_ERROR',
      };
    }

    try {
      // Implement functionality
      const result = await this.performAction(params);

      // Log for audit trail (PROC-AI-001 Section 9.3)
      this.logAuditEvent('custom.action', params, result);

      return {
        success: true,
        data: result,
      };
    } catch (error) {
      // Error handling per PROC-SDLC-001
      this.logError('custom.action', error);
      return {
        error: error.message,
        code: 'INTERNAL_ERROR',
      };
    }
  }

  async performAction(params) {
    // Implementation logic
    return {};
  }

  logAuditEvent(action, input, output) {
    // Audit logging per ISMS-001 Section 12.4
    console.log(
      JSON.stringify({
        timestamp: new Date().toISOString(),
        action,
        user: process.env.USER,
        input: this.sanitize(input),
        output: this.sanitize(output),
      })
    );
  }

  sanitize(data) {
    // Remove sensitive data per ISMS-001 Section 8.2
    // Implementation depends on data structure
    return data;
  }
}

// Start server
const server = new CustomMCPServer();
server.start();
```

**Testing MCP Servers**:

```javascript
// tests/server.test.js
const { expect } = require('chai');
const CustomMCPServer = require('../server');

describe('CustomMCPServer', () => {
  let server;

  beforeEach(() => {
    server = new CustomMCPServer();
  });

  it('should handle custom action with valid input', async () => {
    const result = await server.handleCustomAction({
      requiredField: 'value',
    });

    expect(result.success).to.be.true;
    expect(result.data).to.exist;
  });

  it('should reject invalid input', async () => {
    const result = await server.handleCustomAction({});

    expect(result.error).to.equal('Missing required field');
    expect(result.code).to.equal('VALIDATION_ERROR');
  });
});
```

---

## 7. QUALITY ASSURANCE

### 7.1 Code Quality Standards

#### Mandatory Checks (Per PROC-AI-001 Section 6.4.2)

All AI-generated code must pass:

| Check                 | Tool                       | Threshold              | Action on Failure                  |
| --------------------- | -------------------------- | ---------------------- | ---------------------------------- |
| **Syntax Validation** | Language compiler/linter   | 0 errors               | Fix before commit                  |
| **Code Style**        | ESLint, Prettier, etc.     | 0 violations           | Auto-fix or manual correction      |
| **Security Scan**     | npm audit, Snyk, SonarQube | 0 critical/high        | Fix immediately                    |
| **Test Coverage**     | Jest, Istanbul             | ≥80% lines             | Add missing tests                  |
| **Performance**       | Profiler, benchmarks       | Within 10% of baseline | Optimize or document justification |
| **Documentation**     | JSDoc validation           | 100% public APIs       | Add missing docs                   |

#### Automated Quality Gates

```bash
# Run all quality checks before commit
npm run quality-check

# This executes:
# 1. npm run lint           # Code style
# 2. npm run test           # Unit tests
# 3. npm run test:coverage  # Coverage check
# 4. npm audit              # Security vulnerabilities
# 5. npm run build          # Build verification
```

### 7.2 AI-Assisted Code Review Process

#### Workflow

1. **AI Self-Review**: Claude Code performs initial review
2. **Automated Checks**: CI/CD runs quality gates
3. **Human Review**: Senior developer reviews changes
4. **Approval**: Code approved only after all checks pass

#### Claude Code Review Commands

```bash
# Comprehensive code review
> Review all changes in current branch for code quality, security, performance, and maintainability

# Security-focused review
> Perform security review of src/<path> checking for OWASP Top 10 vulnerabilities

# Performance review
> Analyze src/<path> for performance bottlenecks and suggest optimizations

# Architecture review
> Review architecture decisions in this PR against project architecture guidelines
```

#### Review Checklist Template

```markdown
## Code Review Checklist - [Feature/Fix Name]

### AI Review (Claude Code)

- [ ] No syntax errors
- [ ] Code follows project conventions
- [ ] No obvious security issues
- [ ] Adequate error handling
- [ ] Sufficient test coverage

### Human Review

- [ ] Business logic correct per requirements
- [ ] Architecture aligns with system design
- [ ] Performance acceptable
- [ ] Documentation complete
- [ ] Backward compatibility maintained

### Compliance (Per PROC-AI-001)

- [ ] AI assistance documented in commit
- [ ] Requirements traced (REQ-\*)
- [ ] Security review completed
- [ ] Test coverage ≥80%
- [ ] No credentials in code

**Reviewer**: [Name]
**Date**: [YYYY-MM-DD]
**Decision**: [ ] Approve [ ] Request Changes [ ] Reject
```

### 7.3 Testing with Claude Code

#### Test Generation

```bash
# Generate unit tests
> Create unit tests for all functions in src/<path> with edge cases and error conditions

# Generate integration tests
> Create integration tests for API endpoints in <module> following project test structure

# Generate E2E tests
> Create end-to-end test scenarios for user workflow <workflow-name>

# Generate test data
> Generate realistic test data for database tables: <table1>, <table2> in JSON format
```

#### Test Execution and Analysis

```bash
# Run tests with AI analysis
> Run all tests and analyze failures to suggest fixes

# Coverage analysis
> Analyze test coverage and identify untested code paths that need tests

# Flaky test detection
> Analyze test execution history and identify potentially flaky tests
```

### 7.4 Quality Metrics

Track these metrics per PROC-AI-001 Section 7.1:

| Metric                   | Target          | Measurement                         | Frequency  |
| ------------------------ | --------------- | ----------------------------------- | ---------- |
| AI Code Acceptance Rate  | >70%            | Approved commits / Total AI commits | Weekly     |
| Code Review Cycle Time   | <4 hours median | PR creation to approval             | Daily      |
| Test Coverage            | ≥80%            | Coverage report                     | Per commit |
| Security Vulnerabilities | 0 critical/high | Security scan                       | Per commit |
| Build Success Rate       | >95%            | Successful builds / Total           | Daily      |
| Code Quality Score       | >85%            | SonarQube score                     | Per PR     |

---

## 8. SECURITY AND COMPLIANCE

### 8.1 Security Best Practices

#### Prompt Security (Per PROC-AI-001 Appendix B)

**DO**:

- ✅ Use placeholder data in examples
- ✅ Sanitize log outputs before sharing
- ✅ Review AI suggestions for security implications
- ✅ Validate all AI-generated code paths

**DON'T**:

- ❌ Include real credentials, API keys, or tokens in prompts
- ❌ Share customer data or PII with AI
- ❌ Blindly trust AI security recommendations
- ❌ Disable security scans for AI-generated code

#### Code Security Checklist

```bash
# Before committing AI-generated code:
> Scan src/<path> for hardcoded credentials, API keys, or sensitive data

> Check src/<path> for SQL injection vulnerabilities

> Verify src/<path> implements proper input validation and sanitization

> Confirm src/<path> follows principle of least privilege for data access
```

### 8.2 Data Classification (Per ISMS-001 Section 8)

| Classification   | Examples                       | AI Usage Policy                           |
| ---------------- | ------------------------------ | ----------------------------------------- |
| **Public**       | Documentation, public APIs     | Unrestricted AI use                       |
| **Internal**     | Business logic, internal tools | AI use allowed with review                |
| **Confidential** | Customer data, financial info  | No direct AI processing; use placeholders |
| **Restricted**   | Credentials, encryption keys   | Never include in AI prompts               |

### 8.3 Compliance Requirements

#### ISO 12207 Alignment

- All AI-assisted development follows documented SDLC procedures
- Traceability maintained from requirements through deployment
- Quality gates enforced at each lifecycle phase
- Configuration management for all AI-generated artifacts

#### ISO 27001 Controls

- Access control: Only authorized personnel use Claude Code
- Audit logging: All AI interactions logged
- Data protection: Sensitive data never exposed to AI
- Incident response: AI-related security issues escalated per ISMS-001

### 8.4 Audit Trail Requirements (Per PROC-AI-001 Section 9)

#### Required Audit Information

Every AI-assisted activity must record:

```json
{
  "timestamp": "2025-10-24T10:30:00Z",
  "user": "john.doe",
  "tool": "claude-code",
  "model": "claude-sonnet-4.5",
  "activity": "code_generation",
  "input": {
    "requirements": ["REQ-AUTH-001", "REQ-AUTH-003"],
    "prompt": "Implement JWT authentication middleware"
  },
  "output": {
    "files": ["src/middleware/auth.js", "tests/middleware/auth.test.js"],
    "linesOfCode": 145,
    "testCoverage": 92
  },
  "review": {
    "reviewer": "jane.smith",
    "reviewDate": "2025-10-24T11:15:00Z",
    "status": "approved",
    "modifications": "Added edge case handling for expired tokens"
  }
}
```

#### Audit Log Retention

- **Development logs**: 1 year
- **Production incident logs**: 3 years
- **Compliance audit logs**: 7 years
- Storage location: `.claude/logs/` (backed up per DR_Backup_Plan.md)

---

## 9. ADVANCED FEATURES

### 9.1 Custom Slash Commands

#### Creating Custom Commands

Create command files in `.claude/commands/`:

**Example: SRS Generation Command**

```markdown
<!-- .claude/commands/srs-generate.md -->

# Generate SRS Document

You are an expert requirements engineer. Generate a Software Requirements Specification (SRS) document following ISO/IEC/IEEE 29148 standards.

## Inputs Required

1. Feature name
2. Stakeholder descriptions
3. High-level goals

## Output Format

Use template: `/mcp-server/services/document/ISO_Doc_Kit/01-Requirements/SRS/TEMPLATE-REQ-002-Software_Requirements_Specification.md`

## Quality Criteria

- All requirements must be testable
- Use unambiguous language (avoid "should", "may", "fast", "scalable" without metrics)
- Include acceptance criteria in Gherkin format
- Assign unique REQ-IDs
- Update traceability matrix

## Process

1. Read the SRS template
2. Generate sections 1-8 with provided information
3. Ensure NFRs include specific metrics
4. Add entries to Traceability Matrix
5. Output complete SRS in markdown format
```

**Usage**:

```bash
claude-code

> /srs-generate
# Claude will prompt for required inputs and generate SRS
```

#### Useful Custom Commands for Mercury Solution

**1. Architecture Decision Record**: `.claude/commands/adr-create.md`

```markdown
# Create ADR

Generate Architecture Decision Record following template TEMPLATE-ARCH-101.

Include:

- Context and problem statement
- Decision drivers
- Considered options (minimum 2)
- Decision outcome with rationale
- Consequences (positive and negative)
- Links to requirements

Follow project ADR numbering convention.
```

**2. API Endpoint Generator**: `.claude/commands/api-endpoint.md`

```markdown
# Generate API Endpoint

Create RESTful API endpoint with:

- OpenAPI specification
- Implementation code (controller, service, repository)
- Input validation
- Error handling
- Unit and integration tests
- API documentation

Follow project API design standards and TEMPLATE-ARCH-102.
```

**3. Database Migration**: `.claude/commands/db-migration.md`

```markdown
# Create Database Migration

Generate database migration script:

- Up and down migrations
- Proper constraints and indexes
- Data type validation
- Comments for complex logic
- Rollback tested

Follow project database naming conventions.
```

### 9.2 Project-Specific Configurations

#### Mercury Solution CLAUDE.md Template

Create `.claude/CLAUDE.md` in project root:

```markdown
# Mercury Solution Project Configuration

## Project Context

You are working on Mercury Solution's Property Management System (PMS), a comprehensive hospitality management platform.

## Architecture

- **Backend**: Laravel 11 (PHP 8.3)
- **Frontend**: React 18 with TypeScript
- **Database**: PostgreSQL 16 with TimescaleDB
- **Cache**: Redis 7
- **Message Queue**: RabbitMQ
- **API**: RESTful + GraphQL

## Standards and Conventions

### Code Style

- **PHP**: PSR-12, Laravel best practices
- **JavaScript/TypeScript**: Airbnb style guide
- **SQL**: Lowercase with underscores

### Naming Conventions

- **Classes**: PascalCase (e.g., `ReservationController`)
- **Methods**: camelCase (e.g., `calculateTotalPrice`)
- **Variables**: camelCase (e.g., `guestCount`)
- **Constants**: SCREAMING_SNAKE_CASE (e.g., `MAX_GUESTS_PER_ROOM`)
- **Database Tables**: plural, snake_case (e.g., `reservations`)
- **Database Columns**: snake_case (e.g., `check_in_date`)

### File Structure
```

backend/
├── app/
│ ├── Http/Controllers/ # API controllers
│ ├── Services/ # Business logic
│ ├── Repositories/ # Data access
│ ├── Models/ # Eloquent models
│ └── DTOs/ # Data transfer objects
├── tests/
│ ├── Unit/ # Unit tests
│ └── Feature/ # Integration tests
└── docs/ # API documentation

```

### Requirements Traceability
- All code must link to requirements (REQ-*)
- Use commit format: `feat(module): description [REQ-XXX-NNN]`
- Update traceability matrix for new features

### Testing Requirements
- **Unit Tests**: Minimum 80% coverage
- **Integration Tests**: All API endpoints
- **E2E Tests**: Critical user workflows
- **Performance Tests**: Response time <200ms P95

### Security Requirements
- All inputs validated and sanitized
- SQL injection prevention (use parameterized queries)
- XSS prevention (escape outputs)
- CSRF protection enabled
- Authentication: JWT with refresh tokens
- Authorization: RBAC per RBAC_Matrix_By_Endpoint.md

### Documentation
- All public methods require docblocks
- API endpoints documented in OpenAPI
- Complex logic explained with comments
- README updated for new features

## ISO Compliance
This project follows:
- ISO/IEC 12207:2017 - Software lifecycle
- ISO/IEC 27001:2022 - Information security
- ISO 9001:2015 - Quality management

Reference procedures in `/mcp-server/services/document/ISO_Doc_Kit/`

## Common Tasks

### Creating New Feature
1. Review SRS in `docs/01-Requirements/SRS/`
2. Create ADR if architectural decision needed
3. Generate OpenAPI spec for new endpoints
4. Implement following TDD approach
5. Update traceability matrix
6. Create/update user documentation

### Bug Fixing
1. Create test reproducing bug
2. Fix bug maintaining backward compatibility
3. Add regression test
4. Update CHANGELOG.md

### Code Review
Use checklist from PROC-AI-001 Section 6.4.2:
- Correctness, Security, Performance
- Error handling, Coding standards
- Maintainability, Testing, Documentation

## MCP Servers Available
- `document`: ISO documentation management
- `pms-core`: PMS database and API operations
- `revenue`: Revenue management calculations
- `ota`: OTA calculator operations
- `database-ops`: Database migrations and operations

## Important Notes
- NEVER commit credentials or API keys
- ALWAYS update tests when changing code
- ALWAYS document AI assistance in commits
- ALWAYS follow security checklist for sensitive code
- ALWAYS update traceability for new requirements
```

### 9.3 Batch Operations

#### Processing Multiple Files

```bash
# Refactor multiple files
> Refactor all files in src/services/ to use async/await instead of callbacks

# Update documentation
> Update README files in all service directories with current API information

# Fix security issues
> Fix all SQL injection vulnerabilities in files: <file1>, <file2>, <file3>
```

#### Batch Testing

```bash
# Run tests for multiple modules
> Run all tests for modules: auth, payment, reservation and report results

# Generate test reports
> Generate test coverage report for all changed files in current branch
```

### 9.4 Integration with CI/CD

#### GitHub Actions Example

```yaml
# .github/workflows/ai-quality-check.yml
name: AI-Assisted Code Quality Check

on: [pull_request]

jobs:
  ai-review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Setup Claude Code
        run: |
          npm install -g @anthropic-ai/claude-code
          echo "${{ secrets.ANTHROPIC_API_KEY }}" > ~/.anthropic-key

      - name: AI Code Review
        run: |
          claude-code --non-interactive review \
            --files=$(git diff --name-only origin/main) \
            --checks=security,performance,quality \
            --output=review-report.json

      - name: Check Results
        run: |
          if [ $(jq '.criticalIssues' review-report.json) -gt 0 ]; then
            echo "Critical issues found"
            exit 1
          fi

      - name: Post Comment
        uses: actions/github-script@v6
        with:
          script: |
            const report = require('./review-report.json');
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: `## AI Code Review Results\n\n${report.summary}`
            });
```

---

## 10. TROUBLESHOOTING

### 10.1 Common Issues and Solutions

#### Issue: "API Key Not Found"

**Symptoms**: Claude Code fails to start, shows authentication error

**Solutions**:

1. Verify API key is set: `echo $ANTHROPIC_API_KEY`
2. Check key is in correct shell profile (~/.bashrc or ~/.zshrc)
3. Reload shell: `source ~/.bashrc`
4. Verify key is valid: `claude-code auth status`

#### Issue: "Model Context Too Large"

**Symptoms**: Claude Code fails with "context length exceeded" error

**Solutions**:

1. Reduce context size in `.claude/config.json`:
   ```json
   {
     "maxTokens": 4096,
     "contextWindow": "focused"
   }
   ```
2. Split large files into smaller modules
3. Use `.claudeignore` to exclude large files:
   ```
   node_modules/
   vendor/
   *.log
   *.min.js
   ```

#### Issue: "Slow Response Times"

**Symptoms**: Claude Code takes long time to respond

**Solutions**:

1. Check network connectivity to Anthropic API
2. Reduce context: Use more specific file paths instead of entire directories
3. Use faster model: Switch to `claude-haiku` for simple tasks
4. Enable caching in config:
   ```json
   {
     "cache": {
       "enabled": true,
       "ttl": 3600
     }
   }
   ```

#### Issue: "MCP Server Connection Failed"

**Symptoms**: MCP server commands don't work

**Solutions**:

1. Verify MCP server is running: `ps aux | grep mcp`
2. Check MCP config in `.claude/mcp.json`
3. Restart MCP server: `claude-code mcp restart <server-name>`
4. Check server logs: `tail -f /path/to/mcp-server/logs/server.log`
5. Verify environment variables are set correctly

#### Issue: "Permission Denied Errors"

**Symptoms**: Claude Code can't write files or execute commands

**Solutions**:

1. Check file permissions: `ls -la`
2. Verify sandbox mode settings in `.claude/config.json`
3. Add paths to allowed list:
   ```json
   {
     "safety": {
       "allowedPaths": ["src/", "tests/", "docs/"]
     }
   }
   ```

#### Issue: "Git Conflicts with AI Commits"

**Symptoms**: Merge conflicts when integrating AI-generated code

**Solutions**:

1. Always pull latest before AI generation: `git pull origin develop`
2. Use feature branches: `git checkout -b feature/<name>`
3. Resolve conflicts manually (don't use AI for conflict resolution)
4. Keep AI commits small and focused

### 10.2 Performance Optimization

#### Reducing Latency

1. **Use local caching**: Enable in `.claude/config.json`
2. **Optimize prompts**: Be specific, avoid unnecessary context
3. **Use appropriate model**: Haiku for simple tasks, Sonnet for complex
4. **Batch similar requests**: Process multiple similar files at once

#### Managing Costs

1. **Monitor usage**: Check `claude-code usage`
2. **Set usage limits**: Configure in `.claude/config.json`
   ```json
   {
     "limits": {
       "dailyRequests": 1000,
       "monthlyTokens": 1000000
     }
   }
   ```
3. **Use appropriate model tiers**: Don't use Opus for simple tasks
4. **Cache frequently accessed content**

### 10.3 Logging and Debugging

#### Enable Debug Logging

```json
// .claude/config.json
{
  "logging": {
    "enabled": true,
    "level": "debug",
    "path": ".claude/logs/",
    "rotation": {
      "maxSize": "10MB",
      "maxFiles": 10
    }
  }
}
```

#### Analyzing Logs

```bash
# View recent logs
tail -f .claude/logs/claude-code.log

# Search for errors
grep ERROR .claude/logs/claude-code.log

# Analyze request patterns
cat .claude/logs/claude-code.log | jq '.requests[] | {time: .timestamp, model: .model, tokens: .tokensUsed}'
```

#### Debug Mode

```bash
# Start Claude Code in debug mode
claude-code --debug

# Verbose output
claude-code --verbose

# Trace mode (very detailed)
claude-code --trace
```

---

## 11. BEST PRACTICES

### 11.1 Effective Prompting

#### Structure

```
[ROLE] You are an expert [domain] developer

[CONTEXT] Working on [project], which uses [stack].
Current file: [path]
Related requirements: [REQ-IDs]

[TASK] [Specific instruction]

[CONSTRAINTS]
- Follow [coding standard]
- Maintain [quality requirement]
- Ensure [security requirement]

[OUTPUT FORMAT]
- [Desired structure]
- Include [specific elements]

[QUALITY CRITERIA]
- [Testability requirement]
- [Performance requirement]
- [Documentation requirement]
```

#### Examples

**Good Prompt**:

```
You are an expert Laravel backend developer.

Working on Mercury Solution PMS reservation module.
Current file: app/Services/ReservationService.php
Related requirements: REQ-PMS-045, REQ-PMS-046

Implement method calculateTotalPrice() that:
1. Calculates accommodation charges based on room type and nights
2. Applies equipment charges from equipment_charges table
3. Applies taxes from tax_rates table
4. Handles promotional discounts

Constraints:
- Follow Laravel service pattern
- Use repository pattern for data access
- All calculations must be auditable (log inputs/outputs)
- Handle edge cases (negative prices, missing tax rates)

Output:
- Method implementation with PHPDoc
- Unit tests with minimum 85% coverage
- Example usage in docblock

Quality Criteria:
- Performance: <10ms for calculation (no database queries in loop)
- Security: Validate all inputs, prevent price manipulation
- Testability: Mock database, test edge cases
```

**Poor Prompt**:

```
Create a function to calculate price
```

### 11.2 Code Generation Best Practices

#### DO

- ✅ Provide clear, specific requirements
- ✅ Include relevant context (requirements, standards)
- ✅ Specify quality criteria (coverage, performance)
- ✅ Request tests along with implementation
- ✅ Review ALL generated code before committing
- ✅ Test generated code thoroughly
- ✅ Document AI assistance in commits

#### DON'T

- ❌ Generate code without understanding requirements
- ❌ Skip code review for AI-generated code
- ❌ Commit without testing
- ❌ Include sensitive data in prompts
- ❌ Trust AI for security-critical code without extra scrutiny
- ❌ Use AI as excuse for poor code quality

### 11.3 Collaboration Best Practices

#### Team Communication

- Share effective prompts with team
- Document common issues and solutions
- Maintain shared `.claude/CLAUDE.md`
- Review AI-generated code as team
- Establish team conventions for AI usage

#### Version Control

- Use conventional commits
- Tag AI-assisted commits clearly
- Review AI commits more thoroughly in PRs
- Don't squash AI-related commit messages

#### Knowledge Sharing

- Document useful Claude Code workflows
- Create team-specific slash commands
- Share MCP server implementations
- Conduct AI tool training sessions

### 11.4 Security Best Practices

#### Data Protection

- Never include real credentials in prompts
- Use placeholder data for examples
- Sanitize logs before sharing
- Review AI output for sensitive data leakage

#### Code Security

- Apply OWASP Top 10 checks to AI code
- Use security linters (e.g., npm audit, Snyk)
- Manual security review for authentication/authorization
- Penetration test AI-generated endpoints

#### Access Control

- Limit Claude Code access to authorized personnel
- Use separate API keys per environment
- Rotate keys quarterly
- Monitor API key usage for anomalies

---

## 12. TRAINING AND CERTIFICATION

### 12.1 Competency Requirements

| Level            | Role                       | Required Training          | Duration |
| ---------------- | -------------------------- | -------------------------- | -------- |
| **Basic**        | All Developers             | Claude Code Fundamentals   | 2 hours  |
| **Intermediate** | Regular Users              | Advanced Workflows and MCP | 4 hours  |
| **Advanced**     | AI Integration Specialists | Custom MCP Development     | 8 hours  |
| **Expert**       | Technical Leads            | AI Governance and Auditing | 4 hours  |

### 12.2 Training Curriculum

#### Module 1: Claude Code Fundamentals (2 hours)

- Installation and setup
- Basic prompting techniques
- Code generation workflows
- Quality assurance basics
- Compliance requirements

#### Module 2: Advanced Workflows (4 hours)

- Complex feature development
- MCP server usage
- Custom slash commands
- Batch operations
- Troubleshooting

#### Module 3: MCP Server Development (8 hours)

- MCP architecture
- Server implementation
- Testing and deployment
- Security considerations
- Integration with Claude Code

#### Module 4: AI Governance (4 hours)

- ISO compliance requirements
- Audit procedures
- Risk management
- Quality metrics
- Incident response

### 12.3 Certification

#### Certification Levels

1. **Claude Code User**: Can use Claude Code for daily development tasks
2. **Claude Code Specialist**: Can create custom commands and troubleshoot issues
3. **MCP Developer**: Can develop and deploy custom MCP servers
4. **AI Integration Expert**: Can govern AI-assisted development processes

#### Assessment

- Written exam (60%)
- Practical exercises (30%)
- Code review assessment (10%)

---

## 13. CONTINUOUS IMPROVEMENT

### 13.1 Feedback Collection

#### User Feedback

- Monthly surveys on tool effectiveness
- Issue tracking for tool problems
- Suggestion box for improvements
- Usage analytics review

#### Metrics Monitoring

- Code acceptance rates
- Review cycle times
- Defect rates
- User satisfaction scores

### 13.2 Process Improvement

#### Quarterly Reviews

- Analyze metrics trends
- Identify pain points
- Plan improvements
- Update documentation

#### Tool Updates

- Monitor Claude Code releases
- Evaluate new features
- Plan rollout strategy
- Train users on changes

### 13.3 Innovation

#### Experimentation

- Pilot new AI models
- Test new MCP servers
- Try novel workflows
- Share learnings

#### Research

- Stay current with AI developments
- Attend Anthropic webinars
- Participate in community forums
- Contribute to open source

---

## 14. APPENDICES

### Appendix A: Quick Reference Commands

```bash
# Setup and Configuration
claude-code init                    # Initialize project
claude-code config show             # Show current configuration
claude-code auth status             # Check authentication
claude-code mcp list                # List MCP servers

# Development
claude-code                         # Start interactive session
claude-code --help                  # Show help
claude-code --version               # Show version
claude-code review <file>           # Quick code review
claude-code test <file>             # Generate tests

# MCP Operations
claude-code mcp start <name>        # Start MCP server
claude-code mcp stop <name>         # Stop MCP server
claude-code mcp restart <name>      # Restart MCP server
claude-code mcp logs <name>         # View server logs

# Troubleshooting
claude-code --debug                 # Debug mode
claude-code --verbose               # Verbose output
claude-code doctor                  # Check system health
claude-code clear-cache             # Clear cache

# Utilities
claude-code usage                   # Show API usage
claude-code export-logs             # Export logs for support
claude-code update                  # Update to latest version
```

### Appendix B: Configuration Reference

#### Complete .claude/config.json Schema

```json
{
  "model": "claude-sonnet-4.5 | claude-opus | claude-haiku",
  "maxTokens": 8096,
  "temperature": 0.7,

  "safety": {
    "sandboxMode": true,
    "requireApproval": ["file_write", "bash_exec", "network_request"],
    "allowedPaths": ["src/", "tests/", "docs/"],
    "restrictedPaths": ["/etc/", "~/.ssh/", "*.env"]
  },

  "logging": {
    "enabled": true,
    "level": "info | debug | trace",
    "path": ".claude/logs/",
    "rotation": {
      "maxSize": "10MB",
      "maxFiles": 10
    }
  },

  "compliance": {
    "commitFormat": "conventional",
    "requireAITag": true,
    "codeReviewRequired": true,
    "traceabilityRequired": true
  },

  "cache": {
    "enabled": true,
    "ttl": 3600,
    "maxSize": "100MB"
  },

  "limits": {
    "dailyRequests": 1000,
    "monthlyTokens": 1000000,
    "maxFileSize": "1MB"
  },

  "notifications": {
    "enabled": true,
    "channels": ["console", "email"],
    "events": ["error", "security", "quota"]
  }
}
```

### Appendix C: Troubleshooting Decision Tree

```
Issue?
├─ Authentication Failed
│  ├─ API key not set → Set ANTHROPIC_API_KEY
│  ├─ Invalid key → Generate new key from console
│  └─ Key expired → Rotate key
│
├─ Slow Performance
│  ├─ Large context → Enable cache, reduce context
│  ├─ Network issues → Check connectivity
│  └─ Wrong model → Use faster model (Haiku)
│
├─ MCP Server Issues
│  ├─ Connection failed → Check server running, verify config
│  ├─ Timeout → Increase timeout in config
│  └─ Authentication → Check MCP server credentials
│
├─ Permission Errors
│  ├─ File write blocked → Check allowedPaths in config
│  ├─ Bash exec blocked → Verify safety.requireApproval
│  └─ Directory access → Check file permissions (ls -la)
│
└─ Quality Issues
   ├─ Low acceptance rate → Review prompts, add context
   ├─ Security vulnerabilities → Enhance security review process
   └─ Test failures → Improve test generation prompts
```

### Appendix D: Useful Resources

#### Official Documentation

- [Claude Code Documentation](https://docs.anthropic.com/claude-code)
- [MCP Specification](https://spec.modelcontextprotocol.io/)
- [Anthropic API Reference](https://docs.anthropic.com/api)

#### Internal Resources

- PROC-AI-001: AI-Assisted Development Procedure
- PROC-SDLC-001: Software Development Lifecycle
- ISO_Doc_Kit: Complete ISO documentation
- Team Wiki: Best practices and examples

#### Community

- Anthropic Discord Server
- GitHub Discussions
- Stack Overflow (tag: claude-code)

### Appendix E: Glossary

| Term                   | Definition                                                        |
| ---------------------- | ----------------------------------------------------------------- |
| **Claude Code**        | AI-powered CLI development assistant by Anthropic                 |
| **MCP**                | Model Context Protocol - extensibility framework for Claude Code  |
| **Prompt Engineering** | Practice of crafting effective AI instructions                    |
| **HITL**               | Human-in-the-Loop - AI process with mandatory human oversight     |
| **Token**              | Unit of text processing in AI models (roughly 0.75 words)         |
| **Context Window**     | Amount of text the AI model can process at once                   |
| **Temperature**        | Parameter controlling AI creativity (0=deterministic, 1=creative) |
| **Hallucination**      | AI generating incorrect or fabricated information                 |
| **Sandbox Mode**       | Restricted execution environment for safety                       |

---

## 15. REVISION HISTORY

| Version | Date       | Author                    | Changes                                                       |
| ------- | ---------- | ------------------------- | ------------------------------------------------------------- |
| 1.0     | 2025-10-24 | AI Integration Specialist | Initial release - Comprehensive Claude Code development guide |

---

## 16. APPROVAL

**Document Approvers**:

| Role                             | Name               | Signature          | Date         |
| -------------------------------- | ------------------ | ------------------ | ------------ |
| **AI Integration Specialist**    | ********\_******** | ********\_******** | **\_\_\_\_** |
| **Development Team Lead**        | ********\_******** | ********\_******** | **\_\_\_\_** |
| **Quality Manager**              | ********\_******** | ********\_******** | **\_\_\_\_** |
| **Information Security Officer** | ********\_******** | ********\_******** | **\_\_\_\_** |

---

**END OF DOCUMENT**

---

**For Support**:

- Technical Issues: Contact AI Integration Specialist
- Process Questions: Contact Development Team Lead
- Compliance Questions: Contact Quality Manager
- Security Questions: Contact Information Security Officer

**Document Location**: `/mcp-server/services/document/ISO_Doc_Kit/04-Supporting/Claude_Code_Development_Tools_Guide.md`

**Retention**: Permanent (updated annually or as needed)
