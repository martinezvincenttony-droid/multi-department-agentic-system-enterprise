from __future__ import annotations

import json
from pathlib import Path

from openpyxl import Workbook


def ensure_fixtures(dirpath: Path) -> None:
    dirpath.mkdir(parents=True, exist_ok=True)
    training = dirpath / "training.xlsx"
    reqs = dirpath / "requirements.xlsx"
    if not training.exists():
        wb = Workbook()
        ws = wb.active
        ws.title = "Training"
        ws.append(["Employee", "Role", "Skill", "Status"])
        rows = [
            ("Ava Chen", "Warehouse Lead", "Forklift", "Certified"),
            ("Ava Chen", "Warehouse Lead", "OSHA-10", "Expired"),
            ("Ava Chen", "Warehouse Lead", "First Aid", "Certified"),
            ("Marcus Diaz", "Warehouse Lead", "Forklift", "In Progress"),
            ("Marcus Diaz", "Warehouse Lead", "OSHA-10", "NOT FOUND"),
            ("Marcus Diaz", "Warehouse Lead", "First Aid", "Certified"),
            ("Priya Shah", "Quality", "ISO Internal Audit", "Certified"),
            ("Priya Shah", "Quality", "First Aid", "Missing"),
            ("Jordan Blake", "Quality", "ISO Internal Audit", "Not Started"),
            ("Jordan Blake", "Quality", "First Aid", "Certified"),
        ]
        for r in rows:
            ws.append(list(r))
        wb.save(training)
    if not reqs.exists():
        wb = Workbook()
        ws = wb.active
        ws.title = "PA"
        ws.append(["Role", "RequiredSkill"])
        for role, skill in [
            ("Warehouse Lead", "Forklift"),
            ("Warehouse Lead", "OSHA-10"),
            ("Warehouse Lead", "First Aid"),
            ("Quality", "ISO Internal Audit"),
            ("Quality", "First Aid"),
        ]:
            ws.append([role, skill])
        wb.save(reqs)
    inbox = dirpath / "inbox.json"
    if not inbox.exists():
        inbox.write_text(json.dumps([
            {"id": "m1", "from": "qa@plant.local", "subject": "OSHA-10 recert window closes Friday", "body": "Marcus and Ava need OSHA-10 on the training matrix before the audit.", "priority": "URGENT"},
            {"id": "m2", "from": "vendor@lifts.example", "subject": "Forklift class seats held until Tuesday", "body": "Two open seats for forklift certification. Reply to confirm.", "priority": "ACTION"},
            {"id": "m3", "from": "all@plant.local", "subject": "Cafeteria menu", "body": "Tacos on Thursday.", "priority": "LOW"},
            {"id": "m4", "from": "hr@plant.local", "subject": "ISO internal audit pre-read", "body": "Jordan has not started ISO Internal Audit training.", "priority": "ACTION"},
        ], indent=2), encoding="utf-8")
    cal = dirpath / "calendar.json"
    if not cal.exists():
        cal.write_text(json.dumps([
            {"id": "c1", "date": "2026-09-21", "time": "09:00", "title": "Monday standup", "attendees": ["Ava Chen", "Marcus Diaz"], "needs_prep": False},
            {"id": "c2", "date": "2026-09-21", "time": "11:00", "title": "Plant audit pre-brief", "attendees": ["Priya Shah", "Jordan Blake"], "needs_prep": True},
            {"id": "c3", "date": "2026-09-22", "time": "14:00", "title": "Forklift vendor call", "attendees": ["Marcus Diaz"], "needs_prep": True},
        ], indent=2), encoding="utf-8")
