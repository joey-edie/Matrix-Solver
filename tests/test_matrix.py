import numpy as np
import pytest

from matrix import Matrix


def test_from_rows_builds_correct_shape_and_values():
    matrix = Matrix.fromRows([[1, 2, 3], [4, 5, 6]])
    assert (matrix.rows, matrix.cols) == (2, 3)
    assert np.array_equal(matrix.values, [[1, 2, 3], [4, 5, 6]])


def test_from_file_reads_matrix(tmp_path):
    path = tmp_path / "matrix.txt"
    path.write_text("1 2 3\n4  5   6\n")

    matrix = Matrix.fromFile(path)
    assert np.array_equal(matrix.values, [[1, 2, 3], [4, 5, 6]])


def test_from_file_rejects_ragged_rows(tmp_path):
    path = tmp_path / "matrix.txt"
    path.write_text("1 2 3\n4 5\n")

    with pytest.raises(ValueError):
        Matrix.fromFile(path)


def test_from_file_rejects_empty_file(tmp_path):
    path = tmp_path / "matrix.txt"
    path.write_text("")

    with pytest.raises(ValueError):
        Matrix.fromFile(path)


def test_parse_row_accepts_extra_whitespace():
    matrix = Matrix(1, 3)
    assert matrix._parseRow("1   2\t3") == [1.0, 2.0, 3.0]


def test_parse_row_rejects_non_numeric_tokens():
    matrix = Matrix(1, 3)
    assert matrix._parseRow("1 abc 3") is None
