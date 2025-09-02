# operations.py

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

def fib(n):
    if n==0 or n==1:
        return 1
    return fib(n-1) + fib(n-2)