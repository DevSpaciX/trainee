import json

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.utils import get_db
from db.models import User

app = FastAPI()


@app.get("/login")
async def get_user(
    login: str,
    password: str,
        db: Session = Depends(get_db)
):
    if db.query(User).filter(User.login == login,User.password == password).first():
        return {"message": "Welcome"}
    return {"message": "User not exist"}


@app.get("/get_line_info")
async def get_info():
    try:
        with open("templates/study_template.json", "r") as json_file:
            data = json.load(json_file)
            return data
    except FileNotFoundError:
        return {"error": "JSON file not found"}
    except json.JSONDecodeError:
        return {"error": "Invalid JSON format in the file"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
