import psycopg2

def retrieve_chunks(search_vector, k_value, table):

    connection = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_DB"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )

    cursor = connection.cursor()

    vector_str = str(search_vector)

    select_query = f"""
    SELECT chunk_id, text, page_range, line_range, filename, embedding
    FROM {table}
    ORDER BY embedding <=> '{vector_str}'
    LIMIT {k_value};
    """

    cursor.execute(select_query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    connection.close()

def main():
    retrieve_chunks([1, 2, 3], 5, "chunks")

if __name__ == "__main__":
    main()

