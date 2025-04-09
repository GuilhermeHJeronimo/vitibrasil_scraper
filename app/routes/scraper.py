
from fastapi import APIRouter, Depends, HTTPException
from app.services.scraper import run_scraper
from app.auth import get_current_user

router = APIRouter()

@router.post("/scrape", tags=["Scraper"])
def start_scraping(current_user: str = Depends(get_current_user)):
    try:
        data = run_scraper()
        return {"message": "Scraping concluído com sucesso!", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
