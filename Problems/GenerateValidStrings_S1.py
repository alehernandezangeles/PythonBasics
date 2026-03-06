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

def generate_strings(starting_characters, next_characters, n):
    if starting_characters is None or next_characters is None or len(next_characters) < 1 or len(starting_characters) < 1:
        return

    helper(starting_characters, next_characters, n)

def helper(curr_str, next_characters, max_length):
    for x in curr_str:
        print(x)

    if len(curr_str[0]) >= max_length:
        return

    new_str = []
    for c_s in curr_str:
        last_c = c_s[-1]
        c_allowed = next_characters[last_c]
        for allowed in c_allowed:
            new_str.append("".join([c_s, allowed]))

    helper(new_str, next_characters, max_length)

    return

starting_characters = ['a', 'b', 'c']
next_character_map = {
    'a': ['b', 'c'],
    'b': ['a'],
    'c': ['a', 'b']
}
n = 4

generate_strings(starting_characters, next_character_map, n)