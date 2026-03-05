print("Concatenation:")
print("Hello " + "world!")

print("Repetition:")
print("Repeat " * 3)

print("Membership:")
print("to the" in "Hello to the world")
print("to THE" in "Hello to the world")

print("Length:")
print(len ("123456"))

print("Slicing:")
print("0123456789"[4])
print("0123456789"[:])
print("0123456789"[:-3])
print("0123456789"[3:])
print("0123456789"[5:8])
print("0123456789"[0::3])

print("Formatting & Case Conversion:")
print("Python is a Programming language".lower())
print("Python is a Programming language".upper())
print("Python is a Programming language".title())
print("Python is a Programming language".capitalize())
print("Python is a Programming language".swapcase())
print("42".zfill(5))

print("Searching & Replacing:")
print("0123456789".find("56"))
print("0123456789".find("568"))
print("0123456789".index("56"))
# print("0123456789".index("568")) # Throws exception (ValueError: substring not found)
print("01230123".count("12"))
print("01230123".count("125"))
print("01230123".replace("12", "__"))
print("0123456789".startswith("01"))
print("0123456789".startswith("67"))
print("0123456789".endswith("89"))
print("0123456789".endswith("56"))


