# GitHub Spec-Kit Framework

**Last Updated:** 2025-01-16  
**Category:** Frameworks  
**Repository:** https://github.com/github/spec-kit  
**Stars:** 55.9k+ | **Forks:** 4.9k+  
**License:** MIT

---

## Overview

GitHub's Spec-Kit is a comprehensive toolkit designed to facilitate spec-driven development with AI coding assistants. It emphasizes intent-driven development, rich specification creation, and multi-step refinement processes.

**Key Philosophy:** Define "what" before "how"

---

## Core Features

### 1. Constitution.md Pattern

**Location:** `memory/constitution.md`

**Purpose:**
- Persistent context file
- Defines stable, non-negotiable rules and constraints
- Acts as architectural guardrails for AI agents
- Prevents context drift across development sessions

**Structure:**
```markdown
# Project Constitution

## Non-Negotiable Rules
- Rule 1
- Rule 2

## Architectural Decisions
- Decision 1
- Decision 2

## Constraints
- Constraint 1
- Constraint 2
```

**Best Practices:**
- Keep it stable (don't change frequently)
- Focus on non-negotiable rules
- Include architectural decisions
- Document constraints clearly

---

### 2. Directory Structure

**Standard Layout:**
```
.
├── memory/
│   └── constitution.md      # Persistent context
├── specs/
│   └── 001-feature-name/
│       ├── spec.md          # Feature specification
│       ├── plan.md          # Implementation plan
│       ├── tasks.md          # Task breakdown
│       ├── contracts/       # API contracts
│       └── data-model.md    # Data models
├── templates/               # Reusable templates
└── scripts/                 # Automation scripts
```

**Key Directories:**
- `memory/` - Persistent context files
- `specs/` - Feature specifications (numbered)
- `templates/` - Reusable templates
- `scripts/` - Automation scripts

---

### 3. CLI Commands

**Available Commands:**

#### `/speckit.plan`
Generate implementation plan from spec

**Usage:**
```
/speckit.plan

We are going to generate this using .NET Aspire, using Postgres as the database...
```

**Output:**
- Creates `plan.md` in feature directory
- Includes implementation details
- References tech stack decisions

#### `/speckit.tasks`
Break down plan into actionable tasks

**Usage:**
```
/speckit.tasks
```

**Output:**
- Creates `tasks.md` file
- Organized by user story
- Includes dependencies
- Marks parallel tasks with `[P]`
- Includes file paths

#### `/speckit.implement`
Execute implementation tasks

**Usage:**
```
/speckit.implement
```

**Process:**
- Validates prerequisites (constitution, spec, plan, tasks)
- Parses task breakdown
- Executes tasks in order
- Respects dependencies
- Handles parallel execution
- Provides progress updates

#### `/speckit.research`
Research technical details

**Usage:**
```
/speckit.research

Research .NET Aspire version compatibility...
```

---

### 4. Workflow

**Step-by-Step Process:**

1. **Create Constitution**
   ```bash
   # Create memory/constitution.md
   # Define project rules and constraints
   ```

2. **Write Specification**
   ```bash
   # Create specs/001-feature-name/spec.md
   # Define feature requirements
   ```

3. **Generate Plan**
   ```bash
   /speckit.plan
   # Creates plan.md with implementation details
   ```

4. **Create Tasks**
   ```bash
   /speckit.tasks
   # Creates tasks.md with task breakdown
   ```

5. **Implement**
   ```bash
   /speckit.implement
   # Executes tasks in order
   ```

---

### 5. Templates

**Available Templates:**

- `CLAUDE-template.md` - Claude-specific prompts
- `spec-template.md` - Specification template
- `plan-template.md` - Implementation plan template
- `tasks-template.md` - Task breakdown template

**Usage:**
- Copy templates to feature directory
- Customize for specific feature
- Maintain consistency across features

---

### 6. AI Assistant Integration

**Supported Assistants:**
- GitHub Copilot
- Claude Code
- Gemini CLI
- Agent-agnostic design

**Integration:**
- Works with any AI coding assistant
- Uses standard file formats
- No vendor lock-in
- Flexible workflow

---

## Best Practices

### 1. Start with Constitution
- Create `memory/constitution.md` first
- Define stable rules
- Document architectural decisions
- Set constraints

### 2. Use Structured Directory Layout
- Number features: `001-feature-name`
- Keep specs organized
- Use consistent naming
- Maintain clear structure

### 3. Validate Before Implementation
- Review spec before planning
- Validate plan before tasks
- Check tasks before implementation
- Ensure prerequisites are met

### 4. Keep Specs Focused
- One feature per spec directory
- Clear and concise
- Human-reviewable
- AI-consumable

### 5. Version Control Everything
- Track all specs in Git
- Version constitution changes
- Maintain history
- Enable rollback

---

## Example Workflow

### Step 1: Create Constitution
```markdown
# memory/constitution.md

## Project Rules
- Use TypeScript strict mode
- Follow clean architecture
- Write tests for all business logic

## Constraints
- No external API calls in business logic
- All errors must be typed
- Use dependency injection
```

### Step 2: Write Spec
```markdown
# specs/001-user-authentication/spec.md

## Problem
Users need to authenticate to access the system

## Expectation
- Login endpoint
- JWT token generation
- Session management

## Constraints
- Use existing auth library
- Tokens expire in 24 hours
- Support refresh tokens
```

### Step 3: Generate Plan
```
/speckit.plan
```

### Step 4: Create Tasks
```
/speckit.tasks
```

### Step 5: Implement
```
/speckit.implement
```

---

## Comparison with Other Tools

| Feature | Spec-Kit | Kiro IDE |
|---------|----------|----------|
| Type | Open-source | Proprietary |
| CLI Commands | ✅ Yes | ❌ No |
| Constitution Pattern | ✅ Yes | ❌ Not explicit |
| Templates | ✅ Yes | ❌ Not mentioned |
| Agent-Agnostic | ✅ Yes | ❌ Integrated |

---

## Key Advantages

1. **Open-Source:** Free to use, modify, and extend
2. **Agent-Agnostic:** Works with any AI assistant
3. **CLI-Driven:** Scriptable and automatable
4. **Constitution Pattern:** Persistent context management
5. **Structured Workflow:** Clear process from spec to code

---

## Resources

- **Repository:** https://github.com/github/spec-kit
- **Documentation:** Included in repository
- **Templates:** Available in `templates/` directory
- **Scripts:** Automation scripts in `scripts/` directory

---

## Related Frameworks

- [Amazon Kiro IDE](./amazon-kiro-ide.md) - Proprietary alternative
- [SuperSpec](./superspec.md) - Declarative agent specs
- [AgentSpec](./agentspec.md) - Runtime constraints

---

**Next:** Compare with [Amazon Kiro IDE](./amazon-kiro-ide.md) to understand differences.

