from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

H0=10
stand= 1
alpha=0.05
n=20

def k(n):
  return(H0 + stats.norm.ppf(1 - alpha) * stand / np.sqrt(n))

dennek=k(n)
print(dennek)

H1=11

# hvilke av disse to er riktig styrke?
styrke1=stats.norm.cdf(dennek, loc=H1, scale=stand / np.sqrt(n))
styrke2=1-stats.norm.cdf(dennek, loc=H1, scale=stand / np.sqrt(n))
print("styrke1=",styrke1)
print("styrke2=",styrke2)


nverdier=np.array([1.,10.,25.,50.])

fig, ax = plt.subplots()
ax.plot(nverdier, k(nverdier), '.-')
ax.set_xlabel('n')
ax.set_ylabel('k')
ax.grid()
plt.show()

muH1sann=33
print(nverdier)

for n in nverdier:
    print(1-stats.norm.cdf(dennek,loc=muH1sann,scale=stand/np.sqrt(n)))