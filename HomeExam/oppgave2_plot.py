import numpy as np
import matplotlib.pyplot as plt
from scipy import constants
E1 = 1/4 #eV
E2 = 1 #eV
E3 = 9/4#eV
E4 = 4 #eV
energy = [0,E1,E2,E3,E4]
percents = [0,0.4,0.3,0.2,0.1]
a = 0.614#nm
x = np.linspace(-a,a)
T = 5
psi =[]
probden = []
for i in range(1,5):
    n = i
    psiXT = abs((np.sqrt(1/a) * np.sin((n*np.pi*x)/(2*a))*np.exp((-1j*energy[i]*T)/constants.hbar)) * np.sqrt(percents[i]))**2
    psi.append(psiXT)
    probden.append(abs(psiXT)**2)
probSum = sum(psi)
psi2 = abs((np.sqrt(1/a) * np.sin((2*np.pi*x)/(2*a))*np.exp((-1j*energy[2]*T)/constants.hbar)) * np.sqrt(percents[2]))**2
plt.plot(x,psi2, label = "E2")
plt.legend()
plt.plot(x,probSum)
plt.xlabel("x[nm]")
plt.ylabel("abs(Psi(x,t))^2")
plt.show()

