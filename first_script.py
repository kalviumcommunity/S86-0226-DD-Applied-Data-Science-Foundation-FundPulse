"""
first_script.py - A simple standalone Python script for data analysis

This file demonstrates basic scripting concepts:
- defining variables and simple calculations
- working with a small sample dataset
- printing results to the console
- executing from top to bottom like a normal Python program

Run it from the terminal with `python first_script.py` or via the editor's run button.
"""


def main():
    # sample dataset: simple list of numbers
    sample_data = [5, 10, 15, 20, 25]

    # basic calculations
    total = sum(sample_data)
    mean = total / len(sample_data)

    print("Sample data:", sample_data)
    print(f"Total: {total}")
    print(f"Mean: {mean}")

    # a simple transformation
    squared = [x ** 2 for x in sample_data]
    print("Squared values:", squared)

    # additional logic to show script flow
    print("Done with basic statistics.")


if __name__ == "__main__":
    main()
