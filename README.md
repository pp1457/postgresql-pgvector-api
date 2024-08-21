# Setup PostgreSQL with pgvector
1. docker-compose up -d
2. docker exec -it pgvector-db psql -U postgres -d mydatabase (Enter DB)
3. CREATE EXTENSION vector;
4. python3 create_table.py
