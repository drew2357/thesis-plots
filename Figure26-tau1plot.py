#Figure 26
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
import seaborn
import matplotlib.patches as mpatches
x1 = []
y1 = []
plt.rcParams["legend.fontsize"] = 18
data1 = np.genfromtxt('../Data/Spine3Tau1change.dat',
                     skip_header=1,
                     names=None,
                     dtype='U',
                     delimiter=None)
#
for d1 in data1:
  x1.append(d1[0].astype(np.float))#time
  y1.append(d1[1].astype(np.float))#Vdend
blue_patch = mpatches.Patch(color='blue', label='$\mathregular{R_{neck}}$ Estimate from varying $\mathregular{\\tau_{1}}$')
black_patch = mpatches.Patch(color='black', label='True $\mathregular{R_{neck}}$ (33M$\Omega$)')
plt.legend(handles=[blue_patch, black_patch])
plt.plot(x1, y1, 'b-')
plt.plot([0, 100], [33, 33], 'k-')
plt.xlabel('$\mathregular{\\tau_{1}}$ (ms)',fontsize=20)
plt.ylabel('R (M$\Omega$)',fontsize=20)
plt.axis([0, 10, 30, 42])
plt.show()
