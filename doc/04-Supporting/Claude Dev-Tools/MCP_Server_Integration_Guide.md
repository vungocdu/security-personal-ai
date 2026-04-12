# MCP Server Integration Guide

**MERCURY SOLUTIONS**
**Model Context Protocol - Enterprise Implementation**

---

## DOCUMENT CONTROL

| Field                | Value                                              |
| -------------------- | -------------------------------------------------- |
| **Document ID**      | SUPP-DEV-002                                       |
| **Title**            | MCP Server Integration Guide                       |
| **Owner**            | AI Integration Specialist                          |
| **Version**          | 1.0                                                |
| **Status**           | Approved                                           |
| **Classification**   | Internal                                           |
| **Creation Date**    | 2025-10-24                                         |
| **Last Updated**     | 2025-10-24                                         |
| **Approved By**      | Development Team Lead, AI Integration Specialist   |
| **Approval Date**    | 2025-10-24                                         |
| **Next Review Date** | 2026-01-24                                         |
| **Related**          | PROC-AI-001, SUPP-DEV-001, PROC-SDLC-001, ISMS-001 |
| **AI-Assisted**      | [X] Yes - Tool: Claude Code 4.5 [ ] No             |

---

## 1. INTRODUCTION

### 1.1 Purpose

This guide defines standards and procedures for developing, deploying, and operating Model Context Protocol (MCP) servers within Mercury Solution's AI-assisted development ecosystem.

### 1.2 Scope

**Covers**:

- MCP architecture and concepts
- Server development lifecycle
- Security and compliance requirements
- Deployment and operations
- Testing and quality assurance
- Mercury Solution MCP server catalog

**Does Not Cover**:

- General Claude Code usage (see SUPP-DEV-001)
- AI-assisted development procedures (see PROC-AI-001)
- Non-MCP integrations

### 1.3 Target Audience

- Backend Developers
- DevOps Engineers
- AI Integration Specialists
- System Architects
- Technical Leads

---

## 2. MCP FUNDAMENTALS

### 2.1 What is MCP?

Model Context Protocol (MCP) is an open protocol that enables AI assistants like Claude Code to interact with external tools, data sources, and services. It extends AI capabilities beyond text generation to include:

- Database operations
- API testing and integration
- File system operations
- Custom business logic execution
- External service integration

### 2.2 Architecture Overview

```
┌─────────────────────────────────────────────────────────┐
│                     Claude Code CLI                      │
│  ┌────────────────────────────────────────────────────┐ │
│  │            MCP Client (Built-in)                   │ │
│  └──────┬──────────────────────┬──────────────────────┘ │
└─────────┼──────────────────────┼────────────────────────┘
          │                      │
          │ MCP Protocol         │ MCP Protocol
          │ (JSON-RPC over       │ (JSON-RPC over
          │  stdio/http)         │  stdio/http)
          │                      │
┌─────────▼──────────┐  ┌────────▼──────────────┐
│  MCP Server:       │  │  MCP Server:          │
│  Document Service  │  │  PMS Core Service     │
├────────────────────┤  ├───────────────────────┤
│ Capabilities:      │  │ Capabilities:         │
│ - Template Gen     │  │ - Database Query      │
│ - Compliance Check │  │ - API Testing         │
│ - Index Search     │  │ - Schema Analysis     │
└────────┬───────────┘  └────────┬──────────────┘
         │                       │
         │                       │
    ┌────▼────┐             ┌────▼──────────┐
    │  Files  │             │  PostgreSQL    │
    │  (Docs) │             │  Database      │
    └─────────┘             └────────────────┘
```

### 2.3 Core Concepts

#### 2.3.1 Capabilities

Services that an MCP server exposes. Examples:

- `database.query` - Execute database queries
- `document.generate` - Generate documents from templates
- `api.test` - Test API endpoints
- `schema.analyze` - Analyze database schemas

#### 2.3.2 Resources

Data or content that an MCP server can provide:

- Database schemas
- API specifications
- Configuration files
- Documentation templates

#### 2.3.3 Tools

Discrete operations that Claude Code can invoke:

- Execute SQL query
- Generate document from template
- Call API endpoint
- Validate data

#### 2.3.4 Prompts

Pre-defined instruction templates for common tasks:

- Generate migration script
- Create test data
- Analyze performance
- Review security

---

## 3. MCP SERVER DEVELOPMENT

### 3.1 Development Standards

#### 3.1.1 Technology Stack

**Required**:

- **Language**: Node.js 18+ (TypeScript recommended)
- **MCP SDK**: `@anthropic-ai/mcp-sdk` latest version
- **Testing**: Jest or Mocha
- **Linting**: ESLint with Airbnb config
- **Formatting**: Prettier

**Optional**:

- Database clients (pg, mysql2, mongodb)
- HTTP clients (axios, node-fetch)
- Logging (winston, pino)
- Monitoring (prometheus-client)

