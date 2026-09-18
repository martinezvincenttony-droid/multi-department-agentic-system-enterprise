from __future__ import annotations

from datetime import datetime, timezone
from enum import Enum
from typing import Any
from uuid import uuid4

from pydantic import BaseModel, Field


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


def nid(prefix: str) -> str:
    return f"{prefix}_{uuid4().hex[:10]}"


class Severity(str, Enum):
    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    INFO = "INFO"


class AgentId(str, Enum):
    CHIEF = "chief_of_staff"
    OPS = "ops"
    FINANCE = "finance"
    PEOPLE = "people"
    STRATEGY = "strategy"
    AUDITOR = "auditor"


class EventKind(str, Enum):
    TASK_CREATED = "task_created"
    ROUTED = "routed"
    TOOL_CALL = "tool_call"
    TOOL_DENIED = "tool_denied"
    TOOL_RESULT = "tool_result"
    FINDING = "finding"
    HANDOFF = "handoff"
    AUDIT_PASS = "audit_pass"
    AUDIT_FAIL = "audit_fail"
    PACKET_READY = "packet_ready"


class Task(BaseModel):
    id: str = Field(default_factory=lambda: nid("task"))
    owner: AgentId
    title: str
    detail: str = ""
    depends_on: list[str] = Field(default_factory=list)
    done: bool = False
    result: dict[str, Any] = Field(default_factory=dict)


class Finding(BaseModel):
    id: str = Field(default_factory=lambda: nid("ev"))
    agent: AgentId
    severity: Severity
    title: str
    evidence: str
    source_tool: str
    source_ref: str
    owner: str | None = None


class Event(BaseModel):
    id: str = Field(default_factory=lambda: nid("evt"))
    ts: datetime = Field(default_factory=utcnow)
    kind: EventKind
    agent: AgentId
    summary: str
    payload: dict[str, Any] = Field(default_factory=dict)


class Decision(BaseModel):
    id: str = Field(default_factory=lambda: nid("dec"))
    statement: str
    evidence_ids: list[str]
    owner: str
    due: str | None = None


class Packet(BaseModel):
    run_id: str
    request: str
    status: str
    findings: list[Finding]
    decisions: list[Decision]
    briefing_md: str
    audit_notes: list[str] = Field(default_factory=list)
    events: list[Event] = Field(default_factory=list)
