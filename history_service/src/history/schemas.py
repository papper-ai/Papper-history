from enum import Enum
from typing import List
from uuid import UUID

from pydantic import BaseModel


class Role(str, Enum):
    USER = "user"
    AI = "ai"


class TracebackUnit(BaseModel):
    document_id: UUID
    information: str


class Message(BaseModel):
    role: str
    message: str
    traceback: List[TracebackUnit]


class History(BaseModel):
    chat_id: UUID
    history: List[Message]
