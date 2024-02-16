import pytest

from algebra.matrix import matrix


@pytest.mark.parametrize(
    "shape,fill,expected",
    [
        ((2, 2), 1.0, [[1.0, 1.0], [1.0, 1.0]]),
        ((3, 2), 0.0, [[0.0, 0.0], [0.0, 0.0], [0.0, 0.0]]),
        ((2, 3), 0.0, [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]),
    ],
)
def test_matrix(shape, fill, expected):
    assert matrix(shape=shape, fill=fill) == expected


def test_docstrings():
    assert matrix.__doc__ is not None