#### 3.1.2 Project Structure

```
mcp-server/services/<service-name>/
├── src/
│   ├── server.ts              # Main server implementation
│   ├── capabilities/          # Capability handlers
│   │   ├── database.ts
│   │   ├── api.ts
│   │   └── index.ts
│   ├── models/                # Data models and DTOs
│   ├── utils/                 # Utility functions
│   ├── config/                # Configuration
│   │   ├── config.ts
│   │   └── constants.ts
│   └── types/                 # TypeScript types
│       └── index.d.ts
├── tests/
│   ├── unit/                  # Unit tests
│   ├── integration/           # Integration tests
│   └── fixtures/              # Test data
├── docs/
│   ├── README.md              # Service documentation
│   ├── API.md                 # API/capability reference
│   └── DEPLOYMENT.md          # Deployment guide
├── .env.example               # Environment variable template
├── .eslintrc.js               # ESLint configuration
├── .prettierrc                # Prettier configuration
├── tsconfig.json              # TypeScript configuration
├── package.json               # Dependencies and scripts
└── jest.config.js             # Jest configuration
```

### 3.2 Server Implementation

#### 3.2.1 Basic Server Template

**File: `src/server.ts`**

```typescript
import { MCPServer, Capability, Tool, Resource } from '@anthropic-ai/mcp-sdk';
import { config } from './config/config';
import { DatabaseCapability } from './capabilities/database';
import { APICapability } from './capabilities/api';

/**
 * Mercury Solution MCP Server
 *
 * @description Provides capabilities for [specific domain]
 * @version 1.0.0
 * @compliance ISO/IEC 12207, ISO/IEC 27001
 */
class MercuryMCPServer extends MCPServer {
  private databaseCapability: DatabaseCapability;
  private apiCapability: APICapability;

  constructor() {
    super({
      name: config.server.name,
      version: config.server.version,
      description: config.server.description,
      author: 'Mercury Solutions',
      license: 'Proprietary',
    });

    // Initialize capabilities
    this.databaseCapability = new DatabaseCapability(config.database);
    this.apiCapability = new APICapability(config.api);

    // Register capabilities
    this.registerCapabilities();

    // Setup error handling
    this.setupErrorHandling();

    // Setup audit logging per ISMS-001
    this.setupAuditLogging();
  }

  /**
   * Register all server capabilities
   */
  private registerCapabilities(): void {
    // Database capabilities
    this.registerCapability(
      'database.query',
      this.databaseCapability.executeQuery.bind(this.databaseCapability)
    );
    this.registerCapability(
      'database.schema',
      this.databaseCapability.getSchema.bind(this.databaseCapability)
    );

    // API capabilities
    this.registerCapability(
      'api.test',
      this.apiCapability.testEndpoint.bind(this.apiCapability)
    );
    this.registerCapability(
      'api.document',
      this.apiCapability.generateDocumentation.bind(this.apiCapability)
    );

    // Health check
    this.registerCapability('health.check', this.healthCheck.bind(this));
  }

  /**
   * Setup error handling
   */
  private setupErrorHandling(): void {
    this.on('error', (error: Error) => {
      this.logError('server.error', error);

      // Critical errors per ISMS-001 Section 11
      if (this.isCriticalError(error)) {
        this.escalateIncident(error);
      }
    });

    // Graceful shutdown
    process.on('SIGTERM', () => {
      this.log('Received SIGTERM, shutting down gracefully');
      this.shutdown();
    });
  }

  /**
   * Setup audit logging per ISMS-001 Section 12.4
   */
  private setupAuditLogging(): void {
    this.on('capability.invoke', event => {
      this.auditLog({
        timestamp: new Date().toISOString(),
        event: 'capability.invoked',
        capability: event.capability,
        user: event.user,
        input: this.sanitizeForAudit(event.input),
        success: true,
      });
    });

    this.on('capability.error', event => {
      this.auditLog({
        timestamp: new Date().toISOString(),
        event: 'capability.failed',
        capability: event.capability,
        user: event.user,
        error: event.error.message,
        success: false,
      });
    });
  }

  /**
   * Health check capability
   */
  private async healthCheck(): Promise<object> {
    return {
      status: 'healthy',
      uptime: process.uptime(),
      memory: process.memoryUsage(),
      timestamp: new Date().toISOString(),
    };
  }

  /**
   * Sanitize data for audit logging
   * Removes sensitive information per ISMS-001 Section 8.2
   */
  private sanitizeForAudit(data: any): any {
    // Remove credentials, API keys, PII
    const sanitized = JSON.parse(JSON.stringify(data));

    const sensitiveFields = [
      'password',
      'apiKey',
      'token',
      'secret',
      'ssn',
      'creditCard',
      'email',
      'phone',
    ];

    const redact = (obj: any): any => {
      if (typeof obj !== 'object' || obj === null) return obj;

      for (const key in obj) {
        if (
          sensitiveFields.some(field =>
            key.toLowerCase().includes(field.toLowerCase())
          )
        ) {
          obj[key] = '[REDACTED]';
        } else if (typeof obj[key] === 'object') {
          redact(obj[key]);
        }
      }

      return obj;
    };

    return redact(sanitized);
  }

  /**
   * Determine if error is critical
   */
  private isCriticalError(error: Error): boolean {
    const criticalPatterns = [
      /authentication/i,
      /authorization/i,
      /security/i,
      /data.*breach/i,
      /injection/i,
    ];

    return criticalPatterns.some(pattern => pattern.test(error.message));
  }

  /**
   * Escalate incident per ISMS-001 Section 11
   */
  private async escalateIncident(error: Error): Promise<void> {
    // Implementation depends on incident management system
    this.logError('critical.incident', error);

    // Notify security team
    // Create incident ticket
    // Follow incident response procedure
  }

  /**
   * Log error with context
   */
  private logError(context: string, error: Error): void {
    console.error({
      timestamp: new Date().toISOString(),
      context,
      message: error.message,
      stack: error.stack,
      server: this.name,
      version: this.version,
    });
  }

  /**
   * Audit log entry
   */
  private auditLog(entry: object): void {
    // Write to audit log file or service
    console.log(JSON.stringify(entry));
  }

  /**
   * Graceful shutdown
   */
  private async shutdown(): Promise<void> {
    try {
      await this.databaseCapability.close();
      await this.apiCapability.close();

      this.log('Server shutdown complete');
      process.exit(0);
    } catch (error) {
      this.logError('shutdown.error', error as Error);
      process.exit(1);
    }
  }

  /**
   * Log message
   */
  private log(message: string): void {
    console.log({
      timestamp: new Date().toISOString(),
      level: 'info',
      message,
      server: this.name,
    });
  }
}

// Start server
const server = new MercuryMCPServer();
server.start().catch(error => {
  console.error('Failed to start MCP server:', error);
  process.exit(1);
});

export default MercuryMCPServer;
```

