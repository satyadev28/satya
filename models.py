from pydantic import BaseModel

class TodoItem(BaseModel):
    id: str
    title: str
    description: str = None
    completed: bool = False
