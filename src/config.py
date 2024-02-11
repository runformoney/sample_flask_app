import os

DATABASE_NAME_SQLITE = os.getenv("DATABASE_NAME", "database.db")
DATABASE_IP_POSTGRES = os.getenv("POSTGRES_HOST", "192.168.0.40")
assert DATABASE_IP_POSTGRES, "Missing IP for Postgres"

DATABASE_PORT = os.getenv("POSTGRES_PORT", "5432")
assert DATABASE_PORT, "Missing PORT for Postgres"

DATABASE_DB = os.getenv("POSTGRES_DB", "school")
assert DATABASE_DB, "Missing DB for Postgres"

DATABASE_USER = os.getenv("POSTGRES_USER", "postgres")
assert DATABASE_USER, "Missing USER for Postgres"

DATABASE_PASSWORD = os.getenv("POSTGRES_PASSWORD", "welcome1")
assert DATABASE_PASSWORD, "Missing PASSWORD for Postgres"
