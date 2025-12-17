# Database Patterns

**Created:** 2025-01-16T12:00:00Z UTC  
**Modified:** 2025-01-16T12:00:00Z UTC

Database design patterns and best practices.

---

## Overview

This document defines patterns and conventions for database design and access.

---

## Table Design

### Naming Conventions
- Use plural nouns: `users`, `articles`, `comments`
- Use snake_case: `user_profiles`, `created_at`
- Be descriptive: `user_authentication_tokens` not `tokens`

### Primary Keys
- Use UUIDs for distributed systems
- Use auto-incrementing integers for simple cases
- Always have a primary key

### Timestamps
- Include `created_at` and `updated_at` on all tables
- Use UTC timezone
- Auto-update `updated_at` on changes

---

## Relationships

### One-to-Many
- Foreign key on the "many" side
- Index foreign keys for performance

### Many-to-Many
- Use junction/join tables
- Include timestamps in junction tables

### One-to-One
- Use foreign key with unique constraint
- Consider if tables should be merged

---

## Indexing

### When to Index
- Foreign keys
- Frequently queried columns
- Columns used in WHERE clauses
- Columns used in JOINs

### Index Naming
- `idx_table_column` - Single column index
- `idx_table_col1_col2` - Composite index

---

## Migrations

- Version all migrations
- Make migrations reversible
- Test migrations in development
- Backup before production migrations

---

## Query Patterns

### Avoid N+1 Queries
- Use eager loading
- Batch queries when possible
- Use joins appropriately

### Use Transactions
- For related operations
- To maintain data consistency
- With proper error handling

---

## Related

- **Database Schema:** `../schemas/database-schema.md` - Schema specification
- **Conventions:** `00-overview.md` - Conventions overview

---

**Note:** Follow these patterns for consistent database design.

