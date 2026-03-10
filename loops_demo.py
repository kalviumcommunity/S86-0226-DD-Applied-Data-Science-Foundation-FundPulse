"""
loops_demo.py - Demonstrate for and while loops in Python

This script shows:
- for loops iterating over ranges and lists
- while loops with condition-based repetition
- using break and continue to control flow
- a commented infinite-loop example with explanation

Run the script with `python loops_demo.py` to observe behavior.
"""


def main():
    print("For loop over range")
    for i in range(5):  # 0 through 4
        print("i =", i)

    print("\nFor loop over list")
    animals = ["cat", "dog", "fish"]
    for pet in animals:
        print("pet =", pet)
        if pet == "dog":
            print("found a dog, breaking out")
            break

    print("\nContinue example")
    for n in range(6):
        if n % 2 == 0:
            continue  # skip even numbers
        print("odd number", n)

    print("\nWhile loop example")
    count = 3
    while count > 0:
        print("counting down", count)
        count -= 1
    print("blast off!")

    print("\nWhile loop with break")
    x = 0
    while True:
        print("x is", x)
        x += 1
        if x >= 3:
            print("reached limit, breaking")
            break

    # warning: the following infinite loop is intentionally commented out
    # to illustrate a common mistake. Uncomment to see what happens.
    #
    # print("\nInfinite loop example")
    # y = 1
    # while y > 0:
    #     print("y keeps growing", y)
    #     # missing update to y leads to infinite iteration

    print("\nDone with loops demonstration.")


if __name__ == "__main__":
    main()
