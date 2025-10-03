import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math

G = 0
M = 0
mu = 3.986e14
def zadacha(x0, y0, z0, vx, vy, vz, dt, t0):
    t = []
    x = []
    y = []
    z = []
    for n in range (t0 // dt):
        r = (x0**2 + y0**2 + z0**2)**0.5
        x_p = vx
        y_p = vy
        z_p = vz
        vx_p = -mu/r**3 * x0
        vy_p = -mu/r**3 * y0
        vz_p = -mu/r**3 * z0
        x_now = x0 + x_p * dt + (vx_p * dt**2)/2
        y_now = y0 + y_p * dt + (vy_p * dt**2)/2
        z_now = z0 + z_p * dt + (vz_p * dt**2)/2
        t += [dt * n]
        x += [x_now]
        y += [y_now]
        z += [z_now]
        x0 = x_now
        y0 = y_now
        z0 = z_now
        vx += vx_p * dt
        vy += vy_p * dt
        vz += vz_p * dt
    return [[t], [x], [y], [z]]

result = zadacha(6400e3, 0, 0, 0, 7700, 0, 1, 10000)

print(result[1])
fig, ax = plt.subplots()

# Поверхность
ax.plot(result[1][0], result[2][0])
ax.set_xlabel('X')
ax.set_ylabel('Y')
plt.show()