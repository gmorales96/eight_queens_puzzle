from fastapi import HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field

from app.db import models
from app.db.session import get_db
from app.services.queens_problem import queens

router = APIRouter(
    prefix='/api'
)

class GenerateRequest(BaseModel):
    n: int = Field(..., gt=0, lt=12, description='An integer greater than 0 and less than 12')

# Endpoint to generate and store N-Queens solutions in the database
@router.post('/solutions/generate')
def generate_solutions(request: GenerateRequest, db: Session = Depends(get_db)):
    # Delete all previous solutions from the database
    db.query(models.Solution).delete()
    db.commit()
    
    # Generate new solutions
    solutions = queens(request.n)
    
    # Iterate over the solutions and store them in the database
    for id_counter, response in enumerate(solutions, start=1):
        solution = models.Solution(n=request.n, order=id_counter, response=response)
        db.add(solution)
    
    db.commit()
    
    return {'message': 'Solutions saved successfully'}

# Endpoint to retrieve a specific solution by its OrderID
@router.get('/solutions/{order}')
def get_solution_by_id(order: int, db: Session = Depends(get_db)):
    # Query the database for a solution with the given OrderID
    solution = db.query(models.Solution).filter(models.Solution.order == order).first()
    
    if solution is None:
        raise HTTPException(status_code=404, detail='Solution not found')
    
    return solution

# Endpoint to retrieve all solutions from the database
@router.get('/solutions')
def fetch_all_solutions(db: Session = Depends(get_db)):
    # Query the database for all solutions
    solutions = db.query(models.Solution).all()
    
    return solutions
