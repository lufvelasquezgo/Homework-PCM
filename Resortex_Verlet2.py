import matplotlib.pyplot as plt
import numpy as np
from functions import *
from matplotlib import style
style.use("classic")

k = 1.5
m = 1
dt = 0.1
final_time = 15
Nsteps = int(final_time / dt)
positions = np.zeros(Nsteps + 2)

positions[0] = 5
aceleracion = compute_spring_force(positions[0], k) / m
positions[1] = euler(positions[0], 0, aceleracion, dt)

for i in range(2, Nsteps + 2):
    aceleracion = compute_spring_force(positions[i - 1], k) / m
    positions[i] = verlet(positions[i - 1], positions[i - 2], aceleracion, dt)

times = np.arange(0, Nsteps + 2) * dt
positions_teo = positions[0] * np.cos(times * np.sqrt(k / m))

plt.figure()
plt.plot(times, positions, "o", label='Verlet')
plt.plot(times, positions_teo, "--r", label='Theoretical')
plt.xlabel(r'$time \rm [s]$')
plt.ylabel(r'$x \rm [m]$')
plt.legend(loc='best')
plt.grid()
plt.tight_layout()
plt.title('Spring-mass system', fontsize=30)
plt.savefig("resorte.pdf")
plt.close()
