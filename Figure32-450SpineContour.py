#Figure 32
import numpy as np
import matplotlib.pyplot as plt
import seaborn
import matplotlib.cm as cm
from matplotlib.collections import LineCollection
xlist = np.linspace(0.0001, 0.55, 100)#(0.05, 0.55, 100)
ylist = np.linspace(0, 2, 100)#(0.1, 1.7, 100)
X, Y = np.meshgrid(xlist, ylist)
Z =  ((1500000*Y)/(np.pi*((X/2)**2)))/1000000
plt.xlabel('diam ($\mu$m)', fontsize=20)
plt.ylabel('length ($\mu$m)', fontsize=20)
levels = [450]#[7, 15, 30, 60, 125, 250, 500, 1000]
contour = plt.contour(X, Y, Z, levels, colors='k')
plt.clabel(contour, colors = 'k', fmt = '%2.1f', fontsize=15)
plt.plot([0.02, 0.077], [0.0942, 1.397], 'ro')
levels = np.arange(-1.2, 1.6, 0.2)
plt.axis([0, 0.1, 0, 2])
#plt.title('$\mathregular{R_{neck}}$ for 150$\Omega$cm cytoplasm', fontsize=30)
plt.show()
