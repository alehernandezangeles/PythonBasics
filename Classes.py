# Instead of defining getters and setters methods, Python supports defining properties that are defined
# by methods to get and set a value.
# All methods and fields are “public” in Python, but it is common to start members’ names from “_”
# if they are not supposed to be used as part of the “public” interface.

class Foo:
    def __init__(self):
        self._bar = 1

    @property
    def bar(self):
        return self._bar

    @bar.setter
    def bar(self, value):
        self._bar = value

foo = Foo()
foo.bar = 5
print (foo.bar) # 5