import time
import csv

from algorithms import *
from utils import *

def single_run(s1,s2,algorithm):
    """
    Run multiplication algorithm for the given numbers.
    """

    if algorithm == 'quadratic':
        result = quadratic(s1,s2)
    elif algorithm == 'karatsuba':
        result = karat(s1,s2)
    elif algorithm == 'intrinsic':
        result = python(s1,s2)
    elif algorithm == 'fft':
        result = fft(s1,s2)

    return result

def main():

    args = parse_arguments()
    print()

    if args.write_data:
        fpath = args.write_dir
        if fpath[-1] != '/':
            fpath += '/'
        fname = args.algorithm+'_'+str(args.N)+'.csv'
        csvfile = open(fpath+fname, 'w')
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(('N','Time'))

    if args.algorithm == 'fft':
        n_type = 'list'
    else:
        n_type = 'str'

    for N in range_N(2,args.N):

        num1 = generate_number(N,num_type=n_type)
        num2 = generate_number(N,num_type=n_type)

        start = time.time()
        result = single_run(num1,num2,args.algorithm)
        time_ = round( time.time()-start, 6 )

        # print_results(num1,num2,result)
        
        print("N: {:<15} Time: {}".format(N,time_))

        if args.write_data:
            writer.writerow((N,time_))

    print()


if __name__ == '__main__':
    main()
