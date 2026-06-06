"""
Calendar Intelligence Engine — pure-Python schedule analysis.
Works on event lists: [{start, end, title, attendees, type}]
"""
from datetime import datetime, timedelta, time

ENERGY_ZONES = [
    (time(9, 0),  time(11, 0), "Peak",       "High-cognitive deep work"),
    (time(11, 0), time(14, 0), "Steady",     "Collaboration & meetings"),
    (time(14, 0), time(16, 0), "Recovery",   "Admin, email, reviews"),
    (time(16, 0), time(17, 30),"Wind-down",  "Planning & light tasks"),
]

MEETING_TYPES = ["1:1", "team", "external", "deep_work", "focus", "admin"]


def _parse(dt):
    if isinstance(dt, datetime):
        return dt
    return datetime.fromisoformat(dt)


def weekly_overview(events):
    """Produce a structured weekly overview grouped by day."""
    by_day = {}
    for e in events:
        s = _parse(e["start"])
        day = s.strftime("%A %Y-%m-%d")
        by_day.setdefault(day, []).append(e)

    overview = {"days": [], "total_events": len(events)}
    for day in sorted(by_day.keys(), key=lambda d: d.split(" ")[1]):
        evts = sorted(by_day[day], key=lambda e: _parse(e["start"]))
        meeting_minutes = sum(
            (_parse(e["end"]) - _parse(e["start"])).total_seconds() / 60
            for e in evts
        )
        overview["days"].append({
            "day": day,
            "event_count": len(evts),
            "meeting_hours": round(meeting_minutes / 60, 1),
            "density": _density_score(meeting_minutes),
            "events": [_summarize_event(e) for e in evts],
        })
    return overview


def _summarize_event(e):
    s, en = _parse(e["start"]), _parse(e["end"])
    return {
        "time": f"{s.strftime('%H:%M')}-{en.strftime('%H:%M')}",
        "title": e.get("title"),
        "type": e.get("type", "meeting"),
        "duration_min": int((en - s).total_seconds() / 60),
    }


def _density_score(minutes):
    if minutes < 120: return "🟢 Light"
    if minutes < 240: return "🟡 Moderate"
    if minutes < 360: return "🟠 Heavy"
    return "🔴 Overloaded"


def analyze_time(events):
    """Time allocation breakdown by type."""
    totals = {t: 0 for t in MEETING_TYPES}
    total_minutes = 0
    for e in events:
        dur = (_parse(e["end"]) - _parse(e["start"])).total_seconds() / 60
        t = e.get("type", "team")
        totals[t] = totals.get(t, 0) + dur
        total_minutes += dur

    return {
        "total_hours": round(total_minutes / 60, 1),
        "by_type": {k: round(v / 60, 1) for k, v in totals.items() if v > 0},
        "deep_work_pct": round((totals.get("deep_work", 0) + totals.get("focus", 0)) / max(total_minutes, 1) * 100),
        "meeting_pct": round((totals.get("team", 0) + totals.get("1:1", 0) + totals.get("external", 0)) / max(total_minutes, 1) * 100),
        "recommendation": _time_recommendation(totals, total_minutes),
    }


def _time_recommendation(totals, total):
    meeting = totals.get("team", 0) + totals.get("1:1", 0) + totals.get("external", 0)
    if total == 0:
        return "No data."
    pct = meeting / total * 100
    if pct > 70:
        return "⚠️ Too much meeting time — protect 2-3 hours of deep work daily."
    if pct < 20:
        return "✅ Strong deep work balance — maintain this pattern."
    return "Healthy mix — consider blocking morning hours for focus work."


def detect_conflicts(events):
    """Detect overlaps and missing buffers."""
    sorted_e = sorted(events, key=lambda e: _parse(e["start"]))
    conflicts, no_buffer = [], []
    for i in range(len(sorted_e) - 1):
        a, b = sorted_e[i], sorted_e[i + 1]
        a_end, b_start = _parse(a["end"]), _parse(b["start"])
        if b_start < a_end:
            conflicts.append({
                "event_a": a.get("title"),
                "event_b": b.get("title"),
                "overlap_min": int((a_end - b_start).total_seconds() / 60),
            })
        elif b_start - a_end < timedelta(minutes=10) and a_end.date() == b_start.date():
            no_buffer.append({
                "between": f"{a.get('title')} → {b.get('title')}",
                "gap_min": int((b_start - a_end).total_seconds() / 60),
            })
    return {"conflicts": conflicts, "back_to_back": no_buffer}


def suggest_slots(events, duration_min=30, work_start=9, work_end=17, days_ahead=5):
    """Find open slots of given duration in working hours."""
    busy_by_day = {}
    for e in events:
        s = _parse(e["start"])
        busy_by_day.setdefault(s.date(), []).append((_parse(e["start"]), _parse(e["end"])))

    slots = []
    today = datetime.now().date()
    for d in range(days_ahead):
        day = today + timedelta(days=d)
        if day.weekday() >= 5:  # skip weekends
            continue
        cursor = datetime.combine(day, time(work_start, 0))
        end_of_day = datetime.combine(day, time(work_end, 0))
        busy = sorted(busy_by_day.get(day, []))
        for b_start, b_end in busy:
            if cursor + timedelta(minutes=duration_min) <= b_start:
                slots.append({
                    "day": day.strftime("%A %Y-%m-%d"),
                    "start": cursor.strftime("%H:%M"),
                    "end": (cursor + timedelta(minutes=duration_min)).strftime("%H:%M"),
                    "energy": _energy_at(cursor.time()),
                })
            cursor = max(cursor, b_end)
        # Trailing slot
        while cursor + timedelta(minutes=duration_min) <= end_of_day:
            slots.append({
                "day": day.strftime("%A %Y-%m-%d"),
                "start": cursor.strftime("%H:%M"),
                "end": (cursor + timedelta(minutes=duration_min)).strftime("%H:%M"),
                "energy": _energy_at(cursor.time()),
            })
            cursor += timedelta(minutes=duration_min)
            if len(slots) >= 10:
                break
    return slots[:10]


def _energy_at(t):
    for start, end, label, _ in ENERGY_ZONES:
        if start <= t < end:
            return label
    return "Off-hours"


def prep_brief(event, related_emails=None, related_notes=None):
    """Generate a meeting prep brief."""
    s, en = _parse(event["start"]), _parse(event["end"])
    brief = {
        "meeting": event.get("title"),
        "when": f"{s.strftime('%A %B %d, %H:%M')} — {en.strftime('%H:%M')}",
        "duration_min": int((en - s).total_seconds() / 60),
        "attendees": event.get("attendees", []),
        "type": event.get("type", "meeting"),
        "objectives_to_clarify": [
            "What is the one decision we need to walk out with?",
            "What's the agenda? Who's driving it?",
            "What questions should I be ready to answer?",
        ],
        "context": {
            "related_emails": related_emails or [],
            "related_notes": related_notes or [],
        },
        "suggested_prep_minutes": max(10, min(30, int((en - s).total_seconds() / 60) // 4)),
    }
    return brief
