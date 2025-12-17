# Testing Standards

**Created:** 2025-01-16T12:00:00Z UTC  
**Modified:** 2025-01-16T12:00:00Z UTC

Testing conventions and standards.

---

## Overview

This document defines testing standards and best practices for the project.

---

## Testing Principles

- **Test from specs** - Derive tests from specifications
- **Test behavior** - Test what the code does, not how
- **Keep tests simple** - One assertion per test when possible
- **Test edge cases** - Include boundary conditions

---

## Test Types

### Unit Tests
- Test individual functions/components
- Isolate dependencies
- Fast execution
- High coverage

### Integration Tests
- Test component interactions
- Use test databases
- Test API endpoints
- Verify data flow

### E2E Tests
- Test complete workflows
- Use realistic data
- Test user scenarios
- Validate against specs

---

## Test Structure

### Arrange-Act-Assert (AAA)
```javascript
// Arrange
const user = createTestUser();

// Act
const result = login(user);

// Assert
expect(result.success).toBe(true);
```

### Test Naming
- Describe what is being tested
- Include expected outcome
- Example: `should return user when valid credentials provided`

---

## Test Data

- Use factories for test data
- Keep test data realistic
- Clean up after tests
- Use fixtures for complex data

---

## Coverage Goals

- Minimum 80% code coverage
- 100% coverage for critical paths
- Test all error cases
- Test edge cases

---

## Related

- **Feature Specs:** `../features/` - Acceptance criteria
- **Testing Docs:** `../../docs/testing/` - Testing guides

---

**Note:** Tests validate that code matches specifications.

