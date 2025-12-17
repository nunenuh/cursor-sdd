# Project Constitution

**Created:** 2025-01-16T12:00:00Z UTC  
**Modified:** 2025-01-16T12:00:00Z UTC

**Purpose:** Stable, non-negotiable rules and constraints for this project  
**Status:** Living document - update only when fundamental decisions change

---

## Non-Negotiable Rules

### Architecture
- [ ] Define your architectural decisions here
- [ ] Example: Use microservices architecture
- [ ] Example: Follow clean architecture principles

### Technology Stack
- [ ] Define your technology choices here
- [ ] Example: TypeScript 5.1+ with strict mode
- [ ] Example: React 18.2+ for frontend
- [ ] Example: Node.js 20+ for backend

### Coding Standards
- [ ] Define your coding standards here
- [ ] Example: All code must be type-safe
- [ ] Example: Use async/await, not callbacks
- [ ] Example: Maximum function length: 50 lines

### Security
- [ ] Define your security requirements here
- [ ] Example: All inputs must be validated
- [ ] Example: Use parameterized queries for database
- [ ] Example: HTTPS only in production

### Performance
- [ ] Define your performance requirements here
- [ ] Example: API response time < 200ms
- [ ] Example: Database queries < 50ms
- [ ] Example: Maximum file size: 10MB

---

## Architectural Decisions

### Decision 1: [Decision Name]
**Date:** YYYY-MM-DD  
**Rationale:** Why this decision was made  
**Alternatives Considered:** What other options were evaluated  
**Consequences:** What this decision means for the project

### Decision 2: [Decision Name]
**Date:** YYYY-MM-DD  
**Rationale:** Why this decision was made  
**Alternatives Considered:** What other options were evaluated  
**Consequences:** What this decision means for the project

---

## Constraints

### Infrastructure
- [ ] Define infrastructure constraints here
- [ ] Example: Maximum memory per service: 512MB
- [ ] Example: Maximum CPU per service: 0.5 cores
- [ ] Example: No persistent storage in containers

### External Dependencies
- [ ] Define external dependency constraints here
- [ ] Example: Maximum external API calls: 100/minute
- [ ] Example: No direct database access from frontend
- [ ] Example: All external APIs must have retry logic

### Compliance
- [ ] Define compliance requirements here
- [ ] Example: GDPR compliance required
- [ ] Example: SOC 2 Type II certification
- [ ] Example: HIPAA compliance for health data

---

## Coding Standards

### Language-Specific Rules
- [ ] Define language-specific rules here
- [ ] Example: TypeScript strict mode enabled
- [ ] Example: Python type hints required
- [ ] Example: Go must use gofmt

### Code Organization
- [ ] Define code organization rules here
- [ ] Example: One class per file
- [ ] Example: Maximum file length: 300 lines
- [ ] Example: Use dependency injection

### Testing Requirements
- [ ] Define testing requirements here
- [ ] Example: Minimum 80% code coverage
- [ ] Example: All public APIs must have tests
- [ ] Example: Use TDD for new features

---

## How to Use This File

1. **For AI Agents:**
   - Load this file first for stable context
   - Reference before generating code
   - Never violate constraints listed here

2. **For Developers:**
   - Review before making architectural decisions
   - Update when fundamental changes occur
   - Reference in code reviews

3. **For Project Managers:**
   - Understand project constraints
   - Reference when planning features
   - Use for stakeholder communication

---

## Update Guidelines

**When to Update:**
- Fundamental architectural changes
- New non-negotiable constraints
- Technology stack changes
- Security requirement changes

**When NOT to Update:**
- Temporary decisions
- Feature-specific choices
- Implementation details
- Frequently changing requirements

**Update Process:**
1. Discuss with team
2. Document rationale
3. Update this file
4. Communicate changes
5. Version control commit

---

**Note:** This file should change infrequently. If you find yourself updating it often, consider if those decisions belong in feature specifications instead.