#### 3.2.2 Capability Implementation

**File: `src/capabilities/database.ts`**

```typescript
import { Pool, QueryResult } from 'pg';
import { DatabaseConfig } from '../config/config';

/**
 * Database capability for MCP server
 * Provides secure database operations with proper access controls
 */
export class DatabaseCapability {
  private pool: Pool;
  private allowedOperations: string[];

  constructor(config: DatabaseConfig) {
    this.pool = new Pool({
      host: config.host,
      port: config.port,
      database: config.database,
      user: config.user,
      password: config.password,
      max: config.maxConnections || 10,
      idleTimeoutMillis: 30000,
      connectionTimeoutMillis: 2000,

      // SSL for production per ISMS-001
      ssl: config.ssl
        ? {
            rejectUnauthorized: true,
            ca: config.sslCA,
          }
        : undefined,
    });

    // Define allowed operations per ISMS-001 Section 12.2
    this.allowedOperations = config.allowedOperations || [
      'SELECT',
      'INSERT',
      'UPDATE',
      'DELETE',
    ];
  }

  /**
   * Execute database query with security controls
   *
   * @param query SQL query to execute
   * @param params Query parameters (prevents SQL injection)
   * @returns Query results
   * @throws Error if query is not allowed or fails
   */
  async executeQuery(params: {
    query: string;
    params?: any[];
    user?: string;
  }): Promise<QueryResult> {
    // Validate query per PROC-AI-001 Section 8
    this.validateQuery(params.query);

    // Check permissions
    if (!this.hasPermission(params.user, params.query)) {
      throw new Error('Insufficient permissions for query operation');
    }

    try {
      // Execute with timeout per NFR criteria
      const client = await this.pool.connect();

      try {
        // Set statement timeout
        await client.query('SET statement_timeout = 30000'); // 30 seconds

        // Execute query
        const result = await client.query(params.query, params.params);

        // Audit log
        this.auditQuery(params, result);

        return result;
      } finally {
        client.release();
      }
    } catch (error) {
      this.logError('query.execution', error as Error, params);
      throw new Error(`Query execution failed: ${(error as Error).message}`);
    }
  }

  /**
   * Get database schema information
   */
  async getSchema(params: {
    tableName?: string;
    schemaName?: string;
  }): Promise<object> {
    const query = `
      SELECT
        table_schema,
        table_name,
        column_name,
        data_type,
        is_nullable,
        column_default,
        character_maximum_length
      FROM information_schema.columns
      WHERE table_schema = $1
      ${params.tableName ? 'AND table_name = $2' : ''}
      ORDER BY table_name, ordinal_position
    `;

    const queryParams = params.tableName
      ? [params.schemaName || 'public', params.tableName]
      : [params.schemaName || 'public'];

    const result = await this.executeQuery({
      query,
      params: queryParams,
    });

    return this.formatSchemaResult(result);
  }

  /**
   * Validate query for security
   */
  private validateQuery(query: string): void {
    // Check for disallowed operations
    const queryUpper = query.toUpperCase().trim();

    const operation = queryUpper.split(/\s+/)[0];
    if (!this.allowedOperations.includes(operation)) {
      throw new Error(`Operation ${operation} is not allowed`);
    }

    // Check for dangerous patterns
    const dangerousPatterns = [
      /;\s*(DROP|TRUNCATE|ALTER)/i,
      /--/, // SQL comments
      /\/\*/, // Multi-line comments
      /xp_/i, // Extended procedures
      /exec(\s|\()/i, // Execute
      /execute(\s|\()/i,
    ];

    for (const pattern of dangerousPatterns) {
      if (pattern.test(query)) {
        throw new Error('Query contains potentially dangerous patterns');
      }
    }

    // Require parameterized queries for user input
    if (query.includes("'") && !query.includes('$')) {
      throw new Error('Use parameterized queries to prevent SQL injection');
    }
  }

  /**
   * Check user permissions
   */
  private hasPermission(user: string | undefined, query: string): boolean {
    // Implementation depends on RBAC system
    // Reference: RBAC_Matrix_By_Endpoint.md

    if (!user) {
      return false;
    }

    // For now, basic operation-based check
    const operation = query.toUpperCase().trim().split(/\s+/)[0];

    // Define role-based permissions
    const permissions: Record<string, string[]> = {
      admin: ['SELECT', 'INSERT', 'UPDATE', 'DELETE'],
      developer: ['SELECT', 'INSERT', 'UPDATE'],
      readonly: ['SELECT'],
    };

    // Get user role (simplified - should integrate with actual RBAC)
    const userRole = this.getUserRole(user);
    const allowedOps = permissions[userRole] || [];

    return allowedOps.includes(operation);
  }

  /**
   * Get user role (simplified)
   */
  private getUserRole(user: string): string {
    // TODO: Integrate with actual RBAC system
    // This is a placeholder
    return 'developer';
  }

  /**
   * Format schema result for readability
   */
  private formatSchemaResult(result: QueryResult): object {
    const tables: Record<string, any> = {};

    for (const row of result.rows) {
      const tableName = row.table_name;

      if (!tables[tableName]) {
        tables[tableName] = {
          schema: row.table_schema,
          columns: [],
        };
      }

      tables[tableName].columns.push({
        name: row.column_name,
        type: row.data_type,
        nullable: row.is_nullable === 'YES',
        default: row.column_default,
        maxLength: row.character_maximum_length,
      });
    }

    return tables;
  }

  /**
   * Audit log query execution
   */
  private auditQuery(params: any, result: QueryResult): void {
    console.log(
      JSON.stringify({
        timestamp: new Date().toISOString(),
        event: 'database.query',
        user: params.user,
        query: params.query.substring(0, 200), // Truncate long queries
        rowCount: result.rowCount,
        duration: result.duration,
      })
    );
  }

  /**
   * Log error
   */
  private logError(context: string, error: Error, params: any): void {
    console.error({
      timestamp: new Date().toISOString(),
      context,
      error: error.message,
      query: params.query?.substring(0, 200),
    });
  }

  /**
   * Close database connection pool
   */
  async close(): Promise<void> {
    await this.pool.end();
  }
}
```

