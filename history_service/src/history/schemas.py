from enum import Enum
from typing import List
from uuid import UUID

from pydantic import BaseModel


class TracebackUnit(BaseModel):
    document_id: UUID
    information: str


class AIMessage(BaseModel):
    content: str
    traceback: List[TracebackUnit | None]


class UserMessage(BaseModel):
    content: str
