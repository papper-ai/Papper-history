from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/hello")
async def hello():
    return {
        "message": "Hello, World!"
    }

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)

