print("=== Iterable operations  ===")

print("Looping:")
my_string = "cat"

# 1. Looping
for letter in my_string:
    print(letter)

print("list:")
# 2. Converting a string to a list -> ['c', 'a', 't']
my_list = list(my_string)
print(my_list)

print("set:")
# 3. Converting a list to a set (removes duplicates)
my_set = set([1, 2, 2, 3])
print(my_set)

print("=== enumerate and zip ===")

print("enumerate:")
names = ["Alice", "Bob", "Charlie"]
for index, name in enumerate(names):
    print(f"{index}: {name}")

print("zip:")
names = ["Alice", "Bob"]
scores = [95, 88]

for name, score in zip(names, scores):
    print(f"{name} got a {score}")

print("=== Math and Aggregation  ====")
print("sum:")
numbers = [10, 20, 30]
print(sum(numbers))

print("max:")
numbers = [10, 20, 30]
print(max(numbers))

print("min:")
numbers = [10, 20, 30]
print(min(numbers))

print("len:")
numbers = [10, 20, 30]
print(len(numbers))

print("=== Logic Checks ===")
print("any:")
statuses = [True, True, False]
print(any(statuses))

print("all:")
statuses = [True, True, False]
print(all(statuses))

print("=== Sorting and Reversing  ===")
print("sorted:")
l3 = sorted([3, 1, 2])
print(l3)

print("reversed:")
l3 = list(reversed([3, 1, 2]))
print(l3)



