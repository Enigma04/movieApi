from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    password: str


class Movie(BaseModel):
    title: str
    summary: str
    watched: bool
