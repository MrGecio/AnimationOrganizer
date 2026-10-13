
from fastapi import FastAPI

from database.database import engine, Base

from model.user import User
from backend.model.rol import Role


Base.metadata.create_all(bind=engine)

app = FastAPI()

