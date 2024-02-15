from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

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


# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Delete all rows from the "students" table
session.query(Student).delete()

# Commit the changes
session.commit()

# Close the session
session.close()
