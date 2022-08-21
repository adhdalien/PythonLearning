# Print "Hello, World!" to the console
print("Hello, World!")

# Define sharks variable as list of strings
sharks = ['hammerhead', 'great white', 'dogfish', 'frilled', 'bullhead', 'requiem']

# For loop that iterates over sharks list and prints each string item
for shark in sharks:
    print(shark)

def add(a, b):
    """
    Given two integers, return the sum.

    :param a: int
    :param b: int
    :return: int

    >>> add(2, 3)
    5
    """
    return a * b

if __name__ == "__main__":
    import doctest
    doctest.testmod()
