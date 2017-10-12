# Figure 35:
#Ca from EPSPdend matching Harnett
import matplotlib.pyplot as plt
import seaborn
import matplotlib.patches as mpatches
import numpy as np
from scipy.interpolate import UnivariateSpline
plt.rcParams["legend.fontsize"] = 15
x=[33,172,305,450,500]
y=[0.00002698, 0.0001, 0.00041, 0.00116, 0.00138]
plt.scatter(x, y)
black_patch = mpatches.Patch(color='black', label='Peak [$\mathregular{Ca^{2+}}$]$_{spine}$ due to EPSP from $\mathregular{I_{inj}}$ matching Harnett et al.')
red_patch = mpatches.Patch(color='red', label='Curve of best fit for relationship between R$_{neck}$ and Peak [$\mathregular{Ca^{2+}}$]$_{spine}$')
s = UnivariateSpline(x, y, s=16, k=2)
xs = np.linspace(33, 500, 100)
ys = s(xs)
plt.plot(xs, ys, 'r-')
#plt.scatter(x, y)
plt.legend(handles=[black_patch, red_patch])
plt.plot([0, 500], [0.00115, 0.00115], 'k-')
plt.ylabel('Peak [$\mathregular{Ca^{2+}}$]$_{spine}$ (mM)', fontsize=20)
plt.xlabel('$\mathregular{R_{neck}}$ (M$\Omega$)', fontsize=20)
plt.axis([0, 500, 0, 0.0015])
plt.show()
