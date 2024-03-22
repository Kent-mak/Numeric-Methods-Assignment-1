from Methods import plot_function, mullers_method
import numpy as np

def driver():
    sub = input("sub problem: ")
    if sub == 'a':
        f = lambda x : 4*x**3 - 3*x**2 + 2*x - 1
        x = np.linspace(0.4, 0.7, 400)
        y = f(x)
        plot_function(x, y, 0.6)
        root = mullers_method(0.5, 0.6, 0.7, f)
        print(f'Muller\'s Method root:{root}')
    else:
        f = lambda x : x**2 + np.exp(x) - 5
        x = np.linspace(-3, 2, 400)
        y = f(x)
        plot_function(x, y)
        root1 = mullers_method(-3, -2, -1, f)
        root2 = mullers_method(0, 1, 2, f)
        print(f'Muller\'s Method roots:{root1},{root2}')