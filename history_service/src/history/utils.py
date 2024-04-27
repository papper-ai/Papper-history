from uuid import UUID

from src.database.repositories import HistoryRepository


async def create_history(chat_id: UUID) -> None:
    history_repository = HistoryRepository()
    await history_repository.add(chat_id=chat_id)


async def clean_history(chat_id: UUID, history_repository: HistoryRepository) -> None:
    await history_repository.clean_history(chat_id=chat_id)


async def delete_history(chat_id: UUID, history_repository: HistoryRepository) -> None:
    await history_repository.delete(chat_id=chat_id)
