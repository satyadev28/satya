from pydantic import BaseModel

class TodoCreate(BaseModel):
    title: str
    description: str = None

class TodoUpdate(BaseModel):
    title: str
    description: str = None
    completed: bool
