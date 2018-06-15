import scipy.special as sp
import matplotlib.pyplot as plt
import numpy as np
import math

dx = float(input('Enter your increment: '))

lb = float(input('Enter your lower bound: '))

ub = float(input('Enter your upper bound: '))


# creating an np array of numbers between -3.83 and 3.83 in increments of 0.01

x = np.arange(lb, ub, dx)

y = np.arange(lb, ub, dx)

# x = np.arange(-3.83, 3.83, 0.01)

# y = np.arange(-3.83, 3.83, 0.01)

# creating a 2d array in which to store the values (x and y) in

I_theta_arr = np.zeros((len(x), len(y)))

# r = 1.0

# initialising the counters for i and j at 0

ci = 0

cj = 0

# to give us a better looking graph, we use log base 10 so we can see the
# contrast difference a bit more clearly

# within the loop, the loop starts with the 0'th value of x
# cj is initialised as 0 within the first loop
# via progression, ci (ci[0]) is put into the loop, and cj (cj[0])
# cj is then incremented, to 1
# ci is then incremented, to 1
# the loop repeats

# what could be added is a clause that says for r <= 10**-10 r = 0.01? (small)


for i in x:

    cj = 0

    for j in y:

        r = x[ci]**2 + y[cj]**2

        I_theta_arr[ci][cj] = math.log(((2 * sp.j1(r) / r) ** 2), 10)

        cj = cj+1

    ci = ci+1

# these help make the lengths more identifiable, can be uncommented if needed

# print(r)
#
# print(I_theta_arr)
# print(I_theta_arr.size)
# print(x.size)
# print(y.size)
# print(r.size)


# setup the 2D grid with Numpy
x, y = np.meshgrid(x, y)

# convert intensity (list of lists) to a numpy array for plotting

I_theta_arr = np.array(I_theta_arr)

# plug the data into pcolourmesh!
plt.pcolormesh(x, y, I_theta_arr.T)
plt.colorbar()  # need a colourbar to show the intensity scale
plt.show()

