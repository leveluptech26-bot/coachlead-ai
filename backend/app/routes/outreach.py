from fastapi import APIRouter
from app.services.ai_writer import generate_outreach

router = APIRouter(prefix="/outreach")

@router.post("/")
def create_outreach(data: dict):

    message = generate_outreach(
        name=data["name"],
        problem=data["problem"]
    )

    return {"message": message}
