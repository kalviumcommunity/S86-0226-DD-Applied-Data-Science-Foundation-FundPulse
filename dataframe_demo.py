"""
dataframe_demo.py - Demonstrate creating Pandas DataFrames from dictionaries and files

This script covers:
- creating a DataFrame from a Python dictionary
- writing a small CSV file in the repo and reading it back
- inspecting the DataFrame's columns, head, and shape
- basic dtype overview

Run with `python dataframe_demo.py`.
"""

import pandas as pd
import os


def main():
    # DataFrame from dictionary
    data = {
        'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 30, 35],
        'city': ['NY', 'LA', 'SF']
    }
    df1 = pd.DataFrame(data)
    print("DataFrame created from dictionary:")
    print(df1)
    print("columns:", df1.columns)
    print("shape:", df1.shape)

    # create a temporary CSV file
    csv_path = 'sample_data.csv'
    df1.to_csv(csv_path, index=False)
    print("\nWrote sample CSV to", csv_path)

    # read from CSV
    df2 = pd.read_csv(csv_path)
    print("\nDataFrame loaded from CSV:")
    print(df2.head())
    print("dtypes:\n", df2.dtypes)

    # cleanup file
    os.remove(csv_path)
    print("\nTemporary CSV file removed.")

    print("\nDone with DataFrame demonstration.")


if __name__ == "__main__":
    main()
