# app/db/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

DATABASE_URL = "postgresql://postgres:priti%40123@localhost:5432/fastapidb"

# Check if DB exists, else create it
if not database_exists(DATABASE_URL):
    create_database(DATABASE_URL)
    print(" Database created:", DATABASE_URL)
else:
    print(" Database already exists")

# Create engine
engine = create_engine(DATABASE_URL)

# Session and Base
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# # Create DB if it doesn't exist
# if not database_exists(engine.url):
#     create_database(engine.url)

# Dependency to get DB session in routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()