import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

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
    r = r = np.linalg.norm(vector[:3])
    aceleration = np.array(-mu/r**3 * vector[:3])
    return np.concatenate([vector[3:6], aceleration])

def rk_step(f, vector, dt, t0):
    k1 = f(vector, t0)
    k2 = f(vector + 0.5*dt*k1, t0 + dt/2)
    k3 = f(vector + 0.5*dt*k2, t0 + dt/2)  
    k4 = f(vector + dt*k3, t0 + dt)
    vector += (k1 + 2*k2 + 2*k3 + k4 )/6
    return vector, t0+dt
     
def zadacha(vector, dt, t0):
    t = []
    vectors = []
    vector = vector.astype(np.float64)
    vectors.append(vector.copy())
    t.append(0)
    for i in range (int(t0//dt)):
        vector_now, t_now = rk_step(f, vectors[-1], dt, t[-1])
        vectors.append(vector_now.copy())
        t.append(t_now)

    if check_time(dt, t0) != 0:
        vector_now, t_now = rk_step(f, vectors[-1], check_time(dt, t0), t[-1])
        vectors.append(vector_now.copy())
        t.append(t_now)
    return t, vectors

res_time, res_vector = zadacha(vector, 1, 100000)
np_vector = np.array(res_vector)
arr_x = np_vector[:, 0]
arr_y = np_vector[:, 1]

fig, ax = plt.subplots()
ax.plot(arr_x, arr_y)
ax.set_xlabel('X')
ax.set_ylabel('Y')
plt.show()