#Figure 27
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
import seaborn
import matplotlib.patches as mpatches
x1 = []
y1 = []
x2 = []
y2 = []
#synaptic stimulation
data1 = np.genfromtxt('../Data/Spine3ForTCslow.dat',
                     skip_header=1,
                     names=None,
                     dtype='U',
                     delimiter=None)
#print(data)
max = 0
for d1 in data1:
  x1.append(d1[0].astype(np.float)-100)#time
  y1.append(d1[1].astype(np.float)+68)#Vspine
  if d1[3].astype(np.float)>max:
    max = d1[3].astype(np.float)
print (max)
#

#current injection on dendrite
data2 = np.genfromtxt('../Data/Spine3ForTCfast.dat',
                     skip_header=1,
                     names=None,
                     dtype='U',
                     delimiter=None)
#print(data)
max = 0
for d2 in data2:
  x2.append(d2[0].astype(np.float)-100)#time
  y2.append(d2[1].astype(np.float)+68)#Vspine
  if d2[3].astype(np.float)>max:
    max = d2[3].astype(np.float)
#
plt.plot(x1, y1, 'b-',x2, y2, 'r-')
#plt.plot(xs, ys)
#plt.scatter(x, y)
plt.ylabel('$\mathregular{V_{spine}}$ (mV)', fontsize=20) # $\mathregular{EPSP^{spine}}$
red_patch = mpatches.Patch(color='red', label='EPSP spine due to fast EPSC estimate')
blue_patch = mpatches.Patch(color='blue', label='EPSP spine due to slow EPSC estimate')
plt.legend(handles=[red_patch, blue_patch])
#plt.legend(handles=[blue_patch])
plt.xlabel('time (ms)', fontsize=20)
plt.axis([0, 100, 0, 50])
#plt.title('Poorly matched EPSPs giving simmilar peak [$\mathregular{Ca^{2+}}$] in spine head',fontsize=30)
plt.show()
#gives65Mohm instead of 33
