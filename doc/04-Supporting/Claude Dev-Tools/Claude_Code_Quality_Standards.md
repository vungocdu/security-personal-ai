# Claude Code Quality Standards

**MERCURY SOLUTIONS**
**AI-Assisted Development Quality Assurance**

---

## DOCUMENT CONTROL

| Field                | Value                                            |
| -------------------- | ------------------------------------------------ |
| **Document ID**      | SUPP-DEV-003                                     |
| **Title**            | Claude Code Quality Standards                    |
| **Owner**            | Quality Manager                                  |
| **Version**          | 1.0                                              |
| **Status**           | Approved                                         |
| **Classification**   | Internal                                         |
| **Creation Date**    | 2025-10-24                                       |
| **Last Updated**     | 2025-10-24                                       |
| **Approved By**      | Quality Manager, Development Team Lead           |
| **Approval Date**    | 2025-10-24                                       |
| **Next Review Date** | 2026-01-24                                       |
| **Related**          | PROC-AI-001, SUPP-DEV-001, QM-001, PROC-SDLC-001 |
| **AI-Assisted**      | [X] Yes - Tool: Claude Code 4.5 [ ] No           |

---

## 1. PURPOSE AND SCOPE

### 1.1 Purpose

This document defines measurable quality standards and acceptance criteria for AI-generated code, documentation, and artifacts produced using Claude Code at Mercury Solution.

### 1.2 Scope

**Applies to**:

- All code generated or assisted by Claude Code
- AI-generated documentation
- AI-assisted testing artifacts
- AI-generated configuration and scripts

**Compliance**:

- ISO/IEC 25010:2011 (Software Quality Model)
- ISO/IEC 12207:2017 (Software Lifecycle)
- PROC-AI-001 (AI-Assisted Development Procedure)
- QM-001 (Quality Management System)

---

## 2. QUALITY DIMENSIONS

### 2.1 ISO 25010 Quality Model

Mercury Solution evaluates AI-generated artifacts against eight quality characteristics:

| Quality Characteristic     | Applies To                    | Priority |
| -------------------------- | ----------------------------- | -------- |
| **Functional Suitability** | Code, APIs, Business Logic    | Critical |
| **Performance Efficiency** | Code, Queries, Algorithms     | High     |
| **Compatibility**          | Integrations, APIs            | High     |
| **Usability**              | Documentation, UI Code        | Medium   |
| **Reliability**            | Error Handling, Resilience    | Critical |
| **Security**               | Authentication, Data Handling | Critical |
| **Maintainability**        | Code Structure, Documentation | High     |
| **Portability**            | Deployment, Configuration     | Medium   |

---

## 3. CODE QUALITY STANDARDS

### 3.1 Functional Correctness

#### 3.1.1 Acceptance Criteria

- [ ] Implements all specified requirements (REQ-\*)
- [ ] Passes all acceptance tests
- [ ] Edge cases handled appropriately
- [ ] Business logic validates against specifications
- [ ] No undefined or null pointer exceptions

#### 3.1.2 Verification Method

```bash
# Run functional tests
npm run test:functional

# Verify requirements traceability
npm run verify:requirements -- --req=REQ-AUTH-001

# Check edge case coverage
npm run test:edge-cases
```

#### 3.1.3 Quality Gates

| Metric                    | Threshold | Action if Failed  |
| ------------------------- | --------- | ----------------- |
| Requirements Coverage     | 100%      | Block merge       |
| Functional Test Pass Rate | 100%      | Fix failures      |
| Edge Case Coverage        | ≥90%      | Add missing tests |

### 3.2 Code Style and Conventions

#### 3.2.1 Acceptance Criteria

- [ ] Follows project coding standards
- [ ] Consistent naming conventions
- [ ] Proper indentation and formatting
- [ ] No linter errors or warnings
- [ ] Comments where necessary (not excessive)

#### 3.2.2 Verification Method

```bash
# Run linter
npm run lint

# Check formatting
npm run format:check

# Verify naming conventions
npm run verify:naming
```

#### 3.2.3 Standards by Language

**TypeScript/JavaScript**:

