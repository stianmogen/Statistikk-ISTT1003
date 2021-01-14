from scipy import stats
import matplotlib.pyplot as plt

x = 2 # hvor mange suksess
n = 5 # antall forsøk
p = 1/15 # sans for suksess

P_punkt = stats.binom.pmf(x, n, p)
P_less = stats.binom.cdf(x, n, p)
P_more = 1 - P_less

print(P_punkt)

start = 0
slutt = 26
xverdier=range(start,slutt) # få en oversikt over alle punktsansynligheter (oppgitt i jupyter notatbok)
arr = stats.binom.pmf(xverdier, n, p)
#print(arr)

fig, ax = plt.subplots()
ax.bar(xverdier, arr)
ax.grid()
#plt.show()
