"""
Email Command Center — triage, draft, digest, and follow-up tracking.
Pure-Python; works with email data passed as dicts or list of dicts.
"""
from datetime import datetime, timedelta
import re

URGENT_KEYWORDS = ["urgent", "asap", "immediately", "today", "deadline", "overdue", "critical", "emergency", "by eod", "end of day"]
ACTION_KEYWORDS = ["please", "could you", "can you", "need", "request", "approve", "review", "confirm", "respond", "feedback"]
FYI_KEYWORDS = ["fyi", "for your information", "heads up", "update", "notification", "newsletter"]
DELEGATE_HINTS = ["scheduling", "calendar", "logistics", "format", "minor", "small", "quick"]


def triage_inbox(emails):
    """
    emails: list of dicts with keys {from, subject, body, received, has_attachment}
    Returns categorized list with priority scores and suggested actions.
    """
    triaged = []
    for e in emails:
        text = f"{e.get('subject','')} {e.get('body','')}".lower()
        score = 0
        category = "FYI"
        action = "Read when convenient"

        if any(k in text for k in URGENT_KEYWORDS):
            category = "URGENT"
            score = 100
            action = "Respond within 2 hours"
        elif "?" in e.get("subject", "") + e.get("body", "") or any(k in text for k in ACTION_KEYWORDS):
            category = "ACTION REQUIRED"
            score = 70
            action = "Respond today"
        elif any(k in text for k in DELEGATE_HINTS):
            category = "DELEGATABLE"
            score = 40
            action = "Forward / delegate"
        elif any(k in text for k in FYI_KEYWORDS):
            category = "FYI"
            score = 20
            action = "Skim & archive"
        else:
            category = "LOW"
            score = 10
            action = "Batch review later"

        # Boost if from VIP / boss / external client
        sender = e.get("from", "").lower()
        if any(v in sender for v in ["ceo", "cfo", "director", "client", "customer"]):
            score += 30

        deadline = _extract_deadline(e.get("body", ""))

        triaged.append({
            "from": e.get("from"),
            "subject": e.get("subject"),
            "category": category,
            "priority_score": score,
            "suggested_action": action,
            "deadline": deadline,
            "received": e.get("received"),
        })

    triaged.sort(key=lambda x: x["priority_score"], reverse=True)
    return triaged


def _extract_deadline(body):
    """Crude deadline extraction."""
    patterns = [
        r"by (\w+day)",
        r"by (\d{1,2}/\d{1,2})",
        r"deadline[:\s]+([\w\s,/-]+)",
        r"due[:\s]+([\w\s,/-]+)",
    ]
    for p in patterns:
        m = re.search(p, body, re.IGNORECASE)
        if m:
            return m.group(1).strip()
    return None


# ---------- Drafting ----------
TEMPLATES = {
    "reply_yes": "Hi {name},\n\nThanks for reaching out. {context}\n\nHappy to confirm — {commitment}.\n\nLet me know if you need anything else.\n\nBest,\n{sender}",
    "reply_decline": "Hi {name},\n\nThanks for thinking of me. Unfortunately, {reason}.\n\n{alternative}\n\nAppreciate the invite — let's connect another time.\n\nBest,\n{sender}",
    "status_update": "Hi {name},\n\nQuick update on {project}:\n\n• Progress: {progress}\n• Next steps: {next_steps}\n• Blockers: {blockers}\n\nLet me know if you have questions.\n\nBest,\n{sender}",
    "meeting_request": "Hi {name},\n\nI'd like to set up a {duration} meeting to discuss {topic}.\n\nWould any of these times work?\n  • {slot1}\n  • {slot2}\n  • {slot3}\n\nLet me know what works best.\n\nBest,\n{sender}",
    "follow_up": "Hi {name},\n\nJust circling back on my note from {date} regarding {topic}.\n\nNo rush — wanted to make sure it didn't get buried.\n\nBest,\n{sender}",
    "thank_you": "Hi {name},\n\nThanks so much for {reason}. {impact}\n\nReally appreciate it.\n\nBest,\n{sender}",
}


def draft_email(template_key, **kwargs):
    """Generate a draft email from a template."""
    if template_key not in TEMPLATES:
        return {"error": f"Unknown template. Available: {list(TEMPLATES.keys())}"}
    body = TEMPLATES[template_key].format(**kwargs)
    subject = kwargs.get("subject", _suggest_subject(template_key, kwargs))
    return {"subject": subject, "body": body}


def _suggest_subject(template_key, kwargs):
    project = kwargs.get("project", "")
    topic = kwargs.get("topic", "")
    return {
        "reply_yes": f"Re: {topic or project}",
        "reply_decline": f"Re: {topic or project}",
        "status_update": f"{project} — Status Update",
        "meeting_request": f"Meeting Request: {topic}",
        "follow_up": f"Following up: {topic or project}",
        "thank_you": f"Thank you — {kwargs.get('reason','')}",
    }.get(template_key, "Update")


# ---------- Digests & Follow-ups ----------
def generate_digest(emails, window_days=7):
    """Group emails by sender into a structured digest."""
    by_sender = {}
    for e in emails:
        s = e.get("from", "Unknown")
        by_sender.setdefault(s, []).append(e)

    digest = {"window_days": window_days, "total_emails": len(emails), "senders": []}
    for sender, msgs in sorted(by_sender.items(), key=lambda kv: -len(kv[1])):
        digest["senders"].append({
            "sender": sender,
            "count": len(msgs),
            "subjects": [m.get("subject") for m in msgs[:5]],
        })
    return digest


def find_followups(sent_emails, received_emails, days_threshold=3):
    """Identify sent emails with no reply after N days."""
    received_subjects = {(r.get("from"), _normalize_subject(r.get("subject", ""))) for r in received_emails}
    pending = []
    cutoff = datetime.now() - timedelta(days=days_threshold)
    for s in sent_emails:
        sent_at = s.get("sent_at")
        if isinstance(sent_at, str):
            try:
                sent_at = datetime.fromisoformat(sent_at)
            except Exception:
                continue
        if sent_at and sent_at < cutoff:
            key = (s.get("to"), _normalize_subject(s.get("subject", "")))
            if key not in received_subjects:
                pending.append({
                    "to": s.get("to"),
                    "subject": s.get("subject"),
                    "sent_at": sent_at.isoformat() if sent_at else None,
                    "days_waiting": (datetime.now() - sent_at).days if sent_at else None,
                    "suggested": "Send polite follow-up",
                })
    return sorted(pending, key=lambda x: x.get("days_waiting") or 0, reverse=True)


def _normalize_subject(s):
    return re.sub(r"^(re:|fwd?:)\s*", "", s.strip().lower())