- Airbnb style guide
- ESLint configuration: `.eslintrc.js`
- Prettier formatting
- camelCase for variables/functions
- PascalCase for classes/interfaces

**PHP (Laravel)**:

- PSR-12 coding standard
- Laravel best practices
- PHP-CS-Fixer configuration
- snake_case for database fields
- PascalCase for classes

**Python**:

- PEP 8 style guide
- Black formatter
- Type hints required
- snake_case for functions/variables
- PascalCase for classes

#### 3.2.4 Quality Gates

| Metric            | Threshold | Action if Failed       |
| ----------------- | --------- | ---------------------- |
| Linter Errors     | 0         | Must fix before commit |
| Linter Warnings   | 0         | Must fix or justify    |
| Formatting Issues | 0         | Run auto-formatter     |

### 3.3 Security Standards

#### 3.3.1 OWASP Top 10 Compliance

**Mandatory Checks**:

1. **Injection Prevention**

   ```bash
   # Check for SQL injection vulnerabilities
   npm run security:check -- --rule=sql-injection
   ```

   - Use parameterized queries
   - Validate and sanitize all inputs
   - No dynamic SQL construction with user input

2. **Authentication Bypass**

   ```bash
   # Verify authentication checks
   npm run security:check -- --rule=auth-bypass
   ```

   - All protected endpoints require authentication
   - Token validation on every request
   - No hardcoded credentials

3. **Sensitive Data Exposure**

   ```bash
   # Scan for sensitive data leaks
   npm run security:check -- --rule=sensitive-data
   ```

   - No credentials in code or logs
   - PII encrypted in transit and at rest
   - Secure key management

4. **XML External Entities (XXE)**
   - Disable external entity processing
   - Validate XML inputs

5. **Broken Access Control**

   ```bash
   # Verify authorization checks
   npm run security:check -- --rule=access-control
   ```

   - Role-based access control (RBAC)
   - Least privilege principle
   - Authorization on every endpoint

6. **Security Misconfiguration**
   - Remove debug flags in production
   - Disable directory listing
   - Security headers configured

7. **Cross-Site Scripting (XSS)**
   - Output encoding/escaping
   - Content Security Policy
   - Sanitize user input

8. **Insecure Deserialization**
   - Validate serialized data
   - Use safe deserialization methods

9. **Using Components with Known Vulnerabilities**

   ```bash
   # Check dependencies
   npm audit --audit-level=high
   ```

   - No high/critical vulnerabilities
   - Dependencies up to date

10. **Insufficient Logging & Monitoring**
    - Security events logged
    - Failed authentication attempts tracked
    - Audit trail for sensitive operations

#### 3.3.2 Security Review Checklist

For AI-generated code, verify:

**Input Validation**:

- [ ] All user inputs validated
- [ ] Whitelist validation used
- [ ] Input length limits enforced
- [ ] Type checking performed

**Output Encoding**:

- [ ] HTML output encoded
- [ ] JSON output properly escaped
- [ ] SQL parameters bound correctly
- [ ] Command injection prevented

**Authentication**:

- [ ] Strong password requirements
- [ ] Multi-factor authentication support
- [ ] Session management secure
- [ ] Token expiration enforced

**Authorization**:

- [ ] RBAC implemented correctly
- [ ] Object-level authorization
- [ ] Function-level authorization
- [ ] No privilege escalation

**Data Protection**:

- [ ] Sensitive data encrypted
- [ ] TLS/HTTPS enforced
- [ ] Secure key storage
- [ ] PII handling compliant

**Error Handling**:

- [ ] No sensitive info in error messages
- [ ] Generic error messages to users
- [ ] Detailed errors in logs only
- [ ] Exception handling complete

#### 3.3.3 Quality Gates

| Metric                   | Threshold | Action if Failed      |
| ------------------------ | --------- | --------------------- |
| Critical Vulnerabilities | 0         | Block deployment      |
| High Vulnerabilities     | 0         | Fix before merge      |
| Medium Vulnerabilities   | <5        | Document and plan fix |
| Security Test Pass Rate  | 100%      | Investigate failures  |

### 3.4 Performance Standards

#### 3.4.1 Performance Criteria

Per NFR_Criteria.md:

