from Methods import newtons_method
import numpy as np

def driver():
    f = lambda x: np.cos(x)**4 + x**2 -x -2

    f_prime = lambda x: 2*x + -4* np.cos(x)**3 *np.sin(x) - 1
    
    root = newtons_method(0, f, f_prime)
  

    print(f'Root:{root}')
