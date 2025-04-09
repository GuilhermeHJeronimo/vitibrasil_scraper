# app/services/scraper/scraper.py

import requests
from bs4 import BeautifulSoup
from app.services.scraper.urls import URL_TABLE_MAP
from app.services.scraper.database import insert_data

def scrape_table(table_name: str):
    url = next((u for u, name in URL_TABLE_MAP.items() if name == table_name), None)
    if not url:
        raise ValueError(f"URL para tabela '{table_name}' não encontrada.")

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find("table", class_="tb_base tb_dados")
    if not table:
        raise Exception("Tabela com classe 'tb_base tb_dados' não encontrada.")

    rows = table.find_all("tr")
    data = []

    for row in rows:
        cols = row.find_all("td")
        if len(cols) == 2:
            categoria = cols[0].text.strip()
            quantidade = cols[1].text.strip().replace(".", "").replace("-", "0")
            data.append((categoria, "", int(quantidade) if quantidade.isdigit() else 0))
        elif len(cols) == 3:
            categoria = cols[0].text.strip()
            subcategoria = cols[1].text.strip()
            quantidade = cols[2].text.strip().replace(".", "").replace("-", "0")
            data.append((categoria, subcategoria, int(quantidade) if quantidade.isdigit() else 0))

    insert_data(table_name, data)
    return {"mensagem": f"Tabela '{table_name}' raspada com sucesso com {len(data)} registros."}
