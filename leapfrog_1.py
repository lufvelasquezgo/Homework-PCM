# LEAPFROG ALGORITHM

import numpy
from matplotlib import pyplot

Nsteps = 30
gravity = numpy.array([0.0, -9.8]) # m / s^2
dt = 0.1 # s

velocities_half = numpy.zeros(shape=(Nsteps + 1, 2))
positions = numpy.zeros(shape=(Nsteps + 1, 2))

positions[0] = numpy.array([0, 50]) # m
initial_velocity = numpy.array([2, 0])

# Euler method to get the update half a time velocity.

def euler_method(velocity, gravity, dt):
    velocity_half_time = velocity - 0.5 * gravity * dt
    return velocity_half_time

# Leapfrog algorithm to get the update position and update velocity.

def leapfrog_integration(position, velocity_before, gravity, dt):
    new_velocity_half = velocity_before + gravity * dt
    new_position = position + new_velocity_half * dt
    return new_velocity_half, new_position

velocity_before = euler_method(initial_velocity, gravity, dt)
velocities_half[0] = velocity_before

for i in range(1, Nsteps + 1):
    velocities_half[i], positions[i] = leapfrog_integration(positions[i - 1], 
    velocities_half[i - 1], gravity, dt)

times = numpy.arange(Nsteps + 1) * dt

x = times * 2
y = 50 - 0.5 * 9.8 * times * times

pyplot.figure()
pyplot.plot(times, positions[:, 0], color='magenta', linewidth=2.0,
            label='Algorithm')
pyplot.plot(times, x, color='cyan', marker='^', linestyle='None',
            label='Theoretical')
pyplot.legend(loc='best')
pyplot.xlabel('$time$ (s)')
pyplot.ylabel('$position_{x}$ (m)')
pyplot.grid()
# pyplot.gca().set_aspect('equal')
pyplot.savefig('x_vs_t.pdf')
pyplot.close()

pyplot.figure()
pyplot.plot(times, positions[:, 1], color='blue', linewidth=2.0,
            label='Algorithm')
pyplot.plot(times, y, color='red', marker='^', linestyle='None',
            label='Theoretical')
pyplot.legend(loc='best')
pyplot.xlabel('$time$ (s)')
pyplot.ylabel('$position_{y}$ (m)')
pyplot.grid()
# pyplot.gca().set_aspect('equal')
pyplot.savefig('y_vs_t.pdf')
pyplot.close()

pyplot.figure()
pyplot.plot(positions[:, 0], positions[:, 1], color='green', linewidth=2.0,
            label='Algorithm')
pyplot.plot(x, y, color='purple', marker='^', linestyle='None',
            label='Theoretical')
pyplot.legend(loc='best')
pyplot.xlabel('$position_x$ (m)')
pyplot.ylabel('$position_y$ (m)')
pyplot.grid()
# pyplot.gca().set_aspect('equal')
pyplot.savefig('x_vs_y.pdf')
pyplot.close()