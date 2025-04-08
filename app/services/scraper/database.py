from sqlalchemy import Table, Column, Integer, String, MetaData
from app.database import engine

metadata = MetaData()

def create_table(table_name: str):
    table = Table(
        table_name,
        metadata,
        Column("id", Integer, primary_key=True),
        Column("coluna1", String),
        Column("coluna2", String),
    )
    metadata.create_all(engine)
