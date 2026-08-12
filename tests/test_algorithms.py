import numpy as np
import pytest

from algorithms import convertToREF, convertToRREF, interpretSolution
from matrix import Matrix


def reduce(rows):
    matrix = Matrix.fromRows(rows)
    convertToREF(matrix, verbose=False)
    convertToRREF(matrix, verbose=False)
    return matrix


def test_identity_matrix_is_unchanged():
    matrix = reduce([[1, 0], [0, 1]])
    assert np.allclose(matrix.values, [[1, 0], [0, 1]])


def test_unique_solution_system():
    # x + y = 3, x - y = 1  ->  x = 2, y = 1
    matrix = reduce([[1, 1, 3], [1, -1, 1]])
    assert np.allclose(matrix.values, [[1, 0, 2], [0, 1, 1]])
    assert interpretSolution(matrix) == "unique"


def test_requires_row_swap_to_find_pivot():
    # first column is zero in row 0, needs a swap to proceed
    matrix = reduce([[0, 2, 4], [1, 0, 1]])
    assert np.allclose(matrix.values, [[1, 0, 1], [0, 1, 2]])
    assert interpretSolution(matrix) == "unique"


def test_inconsistent_system_has_no_solution():
    # x + y = 3, 2x + 2y = 7 has no solution
    matrix = reduce([[1, 1, 3], [2, 2, 7]])
    assert interpretSolution(matrix) == "none"


def test_dependent_system_has_infinite_solutions():
    # second equation is a multiple of the first -> free variable
    matrix = reduce([[1, 1, 1, 3], [2, 2, 2, 6]])
    assert interpretSolution(matrix) == "infinite"


def test_non_square_matrix():
    matrix = reduce([[1, 2, 3], [4, 5, 6]])
    assert matrix.rows == 2 and matrix.cols == 3
    # should reach RREF without error; first two columns become pivots
    assert np.isclose(matrix.values[0, 0], 1)
    assert np.isclose(matrix.values[1, 1], 1)


def test_zero_matrix_stays_zero():
    matrix = reduce([[0, 0], [0, 0]])
    assert np.allclose(matrix.values, [[0, 0], [0, 0]])


def test_interpret_solution_requires_augmented_column():
    matrix = Matrix.fromRows([[1]])
    with pytest.raises(ValueError):
        interpretSolution(matrix)
