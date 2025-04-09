from fastapi import FastAPI
from app.routes import user, auth
from app.services.scraper import scraper

app = FastAPI(
    title="Vitibrasil Scraper API",
    description="API de scraping dos dados do site da Embrapa - Desenvolvido por Guilherme Jeronimo",
    version="1.0.0"
)

app.include_router(auth.router)
app.include_router(user.router)

@app.get("/")
def root():
    return {"message": "Vitibrasil API Online — by Guilherme Jeronimo"}
