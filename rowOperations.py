import numpy as np

"""
Swaps r1 with r2 in the matrix
Parameters:
    matrix - the values array to execute the operation on
    r1 - the row of the matrix to switch to r2
    r2 - the row of the matrix to switch to r1
"""
def swapRows(matrix: np.ndarray, r1: int, r2: int):
    matrix[[r1, r2]] = matrix[[r2, r1]]

"""
Scales row by scale in matrix
Parameters:
    matrix - the values array to execute the operation on
    row - the row to be scaled
    scale - the scale factor
"""
def scaleRow(matrix: np.ndarray, row: int, scale: float):
    matrix[row] *= scale

"""
Adds a multiple of r1 to r2 and puts result in r2
Parameters:
    matrix - the values array to execute the operation on
    r1 - the row to be scaled and added to r2
    r2 - the row to recieve the addition from the multiple of r1
    scalar - the amount to multiply r1 by before adding to r2
"""
def addMultipleOfRow(matrix: np.ndarray, r1: int, r2: int, scalar: float):
    matrix[r2] += matrix[r1] * scalar
