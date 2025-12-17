# Specifications Directory

**Created:** 2025-01-16T12:00:00Z UTC  
**Modified:** 2025-01-16T12:00:00Z UTC

This directory contains **AI-readable specifications** that serve as the single source of truth for the project. These specs are designed to be consumed by AI coding assistants (like Cursor, GitHub Copilot, Claude Code) to understand requirements and generate consistent code.

**⚠️ IMPORTANT:** All files in this directory are **examples and templates**. Customize them for your specific project needs.

---

## Purpose

Specifications in this directory define:
- **What to build** - Feature requirements and expectations
- **How to build it** - Technical design and constraints
- **API contracts** - Request/response formats
- **Data schemas** - Database and validation schemas
- **Coding standards** - Conventions and best practices

---

## Directory Structure

```
specs/
├── README.md              # This file
├── index.md               # Master index and table of contents
├── features/              # Feature specifications (EXAMPLES)
│   └── [feature-name]/   # Feature-specific specs
├── api/                   # API contracts and schemas (EXAMPLE)
│   └── openapi.yaml       # OpenAPI specification
├── components/            # Reusable OpenAPI components (EXAMPLES)
│   ├── common/           # Common components (pagination, errors)
│   └── models/           # Data models
├── contracts/            # API contracts (EXAMPLE)
│   └── api-contract.md   # Complete API contract
├── conventions/          # Coding standards and patterns
│   ├── 00-overview.md
│   ├── 01-language-conventions.md
│   └── ...
├── examples/             # Request/response examples (EXAMPLES)
│   ├── requests/        # Request examples (JSON)
│   ├── responses/       # Response examples (JSON)
│   ├── typescript/      # TypeScript code examples
│   └── python/          # Python code examples
├── schemas/             # Data schemas (EXAMPLE)
│   └── database-schema.md
├── security/            # Security specifications
├── tests/               # Test specifications
├── validation/          # Validation rules
├── versions/            # API versioning
├── workflows/           # Process workflows
└── integrations/       # Integration specifications
```

---

## Specification Types

### Feature Specifications
- **Location:** `specs/features/[feature-name]/`
- **Format:** Markdown with P.E.C model
- **Purpose:** Define what features to build
- **Note:** All feature specs are examples - customize for your project

### API Specifications
- **Location:** `specs/api/openapi.yaml`
- **Format:** OpenAPI 3.0
- **Purpose:** Machine-readable API contracts
- **Note:** This is an example API - replace with your actual API

### Data Schemas
- **Location:** `specs/schemas/`
- **Format:** Markdown, JSON Schema, or Zod
- **Purpose:** Database and validation schemas
- **Note:** Example schemas - customize for your data model

### Conventions
- **Location:** `specs/conventions/`
- **Format:** Markdown
- **Purpose:** Coding standards and best practices
- **Note:** Templates to customize for your language/stack

---

## Code Examples

This boilerplate includes code examples in multiple languages:

### TypeScript Examples
- **Location:** `specs/examples/typescript/`
- **Purpose:** TypeScript implementation examples
- **Usage:** Reference when implementing features in TypeScript

### Python Examples
- **Location:** `specs/examples/python/`
- **Purpose:** Python implementation examples
- **Usage:** Reference when implementing features in Python

---

## Source of Truth

**Specifications are the source of truth** - code must match specifications.

- ✅ Read specs before writing code
- ✅ Update specs when requirements change
- ✅ Validate code against specs
- ✅ Keep specs synchronized with implementation

---

## For AI Agents

When generating code:
1. Read feature spec from `specs/features/`
2. Check API contract from `specs/api/` or `specs/contracts/`
3. Reference conventions from `specs/conventions/`
4. Use examples from `specs/examples/` (JSON, TypeScript, Python)
5. Follow schemas from `specs/schemas/`

---

## Customization

**All specifications are examples!** Customize them for your project:

1. **Replace example features** with your actual features
2. **Update API spec** with your actual endpoints
3. **Customize conventions** for your language/stack
4. **Add your own examples** in `specs/examples/`
5. **Update schemas** with your data model

---

## Related

- **Documentation:** `../docs/` - Human-readable documentation
- **Constitution:** `memory/constitution.md` - Project rules (persistent context)
- **Research:** `../research/` - Best practices

---

**Note:** All specifications use AI-agnostic formats (Markdown, YAML, JSON) for maximum compatibility. All content is example/template - customize for your project!
