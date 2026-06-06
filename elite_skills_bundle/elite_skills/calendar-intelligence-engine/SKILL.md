---
name: calendar-intelligence-engine
description: Schedule optimization and meeting intelligence engine. Produces weekly schedule overviews, meeting prep briefs, conflict detection, time analytics (deep work vs meetings), and energy-based scheduling recommendations.
license: MIT
---

# Calendar Intelligence Engine

## Rules
- Always work in the user's local timezone unless told otherwise
- Flag back-to-back meetings (no buffer) and >4 hour meeting blocks
- Distinguish meeting types: 1:1, team, external/client, deep work, focus, admin
- Protect deep work blocks — recommend defending them
- Energy zones: Peak (9-11am), Steady (11am-2pm), Recovery (2-4pm), Wind-down (4-5:30pm)
- Recommend morning slots for high-cognitive tasks, afternoons for collaborative work

## Workflow
1. Receive calendar data (list of events with start, end, title, attendees, type)
2. Run `weekly_overview()` for a high-level view
3. Run `analyze_time()` for time-allocation breakdown
4. Run `detect_conflicts()` for overlap & buffer issues
5. Use `suggest_slots()` for new meeting placement
6. Use `prep_brief()` to generate context for an upcoming meeting

## Good fits
- "What does my week look like?"
- "Find a 30-min slot for a 1:1 with Sarah this week"
- "How much time am I spending in meetings vs deep work?"
- "Prep me for my 2pm meeting with the engineering team"
- "Are there any conflicts in my schedule?"

## Avoid by default
- Do not auto-accept or auto-decline meetings — always recommend
- Do not assume attendee availability without data
- Do not over-schedule — leave at least 25% open buffer
