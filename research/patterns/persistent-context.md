# Persistent Context Pattern (Constitution.md)

**Last Updated:** 2025-01-16  
**Category:** Patterns  
**Source:** GitHub Spec-Kit, VirtusLab Research

---

## Overview

The Persistent Context pattern uses stable, version-controlled files (like `constitution.md`) to provide AI agents with persistent memory across development sessions. This prevents context drift and ensures consistent behavior.

**Key Concept:**
> Specs become **externalized, persistent memory**

---

## The Problem

### Context Window Limitations

**Issues:**
- AI agents have limited context windows
- Context is lost between sessions
- AI forgets decisions
- Rebuilds logic repeatedly
- Hallucinates "reasonable" but wrong solutions

### Context Drift

**Symptoms:**
- AI makes different decisions in different sessions
- Inconsistent code generation
- Forgets architectural decisions
- Violates previously established rules

---

## The Solution: Constitution.md

### What is Constitution.md?

A persistent file that defines:
- Stable, non-negotiable rules
- Architectural decisions
- Project constraints
- Coding standards
- Design principles

**Location:** `memory/constitution.md` (or root `constitution.md`)

### Key Characteristics

1. **Stable:** Changes infrequently
2. **Non-Negotiable:** Must be followed
3. **Persistent:** Survives across sessions
4. **Version-Controlled:** Tracked in Git

---

## Structure

### Basic Structure

```markdown
# Project Constitution

## Non-Negotiable Rules
- Rule 1: Description
- Rule 2: Description

## Architectural Decisions
- Decision 1: Rationale
- Decision 2: Rationale

## Constraints
- Constraint 1: Limit
- Constraint 2: Limit

## Coding Standards
- Standard 1: Requirement
- Standard 2: Requirement
```

### Example Constitution

```markdown
# Project Constitution

## Non-Negotiable Rules
- All code must be type-safe (TypeScript strict mode)
- Follow clean architecture principles
- Write tests for all business logic
- Use dependency injection

## Architectural Decisions
- Use PostgreSQL for primary database
- Redis for caching
- RESTful API design
- Microservices architecture

## Constraints
- No external API calls in business logic layer
- All errors must be typed
- Maximum function length: 50 lines
- All public APIs must be documented

## Coding Standards
- Use async/await, not callbacks
- Prefer composition over inheritance
- Use meaningful variable names
- Follow project linting rules
```

---

## Best Practices

### 1. Keep It Stable

**Do:**
- Focus on non-negotiable rules
- Document architectural decisions
- Set clear constraints
- Update only when necessary

**Don't:**
- Include frequently changing details
- Add temporary rules
- Mix with implementation details
- Over-specify

### 2. Make It Clear

**Do:**
- Use clear language
- Provide examples
- Explain rationale
- Be specific

**Don't:**
- Use vague descriptions
- Assume knowledge
- Leave ambiguities
- Over-complicate

### 3. Version Control

**Do:**
- Track in Git
- Use semantic versioning
- Document changes
- Maintain history

**Don't:**
- Store outside version control
- Ignore changes
- Lose history
- Skip documentation

### 4. Reference in Specs

**Do:**
- Link to constitution from specs
- Reference architectural decisions
- Enforce constraints
- Maintain consistency

**Don't:**
- Duplicate constitution content
- Create conflicting rules
- Ignore constitution
- Override without reason

---

## Directory Structure Options

### Option 1: Memory Directory (Spec-Kit Style)

```
.
├── memory/
│   └── constitution.md
├── specs/
│   └── ...
```

**Benefits:**
- Clear separation
- Organized structure
- Easy to find

### Option 2: Root Level

```
.
├── constitution.md
├── specs/
│   └── ...
```

**Benefits:**
- Easy to access
- Visible at root
- Simple structure

**Note:** The concept is what matters, not the exact directory name.

---

## How AI Agents Use It

### Workflow

1. **AI Agent Starts**
   - Loads `constitution.md`
   - Understands project rules
   - Reads constraints

2. **During Development**
   - References constitution
   - Applies rules
   - Respects constraints
   - Follows standards

3. **Context Persistence**
   - Constitution persists across sessions
   - AI re-hydrates context
   - Consistent behavior
   - No context drift

---

## Benefits

### For AI Agents
- Persistent memory
- Consistent behavior
- Reduced hallucinations
- Better code quality

### For Development Teams
- Shared understanding
- Consistent codebase
- Easier onboarding
- Better maintainability

---

## Common Patterns

### Pattern 1: Architecture Rules

```markdown
## Architectural Decisions

### Database
- Use PostgreSQL 15+
- Use Drizzle ORM
- All migrations must be reversible

### API Design
- RESTful principles
- Version all APIs
- Use OpenAPI specs
```

### Pattern 2: Coding Standards

```markdown
## Coding Standards

### TypeScript
- Strict mode enabled
- No `any` types
- Prefer interfaces over types
- Use async/await

### Testing
- Write tests before code (TDD)
- Minimum 80% coverage
- Use descriptive test names
```

### Pattern 3: Constraints

```markdown
## Constraints

### Performance
- API response time < 200ms
- Database queries < 50ms
- Max file size: 10MB

### Security
- All inputs validated
- Use parameterized queries
- HTTPS only in production
```

---

## Integration with Specs

### Constitution → Specs → Code

```
constitution.md (stable rules)
    ↓
specs/001-feature/ (feature-specific)
    ↓
code/ (implementation)
```

**Flow:**
1. Constitution defines project-wide rules
2. Specs define feature-specific requirements
3. Code implements following both

---

## Related Patterns

- [AI-Agnostic Documentation](./ai-agnostic-documentation.md) - Tool-agnostic approach
- [Three-Document Pattern](./three-document-pattern.md) - Requirements/Design/Tasks
- [Directory Structures](./directory-structures.md) - Common structures

---

## References

- GitHub Spec-Kit: Constitution.md pattern
- VirtusLab: Spec-Kit Tames AI Coding Chaos
- Intent-Driven.dev: Context Management

---

**Next:** Explore [Three-Document Pattern](./three-document-pattern.md) for feature-level specifications.

