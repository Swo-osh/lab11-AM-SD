"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math


# First example
import math


def add(a, b): 
    return a + b

def add(a, b): return a + b

def subtract(a,b): return a - b

def multiply(a, b): return a * b

def logarithm(a, b): 
    try:
        math.log(b, a)
    except:
        raise ValueError("Enter valid number for logarithm")

def exponent(a, b):
    return a ** b


def sub(a, b):
    return a - b

def mul(a, b):
    return a * b   

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def log(x, base):
    if x <= 0:
        raise ValueError("Logarithm argument must be positive")
    if base <= 0 or base == 1:
        raise ValueError("Logarithm base must be positive and not equal to 1")
    return math.log(x, base)

def exp(a, b):
    return a ** b