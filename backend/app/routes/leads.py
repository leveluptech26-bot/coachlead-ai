from fastapi import APIRouter

router = APIRouter(prefix="/leads")

fake_leads = []

@router.get("/")
def get_leads():
    return fake_leads

@router.post("/")
def create_lead(lead: dict):
    fake_leads.append(lead)
    return {"status": "lead added"}
