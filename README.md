# Spec-Driven Development Boilerplate

**Created:** 2025-01-16T12:00:00Z UTC  
**Modified:** 2025-01-16T12:00:00Z UTC

**A ready-to-use boilerplate for Spec-Driven Development (SDD) tailored for AI agents, LLMs, and AI coding assistants.**

---

## 🎯 Purpose

This boilerplate provides a structured foundation for projects that follow **Spec-Driven Development** principles, where specifications serve as the single source of truth before implementation. It's specifically designed to work seamlessly with AI coding assistants like Cursor, GitHub Copilot, Claude Code, and others.

---

## 📁 Directory Structure

```
.
├── specs/                    # All specifications (single source of truth) ⚠️ EXAMPLES
│   ├── README.md            # Specs overview and structure
│   ├── index.md              # Master index of all specs
│   ├── features/             # Feature specifications (P.E.C model)
│   │   ├── example-feature.md          # Complete example
│   │   └── user-management/           # Feature examples
│   ├── api/                 # API contracts and schemas
│   │   ├── openapi.yaml      # OpenAPI 3.0 specification (EXAMPLE)
│   │   └── README.md
│   ├── components/          # Reusable OpenAPI components
│   │   ├── common/          # Common components (pagination, errors, auth)
│   │   └── models/          # Data models
│   ├── contracts/           # API contracts
│   │   └── api-contract.md  # Human-readable contract (EXAMPLE)
│   ├── conventions/         # Coding standards and patterns
│   │   ├── 00-overview.md
│   │   ├── 00-feature-spec-template.md  # P.E.C template
│   │   ├── 01-language-conventions.md
│   │   ├── 02-api-design.md
│   │   ├── 03-database-patterns.md
│   │   ├── 04-testing-standards.md
│   │   ├── 05-security-guidelines.md
│   │   ├── 06-deployment-rules.md
│   │   └── 07-documentation-standards.md
│   ├── examples/            # Code and API examples
│   │   ├── typescript/      # TypeScript implementation examples
│   │   ├── python/          # Python implementation examples
│   │   ├── requests/        # Request examples (JSON)
│   │   └── responses/       # Response examples (JSON)
│   ├── schemas/             # Data schemas
│   │   └── database-schema.md
│   ├── security/            # Security specifications
│   ├── tests/               # Test specifications
│   ├── validation/          # Validation rules
│   ├── versions/            # API versioning
│   ├── workflows/           # Process workflows
│   └── integrations/       # Integration specifications
├── docs/                    # Human-readable documentation (for humans and AI)
│   ├── api/                 # API documentation
│   ├── architecture/        # System architecture
│   ├── decisions/           # Architectural Decision Records (ADRs)
│   ├── deployment/          # Deployment guides
│   ├── implementation/      # Implementation guides
│   ├── planning/            # Planning documents
│   ├── quick-start/         # Getting started guides
│   ├── testing/            # Testing guides
│   └── guides/              # General guides
├── specs/                    # All specifications (single source of truth) ⚠️ EXAMPLES
│   ├── memory/              # Persistent context files
│   │   └── constitution.md # Non-negotiable project rules
├── .cursor/                 # Cursor-specific planning
│   └── planning.md          # Planning and context document
├── .cursorrules             # Cursor AI assistant rules
├── .cursorignore            # Files to ignore in Cursor
└── research/                # Research and best practices (reference)

```

---

## 🚀 Quick Start

### 1. Understand the Structure

- **`specs/`** - Write specifications here before coding
- **`docs/`** - Human-readable documentation (architecture, guides, ADRs)
- **`specs/memory/constitution.md`** - Define stable project rules
- **`.cursorrules`** - Configure AI assistant behavior
- **`specs/conventions/`** - Coding standards and templates

### 2. Set Up Your Project

1. **Update Constitution:**
   ```bash
   # Edit specs/memory/constitution.md
   # Define your non-negotiable rules, architecture, constraints
   ```

2. **Create Your First Feature Spec:**
   ```bash
   # Copy the template
   cp specs/conventions/00-feature-spec-template.md specs/features/my-feature.md
   # Fill in Problem, Expectation, Constraint sections
   ```

3. **Configure Cursor Rules:**
   ```bash
   # Edit .cursorrules
   # Customize for your project's needs
   ```

### 3. Start Developing

1. Write specification in `specs/features/[feature-name].md`
2. Get stakeholder approval
3. AI assistant reads spec and generates code
4. Write tests from acceptance criteria
5. Validate implementation matches spec

---

## 📋 Core Concepts

### P.E.C Model

All feature specifications follow the **P.E.C model**:

- **Problem** - What is being solved?
- **Expectation** - What outputs are expected?
- **Constraint** - Hard limits that must never be violated

See `specs/conventions/00-feature-spec-template.md` for the template.

### Constitution Pattern

The `specs/memory/constitution.md` file provides **persistent context** for AI agents:

- Stable, non-negotiable rules
- Architectural decisions
- Technology constraints
- Security requirements

This prevents context drift across development sessions.

### AI-Agnostic Documentation

All specifications use standard formats:
- ✅ Markdown (`.md`)
- ✅ YAML (`.yaml`)
- ✅ JSON Schema (`.json`)
- ✅ Mermaid diagrams (`.mmd`)

This ensures compatibility with any AI coding assistant.

---

## 📖 Usage Guide

