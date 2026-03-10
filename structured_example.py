"""
structured_example.py - Demonstrate well-structured Python code

This script shows how to organize code for readability and reuse:

1. Imports and constants at the top
2. Helper functions grouped together and defined before use
3. A single `main()` function that orchestrates execution
4. Minimal code at top level (only the import block and the entry check)
5. Reuse of functions to avoid repetition

The example simply computes summary statistics on a sample dataset and
prints formatted results. It's contrived but illustrates structure.
"""

# imports
import math

# constants (all-caps with underscores)
DEFAULT_DATA = [3, 7, 1, 9, 4]


def compute_mean(numbers):
    """Return the average of a list of numbers."""
    return sum(numbers) / len(numbers) if numbers else 0


def compute_stddev(numbers):
    """Return the population standard deviation of the list."""
    if not numbers:
        return 0
    mean_val = compute_mean(numbers)
    variance = sum((x - mean_val) ** 2 for x in numbers) / len(numbers)
    return math.sqrt(variance)


def format_summary(numbers):
    """Build a formatted string containing statistics for the list."""
    mean_val = compute_mean(numbers)
    stddev_val = compute_stddev(numbers)
    return (
        f"count: {len(numbers)}\n"
        f"mean: {mean_val:.2f}\n"
        f"stddev: {stddev_val:.2f}"
    )


def main():
    # top-level execution logic is confined to main()
    data = DEFAULT_DATA  # could be replaced by data loading logic

    # many operations reuse helper functions instead of repeating code
    print("Data summary for default dataset:")
    print(format_summary(data))

    # show how easy it is to reuse with another list
    customized = [2, 2, 5, 10]
    print("\nData summary for customized list:")
    print(format_summary(customized))


if __name__ == "__main__":
    main()
