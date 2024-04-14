from typing import List
from uuid import UUID

from pydantic import BaseModel


class Document(BaseModel):
    chat_id: UUID
    name: str
    history: List[
        {'role': 'user' / 'ai',
         'message': 'Privet',
         'traceback': [] / [{
            "document_id": "1",
            "information": "dop infa"}]
    }
    ]


