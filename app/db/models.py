from sqlalchemy import Column, Integer, ARRAY
from app.db.session import Base

# Define the Solution model to store n-Queens problem solutions
class Solution(Base):
    __tablename__ = 'solutions' 

    id = Column(Integer, primary_key=True, autoincrement=True) 
    n = Column(Integer)
    order = Column(Integer)
    response = Column(ARRAY(Integer), nullable=False)
