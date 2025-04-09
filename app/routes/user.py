# app/routes/user.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User
from app.schemas import UserCreate, UserOut
from app.auth import get_password_hash
from app.dependencies import get_current_user

router = APIRouter()

@router.post("/create-user", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Usuário já existe.")
    
    hashed_password = get_password_hash(user.password)
    new_user = User(username=user.username, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/users", response_model=list[UserOut])
def list_users(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(User).all()

@router.delete("/delete-user/{username}")
def delete_user(username: str, db: Session = Depends(get_db), user=Depends(get_current_user)):
    user_to_delete = db.query(User).filter(User.username == username).first()
    if not user_to_delete:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    db.delete(user_to_delete)
    db.commit()
    return {"detail": f"Usuário '{username}' deletado com sucesso."}
