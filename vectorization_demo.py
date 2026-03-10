"""
vectorization_demo.py - Compare loop-based operations with vectorized NumPy code

This script shows:
- a simple loop that adds 5 to each element of a NumPy array
- the equivalent vectorized expression without an explicit loop
- element-wise comparisons vectorized vs loop
- explanation comments and printouts demonstrating output equivalence

Run the script with `python vectorization_demo.py`.
"""

import numpy as np


def add_five_loop(arr):
    # loop-based approach: creates a new list using Python iteration
    result = []
    for x in arr:
        result.append(x + 5)
    return np.array(result)


def add_five_vectorized(arr):
    # vectorized: adds 5 to every element at once
    return arr + 5


def comparison_loop(arr):
    # manual comparison generating boolean list
    result = []
    for x in arr:
        result.append(x > 2)
    return np.array(result)


def comparison_vectorized(arr):
    # element-wise comparison, returns boolean array
    return arr > 2


def main():
    data = np.array([1, 2, 3, 4, 5])

    print("Original array:", data)

    loop_result = add_five_loop(data)
    vec_result = add_five_vectorized(data)
    print("\nLoop result:", loop_result)
    print("Vectorized result:", vec_result)

    # they should be equal
    print("Equal?", np.array_equal(loop_result, vec_result))

    # comparisons
    print("\nComparison with loop:", comparison_loop(data))
    print("Comparison vectorized:", comparison_vectorized(data))

    # note readability difference
    print("\nVectorized code is shorter and avoids explicit iteration.")
    print("Loops are easy to write but slower on large datasets.")

    print("\nDone with vectorization demonstration.")


if __name__ == "__main__":
    main()
