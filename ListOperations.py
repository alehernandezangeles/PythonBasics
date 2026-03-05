print("=== Adding elements ===")
print("append:")
l1 = [10, 21, 32]
l1.append(3)
print(l1)

print("extend:")
l2 = [10]
l2.extend([21, 92])
print(l2)

print("insert:")
l3 = [10, 91, 12]
l3.insert(1, 0.5)
print(l3)

print("=== Removing elements ===")

print("remove:")
l1 = ["hello", "world", "europe", "world"]
l1.remove("world")
print(l1)
# l1.remove("Asia") # Throws exception (ValueError: list.remove(x): x not in list)

print("pop:")
l2 = [10, 91, 22, 31, 14]
item1 = l2.pop(2)
print(item1)
print(l2)
item2 = l2.pop()
print(item2)
print(l2)

print("clear:")
l3 = [10, 91, 22, 31, 14]
l3.clear()
print(l3)

print("del:")
l1 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
del l1[0]
print(l1)
l1 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
del l1[3:6]
print(l1)

print("=== Organizing & Sorting ===")
print("sort:")
l1 = ["Africa", "Oceania", "Asia", "Europe"]
l1.sort()
print(l1)
l1.sort(reverse=True)
print(l1)

print("reverse:")
l1 = ["Africa", "Oceania", "Asia", "Europe"]
l1.reverse()
print(l1)

print("=== Searching & Counting ===")
print("index:")
l1 = ["Africa", "Oceania", "Asia", "Europe", "Oceania"]
i1 = l1.index("Oceania")
print(i1)
# i2 = l1.index("Antarctica") # Throws exception (ValueError: 'Antarctica' is not in list)

print("count:")
l1 = ["Africa", "Oceania", "Asia", "Europe", "Oceania"]
print(l1.count("Oceania"))
print(l1.count("Antarctica"))

print("in:")
l1 = ["Africa", "Oceania", "Asia", "Europe", "Oceania"]
print("Asia" in l1)
print("asia" in l1)

print("len:")
l1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(len(l1))

print("=== Math & Slicing ===")
print("Concatenation:")
l1 = ["Africa", "Oceania"]
l2 = ["Asia", "Europe"]
print(l1 + l2)

print("Repetition:")
l1 = ["Asia"] * 3
print(l1)

print("Slicing:")
l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = l1[3:7]
print(l2)