from typing import Callable

type Matrix = list[list[float]]

matrix_a: Matrix = [[1, 2, 3], [4, 5, 6]]
matrix_b: Matrix = [[1, 2], [3, 4], [5, 6]]


def shape(matrix: Matrix) -> tuple[int, int]:
    """Returns (# of rows, # of columns)"""
    num_rows = len(matrix)  # matrix A has 2 rows
    num_cols = len(matrix[0])  # matrix A has 3 columns
    return num_rows, num_cols


def get_row(matrix: Matrix, i: int) -> list[float]:
    """Returns the i-th row of matrix A (as a vector)"""
    return matrix[i]


def get_column(matrix: Matrix, j: int) -> list[float]:
    """Returns the j-th column of matrix A (as a vector)"""
    return [row[j] for row in matrix]


def make_matrix(
    num_rows: int, num_cols: int, entry_fn: Callable[[int, int], float]
) -> Matrix:
    """Returns a num_rows x num_cols matrix whose (i, j)-entry is entry_fn(i, j)"""
    return [[entry_fn(i, j) for j in range(num_cols)] for i in range(num_rows)]


def identity_matrix(n: int) -> Matrix:
    """Returns the n x n identity matrix"""
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)


assert shape([[1, 2, 3], [4, 5, 6]]) == (2, 3)
assert get_row([[1, 2, 3], [4, 5, 6]], 0) == [1, 2, 3]
assert get_column([[1, 2, 3], [4, 5, 6]], 0) == [1, 4]
assert make_matrix(2, 3, lambda i, j: i + j) == [[0, 1, 2], [1, 2, 3]]
assert identity_matrix(5) == [
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
]
