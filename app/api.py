from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import auth, schemas
from app.database import get_db

router = APIRouter(prefix="/api", tags=["Auth"])

@router.post("/login", response_model=schemas.Token)
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    user_db = auth.authenticate_user(db, user.username, user.password)
    if not user_db:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    access_token = auth.create_access_token(data={"sub": user_db.username})
    return {"access_token": access_token, "token_type": "bearer"}
