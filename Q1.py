
import matplotlib.pyplot as plt
import numpy as np
from Methods import Bisection

def f(x):
    return x * np.sin((x-2)/(x-1))

def find_intervals(x_vals, y_vals):
    intervals = []
    for i in range(len(x_vals)-1):
        if x_vals[i] <= 1 and x_vals[i+1] >= 1 :
            continue
        if y_vals[i] * y_vals[i+1] < 0:
            intervals.append((x_vals[i], x_vals[i+1]))
    
    return intervals

        
def sol(intervals):
    roots = []
    for interval in intervals:
        root, iterations = Bisection(interval, f)
        roots.append((root,iterations))

    roots.sort(key=lambda r : abs(r[0]-0.95))
    for i in range(4):
        print(f'{round(roots[i][0], 5)}, {roots[i][1]} iterations')
        


