from typing import List
from uuid import UUID
from pydantic import BaseModel, Field


class Traceback(BaseModel):
    document_id: UUID
    information: str


class Message(BaseModel):
    role: str
    message: str
    traceback: List[Traceback] = Field(default=[])


class ChatData(BaseModel):
    chat_id: UUID
    name: str
    history: List[Message]

