import numpy
import matplotlib.pyplot as plt
import numpy as np

k_1 = 0.6
k_2 = 0.7
A = 1
m = 1
w_1 = np.sqrt((k_1)**2 + m**2)
w_2 = np.sqrt((k_2)**2 + m**2)
time = 1000
N = 200000
dt = 0.01
y1 = np.zeros((N))
y2 = np.zeros((N))
y = np.zeros((N))
t = np.zeros((N))
x = np.linspace(0,2000,N)

for i in range(1,N-1):
    y1[i+1]=  A* np.sin((k_1*x[i]) - (w_1*t[i]) )
    y2[i+1]=  A* np.sin((k_2*x[i]) - (w_2*t[i]) )
    t[i+1] = t[i] + dt
    y[i+1] = y1[i]+y2[i]

plt.plot(t,y)
plt.grid()
plt.ylabel('Amplitude')
plt.xlabel('Time')
plt.show()
v_1f = np.sqrt((k_1)**2 + m**2)/k_1
v_2f = np.sqrt((k_2)**2 + m**2)/k_2
v_1g = 1/v_1f
v_2g = 1/v_2f
print('phase velocity wave 1: ', v_1f)
print('phase velocity wave 2: ', v_2f)
print('group velocity wave 1: ', v_1g)
print('group velocity wave 2: ', v_2g)




