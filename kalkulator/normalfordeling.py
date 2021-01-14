from scipy import stats
from math import  sqrt
x = 4 #hva vi tester
forv = 8 #forventningsverdi, u
stand = 5/sqrt(9) #standardavvik, o


less = stats.norm.cdf(x, forv, stand) #mindre enn
more = 1 - less

print(less)