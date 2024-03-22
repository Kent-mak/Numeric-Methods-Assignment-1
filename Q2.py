
from Q1 import f
from Methods import secant_method
import numpy as np


    
def sol():
    step = np.linspace(0.9, 1, 400)
    # print(step)
    roots = []
    for i in range(399):

        root,iterations = secant_method(step[i], step[i+1], f)
        if root is not None:
            roots.append((round(root,5),iterations))

    roots = sorted(roots, key=lambda r:( abs(r[0] - 0.95), r[1]))


    i = 0
    count = 0
    while count < 4 and i < len(roots):
        if i == 0:
            print(f'{round(roots[i][0], 5)}, {roots[i][1]} iterations')
            count += 1
            i+=1
            continue

        if roots[i][0] != roots[i-1][0]:
            print(f'{roots[i][0]}, {roots[i][1]} iterations')
            count += 1
        i+=1


    