### 3.3 Security Requirements

#### 3.3.1 Authentication and Authorization

Per ISMS-001 Section 9:

- Implement API key authentication for MCP server access
- Validate all incoming requests
- Implement rate limiting
- Use principle of least privilege

#### 3.3.2 Data Protection

Per ISMS-001 Section 8:

- Encrypt sensitive data in transit (TLS)
- Sanitize logs (remove PII, credentials)
- Validate and sanitize all inputs
- Implement SQL injection prevention

#### 3.3.3 Audit Logging

Per ISMS-001 Section 12.4:

- Log all capability invocations
- Include timestamp, user, action, result
- Retain logs per data retention policy
- Secure logs from tampering

---

## 4. TESTING AND QUALITY ASSURANCE

### 4.1 Unit Testing

**Example: `tests/unit/database.capability.test.ts`**

```typescript
import { DatabaseCapability } from '../../src/capabilities/database';
import { Pool } from 'pg';

jest.mock('pg', () => {
  const mockPool = {
    connect: jest.fn(),
    end: jest.fn(),
  };
  return { Pool: jest.fn(() => mockPool) };
});

describe('DatabaseCapability', () => {
  let capability: DatabaseCapability;
  let mockClient: any;

  beforeEach(() => {
    mockClient = {
      query: jest.fn(),
      release: jest.fn(),
    };

    (Pool as any).mockImplementation(() => ({
      connect: jest.fn().mockResolvedValue(mockClient),
      end: jest.fn(),
    }));

    capability = new DatabaseCapability({
      host: 'localhost',
      port: 5432,
      database: 'test',
      user: 'test',
      password: 'test',
      allowedOperations: ['SELECT'],
    });
  });

  describe('executeQuery', () => {
    it('should execute valid SELECT query', async () => {
      const mockResult = {
        rows: [{ id: 1, name: 'Test' }],
        rowCount: 1,
      };

      mockClient.query.mockResolvedValue(mockResult);

      const result = await capability.executeQuery({
        query: 'SELECT * FROM users WHERE id = $1',
        params: [1],
        user: 'test-user',
      });

      expect(result.rowCount).toBe(1);
      expect(result.rows).toHaveLength(1);
    });

    it('should reject disallowed operations', async () => {
      await expect(
        capability.executeQuery({
          query: 'DROP TABLE users',
          user: 'test-user',
        })
      ).rejects.toThrow('Operation DROP is not allowed');
    });

    it('should reject queries with SQL injection attempts', async () => {
      await expect(
        capability.executeQuery({
          query: "SELECT * FROM users WHERE name = 'admin' --",
          user: 'test-user',
        })
      ).rejects.toThrow('dangerous patterns');
    });

    it('should enforce parameterized queries', async () => {
      await expect(
        capability.executeQuery({
          query: "SELECT * FROM users WHERE name = 'test'",
          user: 'test-user',
        })
      ).rejects.toThrow('Use parameterized queries');
    });
  });

  describe('getSchema', () => {
    it('should return formatted schema information', async () => {
      const mockSchemaResult = {
        rows: [
          {
            table_schema: 'public',
            table_name: 'users',
            column_name: 'id',
            data_type: 'integer',
            is_nullable: 'NO',
            column_default: 'nextval',
            character_maximum_length: null,
          },
          {
            table_schema: 'public',
            table_name: 'users',
            column_name: 'name',
            data_type: 'varchar',
            is_nullable: 'YES',
            column_default: null,
            character_maximum_length: 255,
          },
        ],
        rowCount: 2,
      };

      mockClient.query.mockResolvedValue(mockSchemaResult);

      const schema = await capability.getSchema({
        tableName: 'users',
      });

      expect(schema).toHaveProperty('users');
      expect((schema as any).users.columns).toHaveLength(2);
    });
  });
});
```

