# A comprehension is a highly concise and optimized way to create a new collection of data (like a List or a Dictionary)
# based on an existing one, entirely in a single line of code.

print("List Comprehensions")
# Read as: "Give me 'i * i', for every 'i' in the range of 5"
squares = [i * i for i in range(5)]

print(squares) # Output: [0, 1, 4, 9, 16]

print("Dictionary Comprehensions")
names = ["Alice", "Bob", "Charlie"]

# Read as: "Map 'name' to 'len(name)', for every 'name' in our list"
name_lengths = {name: len(name) for name in names}

print(name_lengths)
# Output: {'Alice': 5, 'Bob': 3, 'Charlie': 7}

print("Set Comprehensions")
numbers = [1, 2, 2, 3, 4, 4, 5]

# Get the square of every number, but only keep unique results
unique_squares = {x * x for x in numbers}

print(unique_squares)
# Output: {1, 4, 9, 16, 25} (Notice it removed the duplicates!)

print("Adding if conditions to filter the data preemptively")
# Create a list of squares, but ONLY if the original number is even
even_squares = [i * i for i in range(10) if i % 2 == 0]

print(even_squares)
# Output: [0, 4, 16, 36, 64]

