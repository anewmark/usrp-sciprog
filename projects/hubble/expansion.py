import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imread
import matplotlib.cbook as cbook
import os

currentdir = os.getcwd()

tab1 = np.genfromtxt('table1.txt', dtype='S')
CAT, NUMBER, R, V, RA, DEC = tab1[:,0], tab1[:,1], tab1[:,2].astype(np.float64), tab1[:,3].astype(np.float64), tab1[:,4], tab1[:,5]

plt.xlabel(r'$\mathregular{km\/s^{-1}}$', size=18)
plt.ylabel(r'$\mathregular{Mpc}$', size=18)
plt.tick_params(labelsize=16)

fun = False
if (fun):
	datafile = cbook.get_sample_data(currentdir + '/tm.png')
	img = imread(datafile)
	plt.imshow(img,zorder=0,extent=[1.1*V.min(), 1.1*V.max(), 0, 1.1*R.max()])
	plt.scatter(V, R, s=100, c='w', marker='*', zorder=1, edgecolor='b')
	plt.axes().set_aspect(500)
else:
	plt.scatter(V, R, s=50, c='r', marker='s', zorder=1, edgecolor='r')

plt.show()





