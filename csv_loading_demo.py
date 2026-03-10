"""
csv_loading_demo.py - Demonstrate loading CSV data into Pandas DataFrames

This script writes a small CSV file, loads it with pandas, and inspects the
result. It also illustrates a common issue (missing header) by loading a file
that lacks column names.

Run with `python csv_loading_demo.py`.
"""

import pandas as pd
import os


def main():
    # create example CSV
    csv_path = 'demo.csv'
    with open(csv_path, 'w', newline='') as f:
        f.write('name,age,city\n')
        f.write('Alice,25,NY\n')
        f.write('Bob,30,LA\n')
        f.write('Charlie,35,SF\n')
    print(f"Wrote CSV file to {csv_path}")

    # load it normally
    df = pd.read_csv(csv_path)
    print("\nLoaded DataFrame:")
    print(df.head())
    print("columns:", df.columns)
    print("shape:", df.shape)

    # simulate missing header issue
    bad_csv = 'bad.csv'
    with open(bad_csv, 'w', newline='') as f:
        f.write('Alice,25,NY\n')
        f.write('Bob,30,LA\n')
    print(f"\nWrote poorly-formatted CSV to {bad_csv} (no header)")

    try:
        bad_df = pd.read_csv(bad_csv)
        print("\nResult of loading bad CSV:")
        print(bad_df.head())
    except Exception as e:
        print("Error loading bad CSV:", e)

    # show how to load with explicit header row
    bad_df2 = pd.read_csv(bad_csv, header=None)
    print("\nLoaded bad CSV with header=None (default numeric column names):")
    print(bad_df2.head())

    # cleanup
    os.remove(csv_path)
    os.remove(bad_csv)
    print("\nTemporary files removed.")

    print("\nDone with CSV loading demonstration.")


if __name__ == "__main__":
    main()
