# API Design Conventions

**Created:** 2025-01-16T12:00:00Z UTC  
**Modified:** 2025-01-16T12:00:00Z UTC

API design patterns, standards, and best practices.

---

## Overview

This document defines conventions for designing and implementing APIs.

---

## RESTful Principles

### Resource Naming
- Use nouns, not verbs: `/users` not `/getUsers`
- Use plural nouns: `/users` not `/user`
- Use kebab-case for multi-word resources: `/user-profiles`

### HTTP Methods
- **GET** - Retrieve resources
- **POST** - Create resources
- **PUT** - Update entire resource
- **PATCH** - Partial update
- **DELETE** - Delete resources

### Status Codes
- **200** - Success
- **201** - Created
- **400** - Bad Request
- **401** - Unauthorized
- **403** - Forbidden
- **404** - Not Found
- **429** - Too Many Requests
- **500** - Internal Server Error

---

## Request/Response Format

### Request Format
- Use JSON for request bodies
- Validate all inputs
- Use consistent field naming

### Response Format
```json
{
  "success": true,
  "data": {},
  "error": null
}
```

### Error Format
```json
{
  "success": false,
  "data": null,
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable message"
  }
}
```

---

## Pagination

### Query Parameters
- `page` - Page number (1-indexed)
- `limit` - Items per page (default: 20, max: 100)

### Response Format
```json
{
  "data": [],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 100,
    "totalPages": 5
  }
}
```

---

## Versioning

- Use URL versioning: `/api/v1/users`
- Maintain backward compatibility
- Document breaking changes

---

## Authentication

- Use Bearer tokens in Authorization header
- Include token expiration information
- Support token refresh

---

## Related

- **OpenAPI Spec:** `../api/openapi.yaml` - API specification
- **Examples:** `../examples/` - Request/response examples
- **Contracts:** `../contracts/` - API contracts

---

**Note:** Follow these conventions for consistent API design across the project.

