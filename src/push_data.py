import os
from sqlalchemy import create_engine, Column, String, Integer, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace 'postgresql://user:password@localhost:5432/database' with your actual PostgreSQL connection string
DATABASE_URI = os.getenv("DATABASE_URI")
engine = create_engine(DATABASE_URI)

Base = declarative_base()

# Define the table class
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    roll_number = Column(Integer)

# Create the table in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Insert two rows
student1 = Student(name="Rukhshan Ur Rehman", roll_number=3)
# student2 = Student(name="Hifzur Rahman", roll_number=2)

session.add_all([student1])
session.commit()

# Close the session
session.close()
