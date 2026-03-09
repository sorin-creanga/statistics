import numpy as np
import matplotlib.pyplot as plt

import math

# simulating some values

initial_X_values = np.random.default_rng()

rand_points_x = initial_X_values.integers(1,10,size=(1000,1))

print(rand_points_x[:10])


# end of initial simulation


"""
counter = 0

list_of_random_means = []


while counts <= counter:

    xholder = []
    value_counter = 0
    while 
    xholder.append(result.random(1,10,size = (1,1)))

    standard_mean = math.mean(clt_new)

    return standard_mean
 


""" 

from marckov_and_chebysev_inequality import marckov_inequality

result =marckov_inequality(rand_points_x,5)
print(result)