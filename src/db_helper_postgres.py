import os
from sqlalchemy import create_engine, Column, String, Integer, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import logging

logging.getLogger().setLevel(logging.INFO)


def get_all_students():
    DATABASE_URI = os.getenv("DATABASE_URI")
    logging.info("Connecting to DB")
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
    logging.info("Creating Session with DB")
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve all rows from the 'students' table
    all_students = session.query(Student).all()

    # Convert the list of Student objects to a list of dictionaries
    students_data = [
        {"id": student.id, "name": student.name, "roll_number": student.roll_number}
        for student in all_students
    ]

    # Close the session
    session.close()

    logging.info("Returning DB Data")
    return {"data": students_data}
