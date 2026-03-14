from pydantic import BaseModel

class Lead(BaseModel):
    name: str
    email: str | None = None
    problem: str
