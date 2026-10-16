#!/usr/bin/env python3
"""Update or remove specific memories from MEMORY.md.

Usage:
    python update_memory.py --remove "old preference text"
    python update_memory.py --replace "old text" --with "new text"
    python update_memory.py --show-category "Preferences"
"""
import os
import sys
import re
import argparse
from datetime import datetime

MEMORY_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "memory", "MEMORY.md"
)

def remove_memory(search_text: str):
    if not os.path.exists(MEMORY_PATH):
        print("[MEMORY] No MEMORY.md found.")
        return
    
    with open(MEMORY_PATH, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    new_lines = []
    removed = 0
    for line in lines:
        if search_text.lower() in line.lower() and line.strip().startswith('- ['):
            print(f"[MEMORY] 🗑️ Removed: {line.strip()}")
            removed += 1
        else:
            new_lines.append(line)
    
    if removed == 0:
        print(f"[MEMORY] No matching memory found for: '{search_text}'")
        return
    
    # Update timestamp
    content = ''.join(new_lines)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = re.sub(r'\*Last updated:.*\*', f'*Last updated: {timestamp}*', content)
    
    with open(MEMORY_PATH, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"[MEMORY] ✅ Removed {removed} memor{'y' if removed == 1 else 'ies'}.")

def replace_memory(old_text: str, new_text: str):
    if not os.path.exists(MEMORY_PATH):
        print("[MEMORY] No MEMORY.md found.")
        return
    
    with open(MEMORY_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_text.lower() not in content.lower():
        print(f"[MEMORY] No matching memory found for: '{old_text}'")
        return
    
    # Case-insensitive replace
    pattern = re.compile(re.escape(old_text), re.IGNORECASE)
    content = pattern.sub(new_text, content)
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = re.sub(r'\*Last updated:.*\*', f'*Last updated: {timestamp}*', content)
    
    with open(MEMORY_PATH, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"[MEMORY] ✅ Replaced '{old_text}' with '{new_text}'")

def show_category(category: str):
    if not os.path.exists(MEMORY_PATH):
        print("[MEMORY] No MEMORY.md found.")
        return
    
    with open(MEMORY_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    
    header = f"## {category}"
    if header not in content:
        print(f"[MEMORY] Category '{category}' not found.")
        return
    
    idx = content.index(header)
    next_section = content.find('\n## ', idx + len(header))
    if next_section == -1:
        next_section = content.find('\n---', idx + len(header))
    
    section = content[idx:next_section].strip() if next_section != -1 else content[idx:].strip()
    print(section)

def main():
    parser = argparse.ArgumentParser(description='Update or remove memories')
    parser.add_argument('--remove', type=str, help='Text to search and remove')
    parser.add_argument('--replace', type=str, help='Text to search and replace')
    parser.add_argument('--with-text', type=str, dest='with_text', help='Replacement text (use with --replace)')
    parser.add_argument('--show-category', type=str, help='Show all entries in a category')
    
    args = parser.parse_args()
    
    if args.remove:
        remove_memory(args.remove)
    elif args.replace and args.with_text:
        replace_memory(args.replace, args.with_text)
    elif args.show_category:
        show_category(args.show_category)
    else:
        print("Usage:")
        print("  python update_memory.py --remove 'text to remove'")
        print("  python update_memory.py --replace 'old' --with-text 'new'")
        print("  python update_memory.py --show-category 'Preferences'")

if __name__ == "__main__":
    main()
