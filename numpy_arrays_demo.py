"""
numpy_arrays_demo.py - Demonstrate basic NumPy array creation and operations

This script shows:
- importing NumPy
- converting Python lists (1D and 2D) to arrays
- inspecting array dtype and shape
- performing simple element-wise operations
- contrasting list behavior with array behavior

Run the script with `python numpy_arrays_demo.py`.
"""

import numpy as np


def main():
    # 1D array from list
    python_list = [1, 2, 3, 4]
    arr1 = np.array(python_list)
    print("1D array:", arr1)
    print("dtype:", arr1.dtype, "shape:", arr1.shape)

    # 2D array from nested lists
    nested = [[1, 2], [3, 4], [5, 6]]
    arr2 = np.array(nested)
    print("\n2D array:\n", arr2)
    print("dtype:", arr2.dtype, "shape:", arr2.shape)

    # basic operations
    print("\narr1 + 5 =", arr1 + 5)
    print("arr1 * 2 =", arr1 * 2)

    # element-wise vs list multiplication
    print("\nlist * 2 gives repetition:", python_list * 2)
    print("array * 2 gives element-wise scaling:", arr1 * 2)

    # broadcasting example
    print("\narr1 + arr1:", arr1 + arr1)

    # inspecting properties again
    print("\narr2 dimensions:", arr2.ndim)

    print("Done with NumPy array demonstration.")


if __name__ == "__main__":
    main()
