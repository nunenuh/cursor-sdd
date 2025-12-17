# Amazon Kiro IDE

**Last Updated:** 2025-01-16  
**Category:** Frameworks  
**Website:** https://kiroide.net | https://kiro.mom  
**Type:** Proprietary Agentic IDE  
**Developer:** Amazon Web Services

---

## Overview

Kiro is Amazon's agentic Integrated Development Environment (IDE) that guides developers from prototype to production using structured, spec-driven development. It transforms vague requirements into AI-executable plans through structured processes.

**Key Philosophy:** Three-document pattern (Requirements → Design → Tasks)

---

## Core Features

### 1. Three-Document Pattern

**The Pattern:**
```
Requirements → Design → Tasks → Implementation
```

#### `requirements.md`
- User stories
- Acceptance criteria
- Functional requirements
- Business rules

#### `design.md`
- Technical architecture
- Components and interactions
- Data models
- API endpoints
- Database schemas

#### `tasks.md`
- Actionable coding tasks
- Ordered by dependencies
- Linked to requirements
- Implementation steps

**Key Benefit:**
- Clear progression from requirements to code
- Traceability from tasks back to requirements
- Structured workflow

---

### 2. Agent Hooks

**What are Agent Hooks?**

Background AI agents triggered by specific actions (commits, saves) to automate tasks.

**Capabilities:**
- Auto-generate documentation
- Analyze test coverage
- Suggest code refactoring
- Context-aware automation
- Quality checks

**Examples:**
- On commit → Generate documentation
- On save → Analyze code quality
- On push → Run test coverage analysis

**Benefits:**
- Automated maintenance
- Continuous quality checks
- Reduced manual work
- Context-aware assistance

---

### 3. MCP Integration

**Model Context Protocol (MCP):**
- Integration with external models
- API and document integration
- Enhanced development workflow
- Extensible architecture

**Use Cases:**
- Connect to external APIs
- Integrate with documentation
- Link to knowledge bases
- Extend functionality

---

### 4. AWS Integration

**Deep AWS Integration:**
- Lambda functions
- EC2 instances
- S3 storage
- Other AWS services

**Benefits:**
- Seamless deployment
- AWS ecosystem compatibility
- Integrated tooling
- Native AWS workflows

---

### 5. Steering Rules

**Purpose:**
- Behavior guidelines
- Consistency enforcement
- Quality standards
- Project-specific rules

**Usage:**
- Define coding standards
- Set quality thresholds
- Enforce best practices
- Maintain consistency

---

## Workflow

### Standard Process

1. **Requirements Phase**
   - Generate `requirements.md` from high-level prompts
   - User stories and acceptance criteria
   - Explicit assumptions
   - Minimize ambiguity

2. **Design Phase**
   - Create `design.md` based on approved requirements
   - Technical architecture
   - Data flow diagrams
   - API endpoints
   - Database schemas

3. **Tasks Phase**
   - Generate `tasks.md` from design
   - Sequence tasks by dependencies
   - Link tasks to requirements
   - Actionable coding steps

4. **Implementation Phase**
   - Execute tasks
   - Generate code
   - Run tests
   - Deploy

5. **Living Documentation**
   - Specs remain synchronized with codebase
   - Up-to-date documentation
   - Maintained automatically

---

## Best Practices

### 1. Use Three-Document Pattern Consistently
- Always create requirements first
- Design follows requirements
- Tasks follow design
- Maintain traceability

### 2. Keep Requirements Focused
- One feature per requirements doc
- Clear acceptance criteria
- Testable requirements
- Explicit assumptions

### 3. Link Tasks to Requirements
- Maintain traceability
- Show requirement coverage
- Enable impact analysis
- Support change management

### 4. Leverage Agent Hooks
- Configure hooks for common tasks
- Automate documentation
- Enable quality checks
- Reduce manual work

### 5. Maintain Living Documentation
- Keep specs synchronized
- Update when code changes
- Review regularly
- Ensure accuracy

---

## Comparison with Spec-Kit

| Feature | Kiro IDE | Spec-Kit |
|---------|----------|----------|
| Type | Proprietary | Open-source |
| Approach | GUI-based | CLI-driven |
| Pattern | Three-document | Constitution + Specs |
| Agent Hooks | ✅ Yes | ❌ No |
| AWS Integration | ✅ Deep | ❌ No |
| MCP Support | ✅ Yes | ❌ Not mentioned |
| CLI Commands | ❌ No | ✅ Yes |
| Templates | ❌ Not mentioned | ✅ Yes |

---

## Key Advantages

1. **Integrated IDE:** Complete development environment
2. **Agent Hooks:** Automated background agents
3. **AWS Integration:** Native AWS workflows
4. **Three-Document Pattern:** Clear structure
5. **Living Documentation:** Auto-synchronized

---

## Key Disadvantages

1. **Proprietary:** Vendor lock-in
2. **AWS-Specific:** Best for AWS projects
3. **No CLI:** GUI-only workflow
4. **Cost:** May require AWS subscription

---

## Use Cases

### Best For:
- AWS-based applications
- Teams preferring GUI workflows
- Projects needing agent hooks
- AWS ecosystem integration

### Not Ideal For:
- Non-AWS projects
- CLI-preferred workflows
- Open-source projects
- Multi-cloud deployments

---

## Resources

- **Official Website:** https://kiroide.net
- **Getting Started:** https://kiro.directory/blog/getting-started-kiro-spec-driven/
- **Tutorials:** TutorialsDojo Amazon Kiro Guide
- **Documentation:** Included in IDE

---

## Related Frameworks

- [GitHub Spec-Kit](./github-spec-kit.md) - Open-source alternative
- [SuperSpec](./superspec.md) - Declarative agent specs
- [Three-Document Pattern](../patterns/three-document-pattern.md) - Pattern details

---

**Next:** Explore [Three-Document Pattern](../patterns/three-document-pattern.md) for implementation details.

