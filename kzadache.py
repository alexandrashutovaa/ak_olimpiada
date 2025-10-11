import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math

G = 0
M = 0
mu = 3.986e14
x0, y0, z0 = 6400e3, 0, 0,
vector = np.array([x0, y0, z0])
vx, vy, vz = 0, 7700, 0
velocity = np.array([vx, vy, vz])

def check_time(dt, t0):
    if (t0 / dt) != (t0 // dt):
        return t0 - (t0 // dt)*dt
    else:
        return 0
    
def zadacha(vector, velocity, dt, t0):
    t = []
    vectors = []
    vector = vector.astype(np.float64)
    velocity = velocity.astype(np.float64)
    for n in range (int(t0 // dt)):
        x, y, z = vector
        r = (x**2 + y**2 + z**2)**0.5
        vector_add = np.array([velocity[0]*dt, velocity[1]*dt, velocity[2]*dt])
        aceleration = np.array([-mu/r**3 * vector[0], -mu/r**3 * vector[1], -mu/r**3 * vector[2]])
        vector += vector_add
        t.append(dt * n)
        vectors.append(vector.copy())
        velocity += aceleration*dt

    if check_time(dt, t0) != 0:
        vectors.append(vector + np.array([vx*check_time(dt, t0), vy*check_time(dt, t0), vy*check_time(dt, t0)]))
        t.append(t0 - check_time(dt, t0))
    return t, vectors

res_time, res_vector = zadacha(vector, velocity, 3, 10000)
arr_x = [vec[0] for vec in res_vector]
arr_y = [vec[1] for vec in res_vector]
fig, ax = plt.subplots()

# Поверхность
ax.plot(arr_x, arr_y)
ax.set_xlabel('X')
ax.set_ylabel('Y')
plt.show()