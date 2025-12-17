#!/bin/bash
# Script to add datetime headers to markdown files

# Get current UTC datetime
CURRENT_UTC=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# Find all markdown files except in research and archive
find . -type f -name "*.md" \
  -not -path "./.git/*" \
  -not -path "./node_modules/*" \
  -not -path "./research/*" \
  -not -path "./ARCHIVE-*" \
  -not -path "./.notebook/*" | while read -r file; do
  
  # Check if file already has Created date
  if ! grep -q "^Created:" "$file"; then
    # Add header after first line (title)
    sed -i "1a\\
\\
**Created:** ${CURRENT_UTC} UTC\\
**Modified:** ${CURRENT_UTC} UTC\\
" "$file"
  fi
done

echo "Datetime headers added to markdown files"

