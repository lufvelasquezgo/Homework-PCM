# LEAPFROG ALGORITHM

import numpy as np
from matplotlib import pyplot as plt
from functions import *
from matplotlib import style
style.use("classic")

Nsteps = 50
dt = 0.1  # s
k = 1.5
m = 1
final_time = 15
Nsteps = int(final_time / dt)

velocities_half = np.zeros(shape=(Nsteps + 1))
positions = np.zeros(shape=(Nsteps + 1))
acelerations = np.zeros(shape=(Nsteps + 1))

positions[0] = 5  # m
initial_velocity = 0.0  # m / s

acelerations[0] = compute_spring_force(positions[0], k) / m
velocities_half[0] = euler_velocity(initial_velocity, acelerations[0], dt)
for i in range(1, Nsteps + 1):
    velocities_half[i], positions[i] = leapfrog_integration(
        positions[i - 1], velocities_half[i - 1], acelerations[i - 1], dt)
    acelerations[i] = compute_spring_force(positions[i], k) / m

times = np.arange(Nsteps + 1) * dt
positions_teo = positions[0] * np.cos(times * np.sqrt(k / m))

plt.figure()
plt.plot(times, positions, '*g', label='Leapfrog')
plt.plot(times, positions_teo, "--r", label='Theoretical')
plt.legend(loc='best')
plt.xlabel(r'$time \rm [s]$', fontsize=20)
plt.ylabel(r'$x \rm [m]$', fontsize=20)
plt.title('Spring-mass system', fontsize=30)
plt.grid()
plt.tight_layout()
plt.savefig('oscilator.pdf')
plt.close()
