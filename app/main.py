from fastapi import FastAPI, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from app.database import engine, SessionLocal
from app import models
from app.auth import get_password_hash, get_current_user
from app.models import User
from app.schemas import UserCreate, UserOut

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="VitiBrasil Scraper API",
    version="0.1.0",
    description="🚀 API para coletar e consultar dados da vitivinicultura brasileira via Embrapa."
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "VitiBrasil API Online"}

@app.post("/create-user", response_model=UserOut)
def create_user(
    user_data: UserCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    existing = db.query(User).filter(User.username == user_data.username).first()
    if existing:
        raise HTTPException(status_code=400, detail="Usuário já existe")

    hashed_password = get_password_hash(user_data.password)
    new_user = User(username=user_data.username, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
