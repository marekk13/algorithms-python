"""
Funcion that takes in a non-empty array of distinct integers and an integer representing a target sum.
If any two numbers in the input array sum up to the target sum, the funcion should return them in an array,
in any order. The target sum has to be obtained by summing two different integers in the array can't add a single
integer to itself in order to obtain the target sum.
Assume that there will be at most one pair of numbers summing up to the target sum.
Sample Input:                                  |      Sample Output:
array_to_check = [3, 5, -4, 8, 11, 1, -1, 6]   |      [-1, 11] # the numbers could be in reverse order
target = 10                                    |
"""


def target_sum(L, target):
    for i, number in enumerate(L):
        if target - number in L[i + 1 :]:
            return [target - number, number]


array_to_check = [3, 5, -4, 8, 11, 1, -1, 6]
target = 10
print(target_sum(array_to_check, target))
