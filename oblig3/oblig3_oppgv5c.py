import numpy
import matplotlib.pyplot as plt
import numpy as np
N = 2000
k_1 = -5
k_2 = 5
k = np.linspace(k_1,k_2,N)
A = 2/(k**2+2**2)
m = 1
w = np.sqrt((k)**2 + m**2)

time = 1000

dt = 0.01
y1 = np.zeros((N))
y2 = np.zeros((N))
y = np.zeros((N))
t = np.zeros((N))
x = np.linspace(0,2000,N)

cossum = np.zeros((N))
for i in range(1,N-1):
    cossum +=  A* np.sin((k*x[i]) - (w*t[i]) )
    t[i + 1] = t[i] + dt


plt.plot(t,cossum)
plt.grid()
plt.ylabel('Amplitude')
plt.xlabel('Time')
plt.show()

