import logging
from uuid import UUID

from src.database.repositories import HistoryRepository
from src.history.schemas import AIMessage, UserMessage


async def create_history(chat_id: UUID) -> None:
    history_repository = HistoryRepository()
    await history_repository.add(chat_id=chat_id)


async def clean_history(chat_id: UUID, history_repository: HistoryRepository) -> None:
    await history_repository.clean_history(chat_id=chat_id)


async def delete_history(chat_id: UUID, history_repository: HistoryRepository) -> None:
    await history_repository.delete(chat_id=chat_id)


async def get_history(
    chat_id: UUID, history_repository: HistoryRepository
) -> dict:
    history = await history_repository.get(chat_id=chat_id)
    return {"chat_id": history["_id"], "history": history["history"]}


async def add_user_message(
    chat_id: UUID,
    message: UserMessage,
    history_repository: HistoryRepository,
) -> None:
    message = {
        "role": "user",
        "content": message.content,
    }

    await history_repository.add_message(chat_id, message)


async def add_ai_message(
    chat_id: UUID,
    message: AIMessage,
    history_repository: HistoryRepository,
) -> None:
    message = {
        "role": "ai",
        "content": message.content,
        "traceback": [
            {
                "document_id": traceback_unit.document_id,
                "information": traceback_unit.information,
            }
            for traceback_unit in message.traceback
        ],
    }

    await history_repository.add_message(chat_id, message)
