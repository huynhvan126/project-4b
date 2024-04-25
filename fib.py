# Author: Van Huynh
# GitHub username: huynhvan126
# Date: 04/24/2024
# Description: create the function definition in Fibonacci sequence
def fib(n):
    """ Calculate the nth number in Fibonacci sequence
    n (int): the position of the number in the Fibonacci sequence"""
    if n <= 0:
        raise ValueError("Error - Input must be positive")
    a = 1
    b = 1
    fib_number = 0
    if n == 1 or n == 2:
        return 1
    for _ in range(3, n + 1):
        fib_number = a + b
        a, b = b, fib_number
    return fib_number
