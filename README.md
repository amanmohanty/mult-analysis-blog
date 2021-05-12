# Analysis of Large Integer Multiplication Algorithms
#### Blog post for CMU 18-647 course
#### Author: Aman Mohanty
#### Contact: amanmoha@andrew.cmu.edu

Implementation of analysis of large scale integer multiplication algorithms. Algorithms covered:
1. Quadratic
2. Karatsuba
3. FFT
4. Python intrinsic multiplication operator

All experiments were conducted on Pittsburgh Supercomputing Center's Bridges2 supercomputer.
Requires Python 3.

To run an experiment: `python multiplication.py --algorithm 'fft' --N 1024`
Add `--write_data` and `--write_dir <directory name>` to save results in csv format. Check `utils.py` for command line arguments options.

To plot results: `python plot.py --data_dir <directory name> --algorithm 'intrinsic fft' --log_scale --save_fname 'int_fft.png'`. This loads the intrinsic and fft data from `<directory name>`, plots the results in log scale and saves the plot in current directory. To plot all the algorithms, remove `--algorithm`. Remove `--log_scale` to plot in normal scale. Remove `--save_fname` to visualize the plot.

`blog_post.pdf` is the writeup.