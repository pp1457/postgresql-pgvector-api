import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def insert_chunk(chunk, table):

    connection = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_DB"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )

    cursor = connection.cursor()

    insert_query = f"""
    INSERT INTO {table} (filename, chunking_method, embedding_model, chunk_id, page_range, line_range, text, embedding)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
    """

    data_to_insert = (
        chunk['filename'],
        chunk['chunking_method'],
        chunk['embedding_model'],
        chunk['chunk_id'],
        f"{{{','.join(map(str, chunk['page_range']))}}}",
        f"{{{','.join(map(str, chunk['line_range']))}}}",
        chunk['text'],
        chunk['embedding']
    )

    cursor.execute(insert_query, data_to_insert)
    connection.commit()

    cursor.close()
    connection.close()

def main():
    for i in range(1, 6):
        chunk = {
            'chunk_id': i+10,
            'text': "Hi, I'm Paul",
            'page_range': (1, 2),
            'line_range': (1, 2),
            'filename': "data/paul.pdf",
            'embedding': [0.1 * i + 1, 0.2 * i, 0.3 * i - 1]
        }

        insert_chunk(chunk, "chunks")

if __name__ == "__main__":
    main()

