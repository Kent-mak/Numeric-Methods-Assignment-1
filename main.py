import argparse
import Q1, Q2
import Methods
import numpy as np

def parse_args():
    parser = argparse.ArgumentParser(description='argument settings')
    parser.add_argument('--Q', type=int, choices=[1,2,3,4,5,6], default=0)

    args = parser.parse_args()

    return args

def main(args):
    question = args.Q
    match question:
        case 1:
            x = np.linspace(0.9, 1, 400)
            y = Q1.f(x)
            Methods.plot_function(x, y, 0.95)
            intervals = Q1.find_intervals(x, y)
            Q1.sol(intervals)
            
        case 2:
            x = np.linspace(0.9, 1, 400)
            y = Q1.f(x)
            Methods.plot_function(x, y, 0.95)
            Q2.sol()

        case 3:
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

        case 4:
            sub = input("sub problem: ")
            if sub == 'a':
                f = lambda x : 4*x**3 - 3*x**2 + 2*x - 1
                x = np.linspace(0.4, 0.7, 400)
                y = f(x)
                Methods.plot_function(x, y, 0.6)
                root, iterations = Methods.mullers_method(0.5, 0.6, 0.7, f)
                print(f'Muller\'s Method root:{root}, {iterations} iterations')
            else:
                f = lambda x : x**2 + np.exp(x) - 5
                x = np.linspace(-3, 2, 400)
                y = f(x)
                Methods.plot_function(x, y)
                root1, iterations1 = Methods.mullers_method(-3, -2, -1, f)
                root2, iterations2 = Methods.mullers_method(0, 1, 2, f)
                print(f'Muller\'s Method roots:{root1},{root2}')
        case 5:
            pass
        case 6:
            pass
        case _:
            print('invalid input')

    

if __name__ == '__main__':
    args = parse_args()
    main(args)