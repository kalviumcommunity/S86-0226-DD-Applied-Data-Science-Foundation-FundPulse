"""
broadcasting_demo.py - Demonstrate NumPy broadcasting with simple examples

This script illustrates:
- scalar-to-array broadcasting
- broadcasting between 1D arrays of compatible shapes
- broadcasting a 1D array across a 2D array (row-wise and column-wise)
- shape inspection and explanations of why each operation works

Run with `python broadcasting_demo.py`.
"""

import numpy as np


def main():
    # scalar broadcasting
    arr = np.array([1, 2, 3])
    print("Original array:", arr)
    print("add scalar 5:", arr + 5)
    print("multiply by scalar 2:", arr * 2)

    # broadcasting between 1D arrays
    a = np.array([1, 2, 3])
    b = np.array([10])  # shape (1,) can broadcast to (3,)
    print("\n1D broadcasting")
    print("a:", a, "shape", a.shape)
    print("b:", b, "shape", b.shape)
    print("a + b ->", a + b)

    # broadcasting with incompatible shapes
    c = np.array([1, 2])
    try:
        print(a + c)
    except ValueError as e:
        print("incompatible shapes error:", e)

    # 2D and 1D broadcasting
    two_d = np.array([[1, 2, 3], [4, 5, 6]])  # shape (2,3)
    row_vec = np.array([10, 20, 30])          # shape (3,)
    col_vec = np.array([[100], [200]])        # shape (2,1)

    print("\n2D array:\n", two_d, "shape", two_d.shape)
    print("row vector:", row_vec, "shape", row_vec.shape)
    print("col vector:\n", col_vec, "shape", col_vec.shape)

    print("two_d + row_vec ->\n", two_d + row_vec)
    print("two_d + col_vec ->\n", two_d + col_vec)

    print("\nDone with broadcasting demonstration.")


if __name__ == "__main__":
    main()
