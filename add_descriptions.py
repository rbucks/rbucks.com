#!/usr/bin/env python3
"""
Add Description frontmatter to all blog posts missing it.

For each .md file in /content/ that lacks a Description: field, this script
generates one from the first substantive paragraph of the post content,
stripping markdown formatting and truncating to a reasonable length.

Usage:
    python3 add_descriptions.py [--dry-run]

Options:
    --dry-run    Preview changes without modifying files
"""

import os
import re
import sys

CONTENT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'content')
MAX_DESC_LENGTH = 160  # Aim for ~155 chars, similar to meta descriptions


def parse_frontmatter_and_body(text):
    """Split markdown text into (frontmatter_lines, body_text)."""
    lines = text.split('\n')
    frontmatter = []
    body_start = 0

    # Frontmatter is at the top: Key: Value lines before first blank line
    for i, line in enumerate(lines):
        if re.match(r'^[A-Za-z_-]+:', line):
            frontmatter.append(line)
        elif line.strip() == '' and i > 0 and frontmatter:
            # Blank line after frontmatter
            body_start = i + 1
            break
        else:
            # Non-frontmatter content at start (unlikely but handle)
            body_start = i
            break

    body = '\n'.join(lines[body_start:])
    return frontmatter, body


def frontmatter_to_dict(frontmatter_lines):
    """Convert frontmatter lines to a dict."""
    meta = {}
    for line in frontmatter_lines:
        match = re.match(r'^([A-Za-z_-]+):\s*(.*)', line)
        if match:
            key = match.group(1).strip()
            value = match.group(2).strip()
            meta[key] = value
    return meta


def has_description(frontmatter_lines):
    """Check if Description field exists in frontmatter."""
    for line in frontmatter_lines:
        if line.startswith('Description:'):
            return True
    return False


def generate_description(body_text):
    """Generate a description from the first substantive paragraph of body text."""
    # Split into paragraphs (separated by blank lines)
    paragraphs = re.split(r'\n\s*\n', body_text.strip())

    for para in paragraphs:
        # Strip markdown formatting
        cleaned = para.strip()
        
        # Remove image tags: ![alt](url) or ![](url)
        cleaned = re.sub(r'!\[.*?\]\(.*?\)', '', cleaned)
        
        # Remove inline links but keep text: [text](url) -> text
        cleaned = re.sub(r'\[([^\]]*?)\]\(.*?\)', r'\1', cleaned)
        
        # Remove HTML tags
        cleaned = re.sub(r'<[^>]+>', '', cleaned)
        
        # Remove bold/italic markers
        cleaned = cleaned.replace('**', '').replace('*', '').replace('__', '').replace('_', '')
        
        # Remove heading markers
        cleaned = re.sub(r'^#+\s*', '', cleaned)
        
        # Remove blockquote markers
        cleaned = cleaned.replace('> ', '').replace('>', '')
        
        # Collapse whitespace
        cleaned = re.sub(r'\s+', ' ', cleaned).strip()
        
        # Skip empty or too-short paragraphs
        if len(cleaned) < 20:
            continue
        
        # Truncate to max length, prefer ending at a sentence boundary
        if len(cleaned) > MAX_DESC_LENGTH:
            truncated = cleaned[:MAX_DESC_LENGTH]
            # Try to break at the last sentence end within range
            last_period = truncated.rfind('. ')
            last_excl = truncated.rfind('! ')
            last_q = truncated.rfind('? ')
            break_at = max(last_period, last_excl, last_q)
            if break_at > MAX_DESC_LENGTH * 0.6:  # Only if it's a reasonable break point
                cleaned = cleaned[:break_at + 1]
            else:
                # Try last space
                last_space = truncated.rfind(' ')
                if last_space > MAX_DESC_LENGTH * 0.6:
                    cleaned = truncated[:last_space] + '...'
                else:
                    cleaned = truncated + '...'
        
        return cleaned
    
    return ''  # Fallback


def process_file(filepath, dry_run=False):
    """Process a single markdown file, adding Description if missing."""
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    frontmatter, body = parse_frontmatter_and_body(text)
    
    if not frontmatter:
        return None  # No frontmatter, skip
    
    if has_description(frontmatter):
        return None  # Already has Description
    
    desc = generate_description(body)
    if not desc:
        return None  # Couldn't generate a description
    
    if dry_run:
        return {
            'file': os.path.relpath(filepath, CONTENT_DIR),
            'description': desc
        }
    
    # Find where to insert Description (alphabetically after Tags, before Summary)
    # Insert after Tags: line, or at end of frontmatter
    insert_after = -1
    for i, line in enumerate(frontmatter):
        if line.startswith('Tags:'):
            insert_after = i
        elif line.startswith('Summary:') and insert_after < 0:
            insert_after = i - 1  # Insert before Summary if Tags not found
    
    if insert_after < 0:
        insert_after = len(frontmatter) - 1  # At end of frontmatter
    
    # Rebuild the file
    new_lines = frontmatter[:insert_after + 1]
    new_lines.append(f'Description: {desc}')
    new_lines.extend(frontmatter[insert_after + 1:])
    new_lines.append('')  # Blank line after frontmatter
    new_lines.append(body)
    
    new_text = '\n'.join(new_lines)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_text)
    
    return {
        'file': os.path.relpath(filepath, CONTENT_DIR),
        'description': desc
    }


def main():
    dry_run = '--dry-run' in sys.argv
    
    content_files = sorted([
        os.path.join(CONTENT_DIR, f)
        for f in os.listdir(CONTENT_DIR)
        if f.endswith('.md')
    ])
    
    results = []
    for filepath in content_files:
        result = process_file(filepath, dry_run=dry_run)
        if result:
            results.append(result)
    
    if dry_run:
        print(f"Found {len(results)} posts missing Description (dry run):\n")
        for r in results:
            rel = r['file']
            print(f"  {rel}")
            print(f"    → {r['description'][:100]}...")
            print()
        print(f"Total: {len(results)} posts would be updated.")
        print("Run without --dry-run to apply changes.")
    else:
        print(f"Added Description to {len(results)} posts:\n")
        for r in results:
            print(f"  {r['file']}")
            print(f"    → {r['description'][:100]}...")
            print()
        print(f"Total: {len(results)} posts updated.")


if __name__ == '__main__':
    main()
