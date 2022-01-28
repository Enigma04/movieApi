from pydantic import BaseModel


class Movies(BaseModel):
    title: str
    summary: str
    watched: bool


class User(BaseModel):
    name: str
    email: str
    password: str
