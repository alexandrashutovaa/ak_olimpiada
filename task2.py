import matplotlib.pyplot as plt
import numpy as np
import math

def runge(f, x0, t0, t1, h):
    x = x0
    t = t0
    n = int((t1 - t0) / h)
    res = []
    res += [[t, x]]
    for i in range(1, n+1):
        temp = t
        t += h
        k1 = h * f(temp)
        k2 = h * f(temp + h / 2)
        k3 = h * f(temp + h / 2)
        k4 = h * f(temp + h)
        x += (k1 + 2*k2 + 2*k3 + k4 )/6
        res += [[t, x]]
    return res

def euler(f, x0, t0, t1, h):
    x = x0
    t = t0
    n = int((t1 - t0) / h)
    res = []
    res += [[t, x]]
    for i in range (1, n+1):
        temp = t
        t += h
        x += f(temp)*h
        res += [[t, x]]
    return res

def f1(t):
    return t**3/2


print("Тест")
result_runge = runge(f1, 1.0, 0.0, 2.0, 0.1)
os_x = [l[0] for l in result_runge]
os_y = [l[1] for l in result_runge]
result_euler = euler(f1, 1.0, 0.0, 2.0, 0.1)
os_x2 = [l[0] for l in result_euler]
os_y2 = [l[1] for l in result_euler]

x = np.linspace(0, 2, 21)

real = [t**4/8 + 1 for t in os_x]

#print(real)


fig, ax = plt.subplots()

ax.scatter(os_x, os_y, color = "blue")
ax.plot(os_x, real, color = "black")
ax.scatter(os_x2, os_y2, color = "red")
plt.show()

