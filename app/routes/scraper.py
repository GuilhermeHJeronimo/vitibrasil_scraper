from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth import get_current_user
from app.services.scraper.scraper import scrape_table

router = APIRouter(prefix="/api", tags=["Scraper"])

@router.get("/scrape")
def scrape(
    table_name: str = Query(..., description="Nome da tabela para scraping"),
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    try:
        result = scrape_table(table_name, db)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
