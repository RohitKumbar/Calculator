# operations.py
import math


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def power(a, b):
    return a**b

def log(n, base):
    return math.log(n, base)
  
def fib(n):
    return 1 if n in [1, 0] else fib(n-1) + fib(n-2)
