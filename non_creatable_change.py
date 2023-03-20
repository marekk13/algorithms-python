"""
Given an array of positive integers representing the values of coins in possession.
Function returns the minimum amount of change (the minimum sum of money) that cannot be created.
The given coins can have any positive integers value and aren't necessarily unique (multiple coins can have the same value).
Sample input:                        |       Sample Output:
coins = [5, 7, 1, 1, 2, 3, 22]       |       20
"""


def change(coins):
    current_change = 0
    for coin in sorted(coins):
        if coin > current_change + 1:
            return current_change + 1
        current_change += coin


coins = [5, 7, 1, 1, 2, 3, 22]