### Creating a Feature Specification

1. **Copy the template:**
   ```bash
   cp specs/conventions/00-feature-spec-template.md specs/features/my-feature.md
   ```

2. **Fill in the P.E.C sections:**
   - **Problem:** What problem does this solve?
   - **Expectation:** What should it do?
   - **Constraint:** What are the hard limits?

3. **Add acceptance criteria:**
   - Testable conditions
   - Success metrics
   - Performance goals

4. **Define technical design:**
   - Components
   - API endpoints
   - Data models

5. **Get approval before implementation**

### Working with AI Assistants

**Before coding:**
- AI reads `specs/memory/constitution.md` for stable context
- AI reads feature spec from `specs/features/`
- AI checks conventions in `specs/conventions/`

**During coding:**
- AI follows specifications exactly
- AI respects constraints from constitution
- AI uses conventions for code style

**After coding:**
- Validate code matches specification
- Write tests from acceptance criteria
- Update spec if requirements change

---

## 🎨 Examples

### Feature Specification Example
See `specs/features/example-feature.md` for a complete example of a feature specification following the P.E.C model.

### Code Examples
This boilerplate includes implementation examples in multiple languages:

**TypeScript Examples:**
- `specs/examples/typescript/auth-login-service.ts` - Service implementation
- `specs/examples/typescript/auth-controller.ts` - API controller
- `specs/examples/typescript/user-model.ts` - Data model

**Python Examples:**
- `specs/examples/python/auth_login_service.py` - Service implementation
- `specs/examples/python/auth_controller.py` - FastAPI controller
- `specs/examples/python/user_model.py` - SQLAlchemy/Pydantic model

**API Examples:**
- `specs/examples/requests/` - Request examples (JSON)
- `specs/examples/responses/` - Response examples (JSON)

---

## 🔧 Configuration Files

### `.cursorrules`

Defines how Cursor AI assistant should behave:
- Specification-first approach
- Context loading order
- Code generation rules
- Constraint enforcement

### `.cursorignore`

Files and directories to ignore in Cursor context:
- Dependencies (`node_modules/`, `vendor/`)
- Build outputs (`dist/`, `build/`)
- Logs and temporary files

### `specs/memory/constitution.md`

Stable project rules:
- Architecture decisions
- Technology stack
- Coding standards
- Security requirements
- Performance constraints

---

## 📚 Research & Best Practices

The `research/` directory contains comprehensive research on:
- Core principles and best practices
- Methodologies (P.E.C model, BDD, TDD)
- Frameworks (GitHub Spec-Kit, Amazon Kiro IDE)
- Patterns (Constitution, AI-Agnostic Documentation)
- Real-world examples

**Reference:** `research/README.md` for navigation.

---

## 🎯 Key Principles

1. **Specification-First:** Define specs before coding
2. **Single Source of Truth:** Specs are authoritative
3. **AI-Agnostic:** Use standard formats
4. **Persistent Context:** Constitution prevents context drift
5. **Human-Reviewable:** Keep specs concise and clear

---

## 📝 Next Steps

1. **Customize Constitution:**
   - Edit `specs/memory/constitution.md`
   - Define your project's rules

2. **Create Your First Spec:**
   - Use `specs/conventions/00-feature-spec-template.md`
   - Follow the P.E.C model

3. **Configure Cursor:**
   - Review `.cursorrules`
   - Adjust for your needs

4. **Start Developing:**
   - Write specs first
   - Let AI assistants read and implement
   - Validate against specs

---

## 🔗 Resources

- **Research:** `research/` directory - Best practices and methodologies
- **Specs Index:** `specs/index.md` - Master index of all specifications
- **Templates:** `specs/conventions/00-feature-spec-template.md` - Feature template
- **Feature Examples:** `specs/features/example-feature.md` - Complete P.E.C example
- **Code Examples:** `specs/examples/` - TypeScript and Python examples
- **API Examples:** `specs/examples/requests/` and `specs/examples/responses/`
- **Constitution:** `specs/memory/constitution.md` - Project rules

---

## ⚠️ Important: All Specs Are Examples

**All specifications in this boilerplate are examples/templates!**

- ⚠️ Replace example features with your actual features
- ⚠️ Update API spec with your actual endpoints
- ⚠️ Customize conventions for your language/stack
- ⚠️ Add your own code examples
- ⚠️ Update schemas with your data model

## 🤝 Customization Guide

This is a boilerplate template. Customize it for your project:

1. **Update Constitution:**
   - Edit `memory/constitution.md` with your rules
   - Define architecture, tech stack, constraints

2. **Configure Cursor:**
   - Modify `.cursorrules` for your workflow
   - Adjust AI assistant behavior

3. **Customize Conventions:**
   - Update `specs/conventions/01-language-conventions.md` for your language
   - Adjust other convention files as needed

4. **Replace Examples:**
   - Replace `specs/features/example-feature.md` with your features
   - Update `specs/api/openapi.yaml` with your API
   - Add your own code examples in `specs/examples/`

5. **Create Your Specs:**
   - Use `specs/conventions/00-feature-spec-template.md`
   - Follow the P.E.C model
   - Reference code examples when implementing

6. **Build Your Project:**
   - Write specs first
   - Let AI assistants implement
   - Validate against specs

---

## 📄 License

This boilerplate is provided as-is for use in your projects.

---

**Happy Spec-Driven Development! 🚀**
