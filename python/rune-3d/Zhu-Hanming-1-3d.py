#
# CS1010X --- Programming Methodology
#
# Mission 2 - 3D Contest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *

########
# Task #
########

# You may submit up to three entries. Please update your entry number below.

# Entry 0 of 3
# ============
# Write your function here. It should return a rune.

import math

def create_conc_grad(depth):
    def square (x):
        return x * x

    def helper (x, y):
        d_sq = square (x - 300) + square (y - 300)
        return 1/(300**2) * d_sq *depth

    return helper

def spiral(painter, n):
    base_figure = scale((2/n)*0.90**n, painter)
    radius = 0.5-1/n
    for i in range(1, n):
        new_figure = scale((2/n)*0.90**(n-i), rotate(math.pi*(i/n), painter))
        translated_figure = translate((i/(n-1))*radius*(math.sin((math.pi/n)*2*(i))),(i/(n-1))*radius*(math.cos((math.pi/n)*2*(i))), new_figure)
        base_figure = overlay_frac(i/(i+1), base_figure, translated_figure)
    return overlay_frac(0.25,base_figure, function_to_painter(create_conc_grad(1)))


# Use one of the following methods to display your rune:
# stereogram(<your rune>)
# anaglyph(<your rune>)

hollusion(spiral(nova_bb, 10))
