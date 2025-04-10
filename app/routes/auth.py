from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.auth import create_access_token, verify_password
from app.models import User
from app.database import get_db

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    token = create_access_token(data={"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}
