"""
function_io_demo.py - Demonstrate passing data into functions and returning results

This script emphasizes:
- defining functions with parameters
- calling them with varying arguments
- returning computation results instead of printing
- storing and reusing return values
- composing functions by feeding outputs into other calls

Run with `python function_io_demo.py` and watch console output.
"""


def multiply(x, y):
    """Return the product of x and y."""
    return x * y


def format_price(amount):
    """Return a nicely formatted string for a numeric price."""
    return f"${amount:.2f}"


def area_of_rectangle(width, height):
    """Compute and return area; shows parameters with descriptive names."""
    return width * height


def main():
    # parameters and arguments
    a = 4
    b = 7
    prod = multiply(a, b)  # pass variables as arguments
    print(f"{a} times {b} equals {prod}")

    # using return values in further calculations
    price_per_item = 19.99
    quantity = 3
    total_cost = multiply(price_per_item, quantity)
    print("total_cost (raw):", total_cost)
    print("total_cost (formatted):", format_price(total_cost))

    # chaining function calls
    w, h = 5, 8
    rect_area = area_of_rectangle(w, h)
    print(f"area of {w}x{h} rectangle =", rect_area)
    print("formatted area as price?", format_price(rect_area))

    # arguments order matters
    print("multiply(2, 10) =", multiply(2, 10))
    print("multiply(10, 2) =", multiply(10, 2))

    # missing return leads to None
    def no_return_example(x):
        y = x * 2
        # forgot to return y

    result = no_return_example(5)
    print("Result of function with no return is", result)

    print("Done with function input/output demonstration.")


if __name__ == "__main__":
    main()
