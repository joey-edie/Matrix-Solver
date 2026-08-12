import numpy as np
from fractions import Fraction


class Matrix:
    """
    Sets initial mxn matrix as zeros to be initialized
    Parameters:
        rows - the number of rows (m) in the matrix
        cols - the number of cols (n) in the matrix
    """

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.values = np.zeros((self.rows, self.cols))

    @classmethod
    def fromRows(cls, rows):
        """
        Builds a Matrix from a list of lists of numbers.
        Parameters:
            rows - a non-empty list of equal-length lists of numbers
        """
        matrix = cls(len(rows), len(rows[0]))
        for i, row in enumerate(rows):
            matrix.values[i] = row
        return matrix

    @classmethod
    def fromFile(cls, path):
        """
        Builds a Matrix by reading whitespace-separated rows of numbers from a text file,
        one row per line.
        Parameters:
            path - path to the text file to read
        """
        with open(path) as f:
            rows = [[float(x) for x in line.split()] for line in f if line.strip()]

        if not rows:
            raise ValueError(f"{path} contains no matrix data")
        if any(len(row) != len(rows[0]) for row in rows):
            raise ValueError(f"{path} has rows of inconsistent length")

        return cls.fromRows(rows)

    def _parseRow(self, rawRow):
        """
        Parses a whitespace-separated line of numbers into a list of floats.
        Returns None if any token is not a valid number.
        """
        try:
            return [float(x) for x in rawRow.split()]
        except ValueError:
            return None

    def initialize(self):
        """
        Initializes the mxn matrix by asking for input from the user, one row at a time.
        Re-prompts on non-numeric input or a row with the wrong number of entries.
        """
        currentRow = 0
        while currentRow < self.rows:
            rawRow = input(f"Enter {self.cols} numbers separated by spaces: ")
            floatRow = self._parseRow(rawRow)

            if floatRow is None:
                print("ERROR! Please enter numbers only.")
                continue
            if len(floatRow) != self.cols:
                print(f"ERROR! Expected {self.cols} numbers, got {len(floatRow)}. Please try again.")
                continue

            self.values[currentRow] = floatRow
            currentRow += 1

        self.prettyPrint()

    def prettyPrint(self):
        cleaned = self.values.copy()

        # remove floating point noise
        cleaned[np.abs(cleaned) < 1e-10] = 0

        for row in cleaned:
            print(" ".join(str(Fraction(x).limit_denominator()) for x in row))

        print("")
