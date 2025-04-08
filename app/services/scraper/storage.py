import os
import pandas as pd
import sqlite3
from app.services.scraper.config import DB_PATH, DATA_DIR

def save_data(table_name: str, data: list):
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    df = pd.DataFrame(data, columns=["categoria", "quantidade"])

    conn = sqlite3.connect(DB_PATH)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()
