# Language Conventions

**Created:** 2025-01-16T12:00:00Z UTC  
**Modified:** 2025-01-16T12:00:00Z UTC

Language-specific coding standards and conventions.

---

## Overview

This document defines coding standards for the primary programming language(s) used in this project.

---

## General Principles

- **Readability** - Code should be easy to read and understand
- **Consistency** - Follow consistent patterns throughout
- **Maintainability** - Write code that's easy to maintain
- **Type Safety** - Use type systems when available

---

## Naming Conventions

### Variables
- Use descriptive names
- Use camelCase for variables (JavaScript/TypeScript)
- Use snake_case for variables (Python)
- Avoid abbreviations unless widely understood

### Functions
- Use verb-noun pattern: `getUser()`, `createReport()`
- Be descriptive: `calculateTotal()` not `calc()`

### Classes
- Use PascalCase: `UserService`, `DatabaseConnection`
- Use nouns: `User`, `Report`, `Validator`

### Constants
- Use UPPER_SNAKE_CASE: `MAX_RETRIES`, `API_BASE_URL`

---

## Code Organization

### File Structure
- One class per file (when applicable)
- Group related functions together
- Keep files focused and manageable

### Function Length
- Maximum 50 lines per function
- Break down complex functions
- Extract reusable logic

---

## Comments

### When to Comment
- Complex algorithms
- Business logic explanations
- Non-obvious code decisions
- Public API documentation

### Comment Style
- Use clear, concise language
- Explain why, not what
- Keep comments up-to-date

---

## Error Handling

- Always handle errors explicitly
- Use appropriate error types
- Provide meaningful error messages
- Log errors appropriately

---

## Related

- **Overview:** `00-overview.md` - Conventions overview
- **API Design:** `02-api-design.md` - API conventions
- **Testing:** `04-testing-standards.md` - Testing conventions

---

**Note:** Customize this file for your project's primary language(s).