### 4.2 Integration Testing

**Example: `tests/integration/server.integration.test.ts`**

```typescript
import { MCPClient } from '@anthropic-ai/mcp-sdk';
import MercuryMCPServer from '../../src/server';

describe('MCP Server Integration', () => {
  let server: MercuryMCPServer;
  let client: MCPClient;

  beforeAll(async () => {
    server = new MercuryMCPServer();
    await server.start();

    client = new MCPClient({
      serverUrl: 'http://localhost:3000',
    });
  });

  afterAll(async () => {
    await server.stop();
  });

  it('should respond to health check', async () => {
    const result = await client.invoke('health.check', {});

    expect(result).toHaveProperty('status', 'healthy');
    expect(result).toHaveProperty('uptime');
  });

  it('should execute database query capability', async () => {
    const result = await client.invoke('database.query', {
      query: 'SELECT * FROM users LIMIT 10',
      params: [],
      user: 'test-user',
    });

    expect(result).toHaveProperty('rows');
    expect(Array.isArray(result.rows)).toBe(true);
  });

  it('should reject unauthorized access', async () => {
    await expect(
      client.invoke('database.query', {
        query: 'DELETE FROM users',
        user: 'unauthorized-user',
      })
    ).rejects.toThrow();
  });
});
```

### 4.3 Quality Standards

Per PROC-AI-001 Section 7:

| Metric                        | Target          | Measurement             |
| ----------------------------- | --------------- | ----------------------- |
| **Unit Test Coverage**        | ≥80%            | Jest coverage report    |
| **Integration Test Coverage** | ≥70%            | End-to-end test results |
| **Security Scan**             | 0 critical/high | npm audit, Snyk         |
| **Code Quality**              | Grade A         | SonarQube analysis      |
| **Performance**               | <100ms P95      | Load testing            |
| **Availability**              | >99.9%          | Uptime monitoring       |

---

## 5. DEPLOYMENT AND OPERATIONS

### 5.1 Deployment Process

#### 5.1.1 Environment Configuration

**Production Environment Variables** (`.env.production`):

```bash
# Server Configuration
NODE_ENV=production
SERVER_NAME=pms-core-mcp
SERVER_VERSION=1.0.0
SERVER_PORT=3000

# Database
DATABASE_HOST=db.production.mercury-solution.com
DATABASE_PORT=5432
DATABASE_NAME=pms_production
DATABASE_USER=mcp_user
DATABASE_PASSWORD=${SECRET_DB_PASSWORD}
DATABASE_SSL=true
DATABASE_MAX_CONNECTIONS=20

# Security
API_KEY=${SECRET_API_KEY}
JWT_SECRET=${SECRET_JWT}
ENCRYPTION_KEY=${SECRET_ENCRYPTION}

# Logging
LOG_LEVEL=info
LOG_PATH=/var/log/mcp-servers/
LOG_RETENTION_DAYS=90

# Monitoring
PROMETHEUS_PORT=9090
HEALTH_CHECK_INTERVAL=30000

# Rate Limiting
RATE_LIMIT_WINDOW=60000
RATE_LIMIT_MAX_REQUESTS=100
```

