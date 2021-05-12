import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
import argparse


# intrinsic value
# MIN_N = 16777216

# karatsuba value
# MIN_N = 1048576

# fft value
# MIN_N = 536870912

# for all plots - quadratic value
MIN_N = 131072

# for single plots
# MIN_N = np.float('inf')

# for final plot
# MIN_N = 50


def parse_arguments():

    parser = argparse.ArgumentParser("Blog-post")
    parser.add_argument('--algorithm',
                        default=None,
                        type=str,
                        help='Algorithm to plot. If None, then plot all.')
    parser.add_argument('--data_dir',
                        default='./',
                        type=str,
                        help='directory path to store data')
    parser.add_argument('--log_scale',
    					default=False,
    					action='store_true',
    					help='True to use log scale for plot.')
    parser.add_argument('--save_fname',
    					default=None,
    					type=str,
    					help='Filename to save plot.')

    return parser.parse_args()


def read_data(dir_name,fnames):
	"""
	Read data from the provided file and write to a dictionary.
	"""
	data = {}
	if dir_name[-1] != '/':
		dir_name += '/'

	for fname in fnames:

		file = open(dir_name+fname+'.csv','r')
		data.setdefault(fname,{})

		for d1,d2 in csv.reader(file, delimiter=','):
			if d1 != 'N' and int(d1) <= MIN_N:
				data[fname][int(d1)] = float(d2)

	return data

def theoretical(data,fnames):

	theoretical_data = {}

	for algorithm in fnames:

		if algorithm == 'fft':
			f = lambda x: x*np.log(x)
		elif algorithm == 'quadratic':
			f = lambda x: x*x
		elif algorithm == 'karatsuba':
			f = lambda x: x**1.58
		elif algorithm == 'intrinsic':
			continue

		sizes = data[algorithm].keys()
		max_val = list(data[algorithm].values())[-1]

		th_data = {n:f(n) for n in sizes}
		theoretical_data[algorithm] = {n:th_data[n]*max_val/max(th_data.values()) for n in sizes}

	return theoretical_data


def plot(data,big_oh):

	colors_list = ['tab:blue','tab:red','tab:orange','tab:purple']
	colors = {a:c for a,c in zip(data.keys(),colors_list)}
	plot_data, plot_theory = {}, {}

	for alg,values in data.items():

		d, = plt.plot(values.keys(),values.values(),'o',color=colors[alg])
		plot_data[alg] = d

		try:
			t, = plt.plot(big_oh[alg].keys(),big_oh[alg].values(),color=colors[alg],linewidth=2)
			plot_theory[alg] = t
		except:
			continue

	theory_labels = [r'$\mathcal{O}$ for %s' %alg for alg in plot_theory.keys()]

	ax = plt.gca()

	if len(data.keys()) == 4:

		# log scale
		legend1 = plt.legend(plot_data.values(),plot_data.keys(),bbox_to_anchor=(0.99,0.5))
		plt.legend(plot_theory.values(),theory_labels,bbox_to_anchor=(0.99,0.25))
		ax.add_artist(legend1)

		# normal scale
		# legend1 = plt.legend(plot_data.values(),plot_data.keys(),bbox_to_anchor=(0.99,0.55))
		# plt.legend(plot_theory.values(),theory_labels,bbox_to_anchor=(0.99,0.3))
		# ax.add_artist(legend1)

	elif len(data.keys()) == 1:
		legend1 = plt.legend(plot_data.values(),['computed'],bbox_to_anchor=(0.99,0.2))
		plt.legend(plot_theory.values(),[r'theoretical - $\mathcal{O}$'],bbox_to_anchor=(0.99,0.1))
		ax.add_artist(legend1)

	else:
		# legend1 = plt.legend(plot_data.values(),plot_data.keys(),bbox_to_anchor=(0.99,0.25))
		# plt.legend(plot_theory.values(),theory_labels,bbox_to_anchor=(0.99,0.1))
		# ax.add_artist(legend1)

		# # intrinsic quadratic
		# legend1 = plt.legend(plot_data.values(),plot_data.keys(),bbox_to_anchor=(0.99,0.35))
		# plt.legend(plot_theory.values(),theory_labels,bbox_to_anchor=(0.99,0.2))
		# ax.add_artist(legend1)

		# # intrinsic quadratic karatsuba
		# legend1 = plt.legend(plot_data.values(),plot_data.keys(),bbox_to_anchor=(0.99,0.95))
		# plt.legend(plot_theory.values(),theory_labels,bbox_to_anchor=(0.99,0.75))
		# ax.add_artist(legend1)

		# intrinsic fft
		legend1 = plt.legend(plot_data.values(),plot_data.keys(),bbox_to_anchor=(0.99,0.25))
		plt.legend(plot_theory.values(),theory_labels,bbox_to_anchor=(0.99,0.1))
		ax.add_artist(legend1)

	# for final plot
	# for alg,values in data.items():

	# 	d, = plt.plot(values.keys(),values.values(),'o-',color=colors[alg])
	# 	plot_data[alg] = d

	# if len(data.keys()) == 4:

	# 	# log scale
	# 	plt.legend(plot_data.values(),plot_data.keys(),bbox_to_anchor=(0.99,0.5))

	if args.log_scale:
		ax.set_yscale('log')

	plt.grid(b=True, which='major', color='0.8')
	plt.xlabel('Number of digits')
	plt.ylabel('Time taken to multiply (in s)')

	if args.save_fname is not None:
		plt.savefig('./plots/'+args.save_fname,dpi=400)
	else:
		plt.show()

def main():

	global args
	args = parse_arguments()

	if args.algorithm is None:
		fname = ['fft','intrinsic','karatsuba','quadratic']
	else:
		alg = args.algorithm.split()
		if len(alg) == 1:
			fname = [alg[0],]
		else:
			fname = alg
	
	data = read_data(args.data_dir,fname)
	big_oh = theoretical(data,fname)

	plot(data,big_oh)

if __name__ == '__main__':
	main()