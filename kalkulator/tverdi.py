import numpy as np
from scipy import stats
from math import sqrt

xbar= 754.3
xnew = 64.9
alpha=0.05 #hvis det er 95% konfidensintervall, skriv inn 0.05
n= 30


S = sqrt(xnew / (n-1))
alphahalve=alpha/2
zalphahalve=stats.norm.ppf(1-alphahalve) # sannsynlighet alpha/2 til høyre har 1-alpha/2 til venstre
talpha = 2.048
print(talpha)

nedre=xbar - (talpha * S / sqrt(n)) #fyll ut resten selv
print("nedre ", nedre)
ovre=xbar + (talpha * S / sqrt(n))# fyll ut resten selv
print("øvre ", ovre)