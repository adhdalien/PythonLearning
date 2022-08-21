# Print "Hello, World!" to the console
print("Hello, World!")

# Define sharks variable as list of strings
sharks = ['hammerhead', 'great white', 'dogfish', 'frilled', 'bullhead', 'requiem']

# For loop that iterates over sharks list and prints each string item
for shark in sharks:
    print(shark)

# Tuples are like lists, but are immutable and are created with round parenthesis
coral = ('blue coral', 'staghorn coral', 'pillar coral')
print(coral)

# Dictionaries are like maps, they map keys to values.
sammy = {'name': 'Sammy', 'animal': 'shark', 'color': 'blue', 'location': 'ocean'}
print(sammy)

# Print out two strings concatenated together
print("Sammy" + "Shark")

# Print out a string repeated n times
print("Sammy" * 9)

# Print out a string in raw-string format, ignoring all escape characters.
print(r"Sammy says,\"The balloon\'s color is red.\"")

# Store a string inside a variable
ss = "Sammy Shark!"

# Print out the upcased verprint(ss[-4:-1])
# Now the lower
print(ss.lower())

# Some more strings to test functions on
number = "5"
letters = "abcdef"
movie = "2001: A SAMMY ODYSSEY"
book = "A Thousand Splendid Sharks"
poem = "sammy lived in a pretty how town"

print(number.isnumeric())
print(letters.isnumeric())
print(movie.islower())
print(movie.isupper())
print(book.istitle())
print(book.isupper())
print(poem.istitle())
print(poem.islower())

# Get and print the length of a string
open_source = "Sammy contributes to open source."
print(len(open_source))

# Joining, splitting, and replacing strings
balloon = "Sammy has a balloon."
print(" ".join(balloon))
print("".join(reversed(balloon)))
print(",".join(["sharks", "crustaceans", "plankton"]))
print(balloon.split())
print(balloon.split("a"))
print(balloon.replace("has","had"))

# Slicing strings
print(ss[6:11])
print(ss[:5])
print(ss[7:])
print(ss[-4:-1])

# Increasing the stride of the slice
print(ss[0:12:2])
print(ss[0:12:4])
print(ss[::-2])

# Counting occurrences of characters
print(ss.count("a"))
print(ss.count("s"))

# You can also count how many times a whole word appears in a string
likes = "Sammy likes to swim in the ocean, likes to spin up servers, and likes to smile."
print(likes.count("likes"))

# We can check to see where the first “m” occurs in the string ss:
print(ss.find("m"))
print(likes.find("likes"))
print(likes.find("likes", 9))
print(likes.find("likes", 40, -6))

def add(a, b):
    """
    Given two integers, return the sum.

    :param a: int
    :param b: int
    :return: int

    >>> add(2, 3)
    5
    """
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testmod()
