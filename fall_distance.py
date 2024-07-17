# Author: Ashton Lee
# Github User: ashton01L
# Date: 7/17/2024
# Description: Determine a distance an object falls in a specific time period due
# to gravity, using a given formula: d = (1/2)gt^2.

def fall_distance(time):
    """
    Calculate the distance an object falls in a specific time period due to gravity,
    using a given formula.
    :param time: time (float) = time in seconds over which the object has been falling.
    :return: dist (float) = distance in meters measuring how far the object has fallen
    """
    grav = 9.8  # acceleration due to gravity in m/s^2
    dist = (1 / 2) * grav * time ** 2
    return dist

#dist = fall_distance(4.5)
#print(dist)
