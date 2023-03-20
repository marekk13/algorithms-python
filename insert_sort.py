"""
Function that takes in an array of integers and returns a sorted version of that array.
The name of algorithm being used is: Insertion Sort
"""


def ins_sort(L):
    j = 0
    for i in range(1, len(L)):
        j = i
        while j >= 1 and L[j - 1] > L[j]:
            L[j - 1], L[j] = L[j], L[j - 1]
            j -= 1


array = [8, 5, 2, 9, 6, 3]
ins_sort(array)
print(array)
