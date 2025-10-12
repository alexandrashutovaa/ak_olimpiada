import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math

mu = 3.986e14
x0, y0, z0 = 6400e3, 0, 0
vx, vy, vz = 0, 7700, 0
vector = np.array([x0, y0, z0, vx, vy, vz])

def check_time(dt, t0):
    if (t0 / dt) != (t0 // dt):
        return t0 - (t0 // dt)*dt
    else:
        return 0
    
def f(vector, t):
    r = (vector[0]**2 + vector[1]**2 + vector[2]**2)**0.5
    aceleration = np.array(-mu/r**3 * vector[:3])
    return np.concatenate([vector[3:6], aceleration])

def runge(f, vector0, dt, t0):
    vector = vector0
    t = t0
    res_vector_runge = [vector0.copy()]
    res_time_runge = [0]
    for i in range(int((t0//dt))):
        t = res_time_runge[-1]
        k1 = f(vector, t)
        k2 = f(vector + 0.5*dt*k1, t + dt/2)
        k3 = f(vector + 0.5*dt*k2, t + dt/2)  
        k4 = f(vector + dt*k3, t + dt)
        vector += (k1 + 2*k2 + 2*k3 + k4 )/6
        res_vector_runge.append(vector.copy())
        res_time_runge.append(t + dt)
    return res_vector_runge, res_time_runge
    
    
def zadacha(vector, dt, t0):
    t = []
    vectors = []
    vector = vector.astype(np.float64)
    vectors, t = runge(f, vector, dt, t0)
    if check_time(dt, t0) != 0:
        vectors.append(vector[:3] + np.array(check_time(dt, t0)*vector[3::]))
        t.append(t0 - check_time(dt, t0))
    return t, vectors

res_time, res_vector = zadacha(vector, 1, 100000)
arr_x = [vec[0] for vec in res_vector]
arr_y = [vec[1] for vec in res_vector]

fig, ax = plt.subplots()
ax.plot(arr_x, arr_y)
ax.set_xlabel('X')
ax.set_ylabel('Y')
plt.show()