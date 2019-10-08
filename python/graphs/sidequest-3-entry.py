#
# CS1010X --- Programming Methodology
#
# Mission 5 - Sidequest 3
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph_connect_ends import *

##########
# Task 1 #
##########


def yj_dragonize ( num_points , curve ):
    if num_points == 0:
        return curve
    else :
        c = yj_dragonize ( num_points -1, curve )
    return  ( connect_ends ( rotate (-pi/2)(c), c))


def dragonize(order, curve):
    if order == 0:
        return curve
    else:
        c = dragonize(order-1, curve)
    return connect_ends(c, rotate(-pi/2)(revert(c)))

# test:
draw_connected_scaled(4096, dragonize(4, unit_line))
