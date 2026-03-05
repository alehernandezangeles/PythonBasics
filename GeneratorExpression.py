# If this code used square brackets [...], it would be a List Comprehension. Python would immediately calculate the
# square of every number from 0 to 999,999, shove all one million of them into your RAM, and hand you a massive list.
# By using parentheses (...), you tell Python to create a Generator instead.

print("Generator expression")
huge_list = (x ** 2 for x in range(1000000))
print(huge_list)

# Iterate and manually keep track of how many we print
for count, value in enumerate(huge_list):
    print(value)

    if count == 4:
        break     # Stop the loop after 10 items

print(next(huge_list))