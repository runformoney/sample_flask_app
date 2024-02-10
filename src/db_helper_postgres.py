import os
from sqlalchemy import create_engine, MetaData, Table, select


def select_all_from_class_table():
    try:
        # Retrieve environment variables
        db_host = os.environ.get("POSTGRES_HOST")
        db_port = os.environ.get("POSTGRES_PORT", "5432")  # Default port is 5432
        db_name = os.environ.get("POSTGRES_DB")
        db_user = os.environ.get("POSTGRES_USER")
        db_password = os.environ.get("POSTGRES_PASSWORD")

        # Create an SQLAlchemy engine
        db_url = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
        engine = create_engine(db_url)

        # Define the "class" table
        metadata = MetaData()
        class_table = Table("class", metadata, autoload=True, autoload_with=engine)

        # Select all rows from the "class" table
        query = select([class_table])
        with engine.connect() as connection:
            result = connection.execute(query).fetchall()

        result_list = [dict(row) for row in result]
        res = {"data": result_list}
        return res

    except Exception as error:
        return f"Error retrieving data: {error}"
