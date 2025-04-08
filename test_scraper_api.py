import requests

BASE_URL = "http://127.0.0.1:8000/api/scrape"

tabelas = [
    "producao",
    "processamento_viniferas",
    "processamento_americanas_hibridas",
    "processamento_uvas_mesa",
    "processamento_uvas_sem_classificacao",
    "comercializacao",
    "importacao_vinhos_mesa",
    "importacao_espumantes",
    "importacao_uvas_frescas",
    "importacao_uvas_passas",
    "importacao_suco_uva",
    "exportacao_vinhos_mesa",
    "exportacao_espumantes",
    "exportacao_uvas_frescas",
    "exportacao_suco_uva"
]

for tabela in tabelas:
    response = requests.get(BASE_URL, params={"tabela": tabela})
    print(f"Tabela: {tabela}")
    print(f"Status: {response.status_code}")
    print(f"Resposta: {response.json()}")
    print("-" * 40)
