"""
Function that returns a new string obtained by shifting every letter in the input string by k positions in the alphabet,
where k is the key.
Sample Input           |        Sample Output
string = 'xyz'         |             "zab"
"""


def caesar(text, k):
    newtext = ""
    k = k % 26
    for letter in text:
        newletter = ord(letter) + k
        if (newletter < 123 and newletter > 96) or (newletter > 64 and newletter < 91):
            newletter = chr(newletter)
            newtext += newletter
    return newtext


print(caesar("abc", 2))
