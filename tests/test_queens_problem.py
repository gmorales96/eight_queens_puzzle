import pytest
from app.services.queens_problem import queens

def test_n_queens_solutions():
    # Test cases with known solutions for some values ​​of N
    assert len(queens(1)) == 1
    assert len(queens(2)) == 0
    assert len(queens(3)) == 0
    assert len(queens(4)) == 2
    assert len(queens(5)) == 10
    assert len(queens(6)) == 4
    assert len(queens(7)) == 40
    assert len(queens(8)) == 92
    assert len(queens(9)) == 352
    assert len(queens(10)) == 724
    assert len(queens(11)) == 2680
