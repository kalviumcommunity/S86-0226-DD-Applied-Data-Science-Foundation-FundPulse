"""
functions_demo.py - Demonstrate defining and calling Python functions

This simple script shows:
- defining functions with def
- calling functions with and without arguments
- returning values
- parameter usage and order
- basic scope demonstration (local vs global)

Run with `python functions_demo.py` to see output.
"""


def greet(name):
    """Return a greeting string for the given name."""
    return f"Hello, {name}!"


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def print_message():
    """A function that prints a fixed message and shows local variable scope."""
    message = "This is inside the function"
    print(message)
    # message is local; outside code cannot access it


def demonstrate_scope():
    global_var = "I'm local to this function"
    print(global_var)


def main():
    print("Calling greet()")
    greeting = greet("Kalvium")
    print(greeting)

    print("\nCalling add() with arguments")
    result = add(10, 5)
    print("10 + 5 =", result)

    print("\nCalling print_message() to show local variable")
    print_message()

    # attempting to print message outside would raise NameError if uncommented
    # print(message)

    print("\nDemonstrating variable scope")
    demonstrate_scope()
    # global_var is not accessible here
    # print(global_var)  # would raise NameError

    print("\nDefining and calling a function inside main")
    def square(x):
        return x * x
    print("square(4) =", square(4))

    print("\nDone with function demonstrations.")


if __name__ == "__main__":
    main()
