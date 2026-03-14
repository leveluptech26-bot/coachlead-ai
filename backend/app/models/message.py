from pydantic import BaseModel

class Message(BaseModel):
    lead_id: int
    message: str
