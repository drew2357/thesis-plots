#Figure 34:
#Neck 0.02 x 0.0942
#Ca peak  0.00116774
import numpy as np
import matplotlib.pyplot as plt
import seaborn
import matplotlib.patches as mpatches
x1 = []
y1 = []
x2 = []
y2 = []
data1 = np.genfromtxt('../Data/harnettScaleDend.dat',
                     skip_header=1,
                     names=None,
                     dtype='U',
                     delimiter=None)
#print(data)
for d1 in data1:
  y1.append(d1[1].astype(np.float))#EPSP
  x1.append(d1[0].astype(np.float))#time
#
data2 = np.genfromtxt('../Data/Spine450BSynMatchHarnettSecond.dat',
                     skip_header=1,
                     names=None,
                     dtype='U',
                     delimiter=None)
#print(data)
max = 0
for d2 in data2:
  x2.append(d2[0].astype(np.float)-100)#time
  y2.append(d2[2].astype(np.float)+68)#Vdend
plt.plot(x1, y1, 'r-', x2, y2, 'b-')
red_patch = mpatches.Patch(color='red', label='$\mathregular{EPSP_{dend}}$ due to glutamate uncaging from Harnett et al.')
blue_patch = mpatches.Patch(color='blue', label='$\mathregular{EPSP_{dend}}$ from Synapse in model')
plt.legend(handles=[red_patch, blue_patch])
#plt.plot(x1, y1, 'r-')
#plt.scatter(x, y, c=z, s=200, cmap='Blues')
plt.ylabel('$\mathregular{V_{dend}}$', fontsize=20)
plt.xlabel('time (ms)', fontsize=20)
plt.axis([0, 40, 0, 2])
plt.show()
