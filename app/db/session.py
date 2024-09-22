import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Create the SQLAlchemy engine using the database URL from environment variables
engine = create_engine(os.getenv('DATABASE_URL'))

Base = declarative_base()


Session = sessionmaker(bind=engine)

# Dependency that provides a database session
def get_db():
    db = Session()
    try:
        # Yield the session to the caller (API endpoint)
        yield db
    finally:
        db.close()
