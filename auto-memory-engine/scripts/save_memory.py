#!/usr/bin/env python3
"""Append new memories to MEMORY.md under the appropriate category.

Usage:
    python save_memory.py --category "Preferences" --entry "Prefers executive summary format with bullet points"
    python save_memory.py --category "Decisions" --entry "Decided to use Claude Opus for all complex analysis tasks"
    python save_memory.py --batch '[{"category": "Preferences", "entry": "Likes tables"}, {"category": "Identity", "entry": "Name: John"}]'
"""
import os
import sys
import json
import argparse
from datetime import datetime

MEMORY_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "memory", "MEMORY.md"
)

VALID_CATEGORIES = [
    "Identity",
    "Preferences",
    "Active Projects",
    "Decisions Log",
    "Patterns & Common Tasks",
    "Corrections",
    "Team Context",
    "Technical Context"
]

def ensure_memory_exists():
    if not os.path.exists(MEMORY_PATH):
        os.system(f"python3 {os.path.dirname(__file__)}/load_memory.py > /dev/null 2>&1")

def append_memory(category: str, entry: str):
    ensure_memory_exists()
    
    with open(MEMORY_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    new_entry = f"- [{timestamp}] {entry}\n"
    
    # Find the category section and append after the comment line
    section_header = f"## {category}"
    if section_header in content:
        # Find the position after the section header and any comment
        idx = content.index(section_header)
        # Find the next line after header
        next_newline = content.index('\n', idx)
        # Check if there's a comment line
        rest = content[next_newline+1:]
        if rest.startswith('<!--'):
            comment_end = rest.index('-->') + 3
            insert_pos = next_newline + 1 + comment_end + 1
        else:
            insert_pos = next_newline + 1
        
        # Check for duplicate (don't add same entry twice)
        existing_section_end = content.find('\n## ', insert_pos)
        if existing_section_end == -1:
            existing_section_end = content.find('\n---', insert_pos)
        existing_section = content[insert_pos:existing_section_end] if existing_section_end != -1 else content[insert_pos:]
        
        # Simple dedup: check if the core entry text already exists
        entry_core = entry.strip().lower()
        if entry_core in existing_section.lower():
            print(f"[MEMORY] Skipped duplicate: '{entry}' already exists in {category}")
            return
        
        content = content[:insert_pos] + new_entry + content[insert_pos:]
    else:
        # Category doesn't exist yet, add it before the footer
        footer_marker = "\n---\n*Last updated:"
        if footer_marker in content:
            idx = content.index(footer_marker)
            new_section = f"\n## {category}\n{new_entry}\n"
            content = content[:idx] + new_section + content[idx:]
        else:
            content += f"\n## {category}\n{new_entry}\n"
    
    # Update timestamp
    timestamp_full = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if "*Last updated:" in content:
        import re
        content = re.sub(r'\*Last updated:.*\*', f'*Last updated: {timestamp_full}*', content)
    
    with open(MEMORY_PATH, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"[MEMORY] ✅ Saved to {category}: {entry}")

def main():
    parser = argparse.ArgumentParser(description='Save memories to MEMORY.md')
    parser.add_argument('--category', '-c', type=str, help='Memory category')
    parser.add_argument('--entry', '-e', type=str, help='Memory entry text')
    parser.add_argument('--batch', '-b', type=str, help='JSON array of {category, entry} objects')
    
    args = parser.parse_args()
    
    if args.batch:
        entries = json.loads(args.batch)
        for item in entries:
            append_memory(item['category'], item['entry'])
        print(f"\n[MEMORY] Batch complete: {len(entries)} memories saved.")
    elif args.category and args.entry:
        append_memory(args.category, args.entry)
    else:
        print("Usage: python save_memory.py --category 'Preferences' --entry 'Likes bullet points'")
        print("   or: python save_memory.py --batch '[{\"category\": \"Preferences\", \"entry\": \"Likes tables\"}]'")
        sys.exit(1)

if __name__ == "__main__":
    main()
