# P.E.C Model (Problem – Expectation – Constraint)

**Last Updated:** 2025-01-16  
**Category:** Methodologies  
**Source:** AI-Native Spec-Driven Development Research

---

## Overview

The P.E.C model is a lightweight formalism specifically designed for AI-native spec-driven development. It structures specifications into three essential components that AI agents must respect.

**Key Distinction:** This is different from the traditional "Plan, Execute, Check" cycle - P.E.C focuses on **what** to specify, not **how** to execute.

---

## Three Components

### 1. Problem

**What is being solved:**
- What is being solved
- Inputs and their formats
- Failure modes to handle
- Edge cases to consider
- User pain points addressed

**Example:**
```markdown
## Problem
Generate PDF exports over 200 pages without blocking UI
```

---

### 2. Expectation

**What outputs are expected:**
- Expected outputs and formats
- Side effects and state changes
- Performance goals (latency, throughput)
- Success criteria
- User experience outcomes

**Example:**
```markdown
## Expectation
- Async generation
- User notified when ready
- Max latency: 5 minutes
- PDF quality: print-ready
```

---

### 3. Constraint

**Hard limits that must never be violated:**
- Hard limits that must never be violated
- Security requirements
- Cost limitations
- Compatibility requirements
- Legal/regulatory constraints
- Infrastructure limits

**Example:**
```markdown
## Constraints
- Laravel queue system
- Redis driver required
- ECS task memory ≤ 1GB
- No HTTP request > 30s
- Must support concurrent exports
```

---

## Complete Example

```markdown
## Problem
Generate PDF exports over 200 pages without blocking UI

## Expectation
- Async generation
- User notified when ready
- Max latency: 5 minutes
- PDF quality: print-ready

## Constraints
- Laravel queue system
- Redis driver required
- ECS task memory ≤ 1GB
- No HTTP request > 30s
- Must support concurrent exports
```

---

## Key Principle

> AI **must not violate constraints**, even if it finds a "clever" solution.

---

## Benefits

- Clear structure for AI consumption
- Prevents constraint violations
- Explicit failure mode handling
- Performance expectations defined
- Easy to validate compliance

---

## Application to AI Agent Development

### Problem
- Define what the agent should solve
- Specify inputs and failure modes
- Identify edge cases

### Expectation
- Specify agent outputs and behavior
- Define performance goals
- Set success criteria

### Constraint
- Set hard limits (token usage, API calls, timeouts)
- Define security boundaries
- Specify infrastructure limits

---

## Best Practices

### 1. Be Specific
- Avoid vague descriptions
- Use concrete examples
- Define measurable criteria

### 2. Prioritize Constraints
- List critical constraints first
- Make constraints testable
- Document rationale

### 3. Keep It Focused
- One problem per spec
- Clear expectations
- Manageable constraints

### 4. Make It Testable
- Define validation criteria
- Create test cases
- Enable automated checking

---

## Comparison: P.E.C vs PEC (Process)

| Aspect | P.E.C (Structure) | PEC (Process) |
|--------|------------------|---------------|
| **Focus** | What to specify | How to work |
| **Purpose** | Specification structure | Development process |
| **Components** | Problem, Expectation, Constraint | Plan, Execute, Check |
| **Use Case** | Documenting requirements | Managing workflow |

**Note:** The P.E.C model (Problem-Expectation-Constraint) is more relevant for AI-native spec-driven development as it directly structures specifications for AI consumption.

---

## Related Methodologies

- [Specification by Example](./specification-by-example.md) - Using examples in specs
- [Behavior-Driven Development](./behavior-driven-development.md) - BDD with P.E.C
- [Formal Specification](./formal-specification.md) - Formal methods

---

## References

- AI-native spec-driven development practices
- Constraint-based specification patterns
- Problem-solving frameworks

---

**Next:** Explore [Specification by Example](./specification-by-example.md) to see how P.E.C works with examples.

