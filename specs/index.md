# Specifications Master Index

**Created:** 2025-01-16T12:00:00Z UTC  
**Modified:** 2025-01-16T12:00:00Z UTC

**⚠️ IMPORTANT:** All specifications in this directory are **examples and templates**. Customize them for your specific project needs.

Complete table of contents for all project specifications.

---

## Quick Links

- **[Features](#features)** - Feature-based specifications
- **[API Specifications](#api-specifications)** - OpenAPI and API contracts
- **[Data Schemas](#data-schemas)** - Database and validation schemas
- **[Conventions](#conventions)** - Coding standards and best practices
- **[Examples](#examples)** - Request/response examples
- **[Components](#components)** - Reusable specification components
- **[Contracts](#contracts)** - API contracts

---

## Features

### User Authentication
- [Feature Specification](./features/example-feature.md) - Complete P.E.C model example
- [API Contract](./api/openapi.yaml#/paths/~1auth~1login) - Login endpoint
- [Request Example](./examples/requests/login-request.json)
- [Response Example](./examples/responses/login-success.json)

### User Management
- [User Profile Management](./features/user-management/user-profile.md) - Profile viewing and updates
- [User Management Overview](./features/user-management/README.md) - User management features

---

## API Specifications

- [OpenAPI Specification](./api/openapi.yaml) - Complete API contract
- [API Contract](./contracts/api-contract.md) - Human-readable API contract
- [API Reference](./api/README.md) - API documentation

---

## Data Schemas

- [Database Schema](./schemas/database-schema.md) - Database structure
- [Validation Schemas](./schemas/) - Data validation rules

---

## Conventions

- [00 - Overview](./conventions/00-overview.md) - Conventions overview
- [00 - Feature Spec Template](./conventions/00-feature-spec-template.md) - Template for features
- [01 - Language Conventions](./conventions/01-language-conventions.md) - Language-specific standards
- [02 - API Design](./conventions/02-api-design.md) - API design patterns
- [03 - Database Patterns](./conventions/03-database-patterns.md) - Database design
- [04 - Testing Standards](./conventions/04-testing-standards.md) - Testing conventions
- [05 - Security Guidelines](./conventions/05-security-guidelines.md) - Security standards
- [06 - Deployment Rules](./conventions/06-deployment-rules.md) - Deployment practices
- [07 - Documentation Standards](./conventions/07-documentation-standards.md) - Documentation requirements

---

## Examples

### Request Examples (JSON)
- [Login Request](./examples/requests/login-request.json)
- [Create User Request](./examples/requests/create-user-request.json)

### Response Examples (JSON)
- [Login Success](./examples/responses/login-success.json)
- [Error Response](./examples/responses/error-response.json)

### Code Examples

#### TypeScript
- [Login Service](./examples/typescript/auth-login-service.ts) - Service implementation example
- [Auth Controller](./examples/typescript/auth-controller.ts) - API controller example
- [User Model](./examples/typescript/user-model.ts) - Data model example

#### Python
- [Login Service](./examples/python/auth_login_service.py) - Service implementation example
- [Auth Controller](./examples/python/auth_controller.py) - FastAPI controller example
- [User Model](./examples/python/user_model.py) - SQLAlchemy/Pydantic model example

---

## Components

### Common Components
- [Pagination](./components/common/pagination.yaml) - Pagination parameters
- [Error Responses](./components/common/error-responses.yaml) - Standard error formats
- [Auth Headers](./components/common/auth-headers.yaml) - Authentication headers

### Models
- [User Model](./components/models/user.yaml) - User data model
- [Common Models](./components/models/) - Other data models

---

## Contracts

- [API Contract](./contracts/api-contract.md) - Complete API contract documentation

---

## Workflows

- [GitHub Workflow](./workflows/github-workflow.md) - Issue tracking, PRs, branch strategy
- [Task Management](./workflows/task-management.md) - Task lifecycle and tracking
- [Issue Tracking](./workflows/issue-tracking.md) - Issue types and lifecycle
- [Bug Tracking](./workflows/bug-tracking.md) - Bug severity, triage, resolution
- [Feature Development](./workflows/feature-development.md) - Feature development stages

---

## Memory & Context

- [Constitution](./memory/constitution.md) - Non-negotiable project rules and constraints

---

## Related Directories

- **Memory:** `memory/` - Persistent context files (constitution)
- **Schemas:** `schemas/` - Data schemas
- **Security:** `security/` - Security specifications
- **Tests:** `tests/` - Test specifications
- **Validation:** `validation/` - Validation rules
- **Versions:** `versions/` - API versioning
- **Workflows:** `workflows/` - Process workflows (tasks, tickets, bugs)
- **Integrations:** `integrations/` - Integration specifications

---

**Last Updated:** Check individual files for modification dates
