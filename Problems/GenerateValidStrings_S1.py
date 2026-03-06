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


def generate_strings(starting_chars, next_valid_chars, max_str_len):
    if starting_chars is None or next_valid_chars is None or len(next_valid_chars) < 1 or len(starting_chars) < 1:
        return

    current_str_len = 1
    helper(starting_chars, next_valid_chars, current_str_len, max_str_len)

def helper(current_str_list, next_valid_chars, current_str_len, max_str_len):
    calc_next_char = True
    if current_str_len >= max_str_len:
        calc_next_char = False

    temp_str_list = []
    for current_str in current_str_list:
        print(current_str)

        if calc_next_char:
            calc_temp_str_list(temp_str_list, current_str, next_valid_chars)

    if not calc_next_char:
        return

    current_str_list = temp_str_list # Memory optimization
    helper(current_str_list, next_valid_chars, current_str_len + 1, max_str_len)

def calc_temp_str_list(temp_str_list, current_str, next_valid_chars):
    last_char_in_str = current_str[-1]
    valid_chars = next_valid_chars[last_char_in_str]
    for valid_char in valid_chars:
        temp_str_list.append("".join([current_str, valid_char]))


starting_characters = ['a', 'b', 'c']
next_character_map = {
    'a': ['b', 'c'],
    'b': ['a'],
    'c': ['a', 'b']
}
n = 4

generate_strings(starting_characters, next_character_map, n)