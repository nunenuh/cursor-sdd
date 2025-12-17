# Database Schema

**Created:** 2025-01-16T12:00:00Z UTC  
**Modified:** 2025-01-16T12:00:00Z UTC

**⚠️ EXAMPLE:** This is an example database schema. Customize for your project.

Database schema specification and structure.

---

## Overview

This document defines the database schema structure, tables, relationships, and constraints.

---

## Tables

### users

User accounts and authentication.

**Columns:**
- `id` (UUID, Primary Key) - Unique user identifier
- `username` (VARCHAR(255), Unique, Not Null) - Username
- `email` (VARCHAR(255), Unique, Not Null) - Email address
- `password_hash` (VARCHAR(255), Not Null) - Hashed password
- `created_at` (TIMESTAMP, Not Null) - Creation timestamp
- `updated_at` (TIMESTAMP, Not Null) - Last update timestamp

**Indexes:**
- Primary key on `id`
- Unique index on `username`
- Unique index on `email`
- Index on `created_at`

**Relationships:**
- One-to-many with `sessions` table

---

## Relationships

```
users
  ├── sessions (one-to-many)
  └── ...
```

---

## Constraints

- Usernames must be unique
- Emails must be unique and valid format
- Passwords must be hashed (never store plain text)
- Timestamps must be UTC

---

## Migration Strategy

- Use database migrations for schema changes
- Version all migrations
- Test migrations in development first
- Backup before production migrations

---

## Related

- **Conventions:** `../conventions/03-database-patterns.md` - Database patterns
- **API Spec:** `../api/openapi.yaml` - API data models

---

**Note:** This schema is an example. Customize for your project needs.
