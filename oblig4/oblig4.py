import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5,5,100)
lmbd = 1
pdf = []

for i in range(len(x)):
    if x[i] < 0:
        fun = np.sqrt(lmbd) * np.exp(lmbd * x[i])
        pdf.append(fun*fun)
    else:
        fun = np.sqrt(lmbd) * np.exp(-lmbd * x[i])
        pdf.append(fun*fun)

plt.plot(x,pdf,label = 'PDF')
plt.vlines(-1/np.sqrt(2), -0.2,1,'g',label='x1')
plt.vlines(1/np.sqrt(2),-0.2,1,'g',label='x2')
plt.xlabel('x')
plt.title("Probability density with standard deviation")
plt.legend()
plt.ylabel('|Ψ(x,t)|^2')
plt.show()

