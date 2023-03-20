"""
Function that takes in an array of integers abd returns a sorted version of that array.
The name of algorithm being used is: Bubble Sort
Sample Input                    |       Sample Output
array = [8, 5, 2, 9, 6, 3]      |      [2, 3, 5, 5 6, 8, 9]
"""


def bubble_sort(L):
    for i in range(len(L)):
        for j in range(1, len(L) - i):
            if L[j] < L[j - 1]:
                L[j - 1], L[j] = L[j], L[j - 1]
    return L


array = [8, 5, 2, 9, 6, 3]
print(bubble_sort(array))
