# API Versioning

**Created:** 2025-01-16T12:00:00Z UTC  
**Modified:** 2025-01-16T12:00:00Z UTC

**⚠️ EXAMPLE:** This directory is for API versioning specifications. Add your versioning specs here.

API versioning specifications and strategy.

---

## Overview

This directory contains API versioning specifications and version history.

---

## Versioning Strategy

### URL Versioning
- Use URL path: `/api/v1/users`
- Increment major version for breaking changes
- Maintain backward compatibility when possible

### Version Files
- `v1.md` - Version 1 specification
- `v2.md` - Version 2 specification (when needed)
- `migration-guide.md` - Migration between versions

---

## Breaking Changes

Document breaking changes:
- What changed
- Why it changed
- Migration path
- Deprecation timeline

---

## Related

- **API Spec:** `../api/openapi.yaml` - Current API specification
- **Contracts:** `../contracts/` - API contracts
- **Conventions:** `../conventions/02-api-design.md` - API design conventions
- **Specs Index:** `../index.md` - Master index

---

**Note:** Versioning allows API evolution while maintaining compatibility. Add your versioning specifications here.
