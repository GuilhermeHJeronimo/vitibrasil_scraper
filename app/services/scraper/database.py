
import sqlite3

def connect_db():
    return sqlite3.connect("vitibrasil.db")

def create_table(table_name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS '{table_name}' (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            categoria TEXT,
            subcategoria TEXT,
            quantidade INTEGER
        );
    """)
    conn.commit()
    conn.close()

def insert_data(table_name, data):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.executemany(
        f"INSERT INTO '{table_name}' (categoria, subcategoria, quantidade) VALUES (?, ?, ?)", data
    )
    conn.commit()
    conn.close()
