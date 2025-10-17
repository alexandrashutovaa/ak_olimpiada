import numpy as np
import matplotlib.pyplot as plt

def parse_sp3_file_simple(filename):
    times = []
    state_vectors = []
    
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        if line.startswith('*'):
            epoch_data = line[1:].split()
            hour = int(epoch_data[3])
            minute = int(epoch_data[4])
            
            total_minutes = hour * 60 + minute
            times.append(total_minutes)
            
            if i + 2 < len(lines):
                pos_line = lines[i + 1].strip()
                if pos_line.startswith('PL52'):
                    pos_data = pos_line.split()[1:4] 
                    position = [float(x) for x in pos_data]
                    
                    vel_line = lines[i + 2].strip()
                    if vel_line.startswith('VL52'):
                        vel_data = vel_line.split()[1:4] 
                        velocity = [float(x) for x in vel_data]
                        
                        state_vector = position + velocity
                        state_vectors.append(state_vector)
                
                i += 3 
            else:
                break
        else:
            i += 1
    
    start_time = times[0]
    times = [t - start_time for t in times]
    
    return np.array(times), np.array(state_vectors)


times, state_vectors = parse_sp3_file_simple("лагеос.txt")
dolg_res = []
for i in range (len(state_vectors)-1):
    pos_vel = state_vectors[i+1] - state_vectors[i]
    cosa = (pos_vel[0]*pos_vel[3] + pos_vel[1]*pos_vel[4] + pos_vel[2]*pos_vel[5])/(((pos_vel[0]**2 + pos_vel[1]**2 + pos_vel[2]**2)**0.5) * ((pos_vel[3]**2 + pos_vel[4]**2 + pos_vel[5]**2)**0.5))
    sina = (1 - cosa**2)**0.5
    dolg = ((pos_vel[0]**2 + pos_vel[1]**2 + pos_vel[2]**2)**0.5) * ((pos_vel[3]**2 + pos_vel[4]**2 + pos_vel[5]**2)**0.5) * sina
    dolg_res += [dolg]

fig, ax = plt.subplots(figsize=(10, 6))

ax.scatter(times[1:], dolg_res, linewidth=2)
plt.show()
