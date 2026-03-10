"""
readability_demo.py - Examples of readable variable names and comments

This script contrasts poor and good naming styles and shows where comments
add value. It's not meant to perform meaningful computation, but to illustrate
PEP 8 conventions and commentary guidelines.

Run with `python readability_demo.py` to see the demonstration output.
"""


def poor_naming_example():
    # hard to understand: what are a, b, c?
    a = 5
    b = 10
    c = a + b
    print("Result of poor naming:", c)


def good_naming_example():
    # variable names clearly describe their purpose
    number_of_apples = 5
    number_of_oranges = 10
    total_fruit = number_of_apples + number_of_oranges
    print("Total fruit count:", total_fruit)


def comment_usefulness_example():
    # compute factorial iteratively; comment explains the *why*
    # (avoids recursion due to potential stack depth issues in large loops)
    n = 5
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i  # multiply by the next number in sequence
    print("5! =", factorial)


def main():
    print("Demonstrating poor vs good names")
    poor_naming_example()
    good_naming_example()

    print("\nIllustrating useful comments")
    comment_usefulness_example()

    # constants should be uppercase with underscores
    MAX_ITERATIONS = 1000
    print("Max iterations allowed:", MAX_ITERATIONS)

    # avoid comments that restate code
    # incorrect: increment counter by one
    counter = 0
    counter += 1  # good: counter tracks number of retries
    print("Counter value:", counter)

    print("Done with readability demonstration.")


if __name__ == "__main__":
    main()
