"""
Function that takes in an array of at least three integers and without sorting the input array, returns a sorted
array of the three largest integers in the input array.
Function returns duplicate integers if necessary; for example, it returns [10, 10, 12] for an input array of [10, 5, 9, 10, 12].
Sample Input:                                           |         Sample Output:
array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]    |         [18, 141, 541]
"""


def three_largest(L):
    ret = [None, None, None]
    for i in range(3):
        ret[i] = max(L)
        L.remove(max(L))
    return ret


array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7, 541, 541]
print(three_largest(array))
