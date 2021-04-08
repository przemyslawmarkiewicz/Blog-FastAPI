from pydantic import BaseModel
from typing import List


class BlogBase(BaseModel):
    title: str
    body: str


class Blog(BlogBase):
    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str
    email: str
    password: str


class User(UserBase):
    class Config:
        orm_mode = True


class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog]

    class Config:
        orm_mode = True


class ShowBlog(BaseModel):
    title: str
    body: str
    creator: User

    class Config:
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str