| Component            | Metric              | Target              | Measurement    |
| -------------------- | ------------------- | ------------------- | -------------- |
| **API Endpoints**    | Response Time       | <200ms P95          | Load testing   |
| **Database Queries** | Execution Time      | <50ms P95           | Query profiler |
| **Page Load**        | Time to Interactive | <2s                 | Lighthouse     |
| **Background Jobs**  | Processing Time     | <5min P95           | Job monitoring |
| **Memory Usage**     | Heap Size           | <512MB per instance | Profiler       |
| **CPU Usage**        | Utilization         | <70% avg            | Monitoring     |

#### 3.4.2 Anti-Patterns to Avoid

Claude Code should not generate:

**N+1 Query Problem**:

```typescript
// ❌ BAD - N+1 queries
for (const user of users) {
  const orders = await db.query('SELECT * FROM orders WHERE user_id = ?', [
    user.id,
  ]);
}

// ✅ GOOD - Single query with join
const usersWithOrders = await db.query(
  `
  SELECT u.*, o.*
  FROM users u
  LEFT JOIN orders o ON o.user_id = u.id
  WHERE u.id IN (?)
`,
  [userIds]
);
```

**Inefficient Algorithms**:

```typescript
// ❌ BAD - O(n²) complexity
function findDuplicates(arr: number[]): number[] {
  const duplicates = [];
  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[i] === arr[j]) duplicates.push(arr[i]);
    }
  }
  return duplicates;
}

// ✅ GOOD - O(n) complexity
function findDuplicates(arr: number[]): number[] {
  const seen = new Set();
  const duplicates = new Set();
  for (const num of arr) {
    if (seen.has(num)) duplicates.add(num);
    seen.add(num);
  }
  return Array.from(duplicates);
}
```

**Memory Leaks**:

```typescript
// ❌ BAD - Event listener not removed
component.addEventListener('click', handler);

// ✅ GOOD - Cleanup
const cleanup = () => component.removeEventListener('click', handler);
```

#### 3.4.3 Performance Testing

```bash
# Run performance tests
npm run test:performance

# Profile code
npm run profile

# Load testing
npm run test:load -- --users=1000 --duration=60s

# Memory leak detection
npm run test:memory-leaks
```

#### 3.4.4 Quality Gates

| Metric                | Threshold | Action if Failed      |
| --------------------- | --------- | --------------------- |
| API Response Time P95 | <200ms    | Optimize queries/code |
| Page Load Time        | <2s       | Optimize assets/code  |
| Memory Leaks          | 0         | Fix before merge      |
| CPU Usage             | <70% avg  | Optimize algorithms   |

### 3.5 Test Coverage Standards

#### 3.5.1 Coverage Requirements

| Test Type             | Coverage Target | Mandatory For           |
| --------------------- | --------------- | ----------------------- |
| **Unit Tests**        | ≥80% lines      | All business logic      |
| **Branch Coverage**   | ≥75% branches   | Complex conditionals    |
| **Integration Tests** | 100% endpoints  | All API endpoints       |
| **E2E Tests**         | 100% flows      | Critical user workflows |

#### 3.5.2 Test Quality Criteria

**Unit Tests**:

- [ ] Test one thing per test
- [ ] Descriptive test names
- [ ] Arrange-Act-Assert pattern
- [ ] No dependencies on external services
- [ ] Fast execution (<100ms per test)
- [ ] Deterministic (no flaky tests)

**Integration Tests**:

- [ ] Test real integrations
- [ ] Use test database/containers
- [ ] Clean state between tests
- [ ] Cover happy path and error cases
- [ ] Test data validation
- [ ] Verify side effects

**E2E Tests**:

- [ ] Test complete user workflows
- [ ] Use realistic test data
- [ ] Verify UI and backend
- [ ] Test error scenarios
- [ ] Browser compatibility

#### 3.5.3 Test Structure

**Good Test Example**:

