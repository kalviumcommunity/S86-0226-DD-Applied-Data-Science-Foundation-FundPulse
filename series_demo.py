"""
series_demo.py - Demonstrate creating Pandas Series from lists and NumPy arrays

This script covers:
- importing pandas and numpy
- creating Series from Python lists
- creating Series from NumPy arrays
- inspecting the index and values attributes
- showing label-based vs positional access

Run with `python series_demo.py`.
"""

import pandas as pd
import numpy as np


def main():
    # Series from list
    fruits = ['apple', 'banana', 'cherry']
    s1 = pd.Series(fruits)
    print("Series from list:")
    print(s1)
    print("values:", s1.values)
    print("index:", s1.index)

    # Series from numpy array
    numbers = np.array([10, 20, 30])
    s2 = pd.Series(numbers)
    print("\nSeries from numpy array:")
    print(s2)
    print("dtype of values:", s2.dtype)

    # accessing elements
    print("\nAccess by position (iloc):", s1.iloc[1])
    print("Access by label (loc):", s1.loc[1])
    # default labels are same as positions; custom index example
    s3 = pd.Series([100, 200, 300], index=['a', 'b', 'c'])
    print("\nSeries with custom index:")
    print(s3)
    print("access by label 'b':", s3.loc['b'])

    print("\nDone with Series demonstration.")


if __name__ == "__main__":
    main()
