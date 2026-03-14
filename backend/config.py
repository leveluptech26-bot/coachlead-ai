import os

class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:password@db:5432/coachlead")

settings = Settings()
