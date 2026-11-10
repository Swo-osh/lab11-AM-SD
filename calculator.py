# https://github.com/Swo-osh/lab11-AM-SD
# Partner 1: Ayush More
# Partner 2: Sahil Desai 


"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

# First example
import math

def square_root(a):
    if a < 0: 
        raise ValueError("Can only take sqrt of nonnegative numbers")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b): return a + b

def subtract(a,b): return a - b

def multiply(a, b): return a * b

def logarithm(a, b): 
    try:
        return math.log(b, a)
    except:
        raise ValueError("Enter valid number for logarithm")

def exponent(a, b):
    return a ** b


def sub(a, b):
    return a - b

def mul(a, b):
    return a * b   

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a

def log(x, base):
    if x <= 0:
        raise ValueError("Logarithm argument must be positive")
    if base <= 0 or base == 1:
        raise ValueError("Logarithm base must be positive and not equal to 1")
    return math.log(x, base)

def exp(a, b):
    return a ** b