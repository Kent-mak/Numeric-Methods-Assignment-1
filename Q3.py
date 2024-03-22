
import numpy as np
from Methods import plot_function, Bisection,secant_method,false_position

def driver():
    p = lambda x : (x - 2)**3 * (x-4)**2
    x = np.linspace(1, 5, 400)
    y = p(x)
    plot_function(x, y)
    method = input("Which Method: ")
    if method == 'a':
        root, iterations = Bisection((1, 5), p)
        print(f'Bisection root:{root}, {iterations} iterations')
    elif method == 'b':
        root, iterations = secant_method(1, 5, p)
        print(f'Secant Method root:{root}, {iterations} iterations')
    else:
        root, iterations = false_position(1, 5, p)
        print(f'False Position root:{root}, {iterations} iterations')