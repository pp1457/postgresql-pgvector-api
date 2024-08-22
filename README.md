# Setup PostgreSQL with pgvector
1. docker-compose up -d
2. docker exec -it pgvector-db psql -U postgres -d mydatabase (Enter DB)
3. CREATE EXTENSION vector;
4. setup .env in following format:
```
DB_HOST="10.1.160.76"
DB_DB="mydatabase"
DB_USER="postgres"
DB_PASSWORD="secret"
DB_PORT="5432"
```

5. python3 create_table.py


# Function Reference
### `create_table(vector_dimension, table)`
### `insert_chunk(chunk, table)`
### `retrieve_chunks(search_vector, k_value,  table)`
### `import_data_from_csv`
