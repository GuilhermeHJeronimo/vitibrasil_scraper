from app.services.scraper.database import create_table
from app.services.scraper.scraper import scrape_table
from app.services.scraper.urls import URL_TABLE_MAP
from app.database import engine
from app import models

# Cria tabelas do SQLAlchemy (ex: users)
models.Base.metadata.create_all(bind=engine)

def run_all():
    for url, table_name in URL_TABLE_MAP.items():
        print(f"🚀 Criando e populando tabela: {table_name}")
        create_table(table_name)
        scrape_table(url)
        print(f"✅ Tabela '{table_name}' concluída.\n")

if __name__ == "__main__":
    run_all()
    print("✅ Todas as tabelas foram criadas com sucesso!")
