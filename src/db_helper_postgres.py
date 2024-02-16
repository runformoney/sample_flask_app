from sqlalchemy import create_engine, Column, String, Integer, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect
import os
import logging

logging.getLogger().setLevel(logging.INFO)

DATABASE_URI = os.getenv("DATABASE_URI")
engine = create_engine(DATABASE_URI)
Base = declarative_base()
Session = sessionmaker(bind=engine)


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    roll_number = Column(Integer)


def create_students_table():
    # Create the table in the database
    Base.metadata.create_all(engine)


def get_all_students():
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
    logging.info(f"{students_data}")
    return {"data": students_data}


def insert_user(name):
    session = Session()

    # Check if the table exists; if not, create it
    inspector = inspect(engine)
    if not inspector.has_table("students"):
        create_students_table()

    # Count the number of existing rows
    existing_rows_count = session.query(func.count(Student.id)).scalar()

    # Increment the count to get the new roll number
    new_roll_number = existing_rows_count + 1

    # Add logic to insert a new user into the database
    new_student = Student(name=name, roll_number=new_roll_number)
    session.add(new_student)
    session.commit()

    # Close the session
    session.close()

    return new_roll_number


from sqlalchemy.exc import SQLAlchemyError


def delete_user(roll_number):
    session = Session()
    roll_number = int(roll_number)

    try:
        # Retrieve the student with the given roll_number
        student_to_delete = (
            session.query(Student).filter_by(roll_number=roll_number).first()
        )

        if student_to_delete:
            # Delete the student
            session.delete(student_to_delete)
            session.commit()
            success_message = (
                f"User with Roll Number {roll_number} deleted successfully."
            )
        else:
            success_message = f"No user found with Roll Number {roll_number}."

    except SQLAlchemyError as e:
        # Handle exceptions, log errors, etc.
        print(f"Error deleting user: {e}")
        success_message = "Error deleting user."

    finally:
        # Close the session
        session.close()

    return success_message
