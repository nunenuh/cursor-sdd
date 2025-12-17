# Three-Document Pattern (Requirements/Design/Tasks)

**Last Updated:** 2025-01-16  
**Category:** Patterns  
**Source:** Amazon Kiro IDE, Spec-Driven Development Research

---

## Overview

The Three-Document Pattern structures feature development into three sequential documents: Requirements, Design, and Tasks. This pattern provides clear traceability from requirements to implementation.

**Pattern:**
```
Requirements → Design → Tasks → Implementation
```

---

## The Three Documents

### 1. Requirements.md

**Purpose:** Capture what needs to be built

**Contents:**
- User stories
- Acceptance criteria
- Functional requirements
- Business rules
- Success criteria

**Key Points:**
- Written from user perspective
- Testable requirements
- Clear acceptance criteria
- Explicit assumptions

**Example Structure:**
```markdown
# Feature: User Authentication

## User Stories
- As a user, I want to login...
- As a user, I want to logout...

## Acceptance Criteria
- User can login with email/password
- User receives JWT token
- Token expires after 24 hours

## Requirements
- Functional: Login, logout, token refresh
- Non-functional: Response time < 200ms
```

---

### 2. Design.md

**Purpose:** Define how to build it

**Contents:**
- Technical architecture
- Components and interactions
- Data models
- API endpoints
- Database schemas
- Data flow diagrams

**Key Points:**
- Based on approved requirements
- Technical decisions documented
- Architecture defined
- Integration points specified

**Example Structure:**
```markdown
# Design: User Authentication

## Architecture
- REST API endpoint
- JWT token generation
- Session management

## Components
- AuthController
- AuthService
- TokenService
- UserRepository

## Data Models
- User entity
- Session entity
- Token entity

## API Endpoints
- POST /auth/login
- POST /auth/logout
- POST /auth/refresh
```

---

### 3. Tasks.md

**Purpose:** Break down into actionable steps

**Contents:**
- Actionable coding tasks
- Ordered by dependencies
- Linked to requirements
- Implementation steps
- File paths

**Key Points:**
- Specific and actionable
- Ordered correctly
- Dependencies clear
- Traceable to requirements

**Example Structure:**
```markdown
# Tasks: User Authentication

## Phase 1: Data Models
- [ ] Create User entity
- [ ] Create Session entity
- [ ] Create migrations

## Phase 2: Services
- [ ] Implement AuthService
- [ ] Implement TokenService
- [ ] Write tests

## Phase 3: API
- [ ] Create AuthController
- [ ] Implement login endpoint
- [ ] Implement logout endpoint
```

---

## Workflow

### Step 1: Requirements

**Input:** High-level feature request

**Process:**
- Generate from prompts
- Refine with stakeholders
- Define acceptance criteria
- Document assumptions

**Output:** `requirements.md`

---

### Step 2: Design

**Input:** Approved requirements + existing codebase

**Process:**
- Analyze requirements
- Design architecture
- Define components
- Specify integrations

**Output:** `design.md`

---

### Step 3: Tasks

**Input:** Design document

**Process:**
- Break down design
- Order by dependencies
- Link to requirements
- Specify file paths

**Output:** `tasks.md`

---

### Step 4: Implementation

**Input:** Tasks document

**Process:**
- Execute tasks in order
- Follow dependencies
- Reference requirements
- Validate against design

**Output:** Working code

---

## Benefits

### Traceability
- Requirements → Design → Tasks → Code
- Clear links between documents
- Easy impact analysis
- Change management

### Clarity
- Clear progression
- Explicit decisions
- Documented rationale
- Shared understanding

### Quality
- Requirements validated before design
- Design validated before tasks
- Tasks validated before code
- Early issue detection

---

## Best Practices

### 1. Maintain Links

**Do:**
- Link tasks to requirements
- Reference design decisions
- Maintain traceability
- Update links when changes occur

**Don't:**
- Create orphaned documents
- Lose traceability
- Ignore dependencies
- Skip updates

### 2. Keep Documents Focused

**Do:**
- One feature per set of documents
- Clear separation of concerns
- Focused content
- Manageable size

**Don't:**
- Mix multiple features
- Over-complicate
- Include unnecessary detail
- Create huge documents

### 3. Update Together

**Do:**
- Update all three when requirements change
- Maintain consistency
- Keep traceability
- Document changes

**Don't:**
- Update only one document
- Create inconsistencies
- Lose synchronization
- Skip documentation

---

## Comparison with Other Patterns

### Spec-Kit Pattern

| Aspect | Three-Document | Spec-Kit |
|--------|---------------|----------|
| Documents | Requirements/Design/Tasks | Spec/Plan/Tasks |
| Focus | Feature-level | Feature-level |
| Structure | Three sequential docs | Spec + Plan + Tasks |
| Tool | Kiro IDE | Spec-Kit CLI |

**Key Difference:**
- Three-Document: Requirements → Design → Tasks
- Spec-Kit: Spec → Plan → Tasks

Both serve similar purposes but with different structures.

---

## Example: Complete Flow

### Requirements.md
```markdown
# User Authentication

## User Story
As a user, I want to login to access the system.

## Acceptance Criteria
- User can login with email/password
- User receives JWT token
- Token valid for 24 hours

## Requirements
- POST /auth/login endpoint
- JWT token generation
- Password hashing (bcrypt)
```

### Design.md
```markdown
# Design: User Authentication

## Architecture
- REST API with Express.js
- JWT for authentication
- PostgreSQL for user storage

## Components
- AuthController: HTTP handlers
- AuthService: Business logic
- TokenService: JWT operations
- UserRepository: Data access

## API Design
POST /auth/login
Request: { email, password }
Response: { token, user }
```

### Tasks.md
```markdown
# Tasks: User Authentication

## Phase 1: Models
- [ ] Create User model
- [ ] Create migration
- [ ] Write model tests

## Phase 2: Services
- [ ] Implement AuthService.login()
- [ ] Implement TokenService.generate()
- [ ] Write service tests

## Phase 3: API
- [ ] Create AuthController
- [ ] Implement POST /auth/login
- [ ] Write API tests
```

---

## Related Patterns

- [Persistent Context](./persistent-context.md) - Constitution.md pattern
- [AI-Agnostic Documentation](./ai-agnostic-documentation.md) - Tool-agnostic specs
- [Directory Structures](./directory-structures.md) - Common structures

---

## References

- Amazon Kiro IDE: Three-document pattern
- Spec-Driven Development best practices
- Requirements engineering practices

---

**Next:** Explore [Directory Structures](./directory-structures.md) for implementation guidance.

