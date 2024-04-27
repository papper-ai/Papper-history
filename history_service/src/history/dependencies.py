from typing import Annotated
from uuid import UUID

from fastapi import Body
from fastapi.exceptions import HTTPException

from src.database.repositories import HistoryRepository


async def history_exists(chat_id: Annotated[UUID, Body()]) -> HistoryRepository:
    history_repository = HistoryRepository()

    history = await history_repository.get(chat_id)
    if not history:
        raise HTTPException(status_code=404, detail="History not found")

    return history_repository


async def history_already_exists(
    chat_id: Annotated[UUID, Body(embed=True)],
) -> HistoryRepository:
    history_repository = HistoryRepository()

    history = await history_repository.get(chat_id)
    if history:
        raise HTTPException(status_code=400, detail="History already exists")

    return chat_id
