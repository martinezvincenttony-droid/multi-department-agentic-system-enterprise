from __future__ import annotations

from deptos.blackboard import Blackboard
from deptos.models import AgentId
from deptos.tools.registry import ToolRegistry


class Agent:
    id: AgentId

    def __init__(self, board: Blackboard, tools: ToolRegistry) -> None:
        self.board = board
        self.tools = tools
