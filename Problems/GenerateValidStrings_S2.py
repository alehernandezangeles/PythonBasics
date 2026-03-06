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


def generate_strings_optimal(starting_chars, next_valid_chars, max_str_len):
    if not starting_chars or not next_valid_chars or max_str_len < 1:
        return

    # A tiny, self-contained recursive function
    def dfs(current_str):
        print(current_str)

        # Stop digging deeper if we hit the limit
        if len(current_str) >= max_str_len:
            return

        last_char = current_str[-1]

        # Dig deeper for every valid next character
        for valid_char in next_valid_chars.get(last_char, []):
            dfs(current_str + valid_char)

    # Kick off the process
    for char in starting_chars:
        dfs(char)

starting_characters = ['a', 'b', 'c']
next_character_map = {
    'a': ['b', 'c'],
    'b': ['a'],
    'c': ['a', 'b']
}
n = 4

generate_strings_optimal(starting_characters, next_character_map, n)