"""Given two strings, write a method to determine if they are permutations of each other.
A permutation is a change or variation of a string or mathematical object."""



# Using Counter 
from collections import Counter 
def check_permutation(string1, string2):
    return Counter(string1) == Counter(string2)

print(check_permutation('abc', 'cba')) # True
print(check_permutation('hi', 'hello')) # False 
