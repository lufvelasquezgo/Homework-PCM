import matplotlib.pyplot as plt
import numpy as np
import random

vel = np.array([2, 0])
pos_actualx = [0]
pos_actualy = [50]
aceleracion = -9.8
dt = 0.1


def verlet(pos_actual, pos_anterior, aceleracion, deltaT):
    return (2*pos_actual)-pos_anterior+aceleracion*deltaT**2


def euler(pos_actual, vel_actual, aceleracion, deltaT):
    return pos_actual+vel_actual*deltaT+0.5*aceleracion*deltaT**2


def grafica(pos_actualx, pos_actualy):
    plt.clf()
    plt.xlim(0, 8)
    plt.ylim(0, 60)
    plt.plot(pos_actualx, pos_actualy, color="green",
             marker='o', linestyle='None')
    plt.pause(0.1)


plt.ion()
plt.figure()
grafica(pos_actualx[-1], pos_actualy[-1])
pos_actualx.append(euler(pos_actualx, vel[0], 0, dt))
pos_actualy.append(euler(pos_actualy, vel[1], aceleracion, dt))

grafica(pos_actualx[-1], pos_actualy[-1])

while pos_actualy[-1] >= 0:
    pos_actualx.append(verlet(pos_actualx[-1], pos_actualx[-2], 0, dt))
    pos_actualy.append(
        verlet(pos_actualy[-1], pos_actualy[-2], aceleracion, dt))
    plt.clf()
    grafica(pos_actualx[-1], pos_actualy[-1])
