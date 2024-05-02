from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Body, Depends, status
from fastapi.responses import JSONResponse

from src.database.repositories import HistoryRepository
from src.history.dependencies import history_already_exists, history_exists
from src.history.schemas import AIMessage, UserMessage
from src.history.utils import (
    add_ai_message,
    add_user_message,
    clear_history,
    create_history,
    delete_history,
    get_history,
)

router = APIRouter(tags=["History"])


@router.post("/create_history", status_code=status.HTTP_201_CREATED)
async def create_history_route(
    chat_id: Annotated[UUID, Depends(history_already_exists)],
) -> None:
    await create_history(chat_id)


@router.post("/add_user_message", status_code=status.HTTP_200_OK)
async def add_user_message_route(
    chat_id: Annotated[UUID, Body(embed=True)],
    message: Annotated[UserMessage, Body()],
    history_repository: Annotated[HistoryRepository, Depends(history_exists)],
) -> None:
    await add_user_message(chat_id, message, history_repository)


@router.post("/add_ai_message", status_code=status.HTTP_200_OK)
async def add_ai_message_route(
    chat_id: Annotated[UUID, Body(embed=True)],
    message: Annotated[AIMessage, Body()],
    history_repository: Annotated[HistoryRepository, Depends(history_exists)],
) -> None:
    await add_ai_message(chat_id, message, history_repository)


@router.post("/clear_history", status_code=status.HTTP_200_OK)
async def clear_history_route(
    chat_id: Annotated[UUID, Body(embed=True)],
    history_repository: Annotated[HistoryRepository, Depends(history_exists)],
) -> None:
    await clear_history(chat_id, history_repository)


@router.delete("/delete_history", status_code=status.HTTP_200_OK)
async def delete_history_route(
    chat_id: Annotated[UUID, Body(embed=True)],
    history_repository: Annotated[HistoryRepository, Depends(history_exists)],
) -> None:
    await delete_history(chat_id, history_repository)


@router.post(
    "/get_history", status_code=status.HTTP_200_OK, response_class=JSONResponse
)
async def get_history_route(
    chat_id: Annotated[UUID, Body(embed=True)],
    history_repository: Annotated[HistoryRepository, Depends(history_exists)],
):
    return await get_history(chat_id, history_repository)
