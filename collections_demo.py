"""
collections_demo.py - Demonstrate Python lists, tuples, and dictionaries

This simple script shows:
- creating and modifying lists
- tuples and their immutability
- dictionaries with key-value pairs
- accessing elements via index or key
- adding/removing items from mutable structures
- choosing appropriate data structures for simple scenarios

Run the script with `python collections_demo.py` to see the output.
"""


def main():
    print("List examples")
    # create a list
    fruits = ["apple", "banana", "cherry"]
    print("initial list", fruits)

    # access by index
    print("first fruit", fruits[0])
    print("last fruit", fruits[-1])

    # modify and add
    fruits[1] = "blueberry"
    fruits.append("date")
    print("after modification", fruits)

    # remove an element
    fruits.remove("apple")
    print("after removal", fruits)

    # iterate
    for f in fruits:
        print("fruit =", f)

    print("\nTuple examples")
    # create tuple
    point = (2, 3)
    print("point =", point, "type", type(point))
    print("x coordinate", point[0])

    # try to modify tuple
    try:
        point[0] = 5
    except TypeError as e:
        print("error modifying tuple:", e)

    # tuples are good for fixed collections
    dimensions = (1920, 1080)
    print("dimensions", dimensions)

    print("\nDictionary examples")
    person = {
        "name": "Alice",
        "age": 30,
        "city": "New York"
    }
    print("person dict", person)

    # access by key
    print("name is", person["name"])

    # add a new key
    person["profession"] = "Engineer"
    print("after adding profession", person)

    # update existing
    person["age"] = 31
    print("after birthday", person)

    # loop through keys/values
    for key, value in person.items():
        print(key, "=>", value)

    print("\nChoosing the right structure")
    print("use list for ordered, mutable sequence")
    print("use tuple for fixed sequence that shouldn't change")
    print("use dict for labeled data accessed by key")

    print("Done with collections demonstration.")


if __name__ == "__main__":
    main()
