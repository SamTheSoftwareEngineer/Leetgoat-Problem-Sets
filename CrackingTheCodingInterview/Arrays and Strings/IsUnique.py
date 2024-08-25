"""Implement an algorithm to determine if a string has all unique characters. What if you can't use additional data structures?"""


# Using a set 
def is_Unique(string):
    unique_chars = set()
    for char in string:
        if char in unique_chars:
            return False
        else:
            unique_chars.add(char)
    return True 

print(is_Unique('hello')) # False
print(is_Unique('dear')) # True

