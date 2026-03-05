# Function with a variable number of positional parameters
def f1(*args):
    # args is a tuple
    print(type(args))
    print(args)

# Function with a variable number of keyword parameters
def f2(**args):
    # args is a dictionary
    print(type(args))
    print(args)

def f3(*args, **kw):
    print(args, kw)

# Enforcing keyword-only arguments
# 'name' is a standard positional argument
# Everything after '*' is keyword-only
def create_user(name, *, is_admin=False, age=None):
    print(f"User: {name}, Admin: {is_admin}, Age: {age}")

# Function Annotations, which are most commonly used today for Type Hinting.
def func_anot(a: int, b: str, c: "param", d: 42):
     print(a, b, c, d)

# A function can return more than one item at a time.
# Items separated by commas are automatically 'packed' into a tuple and can be 'unpacked' on the receiving end
def f4():
    return 1, "hi"

f1(1)
f1(1, 2, 3)

f2(a=1, b=2, c=3)

lst = [1, 2, 3]
d = {'a': 1, 'b': 2}

# Example of unpacking into a variable number of parameters
# This is equivalent to passing f3(1, 2, 3, a=1, b=2)
f3(*lst, **d)

create_user("John") # Correct
# create_user("John", True) # Error (TypeError: create_user() takes 1 positional argument but 2 were given)
create_user("John", is_admin=True, age=42) # Correct

func_anot(5, "Hi", True, [1, 2])
func_anot(True, 123, True, [1, 2]) # annotations are not enforced

res1, res2 = f4()
print(res1, res2)
