from sqlalchemy import create_engine, Column, String, Integer, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import logging

logging.getLogger().setLevel(logging.INFO)


def get_all_students():
    # Replace 'postgresql://user:password@localhost:5432/database' with your actual PostgreSQL connection string
    DATABASE_URI = os.getenv("DATABASE_URI")
    engine = create_engine(DATABASE_URI)

    Base = declarative_base()

    # Define the table class
    class Student(Base):
        __tablename__ = "students"

        id = Column(Integer, primary_key=True)
        name = Column(String)
        roll_number = Column(Integer)

    # Create the table in the database
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve all rows from the 'students' table
    all_students = session.query(Student).all()

    # Close the session
    session.close()
    resp = {"data": all_students}
    return resp
