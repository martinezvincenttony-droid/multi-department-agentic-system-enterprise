#!/usr/bin/env python3
"""Load and display the current MEMORY.md file."""
import os
import sys

MEMORY_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "memory", "MEMORY.md"
)

def load_memory():
    if not os.path.exists(MEMORY_PATH):
        # Create initial memory file
        os.makedirs(os.path.dirname(MEMORY_PATH), exist_ok=True)
        initial = """# 🧠 Personal Memory Store\n\n> This file is automatically maintained by the system. It stores your preferences,\n> decisions, and context so that every conversation starts where the last one left off.\n\n---\n\n## Identity\n<!-- Name, role, department, location -->\n\n## Preferences\n<!-- Communication style, report format, language, tools -->\n\n## Active Projects\n<!-- Current projects, deadlines, stakeholders -->\n\n## Decisions Log\n<!-- Key decisions with dates and rationale -->\n\n## Patterns & Common Tasks\n<!-- Recurring requests, workflows, shortcuts -->\n\n## Corrections\n<!-- Things corrected — avoid repeating these mistakes -->\n\n## Team Context\n<!-- Key people, roles, relationships -->\n\n## Technical Context\n<!-- Systems, data sources, file locations, integrations -->\n\n---\n*Last updated: Never*\n"""
        with open(MEMORY_PATH, 'w', encoding='utf-8') as f:
            f.write(initial)
        print("[MEMORY] Initialized new MEMORY.md — no prior memories found.")
        print(initial)
    else:
        with open(MEMORY_PATH, 'r', encoding='utf-8') as f:
            content = f.read()
        size = os.path.getsize(MEMORY_PATH)
        print(f"[MEMORY] Loaded MEMORY.md ({size} bytes)")
        print(content)

if __name__ == "__main__":
    load_memory()