```typescript
describe('ReservationService', () => {
  describe('calculateTotalPrice', () => {
    it('should calculate correct total with single room for 3 nights', async () => {
      // Arrange
      const reservation = {
        roomTypeId: 'RT-001',
        checkIn: '2025-10-24',
        checkOut: '2025-10-27',
        guests: 2,
      };
      const mockRoomRate = 150.0;

      jest.spyOn(roomRateRepository, 'getRate').mockResolvedValue(mockRoomRate);

      // Act
      const total = await reservationService.calculateTotalPrice(reservation);

      // Assert
      expect(total).toBe(450.0); // 150 * 3 nights
      expect(roomRateRepository.getRate).toHaveBeenCalledWith(
        'RT-001',
        '2025-10-24'
      );
    });

    it('should throw error for invalid date range', async () => {
      // Arrange
      const invalidReservation = {
        roomTypeId: 'RT-001',
        checkIn: '2025-10-27',
        checkOut: '2025-10-24', // Check-out before check-in
        guests: 2,
      };

      // Act & Assert
      await expect(
        reservationService.calculateTotalPrice(invalidReservation)
      ).rejects.toThrow('Check-out date must be after check-in date');
    });
  });
});
```

#### 3.5.4 Verification Method

```bash
# Run tests with coverage
npm run test:coverage

# Generate coverage report
npm run coverage:report

# Check coverage thresholds
npm run coverage:check
```

#### 3.5.5 Quality Gates

| Metric                    | Threshold | Action if Failed  |
| ------------------------- | --------- | ----------------- |
| Line Coverage             | ≥80%      | Add missing tests |
| Branch Coverage           | ≥75%      | Test all paths    |
| Integration Test Coverage | 100% APIs | Add missing tests |
| Test Pass Rate            | 100%      | Fix failures      |
| Flaky Tests               | 0         | Fix or remove     |

### 3.6 Documentation Standards

#### 3.6.1 Code Documentation

**Function Documentation**:

```typescript
/**
 * Calculate total reservation price including room rate, taxes, and fees
 *
 * @param {ReservationInput} reservation - Reservation details
 * @param {PricingOptions} options - Pricing calculation options
 * @returns {Promise<PriceBreakdown>} Detailed price breakdown
 * @throws {ValidationError} If reservation data is invalid
 * @throws {NotFoundError} If room type or rate not found
 *
 * @example
 * const price = await calculateTotalPrice({
 *   roomTypeId: 'RT-001',
 *   checkIn: '2025-10-24',
 *   checkOut: '2025-10-27',
 *   guests: 2
 * });
 * // Returns: { subtotal: 450, taxes: 67.50, total: 517.50 }
 *
 * @see {@link ReservationService#createReservation}
 * @since 1.0.0
 */
async calculateTotalPrice(
  reservation: ReservationInput,
  options?: PricingOptions
): Promise<PriceBreakdown>
```

**Class Documentation**:

```typescript
/**
 * Service for managing hotel reservations
 *
 * Handles reservation creation, modification, cancellation,
 * and pricing calculations. Implements business rules per
 * SRS-PMS-Reservation-v0.1.md.
 *
 * @class ReservationService
 * @implements {IReservationService}
 *
 * @example
 * const service = new ReservationService(repository, pricingService);
 * const reservation = await service.createReservation(data);
 *
 * @requirements REQ-PMS-001, REQ-PMS-002, REQ-PMS-015
 */
export class ReservationService implements IReservationService {
  // Implementation
}
```

#### 3.6.2 API Documentation

Must follow OpenAPI 3.0 specification:

```yaml
paths:
  /api/v1/reservations:
    post:
      summary: Create new reservation
      description: |
        Creates a new hotel reservation with specified details.
        Validates availability, calculates pricing, and confirms booking.

        **Business Rules**:
        - Check-in time: 3:00 PM
        - Check-out time: 11:00 AM
        - Minimum stay: 1 night
        - Maximum advance booking: 365 days

        **Requirements**: REQ-PMS-001, REQ-PMS-002
      operationId: createReservation
      tags:
        - Reservations
      security:
        - bearerAuth: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateReservationRequest'
            examples:
              basicReservation:
                summary: Basic reservation
                value:
                  roomTypeId: 'RT-001'
                  checkIn: '2025-10-24'
                  checkOut: '2025-10-27'
                  guests: 2
                  guestName: 'John Doe'
                  email: 'john@example.com'
      responses:
        '201':
          description: Reservation created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ReservationResponse'
        '400':
          $ref: '#/components/responses/BadRequest'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '409':
          description: Room not available for specified dates
```

