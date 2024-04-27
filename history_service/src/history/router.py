from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Body, Depends, status

from src.database.repositories import HistoryRepository
from src.history.dependencies import history_exists
from src.history.utils import clean_history, create_history, delete_history

router = APIRouter(tags=["History"])


@router.post("/create_history", status_code=status.HTTP_201_CREATED)
async def create_history_route(chat_id: Annotated[UUID, Body(embed=True)]) -> None:
    await create_history(chat_id)


@router.post("/clean_history", status_code=status.HTTP_200_OK)
async def clean_history_route(
    chat_id: Annotated[UUID, Body(embed=True)],
    history_repository: Annotated[HistoryRepository, Depends(history_exists)],
) -> None:
    await clean_history(chat_id, history_repository)


@router.delete("/delete_history", status_code=status.HTTP_200_OK)
async def delete_history_route(
    chat_id: Annotated[UUID, Body(embed=True)],
    history_repository: Annotated[HistoryRepository, Depends(history_exists)],
) -> None:
    await delete_history(chat_id, history_repository)
