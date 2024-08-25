"""Write a method to replace all spaces in a string with %20. You may assume that the string has sufficent space
at the end to hold the additional characters, and that you are given the 'true' length of the string. """

"""Example:
Input: Mr. John Smith
Output: Mr%20John%20Smith"""

def URLify(string):
    string = string.split()
    joined_string = '%20'.join(string)
    print(joined_string)
    


print(URLify('Mr John Smith'))