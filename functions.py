def verlet(pos_actual, pos_anterior, aceleration, deltaT):
    return (2 * pos_actual) - pos_anterior + aceleration * deltaT ** 2


def euler(pos_actual, vel_actual, aceleration, deltaT):
    return pos_actual + vel_actual * deltaT + 0.5 * aceleration * deltaT ** 2


def euler_velocity(velocity, aceleration, dt):
    """
    Euler method to get the update half a time velocity.
    """

    velocity_half_time = velocity - 0.5 * aceleration * dt
    return velocity_half_time


def leapfrog_integration(position, velocity_before, gravity, dt):
    """
    Leapfrog algorithm to get the update position and update velocity
    """

    new_velocity_half = velocity_before + gravity * dt
    new_position = position + new_velocity_half * dt
    return new_velocity_half, new_position


def compute_spring_force(position, k):
    return -k * position
