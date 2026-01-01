from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root() -> str:
    return "Welcome to Genesis!"


@app.get("/api/v1/status")
async def api_v1_status() -> str:
    return "OK"
