"""
array_shape_demo.py - Demonstrate array shape, dimensions, and indexing in NumPy

This script covers:
- inspecting shape and ndim of 1D and 2D arrays
- accessing individual elements using zero-based indices
- visualizing layout via print statements and comments
- showing row/column indexing for 2D arrays

Run with `python array_shape_demo.py` to explore behavior.
"""

import numpy as np


def main():
    # 1D array example
    one_d = np.array([10, 20, 30, 40])
    print("1D array:", one_d)
    print("shape:", one_d.shape)
    print("ndim:", one_d.ndim)
    # access elements by index
    print("first element (index 0):", one_d[0])
    print("last element (index 3):", one_d[3])
    # beware of out-of-range
    try:
        print(one_d[4])
    except IndexError as e:
        print("access error:", e)

    # 2D array example
    two_d = np.array([[1, 2, 3], [4, 5, 6]])
    print("\n2D array:\n", two_d)
    print("shape:", two_d.shape, "(rows, columns)")
    print("ndim:", two_d.ndim)
    # access by [row, col]
    print("element at row0,col0:", two_d[0, 0])
    print("element at row1,col2:", two_d[1, 2])
    # row slicing yields 1D
    print("first row:", two_d[0])
    # column access using :,
    print("second column:", two_d[:, 1])

    # demonstration of layout: rows are outer list items
    # indexing rule: two_d[row_index, column_index]

    print("\nDone with array shape and indexing demonstration.")


if __name__ == "__main__":
    main()
