import math as ma

def add(x, y):
    sum = x + y
    return sum

def factorial(x):
    s = 1
    if x == 0:
        s = 1
    else:
        while x > 0:
            s = s * x
            x = x - 1
    return s
    
def sin(x, N):
    s = 0
    i = 0
    while i <= N:
        s += ((-1)**i*x**(2*i+1))/(factorial(2*i+1))
        i += 1
    return s

def divide(x, y):
    sum = x/y
    return sum

def circumference(x):
    sum = 2 * ma.pi * x
    return sum

def multiply(x, y):
    sum = x * y
    return sum