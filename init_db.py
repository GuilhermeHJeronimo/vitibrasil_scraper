from app.database import engine
from app import models
from app.services.scraper.scraper import scrape_table
from app.services.scraper.urls import URL_TABLE_MAP
from app.services.scraper.database import create_table

models.Base.metadata.create_all(bind=engine)

def run_all():
    for url, table_name in URL_TABLE_MAP.items():
        print(f"Criando e populando: {table_name}")
        create_table(table_name)
        scrape_table(table_name)
        print(f"Tabela '{table_name}' completa.\n")

if __name__ == "__main__":
    run_all()
