import numpy as np
import matplotlib.pyplot as plt
import math

def parse_gracefo_data(file_content):
    lines = file_content.strip().split('\n')
    
    times = []
    state_vectors = []
    
    for line in lines:
        # Ищем строки с данными (начинаются с цифр)
        if line.strip() and line[0].isdigit():
            parts = line.split()
            
            # Время (первая колонка)
            time = float(parts[0])
            times.append(time)
            
            # Координаты (колонки 4-6) и скорости (колонки 10-12)
            xpos, ypos, zpos = float(parts[3]), float(parts[4]), float(parts[5])
            xvel, yvel, zvel = float(parts[9]), float(parts[10]), float(parts[11])
            
            state_vectors.append([xpos, ypos, zpos, xvel, yvel, zvel])
    
    return np.array(times), np.array(state_vectors)

def calculate_kepler_elements(r, v, mu = 398600.4418):
    r = np.array(r)  # Вектор положения [X, Y, Z]
    v = np.array(v)  # Вектор скорости [VX, VY, VZ]

    L = np.cross(r, v)
    Lx, Ly, Lz = L

    N = np.cross([0, 0, 1], L)
    Nx, Ny, Nz = N

    cosL = Lz/np.linalg.norm(L)
    sinL = ((Lx**2 + Ly**2)**0.5)/np.linalg.norm(L)

    i = np.arctan2(sinL, cosL)  # i = atan2(sinL, cosL)
    Omega = np.arctan2(Ny, Nx)

    mod_r = np.linalg.norm(r)
    mod_v = np.linalg.norm(v)
    a = 1 / (2/mod_r - mod_v**2/mu)
    
    e_vec = np.cross(v, L)/mu - r/np.linalg.norm(r)
    e = np.linalg.norm(e_vec)

    return Omega, i, a, e

# ШАГ 3: ОСНОВНАЯ ПРОГРАММА

with open('gracefo.txt', 'r') as f:
    file_content = f.read()

# Парсим данные из файла
times, state_vectors = parse_gracefo_data(file_content)

Omega_res = []
i_res = []
a_res=[]
e_res=[]
mu=398600.4418
Re = 6378.1
    
for g in range(len(state_vectors)):
    r = state_vectors[g][:3]  
    v = state_vectors[g][3:]  
    Omega, i, a, e = calculate_kepler_elements(r, v, mu)
    Omega_res += [Omega]
    i_res += [i]
    a_res += [a]
    e_res += [e]
a = np.mean(a_res)
i = np.mean(i_res)
e = np.mean(e_res)

fig, ax = plt.subplots()
    
ax.scatter(times, Omega_res, s=1, alpha=0.7, color="blue")
ax.set_xlabel('Время (минуты)')
ax.set_ylabel('Долгота восходящего узла')
ax.grid(True, alpha=0.3)
k, b = np.polyfit(times, Omega_res, 1)
ax.plot(times, k*times + b, 'r-', linewidth=2, label=f'МНК: y={a:.4f}x+{b:.4f}')
print(k)
plt.show()
j2 = (2 * k * a**2 * (1 - e**2)**2)/(-3 * (mu/a**3)**0.5 * Re**2)
print(j2)