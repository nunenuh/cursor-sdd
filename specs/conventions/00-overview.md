# Specification Conventions Overview

**Created:** 2025-01-16T12:00:00Z UTC  
**Modified:** 2025-01-16T12:00:00Z UTC

**Purpose:** Define how specifications are structured and organized in this project

---

## Directory Structure

```
specs/
├── README.md         # Specs overview
├── index.md          # Master index
├── features/         # Feature specifications (P.E.C model)
├── api/             # API contracts and schemas
├── components/      # Reusable OpenAPI components
├── contracts/       # API contracts
├── conventions/     # This directory - coding standards and patterns
├── examples/        # Code examples (TypeScript, Python) and API examples
├── schemas/         # Data schemas
├── security/        # Security specifications
├── tests/           # Test specifications
├── validation/      # Validation rules
├── versions/        # API versioning
├── workflows/       # Process workflows
└── integrations/   # Integration specifications
```

---

## Convention Files

This directory contains numbered convention files:

- `00-overview.md` - This file - overview of conventions
- `00-feature-spec-template.md` - P.E.C model template for features
- `01-language-conventions.md` - Language-specific coding standards
- `02-api-design.md` - API design patterns and standards
- `03-database-patterns.md` - Database design patterns
- `04-testing-standards.md` - Testing conventions
- `05-security-guidelines.md` - Security standards
- `06-deployment-rules.md` - Deployment and infrastructure
- `07-documentation-standards.md` - Documentation requirements

---

## Specification Types

### Feature Specifications
- **Location:** `specs/features/[feature-name].md`
- **Template:** See `00-feature-spec-template.md`
- **Structure:** P.E.C model (Problem, Expectation, Constraint)

### API Specifications
- **Location:** `specs/api/[api-name].yaml` or `.json`
- **Format:** OpenAPI, AsyncAPI, or JSON Schema
- **Purpose:** Machine-readable API contracts

### Workflow Specifications
- **Location:** `specs/workflows/[workflow-name].md`
- **Purpose:** Process definitions and workflows
- **Format:** Markdown with Mermaid diagrams

---

## Naming Conventions

### Files
- Use kebab-case: `feature-name.md`
- Be descriptive: `user-authentication.md` not `auth.md`
- Include numbers for ordered files: `01-language-conventions.md`

### Directories
- Use lowercase: `features/`, `api/`, `conventions/`
- Be clear: `user-management/` not `users/`

---

## Specification Lifecycle

1. **Create:** Write specification before implementation
2. **Review:** Get stakeholder approval
3. **Implement:** Code follows specification
4. **Validate:** Tests verify specification compliance
5. **Update:** Keep specification synchronized with code

---

## AI Agent Guidelines

When reading specifications:
- Start with `00-overview.md` for structure
- Check `../memory/constitution.md` for constraints
- Read feature spec before implementation
- Reference conventions for standards
- Validate against API contracts

---

## Code Examples

When implementing features, reference code examples:

- **TypeScript:** `../examples/typescript/` - Service, controller, model examples
- **Python:** `../examples/python/` - Service, controller, model examples
- **API Examples:** `../examples/requests/` and `../examples/responses/`

## Related Files

- **Constitution:** `../memory/constitution.md` - Project rules
- **Feature Template:** `00-feature-spec-template.md` - P.E.C template
- **Feature Example:** `../features/example-feature.md` - Complete example
- **Specs Index:** `../index.md` - Master index
- **Research:** `../../research/` directory - Best practices

---

**Next:** Review `00-feature-spec-template.md` for feature specification structure, then check `../features/example-feature.md` for a complete example.

