import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as const

hbar = const.hbar
m = (hbar**2)
k = 1
omg = np.sqrt(k/m)
gm = (omg*m)/hbar
x = np.linspace(-10,10,100)
def SI0(x):
    return (gm/np.pi)**(1/4)*np.exp(-(gm/2)*x**2)

def SI1(x):
    return (gm/np.pi)**(1/4) * np.sqrt(2*gm)* x *np.exp(-(gm/2)*x**2)

def SI2(x):
    return (1/np.sqrt(2)) * (gm/np.pi)**(1/4)*(2*gm*x**2-1)*np.exp(-(gm/2)*x**2)

x_f_0 = hbar/(2*m*omg)
x_f_1 = (3*hbar)/(2*m*omg)

V_0 = 0.5*m*omg**2 *x_f_0
V_1 = 0.5*m*omg**2 *x_f_1
plt.title("Task 4")
plt.plot(V_0, label = "V_0")
plt.plot(V_1, label = "V_1")
plt.plot(x, SI0(x), label = "PSI 1")
plt.plot(x, SI1(x), label = "PSI 2")
plt.plot(x, SI2(x), label = "PSI 3")
plt.grid()
plt.xlabel("x (nm)")
plt.ylabel("Psi (x)")
plt.legend()
plt.show()






