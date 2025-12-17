# Cursor Planning Document

**Created:** 2025-01-16T12:00:00Z UTC  
**Modified:** 2025-01-16T12:00:00Z UTC

**Purpose:** Planning and context for Cursor AI assistant

---

## Project Context

This project follows **Spec-Driven Development (SDD)** principles where specifications serve as the single source of truth before implementation.

---

## Key Files to Reference

### Before Any Implementation
1. **Constitution:** `specs/memory/constitution.md` - Non-negotiable rules
2. **Specs Index:** `specs/index.md` - Master index of all specifications
3. **Feature Spec:** `specs/features/[feature-name].md` - Feature requirements (P.E.C model)
4. **API Contract:** `specs/api/openapi.yaml` or `specs/contracts/` - API specifications
5. **Conventions:** `specs/conventions/` - Coding standards
6. **Code Examples:** `specs/examples/typescript/` or `specs/examples/python/` - Implementation examples

### During Implementation
- Follow specifications exactly
- Reference conventions for code style
- Check constitution for constraints
- Validate against API contracts

### After Implementation
- Update tests based on specifications
- Validate implementation matches spec
- Update spec if requirements change

---

## Common Tasks

### Adding a New Feature
1. Copy template: `specs/conventions/00-feature-spec-template.md`
2. Create feature spec in `specs/features/[feature-name].md`
3. Use P.E.C model (Problem, Expectation, Constraint)
4. Reference code examples: `specs/examples/typescript/` or `specs/examples/python/`
5. Get stakeholder approval
6. Implement following spec
7. Write tests from acceptance criteria
8. Validate against spec

### Updating Constitution
1. Only update for fundamental changes
2. Document rationale
3. Get team approval
4. Update file
5. Communicate changes

### Creating API Contract
1. Define in `specs/api/[api-name].yaml`
2. Use OpenAPI or AsyncAPI format
3. Include request/response schemas
4. Document errors
5. Reference in feature specs

---

## AI Agent Guidelines

### Context Loading Order
1. Load `specs/memory/constitution.md` first (stable context)
2. Load `specs/index.md` for overview
3. Load relevant feature spec (`specs/features/[feature-name].md`)
4. Load API contract (`specs/api/openapi.yaml` or `specs/contracts/`)
5. Load code examples (`specs/examples/typescript/` or `specs/examples/python/`)
6. Load related conventions (`specs/conventions/`)
7. Load schemas if applicable (`specs/schemas/`)

### Code Generation Rules
- Never violate constraints in `specs/memory/constitution.md`
- Follow specifications exactly
- Use conventions for code style
- Validate against API contracts
- Write tests from acceptance criteria

### Error Handling
- If spec is unclear, ask for clarification
- If constraint conflicts, flag immediately
- If implementation differs from spec, update spec first
- Document any deviations

---

## Code Examples

### TypeScript Examples
- `specs/examples/typescript/auth-login-service.ts` - Service implementation
- `specs/examples/typescript/auth-controller.ts` - API controller
- `specs/examples/typescript/user-model.ts` - Data model

### Python Examples
- `specs/examples/python/auth_login_service.py` - Service implementation
- `specs/examples/python/auth_controller.py` - FastAPI controller
- `specs/examples/python/user_model.py` - SQLAlchemy/Pydantic model

## Research References

- Research directory: `research/`
- Best practices: `research/concepts/best-practices.md`
- Frameworks: `research/frameworks/`
- Patterns: `research/patterns/`

## Important Notes

- ⚠️ **All specs are examples** - Customize for your project
- Use P.E.C model for all feature specifications
- Reference code examples when implementing
- Keep specs synchronized with code

---

**Note:** This file helps Cursor AI understand the project structure and workflow. Update as the project evolves.
