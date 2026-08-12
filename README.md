# Matrix Solver

A command-line tool that row-reduces a matrix step by step, showing each
elementary row operation as it happens, then reports it in **Row Echelon
Form (REF)** and **Reduced Row Echelon Form (RREF)**. Optionally interprets
the result as the solution to a system of linear equations.

## Features

- Converts any m×n matrix to REF, then RREF, printing the matrix after every
  row swap, scale, and elimination step
- Displays entries as exact fractions (via `Fraction.limit_denominator`)
  instead of floating-point noise
- Solves systems of linear equations: reports whether an augmented matrix
  has a unique solution, infinitely many solutions, or no solution
- Two ways to provide a matrix: type it in interactively, or load it from a
  text file with `--file`
- Input is validated — non-numeric entries, wrong row/column counts, and
  invalid dimensions are caught and re-prompted rather than crashing
- Covered by a pytest suite (identity, singular, dependent, and inconsistent
  systems, non-square matrices, file loading)

## Installation

```bash
git clone <this-repo-url>
cd MatrixSolver
python -m venv .venv
.venv\Scripts\activate      # Windows
# source .venv/bin/activate # macOS/Linux
pip install -r requirements.txt
```

## Usage

### Interactive mode

```bash
python main.py
```

```
Welcome to the Matrix Solver!
To start, how many rows will your matrix have?: 2
And how many columns will your matrix have?: 3
Enter 3 numbers separated by spaces: 1 1 3
Enter 3 numbers separated by spaces: 1 -1 1
```

### Load a matrix from a file

Create a text file with one row per line, values separated by whitespace:

```
1 1 3
1 -1 1
```

Then run:

```bash
python main.py --file sample_matrix.txt
```

### Sample run

Solving `x + y = 3`, `x - y = 1` (answer: `x = 2`, `y = 1`):

```
Welcome to the Matrix Solver!
Loaded matrix:
1 1 3
1 -1 1

Step 1: Converting to Row Echelon Form
1 1 3
0 -2 -2

1 1 3
0 1 1

Matrix successfully converted to Row Echelon Form
Step 2: Converting to Reduced Row Echelon Form
1 0 2
0 1 1

Matrix successfully converted to Reduced Row Echelon Form
Interpret the last column as constants in a system of equations? [y/N]: y
The system has exactly one solution.
```

## Running tests

```bash
pip install -r requirements-dev.txt
pytest
```

## Project structure

```
matrix.py         # Matrix class: storage, input parsing, file loading, pretty-printing
rowOperations.py  # Elementary row operations: swap, scale, add-multiple-of-row
algorithms.py     # REF/RREF conversion and solution interpretation
main.py           # CLI entry point
tests/            # pytest suite
```

## How it works

Row reduction is performed with the three elementary row operations
(`rowOperations.py`): swapping two rows, scaling a row, and adding a
multiple of one row to another. `convertToREF` sweeps left to right,
choosing a pivot in each column (preferring a row that's already ±1 to
avoid unnecessary fraction growth), then eliminates every entry below it.
`convertToRREF` then sweeps bottom to top, eliminating above each pivot to
finish the reduction. `interpretSolution` reads the resulting RREF of an
augmented matrix `[A|b]`: any all-zero coefficient row with a nonzero
constant means no solution; otherwise the rank of the coefficient matrix
determines whether the solution is unique or there are free variables.
