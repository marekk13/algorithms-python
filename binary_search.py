"""
Function that takes in a sorted array of integers as well as a target integer.
The function use the Binary Search algorithm to determine if the target integer is contained in the array
and returns its index if it is, otherwise - 1.
Sample input:                               |       Sample Output:
array = [0, 1, 21, 33, 45, 61, 71, 73]      |            3
target = 33                                 |
"""


def bin_search(L, target, left, right):
    sr = (left + right) // 2
    if left > right:
        return -1
    if L[sr] == target:
        return sr
    elif L[sr] > target:
        return bin_search(L, target, 0, sr)
    else:
        return bin_search(L, target, sr + 1, len(L) - 1)


array = [0, 1, 21, 33, 45, 61, 71, 73]
target = 71

print(bin_search(array, target, 0, len(array) - 1))
