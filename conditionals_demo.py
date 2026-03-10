"""
conditionals_demo.py - Demonstrate conditional statements in Python

This script covers:
- basic if checks
- if/else branching
- multi-way logic using elif
- combining conditions using and, or, not
- printing results to observe which branch executes

Run with `python conditionals_demo.py` to view behavior.
"""


def main():
    x = 5
    print("Basic if statement")
    if x > 0:
        print(f"x is positive ({x})")
    if x < 0:
        print("this won't print because x is not negative")

    print("\nIf-else example")
    if x % 2 == 0:
        print(f"{x} is even")
    else:
        print(f"{x} is odd")

    print("\nIf-elif-else example")
    grade = 82
    if grade >= 90:
        print("A grade")
    elif grade >= 80:
        print("B grade")
    elif grade >= 70:
        print("C grade")
    else:
        print("Below C")

    print("\nLogical operators")
    a = 10
    b = 3
    if a > 5 and b > 5:
        print("both a and b are greater than 5")
    else:
        print("not both greater than 5")

    if a > 5 or b > 5:
        print("at least one of a or b is greater than 5")

    if not (b > 5):
        print("b is not greater than 5")

    # Edge-case example
    day = "Saturday"
    if day == "Saturday" or day == "Sunday":
        print(f"{day} is a weekend")
    else:
        print(f"{day} is a weekday")

    print("\nDone with conditional demonstrations.")


if __name__ == "__main__":
    main()
