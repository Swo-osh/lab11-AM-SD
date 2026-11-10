"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
def square_root(a):
    if a < 0:
        raise ValueError("a has to be nonnegative")
    return math.sqrt(a)

def hypotenuse(a, b): 
    return math.hypot(a, b)
    
def add(a, b): return a + b

def subtract(a,b): return a - b

def multiply(a, b): return a * b

def divide(a, b): 
    if a == 0:
        raise ZeroDivisionError("Divisor cannot be zero")
    return b / a

def logarithm(a, b): 
    try:
        return math.log(b, a)
    except:
        raise ValueError("Enter valid number for logarithm")

def exponent(a, b):
    return a ** b




