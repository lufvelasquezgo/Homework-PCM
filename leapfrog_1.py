# LEAPFROG ALGORITHM

import numpy as np
from matplotlib import pyplot as plt
from functions import euler_velocity, leapfrog_integration
from matplotlib import style
style.use("classic")

Nsteps = 30
aceleration = np.array([0.0, -9.8])  # m / s^2
dt = 0.1  # s

velocities_half = np.zeros(shape=(Nsteps + 1, 2))
positions = np.zeros(shape=(Nsteps + 1, 2))

positions[0] = np.array([0, 50])  # m
initial_velocity = np.array([2, 0])


velocity_before = euler_velocity(initial_velocity, aceleration, dt)
velocities_half[0] = velocity_before

for i in range(1, Nsteps + 1):
    velocities_half[i], positions[i] = leapfrog_integration(
        positions[i - 1], velocities_half[i - 1], aceleration, dt)


time = np.arange(Nsteps + 1) * dt

x = positions[0, 0] + initial_velocity[0] * \
    time + aceleration[0] * time ** 2 / 2
y = positions[0, 1] + initial_velocity[1] * \
    time + aceleration[1] * time ** 2 / 2


plt.figure()
plt.plot(positions[:, 0], positions[:, 1], color='green', linewidth=2.0,
         label='Leapfrog')
plt.plot(x, y, color='purple', marker='^', linestyle='None',
         label='Theoretical')
plt.legend(loc='best')
plt.xlabel(r"$x \rm [m]$", fontsize=20)
plt.ylabel(r"$y \rm [m]$", fontsize=20)
plt.title('Projectile motion', fontsize=30)
plt.grid()
# plt.gca().set_aspect('equal')
plt.savefig('x_vs_y.pdf')
plt.close()
