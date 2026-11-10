"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
<<<<<<< HEAD

# First example
import math


def add(a, b): 
    return a + b
=======
def add(a, b): return a + b

def subtract(a,b): return a - b

def multiply(a, b): return a * b

def divide(a, b): 
    if a == 0:
        raise ZeroDivisionError("Divisor cannot be zero")
    return b / a

def logarithm(a, b): 
    try:
        math.log(b, a)
    except:
        raise ValueError("Enter valid number for logarithm")

def exponent(a, b):
    return a ** b


>>>>>>> ee14dc8ddd8e09f01d95d1eed2d97b4e94a3db41

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b   

def div(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def log(x, base):
    if x <= 0:
        raise ValueError("Logarithm argument must be positive")
    if base <= 0 or base == 1:
        raise ValueError("Logarithm base must be positive and not equal to 1")
    return math.log(x, base)

def exp(a, b):
    return a ** b