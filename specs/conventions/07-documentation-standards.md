# Documentation Standards

**Created:** 2025-01-16T12:00:00Z UTC  
**Modified:** 2025-01-16T12:00:00Z UTC

Documentation requirements and standards.

---

## Overview

This document defines standards for project documentation.

---

## Documentation Types

### Specifications (`specs/`)
- Feature specifications
- API contracts
- Data schemas
- Conventions

### Documentation (`docs/`)
- Architecture documentation
- Implementation guides
- User guides
- ADRs

---

## Markdown Standards

### File Headers
All markdown files must include:
```markdown
# Document Title

**Created:** YYYY-MM-DDTHH:MM:SSZ UTC  
**Modified:** YYYY-MM-DDTHH:MM:SSZ UTC
```

### Structure
- Use clear headings (H1 for title, H2 for sections)
- Use lists for multiple items
- Include code examples
- Link to related documents

---

## Code Documentation

### Comments
- Explain why, not what
- Document complex logic
- Keep comments up-to-date
- Use clear language

### API Documentation
- Document all public APIs
- Include parameter descriptions
- Provide examples
- Document error cases

---

## Keeping Documentation Updated

- Update docs when code changes
- Review docs in code reviews
- Keep specs synchronized with implementation
- Remove outdated documentation

---

## Related

- **Templates:** `../../docs/templates/` - Documentation templates
- **Markdown Template:** `../../docs/templates/markdown-header-template.md`

---

**Note:** Good documentation is essential for maintainability and AI agent understanding.

