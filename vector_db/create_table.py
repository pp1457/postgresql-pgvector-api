import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def main(vector_dimension, table):

    connection = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_DB"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )

    cursor = connection.cursor()

    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {table} (
        chunk_pkey SERIAL PRIMARY KEY,
        filename TEXT NOT NULL,
        chunking_method TEXT NOT NULL,
        embedding_model TEXT NOT NULL,
        chunk_id INTEGER NOT NULL,
        page_range INT[2] NOT NULL,
        line_range INT[2] NOT NULL,
        text TEXT NOT NULL,
        embedding VECTOR({vector_dimension})
    );
    """
    cursor.execute(create_table_query)
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    main(1536, "chunks")
