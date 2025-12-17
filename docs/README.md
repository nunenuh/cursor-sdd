# Documentation Directory

**Created:** 2025-12-17T04:58:48Z UTC
**Modified:** 2025-12-17T04:58:48Z UTC


**Purpose:** Human-readable documentation that complements the `specs/` directory  
**Audience:** Both humans and AI agents  
**Format:** Markdown (AI-agnostic, human-friendly)

---

## Overview

The `docs/` directory contains narrative, explanatory documentation that works alongside the structured specifications in `specs/`. While `specs/` focuses on formal specifications (P.E.C model, API contracts), `docs/` provides:

- **Architecture explanations** - How the system works
- **Implementation guides** - How to build features
- **Decision records** - Why decisions were made
- **Quick start guides** - Getting started tutorials
- **API documentation** - Human-readable API docs

---

## Directory Structure

```
docs/
├── README.md              # This file
├── api/                   # API documentation
├── architecture/          # System architecture
├── archive/               # Archived documentation
├── current/               # Current active documentation
├── decisions/             # Architectural Decision Records (ADRs)
├── deployment/            # Deployment guides
├── development/           # Development environment and workflows
├── feedback/              # User and stakeholder feedback
├── guides/                # General guides
├── implementation/        # Implementation guides
├── infra/                 # Infrastructure documentation
├── issues/                # Known issues and bug tracking
├── meetings/              # Meeting notes and decisions
├── planning/              # Planning documents
├── product/               # Product documentation
├── projects/              # Project-specific documentation
├── quick-start/           # Getting started guides
├── requirements/          # Business and functional requirements
├── roadmaps/              # Product and project roadmaps
├── templates/             # Documentation templates
├── testing/               # Testing guides
└── troubleshooting/       # Troubleshooting guides
```

---

## Relationship with `specs/` Directory

### `specs/` - Structured Specifications
- **Purpose:** Formal, structured specifications
- **Format:** P.E.C model, OpenAPI, JSON Schema
- **Focus:** What to build, constraints, contracts
- **AI Consumption:** Primary source for AI agents

### `docs/` - Narrative Documentation
- **Purpose:** Explanatory, narrative documentation
- **Format:** Markdown with examples
- **Focus:** How things work, why decisions were made
- **AI Consumption:** Context and explanations

**Both are readable by AI and humans!**

---

## Subdirectories

### `api/`
API documentation, endpoints, authentication, examples

### `architecture/`
System design, component interactions, data flow, diagrams

### `archive/`
Archived documentation and deprecated content

### `current/`
Current, actively maintained documentation

### `decisions/`
Architectural Decision Records (ADRs), rationale, alternatives

### `deployment/`
Deployment guides, infrastructure, CI/CD, environments

### `development/`
Development environment setup and workflows

### `feedback/`
User feedback, reviews, and improvement suggestions

### `guides/`
General guides, how-tos, troubleshooting

### `implementation/`
How to implement features, code examples, best practices

### `infra/`
Infrastructure setup, configuration, and management

### `issues/`
Known issues, bug tracking, and problem documentation

### `meetings/`
Meeting notes, decisions, and action items

### `planning/`
Project planning, roadmaps, milestones, next steps

### `product/`
Product requirements, features, and product-related documentation

### `projects/`
Project-specific documentation and sub-projects

### `quick-start/`
Getting started guides, setup instructions, tutorials

### `requirements/`
Business and functional requirements

### `roadmaps/`
Product and project roadmaps

### `templates/`
Reusable templates for documentation

### `testing/`
Testing strategies, test guides, examples

### `troubleshooting/`
Common problems and their solutions

---

## Writing Guidelines

### For Humans
- Clear, narrative explanations
- Examples and code snippets
- Diagrams where helpful
- Step-by-step instructions

### For AI Agents
- Use standard Markdown
- Clear headings and structure
- Include code examples
- Reference related specs

### Best Practices
- ✅ Use Markdown format
- ✅ Include code examples
- ✅ Link to related specs
- ✅ Keep it concise
- ✅ Update regularly
- ❌ Don't duplicate specs
- ❌ Don't use tool-specific formats

---

## Index

See individual subdirectories for specific documentation:

- [API Documentation](./api/) - API endpoints and examples
- [Architecture](./architecture/) - System design and structure
- [Archive](./archive/) - Archived documentation
- [Current](./current/) - Current active documentation
- [Decisions](./decisions/) - Architectural Decision Records
- [Deployment](./deployment/) - Deployment guides
- [Development](./development/) - Development environment and workflows
- [Feedback](./feedback/) - User and stakeholder feedback
- [Guides](./guides/) - General guides
- [Implementation](./implementation/) - Implementation guides
- [Infrastructure](./infra/) - Infrastructure documentation
- [Issues](./issues/) - Known issues and bug tracking
- [Meetings](./meetings/) - Meeting notes and decisions
- [Planning](./planning/) - Project planning
- [Product](./product/) - Product documentation
- [Projects](./projects/) - Project-specific documentation
- [Quick Start](./quick-start/) - Getting started
- [Requirements](./requirements/) - Business and functional requirements
- [Roadmaps](./roadmaps/) - Product and project roadmaps
- [Templates](./templates/) - Documentation templates
- [Testing](./testing/) - Testing guides
- [Troubleshooting](./troubleshooting/) - Troubleshooting guides

---

## Related Files

- **Specifications:** `../specs/` directory
- **Constitution:** `../specs/memory/constitution.md`
- **Research:** `../research/` directory

---

**Note:** This directory complements `specs/` but doesn't replace it. Both are important for complete project understanding.
