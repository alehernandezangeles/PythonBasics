print("=== Accessing Data ===")

d = {"A": 1, "B": 2, "C": 3}

print("By index:")
print(d["A"])
# print(d["T"]) # Error (KeyError: 'T')

print("get:")
print(d.get("A"))
print(d.get("T"))
print(d.get("T", 999))

print('in:')
print('A' in d)
print('T' in d)

print("=== Adding & Updating Data ===")

print("By index:")
d = {"A": 1, "B": 2, "C": 3}
d["B"] = 123 # Changing existing key
print(d)
d["T"] = 123 # If key doesn't exist, add it.
print(d)

print("update:")
d = {"A": 1, "B": 2, "C": 3}
new_d = {"T": 999, "B": 123}
d.update(new_d)
print(d)

print("setdefault:")
d = {"A": 1, "B": 2, "C": 3}
k = d.setdefault("B", 123)
print(k)
print(d)

d2 = {"A": 1, "C": 3}
k2 = d2.setdefault("B", 123)
print(k2)
print(d2)

print("=== Removing Data ===")

print("pop")
d = {"A": 1, "B": 2, "C": 3}
k = d.pop("B")
print(k)
print(d)

# k = d.pop("T") # Error (KeyError: 'T')
k = d.pop("T", 999)
print(k)
print(d)

print("popitem:")
d = {"A": 1, "B": 2, "C": 3}
k = d.popitem()
print(k)
print(d)

print("del:")
d = {"A": 1, "B": 2, "C": 3}
del d["B"]
print(d)

print("clear:")
d = {"A": 1, "B": 2, "C": 3}
d.clear()
print(d)

# del d["T"] # Error (KeyError: 'T')

print("=== Iterating & Views ===")

d = {"A": 1, "B": 2, "C": 3}

print("keys:")
print(d.keys())

print("values:")
print(d.values())

print("items:")
print(d.items())

print("=== Dictionary Math ===")

print("Merge |:")
d1 = {"A": 1, "B":2}
d2 = {"B": 100, "C": 3}
d = d1 | d2
print(d)

print("Update |=:")
d = {"A": 1, "B":2}
d2 = {"B": 100, "C": 3}
d |= d2
print(d)


print("=== Misc ===")
d = {"A": 1, "B": 2, "C": 3}

print('len:')
print(len(d))

print("list:")
l = list(d.keys())
print(l)
