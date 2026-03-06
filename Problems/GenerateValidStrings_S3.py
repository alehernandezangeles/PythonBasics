"""
Write a program to generate all "valid strings" up to a certain length. A valid
string is a string that starts with an "allowed starting character", and in
which every character is followed by an "allowed" character. You are given a
list of starting allowed characters and a dictionary mapping each character to
a list of allowed characters that can follow it in valid strings. You are also
given an integer n > 0 and you should generate all valid strings up to and
including length n.

Print the output to console directly. You do not need to store all the output
in a list or other collection.

Example 1:

starting_characters = ['a', 'b', 'c']
next_character_map = {
    'a': ['b' , 'c'],
    'b': ['a'],
    'c': ['a', 'b']
}
n = 4

Expected output:

'a'
'b'
'c'
'ab'
'ac'
'ba'
'ca'
'cb'
'aba'
'aca'
'acb'
...

...
'caca'
...
'cbac'

"""
from typing import Any


def generate_strings_dfs(starting_chars, next_valid_chars, max_str_len):
    # 1. Input validation
    if not starting_chars or not next_valid_chars or max_str_len < 1:
        return

    # 2. Define the recursive generator
    def dfs(current_str):
        # Instantly yield the valid string we just built
        yield current_str

        # Base case: Stop digging if we hit the max length
        if len(current_str) >= max_str_len:
            return

        # Look at the last character to find what comes next
        last_char = current_str[-1]
        valid_nexts = next_valid_chars.get(last_char, [])

        # Dig deeper for each valid next character
        for next_char in valid_nexts:
            # 'yield from' acts as a pipeline, sending values from
            # the deepest recursive calls straight to the surface
            yield from dfs(current_str + next_char)

    # 3. Kick off the search for every starting character
    for start_char in starting_chars:
        yield from dfs(start_char)

starting_characters = ['a', 'b', 'c']
next_character_map = {
    'a': ['b', 'c'],
    'b': ['a'],
    'c': ['a', 'b']
}
n = 4

for result in generate_strings_dfs(starting_characters, next_character_map, max_str_len=n):
    print(result)