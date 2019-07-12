# LEAPFROG ALGORITHM

import numpy
from matplotlib import pyplot

Nsteps = 50
dt = 0.1 # s
constant_k = 2.5 

velocities_half = numpy.zeros(shape=(Nsteps + 1, 2))
positions = numpy.zeros(shape=(Nsteps + 1, 2))
forces = numpy.zeros(shape=(Nsteps + 1, 2))

positions[0] = numpy.array([5, 0]) # m
initial_velocity = numpy.array([0, 0]) # m / s

def force(constant_k, positions):
    new_force = - constant_k * positions
    return new_force

# Euler method to get the update half a time velocity.

def euler_method(velocity, new_force, dt):
    velocity_half_time = velocity - 0.5 * new_force * dt
    return velocity_half_time

# Leapfrog algorithm to get the update position and update velocity.

def leapfrog_integration(position, velocity_before, new_force, dt):
    new_velocity_half = velocity_before + new_force * dt
    new_position = position + new_velocity_half * dt
    return new_velocity_half, new_position

force_before = force(constant_k, positions[0])
forces[0] = force_before
velocity_before = euler_method(initial_velocity, force_before, dt)
velocities_half[0] = velocity_before

for i in range(1, Nsteps + 1):
    velocities_half[i], positions[i] = leapfrog_integration(positions[i - 1], 
    velocities_half[i - 1], forces[i - 1], dt)
    forces[i] = force(constant_k, positions[i])

times = numpy.arange(Nsteps + 1) * dt

pyplot.figure()
pyplot.plot(times, positions[:, 0], color='crimson', marker='*')
pyplot.xlabel('$time$ (s)')
pyplot.ylabel('$position_{x}$ (m)')
pyplot.grid()
pyplot.savefig('oscilator.pdf')
pyplot.close()