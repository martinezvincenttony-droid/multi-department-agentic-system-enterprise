---
name: calendar-intelligence-engine
description: "Advanced calendar management, scheduling optimization, meeting preparation, time analytics, and calendar intelligence. Use when the user needs to analyze their schedule, find optimal meeting times, prepare meeting agendas, review upcoming commitments, identify scheduling conflicts, generate weekly schedule overviews, assess time allocation, create calendar events with smart defaults, or optimize their daily/weekly schedule. Also triggers when the user asks about their availability, upcoming meetings, meeting prep, or workload distribution."
license: Proprietary
---

# Calendar Intelligence Engine

Advanced calendar management and intelligence system for schedule optimization, meeting preparation, and time analytics.

## Rules

- Always call `get_current_datetime` first to establish the current time reference.
- Use `calendar_list_events` with explicit ISO date ranges for reliable results.
- When analyzing schedules, calculate: total meeting hours, focus time blocks, meeting density.
- For meeting prep, search emails and Teams messages for relevant context.
- Present schedule data in clear table format with color-coded indicators.
- When creating events, always include: subject, start/end time, timezone, attendees, agenda body.
- Never delete or cancel events without explicit user confirmation.
- Consider the user's timezone (typically CET/CEST for the organization).

## Workflow

### Schedule Overview
1. Call `get_current_datetime` to get current date/time.
2. Use `calendar_list_events` for the requested range (default: current week).
3. Analyze events: count meetings, calculate total hours, identify gaps.
4. Present structured overview with:
   - Day-by-day breakdown
   - Total meeting hours per day
   - Available focus time blocks
   - Conflict indicators
   - Meeting density score (Low/Medium/High/Overloaded)

### Meeting Preparation
1. Get event details via `calendar_get_event`.
2. Search emails related to the meeting topic using `outlook_search_emails`.
3. Search Teams messages if relevant using `teams_search_messages`.
4. Compile meeting prep brief:
   - Meeting details (time, attendees, location)
   - Background context from emails/messages
   - Key discussion points identified
   - Open action items from previous meetings
   - Suggested agenda items

### Schedule Optimization
1. Retrieve full week calendar.
2. Analyze for:
   - Back-to-back meeting clusters (no buffer time)
   - Fragmented focus time (< 1 hour blocks)
   - Meeting-heavy days vs. meeting-light days
   - Early morning / late afternoon loading
3. Provide recommendations:
   - Suggested meeting consolidation
   - Recommended focus time blocks
   - Buffer time suggestions
   - Optimal days for deep work

### Smart Event Creation
1. Gather: subject, attendees, duration, preferred time.
2. Check calendar for conflicts.
3. Suggest optimal time slot based on:
   - Existing free time
   - Meeting density of the day
   - Buffer time around other meetings
4. Create event with proper formatting via `calendar_create_event`.

### Time Analytics
1. Pull events for the analysis period (week/month).
2. Calculate:
   - Total meeting hours
   - Meeting categories breakdown
   - Average meetings per day
   - Longest meeting-free block
   - Percentage of time in meetings vs. focus time
3. Present analytics with charts or tables.

## Meeting Density Scoring

| Score | Hours/Day | Assessment | Recommendation |
|-------|-----------|------------|----------------|
| Low | 0-2 hrs | Good focus time | Ideal for deep work days |
| Medium | 2-4 hrs | Balanced | Healthy meeting load |
| High | 4-6 hrs | Heavy | Consider declining optional meetings |
| Overloaded | 6+ hrs | Critical | Schedule review needed |

## Good fits

- "What does my week look like?"
- "Prepare me for my next meeting"
- "Find time for a 1-hour meeting with [person]"
- "How much time am I spending in meetings?"
- "Optimize my schedule for tomorrow"
- "Show me my availability this week"
- "Create a meeting about [topic] with [attendees]"
- "Analyze my calendar workload this month"
- "Brief me for my 2pm meeting"

## Avoid by default

- Canceling or declining meetings without explicit approval
- Modifying other people's calendar events
- Scheduling over existing commitments without flagging conflicts
- Making assumptions about meeting importance without checking
