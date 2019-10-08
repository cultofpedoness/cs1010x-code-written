#
# CS1010X --- Programming Methodology
#
# Mission 5 - Sidequest 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph_connect_ends import *

##########
# Task 1 #
##########

def kochize(level):
    if level == 0:
        return unit_line
    else:
        return connect_ends(connect_ends(scale(1/3)(kochize(level-1)), scale(1/3)(rotate(pi/3)(kochize(level-1)))), connect_ends(scale(1/3)(rotate(-pi/3)(kochize(level-1))),scale(1/3)(kochize(level-1))))

def show_connected_koch(level, num_points):
    draw_points(num_points, kochize(level))

#show_connected_koch(0, 4000)
#show_connected_koch(4, 4000)

##########
# Task 2 #
##########

def snowflake():
    def resulting_snowflake(t):
        if t<1/3:
            return kochize(5)(3*t)
        elif t<2/3:
            return translate(1,0)(rotate(4*pi/3)(kochize(5)))(3*t-1)
        else:
            return translate(0.5,-sin(pi/3))(rotate(-4*pi/3)(kochize(5)))(3*t-2)
    return resulting_snowflake

draw_connected_scaled(10000, snowflake())
