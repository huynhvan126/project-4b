# Author: Van Huynh
# GitHub username: huynhvan126
# Date: 04/24/2024
# Description: create the function definition in Fibonacci sequence
def fib(n):
    """ Calculate the nth number in Fibonacci sequence
    n (int): the position of the number in the Fibonacci sequence"""
    if n <= 0:
        raise ValueError("Error - Input must be positive")
    a, b = 1, 1
    for _ in range(2, n):
        a, b = b, a + b
        return b if n > 1 else a
