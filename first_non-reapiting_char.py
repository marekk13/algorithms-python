"""
Function that takes in a string of lowercase English-alphabet letters and returns the index of the string's first
non-repeating character. The first non-repeating character is the first character in a string that occurs only once.
If the input string doesn't have any non-repeating characters, function returns -1.
Sample Input            |       Sample Output
string = "abcdcaf"      |           1    # the first non-repeating character is "b" and is found at index 1
"""


def first_nonrp(string):
    for i, letter in enumerate(string):
        if letter not in string[i + 1 :]:
            return i
    else:
        return -1


string = "abcdcaf"
print(first_nonrp(string))
