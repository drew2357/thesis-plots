
# Figure 36
import numpy as np
import matplotlib.pyplot as plt
import seaborn
import matplotlib.patches as mpatches
x1 = []
y1 = []

data1 = np.genfromtxt('../Data/CaEPSPupSpineHHighESyn.dat',
                     skip_header=1,
                     names=None,
                     dtype='U',
                     delimiter=None)
#print(data)
for d1 in data1:
  y1.append(d1[0].astype(np.float))#Ca
  x1.append(d1[1].astype(np.float)+68)#V

plt.plot(x1, y1, 'r-')
plt.plot([0, 70], [0.0001, 0.0001], 'k-')
plt.plot([0, 70], [0.0002, 0.0002], 'k-')
plt.plot([0, 70], [0.0007, 0.0007], 'k-')
plt.plot([0, 70], [0.0008, 0.0008], 'k-')
plt.plot([0, 70], [0.0016, 0.0016], 'k-')
plt.plot([0, 70], [0.0017, 0.0017], 'k-')
plt.ylabel('Peak [$\mathregular{Ca^{2+}}$](mM)', fontsize=20)
plt.xlabel('EPSP Amplitude (mV)', fontsize=20)
plt.axis([0, 68, 0, 0.0018])
plt.show()
