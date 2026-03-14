from fastapi import FastAPI
from app.routes import leads, outreach, bookings

app = FastAPI(title="CoachLead AI")

app.include_router(leads.router)
app.include_router(outreach.router)
app.include_router(bookings.router)

@app.get("/")
def root():
    return {"message": "CoachLead AI API running"}
