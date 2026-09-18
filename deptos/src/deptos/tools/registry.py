from __future__ import annotations

from collections.abc import Callable
from typing import Any

from deptos.blackboard import Blackboard
from deptos.models import AgentId, EventKind


class ToolDenied(PermissionError):
    pass


class ToolRegistry:
    """Least-privilege tool bus. Agents may only call tools on their allowlist."""

    def __init__(self, board: Blackboard) -> None:
        self.board = board
        self._impl: dict[str, Callable[..., Any]] = {}
        self._allow: dict[AgentId, set[str]] = {aid: set() for aid in AgentId}

    def register(self, name: str, fn: Callable[..., Any], allowed: list[AgentId]) -> None:
        self._impl[name] = fn
        for aid in allowed:
            self._allow[aid].add(name)

    def call(self, agent: AgentId, name: str, **kwargs: Any) -> Any:
        if name not in self._impl:
            raise KeyError(f"unknown tool: {name}")
        if name not in self._allow[agent]:
            self.board.emit(agent, EventKind.TOOL_DENIED, f"{agent.value} blocked from {name}", {"tool": name})
            raise ToolDenied(f"{agent.value} cannot call {name}")
        self.board.emit(agent, EventKind.TOOL_CALL, f"{agent.value} -> {name}", {"tool": name})
        result = self._impl[name](**kwargs)
        self.board.emit(agent, EventKind.TOOL_RESULT, f"{name} returned", {"tool": name})
        return result
