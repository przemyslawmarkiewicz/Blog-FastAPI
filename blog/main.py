from typing import List
from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import schemas, models
from .database import engine, get_db
from .routers import blog, user, authentication

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
