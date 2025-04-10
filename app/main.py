from fastapi import FastAPI
from app.routes import auth, user, scraper

app = FastAPI(
    title="VitiBrasil Scraper API",
    version="1.0.0"
)

app.include_router(auth.router, tags=["Auth"])
app.include_router(user.router, tags=["Users"])
app.include_router(scraper.router, tags=["Scraper"])

@app.get("/")
def root():
    return {"message": "Vitibrasil API Online!"}
