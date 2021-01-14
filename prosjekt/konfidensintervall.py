import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from math import sqrt

xbar= 0.125
stand= 0.04677
alpha= 0.05 #hvis det er 95% konfidensintervall, skriv inn 0.05
n= 1

alphahalve=alpha/2
zalphahalve=stats.norm.ppf(1-alphahalve) # sannsynlighet alpha/2 til høyre har 1-alpha/2 til venstre
print(zalphahalve)

nedre=xbar - (zalphahalve * stand / sqrt(n)) #fyll ut resten selv
print("nedre ", nedre)
ovre=xbar + (zalphahalve * stand / sqrt(n))# fyll ut resten selv
print("øvre ", ovre)




def breddefunc(n):
  return(2*zalphahalve*stand/np.sqrt(n))

nverdier=np.arange(1,40)

fig, ax = plt.subplots()
ax.plot(nverdier, breddefunc(nverdier), '.-')
ax.set_xlim(20, 35)
ax.set_ylim(0.1, 0.2)
ax.set_xlabel('n')
ax.set_ylabel('bredde')
ax.hlines(y=0.11, xmin=1, xmax=40, linewidth=2, color='r')
#ax.grid()
#plt.show()