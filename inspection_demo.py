"""
inspection_demo.py - Demonstrate inspecting Pandas DataFrames with head(), info(), describe()

This script creates a small DataFrame (via CSV) and then calls the three
inspection methods.  It's meant to be run after the earlier csv_loading_demo,
but is standalone for this milestone.

Run with `python inspection_demo.py`.
"""

import pandas as pd
import os


def main():
    # prepare a sample CSV to load
    path = 'inspection.csv'
    with open(path, 'w', newline='') as f:
        f.write('name,age,score\n')
        f.write('Alice,25,88.5\n')
        f.write('Bob,30,92.0\n')
        f.write('Charlie,35,79.3\n')
        f.write('Dana,,85.0\n')  # missing age to show non-null counts

    df = pd.read_csv(path)
    print("DataFrame loaded for inspection:")
    print(df)

    print("\nUse head() to preview first rows:")
    print(df.head())

    print("\nUse info() to view structure and non-null counts:")
    df.info()

    print("\nUse describe() to summarize numeric columns:")
    print(df.describe())

    os.remove(path)
    print("\nTemporary CSV removed; inspection complete.")


if __name__ == "__main__":
    main()
