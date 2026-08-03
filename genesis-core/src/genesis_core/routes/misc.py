from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

router = APIRouter()


@router.get("/", response_class=PlainTextResponse)
async def root() -> str:
    return "Welcome to Genesis!"


@router.get("/api/v1/status", response_class=PlainTextResponse)
async def api_v1_status() -> str:
    return "OK"
