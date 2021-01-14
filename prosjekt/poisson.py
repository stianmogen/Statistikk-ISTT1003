from scipy import stats
import matplotlib.pyplot as plt

x = 0
lam = 1/8 * 15

P_punkt = stats.poisson.pmf(x, lam)

P_under = stats.poisson.cdf(x, lam)

P_over = 1 - P_under

print(P_over)

nr1 = stats.poisson.cdf(4, lam)
nr2 = stats.poisson.cdf(5, lam)
ans = nr2 - nr1
print(P_under)

#finn største

#xverdier=range(0,21)
#stats.poisson.pmf(xverdier, lam)

#fig, ax = plt.subplots()
#ax.bar(xverdier, stats.poisson.pmf(xverdier, lam))
#ax.grid()
#plt.show()
