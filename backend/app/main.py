from fastapi import FastAPI

from app.db.base import Base
from app.db.session import engine
from app.api.routes.file_routes import router as file_router
from app.api.routes.auth_routes import router as auth_router

app = FastAPI(
    title="Chat-AI CRUD Agent",
    description = "This is a chat bot CURD agent with JWT and HITL",
    version = "0.1"
)

#auto creates table on start (replace later with "ALEMBIC")
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message":"Chat AI CRUD Agent"}


@app.get("/health")
def health():
    return {"Status":"Healthy", "Messsage": "Agent working perfectly"}

app.include_router(file_router)
app.include_router(auth_router)