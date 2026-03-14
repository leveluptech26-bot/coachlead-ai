from fastapi import APIRouter

router = APIRouter(prefix="/bookings")

@router.get("/")
def bookings():
    return {"bookings": []}
