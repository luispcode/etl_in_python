
#the base script with the three SQLAlchemy core components wich are engine, session and base.

# Import the modules required
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base

# Create the engine
engine = create_engine("postgresql+psycopg2://dcstudent:S3cretPassw0rd@localhost:5432/campdata-prod")

# Initialize the session
session = Session(engine)

# Initialize the declarative base
Base = declarative_base()