#### 5.1.2 Docker Deployment

**Dockerfile**:

```dockerfile
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm ci --only=production

# Copy application
COPY dist/ ./dist/
COPY .env.production ./.env

# Security: Run as non-root user
RUN addgroup -g 1001 -S mcpuser && \
    adduser -S mcpuser -u 1001
USER mcpuser

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD node -e "require('http').get('http://localhost:3000/health', (r) => { process.exit(r.statusCode === 200 ? 0 : 1); })"

# Expose port
EXPOSE 3000

# Start server
CMD ["node", "dist/server.js"]
```

**docker-compose.yml**:

```yaml
version: '3.8'

services:
  mcp-pms-core:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: mcp-pms-core
    restart: unless-stopped
    ports:
      - '3000:3000'
      - '9090:9090' # Prometheus metrics
    environment:
      - NODE_ENV=production
    env_file:
      - .env.production
    volumes:
      - ./logs:/var/log/mcp-servers
    networks:
      - mcp-network
    depends_on:
      - postgres
    healthcheck:
      test: ['CMD', 'curl', '-f', 'http://localhost:3000/health']
      interval: 30s
      timeout: 3s
      retries: 3
      start_period: 40s

  postgres:
    image: postgres:16-alpine
    container_name: mcp-postgres
    restart: unless-stopped
    environment:
      POSTGRES_DB: pms_production
      POSTGRES_USER: mcp_user
      POSTGRES_PASSWORD: ${SECRET_DB_PASSWORD}
    volumes:
      - postgres-data:/var/lib/postgresql/data
    networks:
      - mcp-network

networks:
  mcp-network:
    driver: bridge

volumes:
  postgres-data:
```

#### 5.1.3 Kubernetes Deployment

**k8s/deployment.yaml**:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mcp-pms-core
  namespace: mcp-servers
  labels:
    app: mcp-pms-core
    version: v1.0.0
spec:
  replicas: 3
  selector:
    matchLabels:
      app: mcp-pms-core
  template:
    metadata:
      labels:
        app: mcp-pms-core
        version: v1.0.0
    spec:
      containers:
        - name: mcp-server
          image: mercury-solution/mcp-pms-core:1.0.0
          ports:
            - containerPort: 3000
              name: http
            - containerPort: 9090
              name: metrics
          env:
            - name: NODE_ENV
              value: 'production'
          envFrom:
            - secretRef:
                name: mcp-secrets
          resources:
            requests:
              memory: '256Mi'
              cpu: '250m'
            limits:
              memory: '512Mi'
              cpu: '500m'
          livenessProbe:
            httpGet:
              path: /health
              port: 3000
            initialDelaySeconds: 30
            periodSeconds: 10
          readinessProbe:
            httpGet:
              path: /health
              port: 3000
            initialDelaySeconds: 5
            periodSeconds: 5
---
apiVersion: v1
kind: Service
metadata:
  name: mcp-pms-core
  namespace: mcp-servers
spec:
  selector:
    app: mcp-pms-core
  ports:
    - name: http
      port: 80
      targetPort: 3000
    - name: metrics
      port: 9090
      targetPort: 9090
  type: ClusterIP
```

### 5.2 Monitoring and Observability

#### 5.2.1 Health Checks

Implement per TEMPLATE-LC-008-SLO_SLI_Plan.md:

```typescript
// Health check endpoint
server.registerCapability('health.check', async () => {
  const checks = {
    server: await this.checkServerHealth(),
    database: await this.checkDatabaseHealth(),
    memory: await this.checkMemoryHealth(),
    disk: await this.checkDiskHealth(),
  };

  const isHealthy = Object.values(checks).every(
    check => check.status === 'healthy'
  );

  return {
    status: isHealthy ? 'healthy' : 'unhealthy',
    checks,
    timestamp: new Date().toISOString(),
    uptime: process.uptime(),
  };
});
```

#### 5.2.2 Metrics Collection

**Prometheus Metrics**:

```typescript
import { Counter, Histogram, Gauge, register } from 'prom-client';

// Request counter
const requestCounter = new Counter({
  name: 'mcp_requests_total',
  help: 'Total number of MCP requests',
  labelNames: ['capability', 'status'],
});

// Request duration
const requestDuration = new Histogram({
  name: 'mcp_request_duration_seconds',
  help: 'Duration of MCP requests',
  labelNames: ['capability'],
  buckets: [0.01, 0.05, 0.1, 0.5, 1, 5],
});

