import os
from sqlalchemy import create_engine, MetaData, Table, select
import logging

logging.getLogger().setLevel(logging.INFO)


def select_all_from_class_table():
    try:
        # Retrieve environment variables
        db_host = os.environ.get("POSTGRES_HOST", "192.168.0.40")
        db_port = os.environ.get("POSTGRES_PORT", "5432")  # Default port is 5432
        db_name = os.environ.get("POSTGRES_DB", "school")
        db_user = os.environ.get("POSTGRES_USER", "postgres")
        db_password = os.environ.get("POSTGRES_PASSWORD", "welcome1")

        # Create an SQLAlchemy engine
        db_url = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
        engine = create_engine(db_url)
        logging.info(f"{engine}")

        # Define the "class" table
        metadata = MetaData()
        class_table = Table("class", metadata, autoload=True, autoload_with=engine)
        # class_table = Table("class", metadata)

        # Select all rows from the "class" table
        query = select([class_table])
        with engine.connect() as connection:
            result = connection.execute(query).fetchall()

        result_list = [dict(row) for row in result]
        res = {"data": result_list}
        return res

    except Exception as error:
        return f"Error retrieving data: {error}"
