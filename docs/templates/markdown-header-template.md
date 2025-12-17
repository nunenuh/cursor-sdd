# [Document Title]

**Created:** YYYY-MM-DDTHH:MM:SSZ UTC  
**Modified:** YYYY-MM-DDTHH:MM:SSZ UTC

[Document content starts here...]

---

## Usage

When creating a new markdown file, include this header format:

```markdown
# Document Title

**Created:** YYYY-MM-DDTHH:MM:SSZ UTC  
**Modified:** YYYY-MM-DDTHH:MM:SSZ UTC
```

### Format Details

- **Created:** UTC datetime when document was first created
- **Modified:** UTC datetime when document was last modified
- **Format:** ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`
- **Timezone:** Always UTC (Z suffix)

### Examples

```markdown
**Created:** 2025-01-16T12:00:00Z UTC  
**Modified:** 2025-01-16T14:30:00Z UTC
```

### Updating Modified Date

When updating a document, update the **Modified** date to the current UTC time.

---

**Note:** This header format ensures all documentation has clear creation and modification timestamps for both humans and AI agents.
