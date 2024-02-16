import pytest

from algebra.matrix import submatrix


@pytest.mark.parametrize(
    "matrix,drop_rows,drop_columns,expected",
    [
        ([[1, 2, 3], [1, 2, 3]], [], [0], [[2, 3], [2, 3]]),
        ([[1, 2, 3], [1, 2, 3]], [0], [0], [[2, 3]]),
        ([[1, 2, 3], [1, 2, 3]], [0], [0, 1], [[3]]),
        ([[1, 2, 3], [1, 2, 3]], [0], [0, 1, 2], []),
    ],
)
def test_submatrix(matrix, drop_rows, drop_columns, expected):
    assert (
        submatrix(matrix=matrix, drop_rows=drop_rows, drop_columns=drop_columns)
        == expected
    )


def test_submatrix_without_args():
    assert id(submatrix(matrix=[[1, 2, 3], [1, 2, 3]])) != id(
        submatrix(matrix=[[1, 2, 3], [1, 2, 3]])
    )


def test_docstrings():
    assert submatrix.__doc__ is not None
