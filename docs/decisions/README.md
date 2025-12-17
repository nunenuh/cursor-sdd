# Architectural Decision Records (ADRs)

**Created:** 2025-12-17T04:58:48Z UTC
**Modified:** 2025-12-17T04:58:48Z UTC


**Purpose:** Document important architectural decisions and their rationale  
**Format:** ADR template (Markdown)  
**Audience:** Team members, future developers, AI agents

---

## Overview

Architectural Decision Records (ADRs) document significant architectural decisions, including:

- What decision was made
- Why it was made
- Alternatives considered
- Consequences

---

## ADR Format

Each ADR follows this structure:

```markdown
# ADR-XXX: [Decision Title]

**Status:** Proposed | Accepted | Deprecated | Superseded  
**Date:** YYYY-MM-DD  
**Deciders:** [Names]

## Context
What is the issue we're trying to address?

## Decision
What is the change we're proposing or have agreed to implement?

## Consequences
What becomes easier or more difficult to do because of this change?

## Alternatives Considered
- Alternative 1: Description
- Alternative 2: Description
```

---

## ADR Numbering

- `adr-001-*.md` - First decision
- `adr-002-*.md` - Second decision
- etc.

---

## Related

- **Constitution:** `../../specs/memory/constitution.md` - Stable rules (non-negotiable)
- **Architecture:** `../architecture/` - System design documentation
- **Specifications:** `../../specs/` - Feature and API specifications

---

**Note:** ADRs document decisions that affect the architecture. Constitution documents non-negotiable rules.

