#
# CS1010X --- Programming Methodology
#
# Mission 2 - Side Quest 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *
from math import sin, cos, pi

##########
# Task 1 #
##########

def tree(n, figure):
    final_figure = figure
    for i in range(2, n+1):
        final_figure = overlay_frac(1/i, scale_independent((n+1-i)/n, (n+1-i)/n, figure), final_figure)
    return final_figure

# Test
#show(tree(4, circle_bb))


##########
# Task 2 #
##########
    
# use help(math) to see functions in math module
# e.g to find out value of sin(pi/2), call math.sin(math.pi/2)

def helix(figure, n):
    scaled_figure = scale_independent(2/n, 2/n, figure)
    radius = 0.5-1/n
    final_figure = translate(0, radius, scaled_figure)
    for i in range(2, n+1):
        next_figure = translate(radius*(math.sin((math.pi/n)*2*(i-1))), radius*(math.cos((math.pi/n)*2*(i-1))), scaled_figure)
        final_figure = overlay_frac((i-1)/i, final_figure, next_figure)
    return final_figure

# Test
show(helix(make_cross(rcross_bb), 12))
