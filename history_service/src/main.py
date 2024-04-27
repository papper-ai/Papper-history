from fastapi import FastAPI

from src.history import history_router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello from history_service"}


app.include_router(history_router)
