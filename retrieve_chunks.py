import psycopg2

def retrieve_chunks(search_vector, k_value):
    connection = psycopg2.connect(
        host="localhost",
        database="mydatabase",
        user="postgres",
        password="secret",
        port="5432"
    )

    cursor = connection.cursor()

    vector_str = str(search_vector)

    select_query = f"""
    SELECT chunk_id, text, page_range, line_range, filename, embedding
    FROM chunks
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
    retrieve_chunks([1, 2, 3], 5)

if __name__ == "__main__":
    main()

