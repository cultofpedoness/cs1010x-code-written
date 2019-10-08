#
# CS1010X --- Programming Methodology
#
# Mission 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *

def spiral(thickness, rounds):
    if thickness==0 or rounds==0:
        return blank_bb
    else:
        result = spiral(thickness, rounds-1)
        step1 = stack_frac(thickness/2, black_bb, blank_bb)
        step2 = stack(black_bb, quarter_turn_right(step1))
        step3 = stack_frac(thickness, step2, quarter_turn_right(result))
        return step3
        
show(spiral(1/5, 50))

###########
# Task 1a #
###########

def fractal(pic, n):
    if n == 1:
        return pic
    else:
        return beside(pic, stack(fractal(pic, n-1),fractal(pic, n-1)))


# Test
#show(fractal(make_cross(rcross_bb), 3))
#show(fractal(make_cross(rcross_bb), 7))
# Write your additional test cases here

###########
# Task 1b #
###########

def fractal_iter(pic, n):
    final_pic = pic
    for i in range(1, n):
        final_pic = beside(pic, stack(final_pic, final_pic))
    return final_pic


# Test
# show(fractal_iter(make_cross(rcross_bb), 3))
# show(fractal_iter(make_cross(rcross_bb), 7))
# Write your additional test cases here


###########
# Task 1c #
###########

def dual_fractal(pic1, pic2, n):
    if n == 1:
        return pic1
    else:
        return beside(pic1, stack(dual_fractal(pic2, pic1, n-1), dual_fractal(pic2, pic1, n-1)))

## using 2 functions and recursion between them:

##def dual_fractal(pic1, pic2, n):
##    if n == 1:
##        return pic1
##    else:
##        return beside(pic1, stack(dual_fractal_2(pic1, pic2, n-1), dual_fractal_2(pic1, pic2, n-1)))
##
##def dual_fractal_2(pic1, pic2, n):
##    if n == 1:
##        return pic2
##    else:
##        return beside(pic2, stack(dual_fractal(pic1, pic2, n-1), dual_fractal(pic1, pic2, n-1)))

# Test
# show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 2))
# show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 4))
# show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 7))
# Write your additional test cases here

# Note that when n is even, the first (biggest) rune should still be rune1

###########
# Task 1d #
###########

def dual_fractal_iter(pic1, pic2, n):
##    iterative = True
##    final_pic = pic1
##    i = 2
##    while iterative:
##        if n==2:
##            pic1, pic2 = pic2, pic1
##            final_pic = quarter_turn_left(stack_frac((2**(i-1)-1)/(2**(i-1)), quarter_turn_right(final_pic), quarter_turn_right(stackn((2**(i-1)), pic1))))
##            iterative = False
##        else:
##            pic1, pic2 = pic2, pic1
##            final_pic = quarter_turn_left(stack_frac((2**i -2)/(2**i -1), quarter_turn_right(final_pic), quarter_turn_right(stackn((2**(i-1)), pic1))))
##            n -= 1
##            i += 1
##    return final_pic
    if n%2 == 1:
        final_pic = pic1
        for i in range(1, n):
            final_pic = beside(pic2, stack(final_pic, final_pic))
            pic1, pic2 = pic2, pic1
    else:
        final_pic = pic2
        for i in range(1, n):
            final_pic = beside(pic1, stack(final_pic, final_pic))
            pic1, pic2 = pic2, pic1
    return final_pic

# Test
# show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 7))
# show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 4))
# show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 7))
# Write your additional test cases here

# Note that when n is even, the first (biggest) rune should still be rune1

##########
# Task 2 #
##########

def steps(top_right, bottom_right, bottom_left, top_left):
    sheet1 = dual_fractal(stack(top_left, blank_bb), blank_bb, 2)
    sheet2 = dual_fractal(stack(blank_bb, bottom_left), blank_bb, 2)
    sheet3 = beside(stack(blank_bb, blank_bb),stack(blank_bb, bottom_right))
    sheet4 = beside(stack(blank_bb, blank_bb),stack(top_right, blank_bb))
    return overlay(overlay(sheet1, sheet2), overlay(sheet3, sheet4))

# Test
# show(steps(rcross_bb, sail_bb, corner_bb, nova_bb))