#### 3.6.3 README Documentation

Every component/module must have README with:

- **Overview**: What does this do?
- **Installation**: How to set up?
- **Usage**: How to use it?
- **API Reference**: What are the interfaces?
- **Examples**: Show me how it works
- **Testing**: How to run tests?
- **Troubleshooting**: Common issues and solutions
- **Contributing**: How to contribute?

#### 3.6.4 Quality Gates

| Metric                   | Threshold | Action if Failed    |
| ------------------------ | --------- | ------------------- |
| Public API Documentation | 100%      | Add missing docs    |
| Code Comment Density     | 10-30%    | Add/remove comments |
| README Completeness      | 100%      | Complete sections   |
| API Doc Validity         | 100%      | Fix invalid specs   |

---

## 4. AI-SPECIFIC QUALITY STANDARDS

### 4.1 Prompt Quality

#### 4.1.1 Effective Prompts

**Structure**:

```
1. ROLE: Clear expertise definition
2. CONTEXT: Relevant background
3. TASK: Specific instruction
4. CONSTRAINTS: Limitations and requirements
5. OUTPUT: Expected format
6. QUALITY: Success criteria
```

**Example**:

```
ROLE: You are an expert Laravel backend developer

CONTEXT:
- Working on Mercury Solution PMS reservation module
- Using PostgreSQL database with Laravel 11
- Following ISO/IEC 12207 development standards
- Requirements: REQ-PMS-045, REQ-PMS-046

TASK:
Implement ReservationService::calculateTotalPrice() method that:
1. Calculates base room rate × nights
2. Applies equipment charges from database
3. Calculates taxes based on tax_rates table
4. Handles promotional discounts

CONSTRAINTS:
- Follow Laravel service pattern
- Use repository pattern for data access
- Performance: <10ms execution time
- Security: Validate all inputs, prevent price manipulation
- Testability: Mock external dependencies

OUTPUT:
- Complete method implementation with PHPDoc
- Unit tests with ≥85% coverage
- Example usage in docblock

QUALITY CRITERIA:
- All requirements (REQ-*) satisfied
- No N+1 query problems
- Error handling for edge cases
- Audit logging for price calculations
```

#### 4.1.2 Prompt Quality Metrics

| Metric                     | Target | Measurement    |
| -------------------------- | ------ | -------------- |
| Prompt Clarity Score       | ≥8/10  | Peer review    |
| First-Time Acceptance Rate | ≥70%   | Output quality |
| Revision Cycles            | ≤2     | Tracking       |
| Context Completeness       | 100%   | Checklist      |

### 4.2 AI Output Verification

#### 4.2.1 Mandatory Review Checklist

Before accepting AI-generated code:

**Correctness**:

- [ ] Implements specified requirements
- [ ] Handles edge cases
- [ ] Logic is sound
- [ ] No obvious bugs

**Security**:

- [ ] No hardcoded secrets
- [ ] Input validation present
- [ ] SQL injection prevented
- [ ] Authentication/authorization correct

**Performance**:

- [ ] No N+1 queries
- [ ] Efficient algorithms
- [ ] Proper indexing
- [ ] Memory management

**Maintainability**:

- [ ] Readable and well-structured
- [ ] Follows conventions
- [ ] Documented appropriately
- [ ] No code duplication

**Testing**:

- [ ] Unit tests included
- [ ] Tests are meaningful
- [ ] Coverage adequate
- [ ] Tests pass

### 4.3 AI Acceptance Metrics

Track per PROC-AI-001 Section 7.1:

| Metric                  | Target    | Action if Below Target          |
| ----------------------- | --------- | ------------------------------- |
| AI Code Acceptance Rate | >70%      | Review prompt quality           |
| AI Test Effectiveness   | >80%      | Improve test generation prompts |
| AI Doc Accuracy         | >95%      | Manual verification             |
| Review Cycle Time       | <2 hours  | Improve prompt specificity      |
| AI-Related Defects      | <5% total | Enhance review process          |

---

## 5. QUALITY ASSURANCE PROCESS

