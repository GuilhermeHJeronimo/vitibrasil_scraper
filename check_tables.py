import sqlite3

DB_PATH = "vitibrasil.db"

def list_tables_and_counts():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    for table in tables:
        name = table[0]
        cursor.execute(f"SELECT COUNT(*) FROM '{name}'")
        count = cursor.fetchone()[0]
        print(f"Tabela '{name}': {count} linhas")

    conn.close()

if __name__ == "__main__":
    list_tables_and_counts()
