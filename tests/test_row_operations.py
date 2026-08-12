import numpy as np

from rowOperations import addMultipleOfRow, scaleRow, swapRows


def test_swap_rows():
    values = np.array([[1.0, 2.0], [3.0, 4.0]])
    swapRows(values, 0, 1)
    assert np.array_equal(values, [[3.0, 4.0], [1.0, 2.0]])


def test_scale_row():
    values = np.array([[1.0, 2.0], [3.0, 4.0]])
    scaleRow(values, 0, 2)
    assert np.array_equal(values, [[2.0, 4.0], [3.0, 4.0]])


def test_add_multiple_of_row():
    values = np.array([[1.0, 2.0], [3.0, 4.0]])
    addMultipleOfRow(values, 0, 1, -3)
    assert np.array_equal(values, [[1.0, 2.0], [0.0, -2.0]])
