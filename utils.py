import argparse
import random


def parse_arguments():

    parser = argparse.ArgumentParser("Blog-post")
    parser.add_argument('--algorithm',
                        default='intrinsic',
                        type=str,
                        help='Algorithm to run multiplication')
    parser.add_argument('--N',
                        default=1024,
                        type=int,
                        help='Final N value')
    parser.add_argument('--write_data',
                        default=False,
                        action='store_true',
                        help='To write data')
    parser.add_argument('--write_dir',
                        default='./',
                        type=str,
                        help='directory path to store data')

    return parser.parse_args()


def generate_number(N,num_type):
    """
    Generate a sequence of numbers of type {num_type} of size N.
    Supported types: "str", "list".
    """
    if num_type == 'str':
        s = "".join(str(random.randint(1,9)))
        s += "".join([ str(random.randint(0,9)) for _ in range(N-1) ])
    elif num_type == 'list':
        s = [random.randint(1,9)]
        s += [ random.randint(0,9) for _ in range(N-1) ]

    return s


def print_results(s1,s2,result):
    """
    Print the numbers and result.
    """
    print("\nNumber 1: ",s1)
    print("Number 2: ",s2)
    print("Result: ",result)
    print()

def range_N(start,size):
    i = start
    while i <= size:
        yield i
        i *= 2
