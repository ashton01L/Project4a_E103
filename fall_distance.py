# Author: Ashton Lee
# Github User: ashton01L
# Date: 7/17/2024
# Description: Determine a distance an object falls in a specific time period due
# to gravity, using a given formula: d = (1/2)gt^2.

def fall_distance(t):
    """
    Calculate the distance an object falls in a specific time period due to gravity,
    using a given formula.
    :param t: t (float) = time in seconds over which the object has been falling.
    :return: d (float) = distance in meters measuring how far the object has fallen
    """
    g = 9.8  # acceleration due to gravity in m/s^2
    d = (1 / 2) * g * t ** 2
    return d

#d = fall_distance(4.5)
#print(d)

