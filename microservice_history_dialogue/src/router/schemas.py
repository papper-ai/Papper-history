from typing import List, Dict
from uuid import UUID

from pydantic import BaseModel


class Message(BaseModel):
    role: str
    message: str
    traceback: List[Dict[str, str]]


class Document(BaseModel):
    chat_id: UUID
    name: str
    history: List[Message]
