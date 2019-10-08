#
# CS1010X --- Programming Methodology
#
# Mission 1 - Side Quest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *

##########
# Task 1 #
##########

def egyptian(pic, n):
    if n>2:
        side_column = stackn(n, pic)
        centre_row = quarter_turn_left(stackn(n-2, quarter_turn_right(pic)))
        centre_bottom = stack_frac((n-2)/(n-1), pic, centre_row)
        centre = stack_frac(1/n, centre_row, centre_bottom)
        right_side = stack_frac((n-2)/(n-1),quarter_turn_right(centre),quarter_turn_right(side_column))
        full_picture = stack_frac(1/n, quarter_turn_right(side_column), right_side)
        return quarter_turn_left(full_picture)
    else:
        pass

# Test
show(egyptian(nova_bb, 20))
