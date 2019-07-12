import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from functions import *
style.use("classic")

vel = np.array([2, 0])
aceleration = np.array([0, -9.8])
dt = 0.1
Nsteps = 20
pos_actual = np.zeros((Nsteps + 2, 2))

pos_actual[0] = np.array([0, 50])
pos_actual[1] = euler(pos_actual[0], vel, aceleration, dt)

for i in range(2, Nsteps + 2):
    pos_actual[i] = verlet(
        pos_actual[i - 1], pos_actual[i - 2], aceleration, dt)

time = np.arange(0, Nsteps + 2) * dt
pos_actual = np.array(pos_actual)

x = pos_actual[0, 0] + vel[0] * time + aceleration[0] * time ** 2 / 2
y = pos_actual[0, 1] + vel[1] * time + aceleration[1] * time ** 2 / 2

# print(pos_actual)

plt.figure()
plt.plot(pos_actual[:, 0], pos_actual[:, 1], "og", label="Verlet")
plt.plot(x, y, "--r", label="Theoretical")
plt.grid()
plt.xlabel(r"$x \rm [m]$", fontsize=20)
plt.ylabel(r"$y \rm [m]$", fontsize=20)
plt.legend(loc="best")
plt.title('Projectile motion', fontsize=30)
plt.tight_layout()
plt.savefig("parab_verlet.pdf")
plt.close()
