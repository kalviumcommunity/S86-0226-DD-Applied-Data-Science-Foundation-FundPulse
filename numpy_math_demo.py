"""
numpy_math_demo.py - Demonstrate basic arithmetic on NumPy arrays

This script covers element-wise operations, scalar ops, and comparison with
Python list behavior. It highlights how NumPy applies math efficiently to
whole arrays at once.

Run the script with `python numpy_math_demo.py`.
"""

import numpy as np


def main():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    print("array a:", a)
    print("array b:", b)

    # element-wise ops
    print("\na + b =", a + b)
    print("a - b =", a - b)
    print("a * b =", a * b)
    print("a / b =", a / b)

    # scalar operations
    print("\na + 10 =", a + 10)
    print("b * 2 =", b * 2)

    # list behavior
    pylist = [1, 2, 3]
    print("\npython list + list ->", pylist + pylist)
    print("python list * 2 ->", pylist * 2)

    # mixing shapes example
    try:
        print(a + np.array([1, 2]))
    except ValueError as e:
        print("shape error:", e)

    print("\nDone with NumPy math demonstration.")


if __name__ == "__main__":
    main()
