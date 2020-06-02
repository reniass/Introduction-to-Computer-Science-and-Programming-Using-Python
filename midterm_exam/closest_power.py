from math import *

def closest_power(base, num):
    exponent = log(num, base)
    exp_int_max = int(exponent) + 1
    exp_int_min = int(exponent)
    if abs(num - base ** exp_int_min) > abs(num - base ** exp_int_max):
        return exp_int_max
    else:
        return exp_int_min


print(closest_power(3, 12))
print(closest_power(4, 1))