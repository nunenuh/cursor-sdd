# Spec-Driven Development Research Directory

**Purpose:** Organized research compilation for Spec-Driven Development (SDD) best practices, methodologies, tools, and patterns.

**Last Updated:** 2025-01-16

**Note:** The original comprehensive research file has been archived as `../ARCHIVE-spec-driven-development-best-practices-research.md` for reference. This modular structure is now the primary research repository.

---

## Directory Structure

```
research/
├── README.md                    # This file - overview and index
├── RESEARCH_STATUS.md           # Research progress tracking
├── ARCHIVE_ORIGINAL_FILE.md     # Info about archived original file
├── concepts/                    # Core concepts and principles
│   ├── core-principles.md
│   ├── best-practices.md
│   ├── epistemic-boundaries.md
│   └── artifacts-concept.md
├── methodologies/               # Development methodologies
│   ├── pec-model.md
│   └── [more to be added]
├── tools/                       # Tools and technologies
│   └── [to be added]
├── frameworks/                  # Frameworks and platforms
│   ├── github-spec-kit.md
│   └── amazon-kiro-ide.md
├── patterns/                    # Design patterns and structures
│   ├── ai-agnostic-documentation.md
│   ├── persistent-context.md
│   └── three-document-pattern.md
├── examples/                    # Real-world examples
│   └── github-repositories.md
└── resources/                   # External resources and links
    ├── articles.md
    └── papers.md
```

---

## Quick Navigation

### Core Concepts
- [Core Principles](./concepts/core-principles.md) - Fundamental principles of SDD
- [Best Practices](./concepts/best-practices.md) - Essential best practices
- [Epistemic Boundaries](./concepts/epistemic-boundaries.md) - Specs as knowledge boundaries
- [Artifacts Concept](./concepts/artifacts-concept.md) - Artifact-based development

### Methodologies
- [P.E.C Model](./methodologies/pec-model.md) - Problem-Expectation-Constraint
- [More methodologies to be added]

### Frameworks
- [GitHub Spec-Kit](./frameworks/github-spec-kit.md) ⭐ Primary tool
- [Amazon Kiro IDE](./frameworks/amazon-kiro-ide.md) ⭐ Proprietary IDE

### Patterns
- [AI-Agnostic Documentation](./patterns/ai-agnostic-documentation.md) - Tool-agnostic specs
- [Persistent Context](./patterns/persistent-context.md) - Constitution.md pattern
- [Three-Document Pattern](./patterns/three-document-pattern.md) - Requirements/Design/Tasks

### Examples
- [GitHub Repositories](./examples/github-repositories.md) - Real-world examples

### Resources
- [Articles](./resources/articles.md) - Blog posts and articles
- [Academic Papers](./resources/papers.md) - Research papers

---

## Research Methodology

### Data Collection
- Web searches across multiple sources
- GitHub repository analysis
- Academic paper review
- Tool documentation review
- Industry blog posts and articles

### Source Types
- Academic papers (ArXiv)
- Industry documentation
- Blog posts and articles
- Tool documentation
- Best practice guides
- Case studies
- GitHub repositories

### Coverage Areas
- Core principles and practices
- Methodologies and approaches
- Tools and technologies
- Implementation strategies
- Challenges and solutions
- Real-world examples

---

## Contributing New Research

When adding new research:

1. **Choose the right directory:**
   - Concepts → Core ideas and principles
   - Methodologies → Development approaches
   - Tools → Specific tools and technologies
   - Frameworks → Complete frameworks/platforms
   - Patterns → Reusable patterns and structures
   - Examples → Real-world implementations

2. **File naming:**
   - Use kebab-case: `my-research-topic.md`
   - Be descriptive and specific
   - Update this README with links

3. **File structure:**
   - Start with overview/description
   - Include key points
   - Add examples where relevant
   - Include references and links
   - Add date and source information

4. **Update index:**
   - Add entry to this README
   - Link to the new file
   - Update relevant sections

---

## Key Insights

### For AI Agent Development
- Use persistent context (`constitution.md`, `memory/` directory)
- Structure specs for AI consumption (P.E.C model)
- Keep specs AI-agnostic (Markdown, YAML, JSON)
- Implement artifacts for re-hydratable context

### Core Principles
- Specifications as single source of truth
- Specs as epistemic boundaries
- AI-agnostic documentation
- Continuous validation

### Best Practices
- Human-reviewable specifications
- Minimal and focused specs
- Meaningful decomposition
- Context management

---

## Related Files

- **Archived Original:** `../ARCHIVE-spec-driven-development-best-practices-research.md` - Comprehensive reference (2,242 lines)
- **This Directory:** Organized, modular research files (active)

---

## For AI Agents

**Recommended Usage:**
- Use modular files for **specific topic queries** (faster, focused)
- Use archived original for **comprehensive overview** (complete context)
- Update modular files for **ongoing research** (maintainable)

---

**Note:** This directory structure allows for easy expansion. New research can be added as new files without modifying existing content. Each file is focused on a specific topic, making it easier to maintain and update.
