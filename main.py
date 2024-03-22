import argparse
import Q1, Q2, Q3, Q4, Q5, Q6

def parse_args():
    parser = argparse.ArgumentParser(description='argument settings')
    parser.add_argument('--Q', type=int, choices=[1,2,3,4,5,6], default=0)

    args = parser.parse_args()

    return args

def main(args):
    question = args.Q
    match question:
        case 1:
            Q1.driver()
            
        case 2:
            Q2.driver()

        case 3:
            Q3.driver()

        case 4:
            Q4.driver()
        case 5:
            Q5.driver()
        case 6:
            Q6.driver()
        case _:
            print('invalid input')

    

if __name__ == '__main__':
    args = parse_args()
    main(args)