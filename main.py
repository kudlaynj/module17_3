from fastapi import FastAPI
from app.models import task, user

app = FastAPI()


@app.get("/")
async def main_():
    return {"message": "Welcome to Taskmanager"}


app.include_router(user.router)
app.include_router(task.router)
