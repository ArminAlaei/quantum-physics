import numpy as np
import matplotlib.pyplot as plt
from scipy import constants


def psi(x,t,n,a, h):
    return np.sqrt(2/a) *np.sin((n*np.pi*x)/a)*np.exp(-np.imag(-1)*((n**2*np.pi**2*h))/2*m*a**2)*t
x = np.linspace(0,10)
a = 1
m = 0.511/constants.c
t = np.linspace(0,10)
n = 3
h =constants.hbar
plt.plot(psi(x,t,n,a,h))
plt.title("Time development, n = 3")
plt.xlabel("Time")
plt.ylabel("Psi(x,t)")
plt.show()


