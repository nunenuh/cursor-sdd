# Security Guidelines

**Created:** 2025-01-16T12:00:00Z UTC  
**Modified:** 2025-01-16T12:00:00Z UTC

Security standards and best practices.

---

## Overview

This document defines security requirements and guidelines for the project.

---

## Authentication

### Password Requirements
- Minimum 8 characters
- Require letters and numbers
- Hash passwords (bcrypt, Argon2)
- Never store plain text passwords

### Token Security
- Use JWT with appropriate expiration
- Sign tokens securely (HS256 or RS256)
- Include expiration time
- Support token refresh

---

## Authorization

### Access Control
- Implement role-based access control (RBAC)
- Check permissions on every request
- Validate user ownership
- Use principle of least privilege

---

## Input Validation

### Always Validate
- All user inputs
- API request parameters
- File uploads
- Database queries (parameterized)

### Validation Rules
- Type checking
- Length limits
- Format validation
- Business rule validation

---

## Data Protection

### Sensitive Data
- Encrypt sensitive data at rest
- Use HTTPS for data in transit
- Never log sensitive information
- Sanitize error messages

### PII Handling
- Minimize PII collection
- Encrypt PII data
- Follow GDPR/privacy regulations
- Implement data retention policies

---

## API Security

### Rate Limiting
- Implement rate limits
- Return 429 status on limit exceeded
- Include retry-after header

### CORS
- Configure CORS appropriately
- Whitelist allowed origins
- Don't allow all origins in production

---

## Related

- **Constitution:** `../memory/constitution.md` - Security constraints
- **API Design:** `02-api-design.md` - API security patterns

---

**Note:** Security is non-negotiable. Follow these guidelines strictly.

