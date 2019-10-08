#
# CS1010X --- Programming Methodology
#
# Mission 6
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from diagnostic import *
from hi_graph_connect_ends import *

# Mission 6 requires certain functions from Mission 5 to work.
# Do copy any relevant functions that you require in the space below:

def your_gosperize_with_angle(theta):
    def inner_gosperize(curve_fn):
        return put_in_standard_position(connect_ends(rotate(theta)(curve_fn), rotate(-theta)(curve_fn)))
    return inner_gosperize

def your_gosper_curve_with_angle(level, angle_at_level):
    if level == 0:
        return unit_line
    else:
        return your_gosperize_with_angle(angle_at_level(level))(your_gosper_curve_with_angle(level-1, angle_at_level))



# Do not copy any other functions beyond this line #
##########
# Task 1 #
##########

# Example from the mission description on the usage of time function:


# Choose a significant level for testing for all three sets of functions.

# -------------
# gosper_curve:
# -------------
# write down and invoke the function that you are using for this testing
# in the space below

#print(profile_fn(lambda: gosper_curve(10)(0.1), 2000))

#Time measurements
#Measurement 1: 359.07615699999997
#Measurement 2: 303.64154899999994
#Measurement 3: 336.71563799999996
#Measurement 4: 337.822504
#Measurement 5: 255.09461500000003

#Average: 318.4700926ms


# ------------------------
# gosper_curve_with_angle:
# ------------------------
# write down and invoke the function that you are using for this testing
# in the space below

#print(profile_fn(lambda: gosper_curve_with_angle(10, lambda lvl: pi/4)(0.1),2000))

#Time measurements
#Measurement 1: 247.6505109999999
#Measurement 2: 314.241577
#Measurement 3: 185.3596129999999
#Measurement 4: 154.126891
#Measurement 5: 274.7103599999999

#Average: 235.2177904ms

#
# -----------------------------
# your_gosper_curve_with_angle:
# -----------------------------
# write down and invoke the function that you are using for this testing
# in the space below

#print(profile_fn(lambda: your_gosper_curve_with_angle(10, lambda lvl: pi/4)(0.1),2000))

#Time measurements
#Measurement 1: 4247.4509290000005
#Measurement 2: 4365.569251
#Measurement 3: 4245.00165
#Measurement 4: 3947.0453489999995
#Measurement 5: 3877.4513950000005

#Average: 4136.503715ms


# Conclusion:
# My understanding of customised is that it allows more arguments to be taken into the function as
# to allow greater control over what is processed in the function.

# From the average readings obtained, it seems that GENERALLY the more customised a function is,
# the slower it is. For example, your_gosper_curve_with_angle takes in more inputs than gosper_curve
# and takes a significantly longer time to process it, 4137ms for the former compared to the
# latter's 318ms.

# However, strangely, gosper_curve_with_angle, which is more customised, takes longer than the less
# customised gosper_curve, with 236ms for the former and 318ms for the latter. Perhaps this is
# related to how the function was written, or the sample size was too small and the results lost
# accuracy due to that.

##########
# Task 2 #
##########

#  1) Yes, it achieves the same purpose as it skips the variable assignment and instead draws the
#     values straight from the curve function.

#  2) Previously, the function was linear as pt was defined using the curve function with t as the
#     input. Afterwards, x and y were assigned to the x_of and y_of pt. This allows any statements
#     calling x and y to be able to retrieve the value using 1 step each, and the number of times this
#     is done scales linearly with t, likely in increments of 2 steps. 

#     However, after skipping the assignment of the pt, every time x and y is called, there is a 
#     need to run through the curve function with argument t to determine the point at a certain
#     unit-interval t. This function has an order of growth of O(t) in terms of time as it needs
#     to run through from 0 to t to determine the exact point to return. Only after doing that,
#     x_of and y_of would determine the x and y respectively. As such, the overall order of growth
#     becomes exponential, O(t^2), due to the need to run through the curve function for every
#     point plotted using joe_rotate.

##########
# Task 3 #
##########

original_rotate = rotate


replace_fn(rotate, joe_rotate)

trace(x_of)
gosper_curve(5)(0.5)
untrace(x_of)

#
# Fill in this table:
#
#                    level      rotate       joe_rotate
#                      1          3              4
#                      2          5              10
#                      3          7              22
#                      4          9              46
#                      5          11             94
#
#  Evidence of exponential growth in joe_rotate.
