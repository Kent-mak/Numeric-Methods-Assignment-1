import numpy as np
from Methods import fixed_point_iteration

def driver():
    f = lambda x: np.exp(x) - 2* x**2
    g_pos = lambda x: np.sqrt(np.exp(x)/2)
    g_neg = lambda x: -1*np.sqrt(np.exp(x)/2)
    gc = lambda x : np.log(2* x**2)

    sub = input('sub problem: ')
    match sub:
        case 'a':
            root_pos = fixed_point_iteration(1.5, g_pos, f)
            root_neg = fixed_point_iteration(-0.5, g_neg, f)
            print(f'positive value: {root_pos}')
            print(f'negative value: {root_neg}')
        case 'b':
            root1 = fixed_point_iteration(2.5, g_pos, f)
            root2 = fixed_point_iteration(2.7, g_pos, f)

            root1_2 = fixed_point_iteration(2.5, g_neg, f)
            root2_2 = fixed_point_iteration(2.7, g_neg, f)

            print(f'x0 = 2.5, positive value:{root1} negative value:{root1_2}')
            print(f'x0 = 2.7, positive value:{root2} negative value:{root2_2}')
        case 'c':
            root = fixed_point_iteration(2.5, gc, f)
            print(f'root: {root}')
        case _:
            print('invalid')

    