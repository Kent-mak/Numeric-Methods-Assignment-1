
import numpy as np
import Methods

def driver():
    p = lambda x : (x - 2)**3 * (x-4)**2
    x = np.linspace(1, 5, 400)
    y = p(x)
    Methods.plot_function(x, y)
    method = input("Which Method: ")
    if method == 'a':
        root, iterations = Methods.Bisection((1, 5), p)
        print(f'Bisection root:{root}, {iterations} iterations')
    elif method == 'b':
        root, iterations = Methods.secant_method(1, 5, p)
        print(f'Secant Method root:{root}, {iterations} iterations')
    else:
        root, iterations = Methods.false_position(1, 5, p)
        print(f'False Position root:{root}, {iterations} iterations')