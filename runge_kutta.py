import matplotlib.pyplot as plt
import numpy as np

N = 100
x = np.linspace(0, 100, N)
h = x[1] - x[0]
res_euler = np.zeros(N)
res_euler[0] = 1

for i in range(1, N):
    res_euler[i] = res_euler[i - 1] + np.exp(x[i - 1]) * h

res_rk4 = np.zeros(N)
res_rk4[0] = 1

for i in range(1, N):
    k1 = np.exp(x[i-1])
    k2 = np.exp(x[i-1] + h/2) 
    k3 = np.exp(x[i-1] + h/2) 
    k4 = np.exp(x[i-1] + h) 
    
    res_rk4[i] = res_rk4[i-1] + (h/6) * (k1 + 2*k2 + 2*k3 + k4)

res_true = np.exp(x)

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(x, res_true, 'g-', linewidth=2)
ax.scatter(x, res_euler, c='red', s=50)
ax.scatter(x, res_rk4, c='blue', s=50)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()
ax.grid(True, alpha=0.3)
plt.show()