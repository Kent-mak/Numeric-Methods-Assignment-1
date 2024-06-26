from typing import Callable
import matplotlib.pyplot as plt
import cmath

TOLERANCE = 1e-6

def plot_function(x_vals, y_vals, mid=None):
    
    plt.plot(x_vals, y_vals, label='f(x)')
    if mid is not None:
        plt.axvline(mid, linestyle='--', label=f'x = {mid}', color='red')
    plt.axhline(0, linestyle='--', color='red')
    plt.legend()
    plt.grid(True)
    plt.show()
    pass

def Bisection(interval, f: Callable):
    iterations = 0
    a, b = interval[0], interval[1]
    val = float('inf')
    while val > TOLERANCE:
        iterations += 1
        midpoint = (a + b) / 2
        val = abs(f(midpoint))
        # print(f'{midpoint}, {val}')
        if f(a) * f(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
    
    return midpoint, iterations


def find_secant_root(x0, x1, f:Callable):
    return x1 - f(x1)*((x0 - x1)/(f(x0)- f(x1)))


def secant_method(x0, x1, f: Callable):
    N = 100

    val = float('inf')
    iterations = 0

    while val > TOLERANCE and iterations < N:

        x2 = find_secant_root(x0, x1, f)

        x0, x1 = x1, x2
        val = abs(f(x2))
        iterations += 1
        
    if iterations >= N:
        x2 = None
    return x2, iterations


def false_position(x0, x1, f:Callable):
    if f(x0) * f(x1) > 0: 
        return None, 0
    
    val = float('inf')
    iterations = 0
    while (val > TOLERANCE):
        x2 = find_secant_root(x0, x1 ,f)
        if f(x2) * f(x0) < 0 :
            x1 = x2
        else:
            x0 = x2
        
        val = abs(f(x2))
        iterations+=1

    return x2, iterations

def mullers_method(x0, x1, x2, f:Callable):


    while abs(f(x2))  > TOLERANCE:
        
        q = (x2 - x1)/(x1 - x0)
        a = q* f(x2) - q*(1+q)*f(x1) + q**2 * f(x0)
        b = (2*q+1)* f(x2) - (1+q)**2 *f(x1) + q**2 * f(x0)
        c = (1+q)*f(x2)
        # print( f'{b} + {cmath.sqrt(b**2 - 4*a*c)} = {(b + cmath.sqrt(b**2 - 4*a*c))}')

        x3_pos = x2 - (x2 - x1)*(2*c) / (b + cmath.sqrt(b**2 - 4*a*c))
        x3_neg = x2 - (x2 - x1)*(2*c) / (b - cmath.sqrt(b**2 - 4*a*c))

        if abs(f(x3_pos)) < abs(f(x3_neg)):
            x3 = x3_pos
        else:
            x3 = x3_neg


        x2, x1, x0 = x3, x2, x1

    return x3

def fixed_point_iteration(x, g: Callable, f:Callable):

    
    while abs(f(x)) > TOLERANCE:
        # print(x)
        x = g(x)
        
    return x


def newtons_method(x, f:Callable, f_prime:Callable):

    while abs(f(x)) > TOLERANCE:
        slope = f_prime(x)
        value = f(x)
        b = value - slope * x
        x = -1*b / slope

    return x


