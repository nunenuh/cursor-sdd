# GitHub Workflow Specification

**Created:** 2025-01-16T12:00:00Z UTC  
**Modified:** 2025-01-16T12:00:00Z UTC

**⚠️ EXAMPLE:** This is an example GitHub workflow. Customize for your project.

GitHub workflow for issue tracking, pull requests, and project management.

---

## Issue Creation

### Issue Types

- **Bug** - Something is broken
- **Feature** - New functionality request
- **Task** - Work item or chore
- **Enhancement** - Improvement to existing feature
- **Documentation** - Documentation updates

### Issue Template

When creating an issue, include:

```markdown
## Description
Clear description of the issue/task

## Acceptance Criteria
- [ ] Criterion 1
- [ ] Criterion 2

## Related
- Related issue: #123
- Related spec: specs/features/[feature].md

## Labels
- `bug` / `feature` / `task`
- `priority: high` / `priority: medium` / `priority: low`
```

---

## Branch Strategy

### Branch Naming

- **Feature:** `feature/[issue-number]-[short-description]`
  - Example: `feature/123-user-authentication`
- **Bugfix:** `bugfix/[issue-number]-[short-description]`
  - Example: `bugfix/456-login-error`
- **Task:** `task/[issue-number]-[short-description]`
  - Example: `task/789-update-docs`

### Branch Workflow

1. Create branch from `main`/`master`
2. Work on branch
3. Create pull request
4. Review and merge

---

## Pull Request Workflow

### PR Requirements

- Link to related issue: `Closes #123`
- Reference spec: `Implements specs/features/[feature].md`
- Include tests
- Update documentation if needed

### PR Template

```markdown
## Description
What does this PR do?

## Related Issue
Closes #123

## Spec Reference
Implements: specs/features/[feature].md

## Changes
- Change 1
- Change 2

## Testing
- [ ] Unit tests added
- [ ] Integration tests added
- [ ] Manual testing completed
```

---

## Labels

### Priority Labels
- `priority: critical` - Blocks production
- `priority: high` - Important, should be done soon
- `priority: medium` - Normal priority
- `priority: low` - Nice to have

### Type Labels
- `bug` - Bug report
- `feature` - Feature request
- `task` - Task or chore
- `documentation` - Documentation
- `enhancement` - Enhancement

### Status Labels
- `in-progress` - Currently being worked on
- `blocked` - Blocked by another issue
- `ready-for-review` - Ready for code review
- `needs-spec` - Needs specification before implementation

---

## Related

- **Feature Specs:** `../features/` - Feature specifications
- **Conventions:** `../conventions/` - Coding conventions
- **Specs Index:** `../index.md` - Master index

---

**Note:** This workflow ensures issues, tasks, and bugs are properly tracked and linked to specifications.