### 5.1 Pre-Commit Quality Gates

Before committing AI-generated code:

```bash
#!/bin/bash
# .git/hooks/pre-commit

# 1. Lint
echo "Running linter..."
npm run lint || exit 1

# 2. Format check
echo "Checking formatting..."
npm run format:check || exit 1

# 3. Run tests
echo "Running tests..."
npm run test || exit 1

# 4. Check coverage
echo "Checking coverage..."
npm run coverage:check || exit 1

# 5. Security scan
echo "Running security scan..."
npm audit --audit-level=high || exit 1

# 6. Verify AI tag
echo "Verifying AI assistance tag..."
if git log -1 --pretty=%B | grep -q "AI-Assisted:"; then
  echo "✅ AI assistance documented"
else
  echo "❌ Missing AI assistance tag in commit message"
  exit 1
fi

echo "✅ All pre-commit checks passed"
```

### 5.2 Code Review Process

Per PROC-AI-001 Section 6.4:

#### 5.2.1 Two-Stage Review

**Stage 1: AI Self-Review**

```bash
claude-code review src/<path> --checks=all --output=review-report.json
```

AI checks:

- Syntax and style
- Common bugs
- Security issues
- Performance anti-patterns
- Documentation gaps

**Stage 2: Human Review**

- Verify business logic
- Check architecture alignment
- Confirm security controls
- Validate test quality
- Approve or request changes

#### 5.2.2 Review SLA

| Priority | Response Time | Review Time |
| -------- | ------------- | ----------- |
| Critical | <2 hours      | <4 hours    |
| High     | <4 hours      | <8 hours    |
| Medium   | <24 hours     | <48 hours   |
| Low      | <48 hours     | <1 week     |

### 5.3 Continuous Monitoring

#### 5.3.1 Quality Metrics Dashboard

Monitor these KPIs:

```javascript
{
  "aiAcceptanceRate": 75,        // Target: >70%
  "testCoverage": 82,             // Target: ≥80%
  "securityVulnerabilities": 2,   // Target: 0 critical/high
  "codeQualityScore": 87,         // Target: >85%
  "buildSuccessRate": 96,         // Target: >95%
  "averageReviewTime": 3.2,       // Target: <4 hours
  "aiDefectRate": 3.8,            // Target: <5%
  "performanceP95": 185           // Target: <200ms
}
```

#### 5.3.2 Trend Analysis

Review trends quarterly:

- Acceptance rate improving?
- Defect rate declining?
- Review time decreasing?
- Coverage increasing?

### 5.4 Quality Improvement

#### 5.4.1 Root Cause Analysis

When quality issues occur:

1. **Identify**: What went wrong?
2. **Classify**: AI issue or human review failure?
3. **Analyze**: Why did it happen?
4. **Correct**: Fix immediate issue
5. **Prevent**: Update processes/prompts
6. **Verify**: Confirm improvement

#### 5.4.2 Continuous Improvement

- Monthly quality metrics review
- Quarterly process improvements
- Share lessons learned
- Update standards as needed

---

## 6. TOOLS AND AUTOMATION

### 6.1 Quality Assurance Tools

| Category          | Tool                       | Purpose                |
| ----------------- | -------------------------- | ---------------------- |
| **Linting**       | ESLint, PHP-CS-Fixer       | Code style enforcement |
| **Formatting**    | Prettier, Black            | Consistent formatting  |
| **Testing**       | Jest, PHPUnit, Pytest      | Test execution         |
| **Coverage**      | Istanbul, Coverage.py      | Coverage measurement   |
| **Security**      | npm audit, Snyk, SonarQube | Vulnerability scanning |
| **Performance**   | Lighthouse, k6, Artillery  | Performance testing    |
| **Documentation** | JSDoc, PHPDoc, Sphinx      | Doc generation         |
| **CI/CD**         | GitHub Actions, GitLab CI  | Automation             |

### 6.2 Automation Scripts

#### 6.2.1 Quality Check Script

