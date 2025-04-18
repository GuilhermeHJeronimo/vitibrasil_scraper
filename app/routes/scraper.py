from fastapi import APIRouter, Depends, HTTPException
from app.services.scraper.scraper import vitibrasil_scraper
from app.database import SessionLocal
from app.auth import get_current_user
from app.models import User

router = APIRouter()


@router.get("/scrape")
def scrape_data(table_name: str, current_user: User = Depends(get_current_user)):
    db = SessionLocal()
    try:
        vitibrasil_scraper.scrape_and_store(table_name, db)
        return {"message": f"Dados da tabela {table_name} foram armazenados com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()
