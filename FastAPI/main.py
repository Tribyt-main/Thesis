from fastapi import FastAPI
from FastAPI.routers import task, user
from FastAPI.backend.db import engine
from app.backend.db import Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get('/')
async def welcome() -> dict:
    return {'message': 'Welcome Taskmanager'}


app.include_router(task.router)
app.include_router(user.router)
