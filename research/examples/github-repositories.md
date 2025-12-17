# GitHub Repository Examples

**Last Updated:** 2025-01-16  
**Category:** Examples  
**Purpose:** Real-world GitHub repositories demonstrating spec-driven development

---

## Overview

This document catalogs GitHub repositories that demonstrate spec-driven development practices, especially for AI agents and AI coding assistants.

---

## Primary Examples

### 1. GitHub Spec-Kit

**Repository:** https://github.com/github/spec-kit  
**Stars:** 55.9k+ | **Forks:** 4.9k+  
**Language:** Python, Shell, PowerShell  
**License:** MIT

**Key Features:**
- Constitution.md pattern
- CLI commands (`/speckit.*`)
- Template system
- Memory directory structure
- Agent-agnostic design

**Directory Structure:**
```
.
├── memory/
│   └── constitution.md
├── specs/
│   └── 001-feature-name/
│       ├── spec.md
│       ├── plan.md
│       ├── tasks.md
│       └── contracts/
├── templates/
└── scripts/
```

**Learn From:**
- How to structure specs directory
- Constitution.md implementation
- CLI command patterns
- Template organization

---

### 2. Spec-Then-Code

**Repository:** https://github.com/mosofsky/spec-then-code  
**Language:** Various  
**License:** MIT

**Key Features:**
- Specification-first approach
- Context management
- Shared knowledge base
- Cross-session continuity

**Learn From:**
- Spec-first workflow
- Context persistence patterns
- Knowledge base structure

---

### 3. LIDR Academy AI Specs

**Repository:** https://github.com/LIDR-academy/ai-specs  
**Language:** Various  
**License:** MIT

**Key Features:**
- Development rules and standards
- AI agent configurations
- Portable setup
- Multi-copilot support

**Learn From:**
- AI agent configuration patterns
- Rule standardization
- Multi-tool compatibility

---

## Repository Patterns to Study

### Pattern 1: Specs Directory Structure

**Common Patterns:**

```
specs/
├── index.md
├── features/
│   ├── feature1.md
│   └── feature2.md
├── api/
│   └── openapi.yaml
├── schemas/
│   └── database-schema.md
└── conventions/
    └── coding-standards.md
```

**Variations:**
- Numbered: `001-feature-name/`
- Named: `feature-name/`
- Hierarchical: `features/category/feature/`

---

### Pattern 2: Constitution/Memory Files

**Common Locations:**
- `memory/constitution.md` (Spec-Kit style)
- `constitution.md` (root level)
- `.cursor/rules/` (Cursor IDE)
- `specs/conventions/` (convention files)

**Learn From:**
- How different projects structure persistent context
- What rules are included
- How they're organized

---

### Pattern 3: .cursorrules Files

**Common Patterns:**
- Project context
- Code style guidelines
- Architecture patterns
- Git workflow
- References to specs

**Learn From:**
- How to structure .cursorrules
- What to include
- How to reference specs
- Best practices

---

## Search Strategies

### Finding Examples

1. **Search GitHub:**
   ```
   "spec-driven development" OR "specification-driven development"
   "constitution.md" OR "memory/constitution.md"
   ".cursorrules" spec-driven
   "specs/" directory structure
   ```

2. **Look for Patterns:**
   - Repos with `specs/` directory
   - Repos with `constitution.md`
   - Repos with `.cursorrules`
   - Repos with `memory/` directory

3. **Check Topics:**
   - `spec-driven-development`
   - `ai-coding-assistant`
   - `cursor-ide`
   - `copilot`

---

## What to Look For

### Directory Structures
- How specs are organized
- Naming conventions
- Hierarchical patterns
- File organization

### Specification Formats
- Markdown structures
- YAML schemas
- JSON contracts
- Template patterns

### Integration Patterns
- How specs link to code
- How AI assistants use specs
- Workflow patterns
- Automation approaches

---

## Contributing Examples

When you find a good example:

1. **Document It:**
   - Repository URL
   - Key features
   - What to learn from it
   - Relevant patterns

2. **Categorize:**
   - Language/stack
   - Pattern type
   - Use case
   - Complexity level

3. **Update This File:**
   - Add to appropriate section
   - Include key learnings
   - Link to repository

---

## Research Status

**Current Status:** Initial research phase

**Next Steps:**
- Search for more repositories
- Analyze patterns
- Document findings
- Categorize examples

---

## Related Files

- [Case Studies](./case-studies.md) - Implementation stories
- [Implementation Examples](./implementation-examples.md) - Code examples
- [Directory Structures](../patterns/directory-structures.md) - Common structures

---

**Note:** This file will be expanded as more repositories are discovered and analyzed. Add new findings here with clear categorization and learnings.