// Active connections
const activeConnections = new Gauge({
  name: 'mcp_active_connections',
  help: 'Number of active connections',
});

// Export metrics endpoint
server.registerCapability('metrics', async () => {
  return register.metrics();
});
```

#### 5.2.3 Logging

**Structured Logging with Winston**:

```typescript
import winston from 'winston';

const logger = winston.createLogger({
  level: process.env.LOG_LEVEL || 'info',
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.errors({ stack: true }),
    winston.format.json()
  ),
  defaultMeta: {
    service: 'mcp-pms-core',
    version: '1.0.0',
  },
  transports: [
    new winston.transports.File({
      filename: '/var/log/mcp-servers/error.log',
      level: 'error',
      maxsize: 10485760, // 10MB
      maxFiles: 10,
    }),
    new winston.transports.File({
      filename: '/var/log/mcp-servers/combined.log',
      maxsize: 10485760,
      maxFiles: 30,
    }),
  ],
});

// Console logging in development
if (process.env.NODE_ENV !== 'production') {
  logger.add(
    new winston.transports.Console({
      format: winston.format.simple(),
    })
  );
}

export { logger };
```

### 5.3 Incident Response

Per ISMS-001 Section 11:

#### 5.3.1 Incident Categories

| Severity     | Description                      | Response Time | Escalation       |
| ------------ | -------------------------------- | ------------- | ---------------- |
| **Critical** | Service down, data breach        | <15 minutes   | Security Officer |
| **High**     | Performance degradation >50%     | <1 hour       | Technical Lead   |
| **Medium**   | Non-critical feature unavailable | <4 hours      | Development Team |
| **Low**      | Minor issues, no impact          | <24 hours     | Development Team |

#### 5.3.2 Runbook

See `/03-Lifecycle/Runbook/TEMPLATE-LC-009-Operational_Runbook.md` for detailed procedures.

**Quick Reference**:

```bash
# Check server status
docker ps | grep mcp
kubectl get pods -n mcp-servers

# View logs
docker logs mcp-pms-core --tail=100
kubectl logs -f deployment/mcp-pms-core -n mcp-servers

# Restart server
docker restart mcp-pms-core
kubectl rollout restart deployment/mcp-pms-core -n mcp-servers

