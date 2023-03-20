"""
The Fibonacci sequence is defined as follows: the first number of the sequence is 0, the second number is 1 and the nth
number is the sum of the (n-1) and (n-2)th numbers. Function has to take an integer n and returns the nth Fubonacci
number.
Sample Input                  |       Sample Output
n = 6                         |    5  # 0, 1, 1, 2, 3, 5
"""


def fibo(n):
    temp = [0, 1]
    count = 3
    while count <= n:
        t = temp[1]
        temp[1] = temp[0] + temp[1]
        temp[0] = t
        count += 1
    return temp[1] if n > 1 else 0


print(fibo(6))
