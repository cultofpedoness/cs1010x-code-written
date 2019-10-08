#
# CS1010X --- Programming Methodology
#
# Mission 5 - Sidequest 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph import *

##########
# Task 1 #
##########
##draw_points(200 , unit_circle )
##draw_points(200 , alternative_unit_circle )
# The intervals along the circumference of the circle are different
# between the points plotted by unit_circle and those by alternative_unit_circle.
# This difference exists as, with reference to the 2 functions, the values of
# x and y used for unit_circle scale linearly with t, while the values for
# alternative_unit_circle scale quadratically with t. Thus, the points plotted
# for unit_circle are more evenly spread out while the points for
# alternative_unit_circle start out very compact at the top left corner of the
# viewer before becoming increasingly spaced out as the points go along the
# circumference towards the bottom right corner of the viewer.

##########
# Task 2 #
##########

# (a)
def spiral(t):
    return make_point(t*sin(2*pi*t), t*cos(2*pi*t))

draw_connected_scaled(1000, spiral)

# (b)
def heart(t):
##    def rev_spiral(t):
##        return make_point(-t*sin(2*pi*t), t*cos(2*pi*t))

    def inv_x(curve):
        def inverted_curve(t):
            point = curve(t)
            new_x = -x_of(point)
            return make_point(new_x, y_of(point))
        return inverted_curve
    
    if t<0.5:
        return spiral(2*t)
    else:
        return rotate(-90)(spiral)(2*t-1)

draw_connected_scaled(1000, heart)

