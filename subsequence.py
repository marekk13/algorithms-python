"""
To a given two non-empty arrays of integers, determines whether the second array is a subsequence of the first one.
A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in the same
order as they appear in the array.
Sample Input:                              |     Sample Output:
                                           |        True
array = [5, 1, 22, 25, 6, -1, 8, 10]       |
sequence = [1, 6, -1, 10]                  |
"""


def subsequence(arr, sq):
    i, j = 0, 0
    while i < len(arr) and j < len(sq):
        if arr[i] == sq[j]:
            j += 1
        i += 1
    return j == len(sq)


array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 8]
print(subsequence(array, sequence))
