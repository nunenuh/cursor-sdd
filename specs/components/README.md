# Reusable Components

**Created:** 2025-01-16T12:00:00Z UTC  
**Modified:** 2025-01-16T12:00:00Z UTC

**⚠️ EXAMPLES:** All components in this directory are examples. Customize for your project.

Reusable OpenAPI components for API specifications.

---

## Structure

```
components/
├── common/          # Common components (pagination, errors, auth)
│   ├── pagination.yaml
│   ├── error-responses.yaml
│   └── auth-headers.yaml
└── models/          # Data models
    └── user.yaml
```

---

## Usage

Reference components in OpenAPI specs:

```yaml
parameters:
  - $ref: '../components/common/pagination.yaml#/parameters/PageParam'

schemas:
  User:
    $ref: '../components/models/user.yaml#/schemas/User'
```

---

## Common Components

- **Pagination** - Standard pagination parameters and schemas
- **Error Responses** - Standard error response formats
- **Auth Headers** - Authentication header parameters

## Models

- **User** - User data model
- Add more models as needed

---

## Code Examples

See how components are used in code examples:
- **TypeScript:** `../examples/typescript/` - Implementation examples
- **Python:** `../examples/python/` - Implementation examples

## Related

- **API Spec:** `../api/openapi.yaml` - Complete API specification
- **API Contract:** `../contracts/api-contract.md` - Human-readable contract
- **Examples:** `../examples/` - Request/response examples

---

**Note:** Components promote reusability and consistency across API specifications. All components are examples - customize for your project.
