import os

DATABASE_URI = os.getenv("DATABASE_URI")
assert (
    DATABASE_URI
), "DATABASE_URI is missing, please export the DATABASE_URI in environment varaibles"
