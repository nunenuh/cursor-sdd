# Usage Guide: Spec-Driven Development Boilerplate

**Created:** 2025-01-16T12:00:00Z UTC  
**Modified:** 2025-01-16T12:00:00Z UTC

**A practical guide for using this boilerplate in your projects**

---

## Table of Contents

1. [Getting Started](#getting-started)
2. [Creating Specifications](#creating-specifications)
3. [Working with AI Assistants](#working-with-ai-assistants)
4. [Best Practices](#best-practices)
5. [Common Workflows](#common-workflows)
6. [Troubleshooting](#troubleshooting)

---

## Getting Started

### Step 1: Understand the Structure

```
specs/              → Write specifications here
specs/memory/       → Stable project rules (constitution.md)
.cursorrules        → AI assistant configuration
specs/conventions/  → Templates and standards
```

### Step 2: Customize Constitution

Edit `specs/memory/constitution.md`:

```markdown
## Non-Negotiable Rules

### Architecture
- Use microservices architecture
- Follow clean architecture principles

### Technology Stack
- TypeScript 5.1+ with strict mode
- React 18.2+ for frontend
- Node.js 20+ for backend

### Coding Standards
- All code must be type-safe
- Maximum function length: 50 lines
```

### Step 3: Create Your First Feature Spec

1. Copy the template:
   ```bash
   cp specs/conventions/00-feature-spec-template.md specs/features/user-authentication.md
   ```

2. Fill in the P.E.C sections:
   - **Problem:** What problem does this solve?
   - **Expectation:** What should it do?
   - **Constraint:** What are the hard limits?

3. Add acceptance criteria and technical design

4. Get stakeholder approval

---

## Creating Specifications

### Feature Specifications

**Location:** `specs/features/[feature-name].md`

**Structure (P.E.C Model):**

```markdown
## Problem
What is being solved?

## Expectation
What outputs are expected?

## Constraints
Hard limits that must never be violated
```

**Example:** See `specs/features/example-feature.md`

### API Specifications

**Location:** `specs/api/[api-name].yaml`

**Format:** OpenAPI or AsyncAPI

```yaml
openapi: 3.0.0
info:
  title: User API
  version: 1.0.0
paths:
  /users:
    get:
      summary: List users
      responses:
        '200':
          description: Success
```

### Convention Files

**Location:** `specs/conventions/[NN]-[topic].md`

**Numbering:**
- `00-overview.md` - Overview
- `01-language-conventions.md` - Language standards
- `02-api-design.md` - API patterns
- etc.

---

## Working with AI Assistants

### How AI Reads Your Project

**Context Loading Order:**

1. **Constitution** (`specs/memory/constitution.md`)
   - Stable rules
   - Architectural decisions
   - Constraints

2. **Feature Spec** (`specs/features/[feature-name].md`)
   - Problem, Expectation, Constraint
   - Acceptance criteria
   - Technical design

3. **Conventions** (`specs/conventions/`)
   - Coding standards
   - Patterns
   - Best practices

4. **API Contracts** (`specs/api/`)
   - Request/response schemas
   - Error definitions

### AI Behavior

**Before Coding:**
- ✅ Reads specifications first
- ✅ Understands constraints
- ✅ Checks constitution
- ✅ Follows conventions

**During Coding:**
- ✅ Implements exactly as specified
- ✅ Never violates constraints
- ✅ Uses conventions for style
- ✅ Validates against API contracts

**After Coding:**
- ✅ Writes tests from acceptance criteria
- ✅ Validates implementation matches spec
- ✅ Updates spec if requirements change

---

## Best Practices

### 1. Write Specs Before Code

**❌ Bad:**
```
1. Write code
2. Document what you did
```

**✅ Good:**
```
1. Write specification
2. Get approval
3. Write code following spec
4. Validate against spec
```

### 2. Keep Specs Focused

**❌ Bad:**
- One huge spec covering everything
- Vague descriptions
- Missing constraints

**✅ Good:**
- One feature per spec
- Clear Problem/Expectation/Constraint
- Specific acceptance criteria

### 3. Update Constitution Sparingly

**❌ Bad:**
- Updating constitution for every feature
- Temporary decisions in constitution

**✅ Good:**
- Only fundamental changes
- Stable, non-negotiable rules
- Feature-specific decisions in feature specs

### 4. Use AI-Agnostic Formats

**❌ Bad:**
- Tool-specific formats
- Proprietary schemas
- Hidden metadata

**✅ Good:**
- Markdown for documentation
- YAML/JSON for structured data
- Standard formats (OpenAPI, JSON Schema)

---

## Common Workflows

### Workflow 1: Adding a New Feature

```
1. Create feature spec
   → specs/features/my-feature.md

2. Fill in P.E.C sections
   → Problem, Expectation, Constraint

3. Add acceptance criteria
   → Testable conditions

4. Get stakeholder approval
   → Review and sign-off

5. AI assistant reads spec
   → Generates implementation

6. Write tests from acceptance criteria
   → Validate spec compliance

7. Review implementation
   → Ensure it matches spec
```

### Workflow 2: Updating Constitution

```
1. Identify fundamental change needed
   → Architecture, technology, security

2. Discuss with team
   → Get consensus

3. Document rationale
   → Why this change?

4. Update constitution.md
   → Add decision and rationale

5. Communicate changes
   → Notify team

6. Version control commit
   → Track changes
```

### Workflow 3: Creating API Contract

```
1. Define API in feature spec
   → Endpoints, request/response

2. Create OpenAPI spec
   → specs/api/my-api.yaml

3. Include schemas
   → Request/response models

4. Document errors
   → Error codes and messages

5. Reference in feature spec
   → Link to API contract

6. Validate implementation
   → Check against contract
```

---

## Troubleshooting

### Problem: AI Assistant Not Following Specs

**Solution:**
- Check `.cursorrules` is configured correctly
- Ensure spec is in `specs/features/` directory
- Verify spec follows P.E.C model structure
- Check constitution.md is readable

### Problem: Context Drift (AI Forgetting Rules)

**Solution:**
- Ensure `specs/memory/constitution.md` exists
- Keep constitution stable (don't change frequently)
- Reference constitution in `.cursorrules`
- Use persistent context pattern

### Problem: Specs Too Large

**Solution:**
- Break into smaller, focused specs
- One feature per spec file
- Use references to other specs
- Keep sections concise

### Problem: Constraint Conflicts

**Solution:**
- Review all constraints in spec
- Check constitution for conflicts
- Prioritize constraints
- Document resolution

---

## Examples

### Example 1: Simple Feature Spec

See `specs/features/example-feature.md` for a complete example.

### Example 2: Constitution

See `specs/memory/constitution.md` for structure (customize for your project).

### Example 3: Convention File

See `specs/conventions/00-overview.md` for convention structure.

---

## Next Steps

1. **Customize:** Update constitution and cursor rules
2. **Create:** Write your first feature specification
3. **Develop:** Use AI assistants to implement
4. **Validate:** Ensure code matches specifications
5. **Iterate:** Refine specs and code together

---

**For more information, see:**
- `README.md` - Overview
- `research/` - Best practices and research
- `specs/conventions/` - Templates and standards