# Check resource usage
docker stats mcp-pms-core
kubectl top pods -n mcp-servers
```

---

## 6. MERCURY SOLUTION MCP CATALOG

### 6.1 Document Service

**Location**: `/mcp-server/services/document/`

**Purpose**: ISO documentation management and generation

**Capabilities**:

- `document.template.generate` - Generate documents from templates
- `document.compliance.check` - Check ISO compliance
- `document.index.search` - Search documentation
- `document.traceability.update` - Update traceability matrix

**Configuration**:

```json
{
  "name": "document-service",
  "version": "1.0.0",
  "capabilities": {
    "template.generate": {
      "templates": "/mcp-server/services/document/ISO_Doc_Kit/",
      "output": "./docs/generated/"
    },
    "compliance.check": {
      "standards": ["ISO/IEC 12207", "ISO/IEC 29148", "ISO/IEC 42010"],
      "rules": "./rules/compliance.json"
    }
  }
}
```

### 6.2 PMS Core Service

**Location**: `/mcp-server/services/pms/pms-core/`

**Purpose**: Property Management System database and API operations

**Capabilities**:

- `database.query` - Execute database queries
- `database.schema` - Get schema information
- `api.test` - Test API endpoints
- `business.validate` - Validate business logic

**Configuration**:

```json
{
  "name": "pms-core-service",
  "version": "1.0.0",
  "database": {
    "host": "localhost",
    "port": 5432,
    "database": "pms_development",
    "allowedOperations": ["SELECT", "INSERT", "UPDATE"]
  },
  "api": {
    "baseUrl": "http://localhost:8000/api/v1",
    "auth": {
      "type": "bearer",
      "token": "${API_TOKEN}"
    }
  }
}
```

### 6.3 Revenue Management Service

**Location**: `/mcp-server/services/pms/revenue/`

**Purpose**: Revenue management calculations and analysis

**Capabilities**:

- `pricing.calculate` - Calculate dynamic pricing
- `forecast.generate` - Generate revenue forecasts
- `metrics.analyze` - Analyze revenue metrics
- `scenario.compare` - Compare pricing scenarios

### 6.4 OTA Calculator Service

**Location**: `/mcp-server/services/pms/ota/`

**Purpose**: OTA commission and rate calculations

**Capabilities**:

- `commission.calculate` - Calculate OTA commissions
- `rate.convert` - Convert rates between currencies
- `parity.check` - Check rate parity across channels

### 6.5 Database Operations Service

**Location**: `/mcp-server/services/pms/database-ops/`

**Purpose**: Database administration and migrations

**Capabilities**:

- `migration.generate` - Generate migration scripts
- `schema.validate` - Validate schema integrity
- `data.seed` - Generate test data
- `backup.create` - Create database backups

### 6.6 Analytics Service

**Location**: `/mcp-server/services/pms/analytics/`

**Purpose**: Data analytics and reporting

**Capabilities**:

- `report.generate` - Generate reports
- `query.optimize` - Optimize queries
- `data.aggregate` - Aggregate data
- `visualization.create` - Create visualizations

---

## 7. COMPLIANCE AND AUDIT

### 7.1 ISO 12207 Compliance

MCP servers must align with software lifecycle processes:

| Process            | MCP Requirement            | Verification            |
| ------------------ | -------------------------- | ----------------------- |
| **Implementation** | Follow coding standards    | Code review, linting    |
| **Integration**    | CI/CD integration tested   | Integration tests       |
| **Verification**   | Unit and integration tests | Test coverage ≥80%      |
| **Validation**     | Stakeholder acceptance     | User acceptance testing |
| **Operation**      | Monitoring and maintenance | Uptime ≥99.9%           |

### 7.2 ISO 27001 Compliance

Security controls per ISMS-001:

| Control                            | Requirement                      | Implementation                |
| ---------------------------------- | -------------------------------- | ----------------------------- |
| **Access Control (9.x)**           | Authentication and authorization | API keys, RBAC                |
| **Cryptography (10.x)**            | Data encryption                  | TLS, encrypted storage        |
| **Operations Security (12.x)**     | Logging and monitoring           | Structured logs, metrics      |
| **Communications Security (13.x)** | Secure communications            | HTTPS, VPN                    |
| **Secure Development (14.x)**      | Security in SDLC                 | Security testing, code review |

### 7.3 Audit Requirements

#### 7.3.1 Audit Checklist

- [ ] Authentication and authorization implemented
- [ ] All inputs validated and sanitized
- [ ] SQL injection prevention in place
- [ ] Sensitive data encrypted in transit
- [ ] Audit logging enabled and working
- [ ] Error handling doesn't expose sensitive info
- [ ] Unit test coverage ≥80%
- [ ] Integration tests passing
- [ ] Security scan shows no critical issues
- [ ] Documentation complete and accurate
- [ ] Deployment procedures documented
- [ ] Monitoring and alerting configured
- [ ] Incident response procedures defined
- [ ] Data retention policy implemented

#### 7.3.2 Audit Evidence

Per Compliance_Matrix_ISO.md:

- Source code repository
- Test results and coverage reports
- Security scan reports
- Deployment logs
- Monitoring dashboards
- Incident reports
- Change management records

---

## 8. BEST PRACTICES

### 8.1 Development

#### DO

- ✅ Use TypeScript for type safety
- ✅ Implement comprehensive error handling
- ✅ Write unit and integration tests
- ✅ Use parameterized queries
- ✅ Validate all inputs
- ✅ Log all operations for audit
- ✅ Follow project coding standards
- ✅ Document all capabilities

#### DON'T

- ❌ Hardcode credentials or secrets
- ❌ Expose sensitive data in logs
- ❌ Skip input validation
- ❌ Allow arbitrary code execution
- ❌ Ignore security warnings
- ❌ Deploy without testing
- ❌ Skip documentation

### 8.2 Security

- Principle of least privilege
- Defense in depth
- Fail securely
- Secure by default
- Input validation everywhere
- Output encoding
- Audit everything
- Encrypt sensitive data

### 8.3 Performance

- Connection pooling
- Query optimization
- Caching where appropriate
- Async operations
- Resource limits
- Timeout handling
- Load testing

---

## 9. REVISION HISTORY

| Version | Date       | Author                    | Changes                                                      |
| ------- | ---------- | ------------------------- | ------------------------------------------------------------ |
| 1.0     | 2025-10-24 | AI Integration Specialist | Initial release - Comprehensive MCP server integration guide |

---

## 10. APPROVAL

**Document Approvers**:

| Role                             | Name               | Signature          | Date         |
| -------------------------------- | ------------------ | ------------------ | ------------ |
| **AI Integration Specialist**    | ********\_******** | ********\_******** | **\_\_\_\_** |
| **Development Team Lead**        | ********\_******** | ********\_******** | **\_\_\_\_** |
| **Information Security Officer** | ********\_******** | ********\_******** | **\_\_\_\_** |
| **Quality Manager**              | ********\_******** | ********\_******** | **\_\_\_\_** |

---

**END OF DOCUMENT**

---

**For Support**:

- Technical Issues: Contact AI Integration Specialist
- Security Questions: Contact Information Security Officer
- Compliance Questions: Contact Quality Manager

**Document Location**: `/mcp-server/services/document/ISO_Doc_Kit/04-Supporting/MCP_Server_Integration_Guide.md`

**Retention**: Permanent (updated annually or as needed)
