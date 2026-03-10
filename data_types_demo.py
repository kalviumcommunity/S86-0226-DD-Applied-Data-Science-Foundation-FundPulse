"""
data_types_demo.py - Demonstrate Python numeric and string data types

This simple script shows:
- integer and float variables
- basic arithmetic operations
- string creation and concatenation
- type inspection using type()
- mixing numbers and strings with explicit conversion
- what happens when you accidentally try to combine incompatible types

Run the script with `python data_types_demo.py` to see the output.
"""


def main():
    # numeric types
    a = 10          # integer
    b = 3.5         # float
    c = -2          # another integer

    print("Numeric examples")
    print(f"a = {a}, type: {type(a)}")
    print(f"b = {b}, type: {type(b)}")
    print(f"c = {c}, type: {type(c)}")

    # arithmetic
    print(f"a + b = {a + b}")
    print(f"a * c = {a * c}")
    print(f"b / a = {b / a} (always float)")
    print(f"a // 3 = {a // 3} (floor division)")
    print(f"a ** 2 = {a ** 2} (exponentiation)")

    # string types
    first = "Kalvium"
    last = 'Data'
    print("\nString examples")
    print(f"first = {first}, type: {type(first)}")
    print(f"last = {last}, type: {type(last)}")

    # concatenation
    full = first + " " + last
    print(f"Concatenated: {full}")

    # accessing characters
    print(f"first[0] = {first[0]}, last[-1] = {last[-1]}")

    # mixing numbers and strings
    print("\nMixing types safely")
    print(f"String + string: {first + ' School'}")
    print(f"Number converted to string: {first + ' ' + str(a)}")

    # attempt incorrect mix (commented out to avoid crash)
    try:
        print(first + a)
    except TypeError as e:
        print(f"Error when adding string and int: {e}")

    # converting string to number
    num_str = "42"
    print(f"num_str is {num_str} with type {type(num_str)}")
    num_val = int(num_str)
    print(f"converted num_val = {num_val}, type {type(num_val)}")

    # inspect types with type() and isinstance
    print("\nType checks")
    print("isinstance(a, int)?", isinstance(a, int))
    print("isinstance(b, float)?", isinstance(b, float))
    print("isinstance(full, str)?", isinstance(full, str))
    
    print("Done with data type demonstration.")


if __name__ == "__main__":
    main()
