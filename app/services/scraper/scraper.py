from app.services.scraper.urls import URL_TABLE_MAP

def scrape_table(url: str):
    table_name = URL_TABLE_MAP.get(url)
    if not table_name:
        raise ValueError(f"Tabela não encontrada para a URL '{url}'")

    print(f"📦 Simulando scraping da URL: {url} → Tabela: {table_name}")
    # Aqui viria o scraping real com requests/BeautifulSoup
