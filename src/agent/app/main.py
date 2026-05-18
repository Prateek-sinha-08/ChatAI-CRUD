from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.agent.app.db.base import Base
from src.agent.app.db.session import engine
from src.agent.app.api.routes.file_routes import router as file_router
from src.agent.app.api.routes.auth_routes import router as auth_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(
    title="Chat-AI CRUD Agent",
    description="This is a chat bot CURD agent with JWT and HITL",
    version="0.1",
    lifespan=lifespan
)

@app.get("/")
def root():
    return {"message":"Chat AI CRUD Agent"}


@app.get("/health")
def health():
    return {"Status":"Healthy", "Message": "Agent working perfectly"}

app.include_router(file_router)
app.include_router(auth_router)