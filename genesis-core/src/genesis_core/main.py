from fastapi import FastAPI

from genesis_core.routes import misc

app = FastAPI()

app.include_router(misc.router)
