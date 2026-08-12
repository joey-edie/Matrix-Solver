import argparse
from matrix import Matrix
from algorithms import convertToREF, convertToRREF, interpretSolution


def readPositiveInt(prompt):
    while True:
        raw = input(prompt)
        try:
            value = int(raw)
        except ValueError:
            print("ERROR! Please enter a whole number.")
            continue
        if value < 1:
            print("ERROR! Please enter a number greater than 0.")
            continue
        return value


def main():
    parser = argparse.ArgumentParser(
        description="Row-reduce a matrix to Row Echelon Form and Reduced Row Echelon Form."
    )
    parser.add_argument(
        "-f", "--file",
        help="path to a text file containing the matrix (whitespace-separated numbers, one row per line)"
    )
    args = parser.parse_args()

    print("Welcome to the Matrix Solver!")

    if args.file:
        matrix = Matrix.fromFile(args.file)
        print("Loaded matrix:")
        matrix.prettyPrint()
    else:
        rows = readPositiveInt("To start, how many rows will your matrix have?: ")
        cols = readPositiveInt("And how many columns will your matrix have?: ")
        matrix = Matrix(rows, cols)
        matrix.initialize()

    print("Step 1: Converting to Row Echelon Form")
    convertToREF(matrix)

    print("Step 2: Converting to Reduced Row Echelon Form")
    convertToRREF(matrix)

    if matrix.cols >= 2:
        answer = input("Interpret the last column as constants in a system of equations? [y/N]: ").strip().lower()
        if answer == "y":
            result = interpretSolution(matrix)
            if result == "none":
                print("The system has no solution (inconsistent).")
            elif result == "unique":
                print("The system has exactly one solution.")
            else:
                print("The system has infinitely many solutions (free variable(s) present).")


if __name__ == "__main__":
    main()