```bash
#!/bin/bash
# scripts/quality-check.sh

set -e

echo "🔍 Running quality checks..."

# Lint
echo "📋 Linting..."
npm run lint

# Format
echo "✨ Checking format..."
npm run format:check

# Tests
echo "🧪 Running tests..."
npm run test

# Coverage
echo "📊 Checking coverage..."
npm run coverage:check

# Security
echo "🔒 Security scan..."
npm audit --audit-level=high

# Build
echo "🏗️  Building..."
npm run build

echo "✅ All quality checks passed!"
```

#### 6.2.2 CI/CD Integration

```yaml
# .github/workflows/quality-check.yml
name: Quality Check

on: [push, pull_request]

jobs:
  quality:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'

      - name: Install dependencies
        run: npm ci

      - name: Lint
        run: npm run lint

      - name: Format check
        run: npm run format:check

      - name: Run tests
        run: npm run test:coverage

      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          files: ./coverage/coverage-final.json

      - name: Security audit
        run: npm audit --audit-level=high

      - name: SonarQube scan
        uses: sonarsource/sonarcloud-github-action@master
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}

      - name: Build
        run: npm run build
```

---

## 7. COMPLIANCE VERIFICATION

### 7.1 Audit Checklist

For auditors reviewing AI-assisted development:

#### Code Quality

- [ ] Linter configured and passing
- [ ] Formatter applied consistently
- [ ] Coding standards followed
- [ ] No code smells (per SonarQube)

#### Testing

- [ ] Unit test coverage ≥80%
- [ ] Integration tests for all APIs
- [ ] E2E tests for critical flows
- [ ] All tests passing

#### Security

- [ ] Security scan shows no critical/high vulnerabilities
- [ ] OWASP Top 10 checks passing
- [ ] Input validation implemented
- [ ] Authentication/authorization correct

#### Documentation

- [ ] Public APIs documented
- [ ] README complete
- [ ] Architecture documented
- [ ] Deployment procedures documented

#### AI Compliance

- [ ] AI assistance documented in commits
- [ ] Human review evidence present
- [ ] Quality metrics within targets
- [ ] Traceability to requirements maintained

### 7.2 Evidence Collection

Per Compliance_Matrix_ISO.md, maintain:

| Evidence Type        | Location               | Retention |
| -------------------- | ---------------------- | --------- |
| **Test Results**     | CI/CD artifacts        | 1 year    |
| **Coverage Reports** | Codecov, SonarQube     | 1 year    |
| **Security Scans**   | Snyk, SonarQube        | 3 years   |
| **Code Reviews**     | Pull request history   | 3 years   |
| **Quality Metrics**  | Monitoring dashboards  | 1 year    |
| **Audit Logs**       | Log aggregation system | 3 years   |

---

## 8. TRAINING AND COMPETENCE

### 8.1 Required Training

| Role                  | Training                   | Duration | Frequency  |
| --------------------- | -------------------------- | -------- | ---------- |
| **All Developers**    | Quality Standards Overview | 2 hours  | Onboarding |
| **All Developers**    | AI Code Quality            | 2 hours  | Annual     |
| **Senior Developers** | Code Review Best Practices | 4 hours  | Annual     |
| **QA Specialists**    | Testing AI-Generated Code  | 4 hours  | Annual     |

### 8.2 Competence Assessment

Developers assessed via:

- Code review quality scores
- Defect escape rates
- Test coverage metrics
- Security issue detection

---

## 9. REVISION HISTORY

| Version | Date       | Author          | Changes                                                                       |
| ------- | ---------- | --------------- | ----------------------------------------------------------------------------- |
| 1.0     | 2025-10-24 | Quality Manager | Initial release - Comprehensive quality standards for AI-assisted development |

---

## 10. APPROVAL

| Role                             | Name               | Signature          | Date         |
| -------------------------------- | ------------------ | ------------------ | ------------ |
| **Quality Manager**              | ********\_******** | ********\_******** | **\_\_\_\_** |
| **Development Team Lead**        | ********\_******** | ********\_******** | **\_\_\_\_** |
| **Information Security Officer** | ********\_******** | ********\_******** | **\_\_\_\_** |

---

**END OF DOCUMENT**

**Document Location**: `/mcp-server/services/document/ISO_Doc_Kit/04-Supporting/Claude_Code_Quality_Standards.md`

**Retention**: Permanent (updated annually)
