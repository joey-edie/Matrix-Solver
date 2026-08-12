import numpy as np
from rowOperations import swapRows, scaleRow, addMultipleOfRow

"""
Converts an mxn matrix to Row Echelon Form
Parameters:
matrix - the mxn matrix to convert
verbose - if True, prints the matrix after each row operation
"""

def convertToREF(matrix, verbose=True):

    pivotRow = 0 # to keep track of the pivot row last created, since every pivot in sequential columns must be lower than the last

    for pivotCol in range(matrix.cols):

        if pivotRow == matrix.rows: # signals the end of the loop
            break

        # variables to check if we have found certain entries, a 1, nonzero entries, and where the pivot will end up being
        nonzeroFound = False
        firstNonZero = -1 # that is not 1
        toBePivotRow = -1

        # check if there are any 1s or nonzero values at all
        for num in range(pivotRow, matrix.rows):
            currentNum = matrix.values[num, pivotCol]
            if np.isclose(currentNum, 1) or np.isclose(currentNum, -1):
                nonzeroFound = True
                toBePivotRow = num # if this is the same as the current pivot row then nothing will happen
                break
            elif not np.isclose(currentNum, 0) and firstNonZero == -1:
                nonzeroFound = True
                firstNonZero = num

        if not nonzeroFound: # if no nonzero entries found, move to next column
            continue

        if toBePivotRow == -1:
            toBePivotRow = firstNonZero

        # swap rows if they are not already
        if toBePivotRow != pivotRow:
            swapRows(matrix.values, toBePivotRow, pivotRow)
            if verbose:
                matrix.prettyPrint()

        # make pivot 1
        if not np.isclose(matrix.values[pivotRow, pivotCol], 1):
            scale = 1 / matrix.values[pivotRow, pivotCol]
            scaleRow(matrix.values, pivotRow, scale)
            if verbose:
                matrix.prettyPrint()

        # eliminate entries below pivotRow
        for rowNum in range(pivotRow + 1, matrix.rows):
            if not np.isclose(matrix.values[rowNum, pivotCol], 0):
                addMultipleOfRow(matrix.values, pivotRow, rowNum, -matrix.values[rowNum, pivotCol])
                if verbose:
                    matrix.prettyPrint()

        pivotRow += 1 # increment after successful pivot

    if verbose:
        print("Matrix successfully converted to Row Echelon Form")


"""
Converts an mxn matrix already in Row Echelon Form to Reduced Row Echelon Form
Parameters:
matrix - the mxn matrix to convert
verbose - if True, prints the matrix after each row operation
"""

def convertToRREF(matrix, verbose=True):

    for pivotRow in range(matrix.rows - 1, -1, -1):

        # Find the pivot in this row
        pivotCol = None
        for col in range(matrix.cols):
            if np.isclose(matrix.values[pivotRow, col], 1):
                pivotCol = col
                break

        if pivotCol is None:
            continue        # zero row

        # Eliminate above the pivot
        for row in range(pivotRow):
            if not np.isclose(matrix.values[row, pivotCol], 0):
                addMultipleOfRow(matrix.values, pivotRow, row, -matrix.values[row, pivotCol])
                if verbose:
                    matrix.prettyPrint()

    if verbose:
        print("Matrix successfully converted to Reduced Row Echelon Form")


"""
Interprets the RREF of an augmented matrix [A|b] (last column holds the constants)
as a system of linear equations.
Parameters:
matrix - the mxn matrix, already in RREF, where the last column is the constants column
Returns:
"none" if the system is inconsistent, "unique" if there is exactly one solution,
or "infinite" if there are free variables
"""

def interpretSolution(matrix):
    numVars = matrix.cols - 1
    if numVars < 1:
        raise ValueError("matrix needs at least one variable column and one constant column")

    rank = 0
    for row in matrix.values:
        coeffs = row[:numVars]
        constant = row[numVars]
        if np.allclose(coeffs, 0):
            if not np.isclose(constant, 0):
                return "none"
            continue
        rank += 1

    return "unique" if rank == numVars else "infinite"
