import os
from pathlib import Path
BASE_DIR=Path(__file__).resolve().parent
class Config:
    SECRET_KEY=os.getenv("SECRET_KEY","dev-secret-change-me")
    SQLALCHEMY_DATABASE_URI=os.getenv("DATABASE_URL",f"sqlite:///{BASE_DIR/'pharmacy.db'}")
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    EXPIRY_WARNING_DAYS=int(os.getenv("EXPIRY_WARNING_DAYS","30"))
    DEFAULT_LOCALE=os.getenv("DEFAULT_LOCALE","en")
    AI_ENABLED=os.getenv("AI_ENABLED","true").lower()=="true"
    AI_PROVIDER=os.getenv("AI_PROVIDER","local")
    AI_MODEL=os.getenv("AI_MODEL","rules-and-analytics")
    AI_API_KEY=os.getenv("AI_API_KEY","")
    AI_BASE_URL=os.getenv("AI_BASE_URL","")
    AI_TIMEOUT=int(os.getenv("AI_TIMEOUT","20"))
class TestingConfig(Config):
    TESTING=True
    SECRET_KEY="test-secret"
    SQLALCHEMY_DATABASE_URI="sqlite:///:memory:"
