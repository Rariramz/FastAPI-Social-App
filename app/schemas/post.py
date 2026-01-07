from pydantic import BaseModel


class PostCreate(BaseModel):
    title: str
    content: str

class PostRead(BaseModel):
    title: str
    content: str