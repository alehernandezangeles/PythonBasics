for a, b in [(1, 2), (3, 4), (5, 6)]:
    print(f'a = {a}, b = {b}')

d = {'key1': 1, 'key2': 2}
print(type(d.items()))
for key, value in d.items():
    print(key, value)