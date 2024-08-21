import psycopg2

def insert_chunk(chunk):
    connection = psycopg2.connect(
        host="localhost",
        database="mydatabase",
        user="postgres",
        password="secret",
        port="5432"
    )

    cursor = connection.cursor()

    insert_query = """
    INSERT INTO chunks (chunk_id, text, page_range, line_range, filename, embedding)
    VALUES (%s, %s, %s, %s, %s, %s);
    """

    data_to_insert = (
        chunk['chunk_id'],
        chunk['text'],
        f"{{{','.join(map(str, chunk['page_range']))}}}",
        f"{{{','.join(map(str, chunk['line_range']))}}}",
        chunk['filename'],
        chunk['embedding']
    )

    cursor.execute(insert_query, data_to_insert)
    connection.commit()

    cursor.close()
    connection.close()

def main():
    for i in range(1, 6):
        chunk = {
            'chunk_id': i,
            'text': "Hi, I'm Paul",
            'page_range': (1, 2),
            'line_range': (1, 2),
            'filename': "data/paul.pdf",
            'embedding': [0.1 * i + 1, 0.2 * i, 0.3 * i - 1]
        }

        insert_data(chunk)

if __name__ == "__main__":
    main()

