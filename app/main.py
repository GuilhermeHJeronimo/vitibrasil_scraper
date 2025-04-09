from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session
from app.database import engine, SessionLocal
from app import models
from app.auth import get_password_hash
from app.models import User
from app.schemas import UserCreate


models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="VitiBrasil Scraper API",
    version="0.1.0"
)

# Função de dependência para obter sessão com o banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "VitiBrasil API Online"}

@app.get("/create-user")
def create_user(
    username: str = Query(..., description="Nome do usuário"),
    password: str = Query(..., description="Senha do usuário"),
    db: Session = Depends(get_db)
):
    user = User(username=username, hashed_password=get_password_hash(password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"message": f"Usuário '{username}' criado com sucesso ✅"}

@app.post("/create-user")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    ...
