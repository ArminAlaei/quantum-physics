import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1001)
print(x)


# defining wavefunction
def wf(lbda, x_):
    if (x_ < 0):
        return np.sqrt(lbda) * np.exp(lbda * x_)
    else:
        return np.sqrt(lbda) * np.exp(-lbda * x_)


probdense = []

# Finding values for probability density for all values of x between -10 and 10
for i in range(len(x)):
    dense = wf(1, x[i]) * wf(1, x[i])
    probdense.append(dense)

plt.plot(x, probdense, 'r')
plt.vlines(1 / np.sqrt(2), -0.2, 1.2, 'y')
plt.vlines(-1 / np.sqrt(2), -0.2, 1.2)
plt.legend(['Bølgefunksjon', 'x0+sigma=1/sqrt(2)', 'x0-sigma=-1/sqrt(2)'])
plt.xlabel('Posisjon')
plt.ylabel('Sannsynlighetstetthet')
plt.show()

S = 0
# are under everything, to check if it is normalized to be = 1
for i in range(len(x)):
    dS = wf(1, x[i]) * wf(1, x[i]) * 20 / 1001
    S += dS
print(S)
area = np.linspace(-1 / np.sqrt(2), 1 / np.sqrt(2), 1001)
s = 0
# arealet mellom linjene
for i in range(len(area)):
    ds = wf(1, area[i]) * wf(1, area[i]) * 2 / (np.sqrt(2) * 1001)
    s += ds
print(s)