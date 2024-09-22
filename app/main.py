from fastapi import FastAPI

from app.api import endpoints  
from app.db.session import engine
from app.db.models import Base

# Create the database tables if they don't exist
Base.metadata.create_all(bind=engine)

# Initialize application
app = FastAPI()

# Include the API router with all defined endpoints
app.include_router(endpoints.router)
