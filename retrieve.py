import psycopg2
import os

from dotenv import load_dotenv
from get_embedding import get_embedding


def retrieve(pdf_filename, chunking_method, embedding_model, query, k_value, threshold, table="chunks"):

    load_dotenv()
    connection = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_DB"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )

    cursor = connection.cursor()

    vector_str = str(get_embedding(query, embedding_model))

    select_query = f"""
    SELECT 
        *,  -- Select all columns
        1 - (embedding <=> '{vector_str}') AS similarity
    FROM {table}
    WHERE 
        filename = '{pdf_filename}' AND
        chunking_method = '{chunking_method}' AND
        embedding_model = '{embedding_model}' AND
        1 - (embedding <=> '{vector_str}') > {threshold}
    ORDER BY similarity DESC
    LIMIT {k_value};
    """
    cursor.execute(select_query)
    rows = cursor.fetchall()

    columns = [desc[0] for desc in cursor.description]

    results = [dict(zip(columns, row)) for row in rows]

    cursor.close()
    connection.close()

    return results


def main():
    print(retrieve(
        "data/fubon.pdf",
        "by_markdown|number_of_hash=4",
        "text-embedding-ada-002",
        "富邦銀行有哪些種類的存款",
        5,
        0
    ))

if __name__ == "__main__":
    main()

