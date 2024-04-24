from typing import List
from uuid import UUID
from pydantic import BaseModel, Field


class Role(str):
    user = "user"
    ai = "ai"


class TracebackItem(BaseModel):
    document_id: UUID
    information: str


class MessageItem(BaseModel):
    role: Role
    message: str
    traceback: List[TracebackItem] = Field(default=[])


class ChatHistory(BaseModel):
    history: List[MessageItem]


class Chat(BaseModel):
    chat_id: UUID
    name: str
    history: ChatHistory


