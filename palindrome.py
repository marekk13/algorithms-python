"""
Function that takes in a non-empty string and that returns a boolean representing whether the string is a palindrome.
A palindrome is defined as a string that's written the same forward and backward.
Sample Input               |        Sample Output
string = 'abcdcba'         |            true
"""


def palindrome(string):
    return string.replace(" ", "") == string.replace(" ", "")[::-1]
