#
# CS1010X --- Programming Methodology
#
# Mission 2 - 2D Contest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *

########
# Task #
########

# You may submit up to 3 entries. Please update your entry number below.

# Entry 1 of 3
# ============
# Write your function here. It should return a rune.

def mangekyou(n):
    def white_circle_bb(vp, frame):
        unit = 50
        p = []
        angle = 0
        while(angle<2*math.pi):
            p.append(Posn(math.cos(angle),math.sin(angle)))
            angle+= unit/viewport_size
        if(is_list(vp[0])):
            for count, port in enumerate(vp):
                draw_solid_polygon(port, map(transform_posn(frame), map(center_and_fill, p)),Posn((0.3 - frame.z1) * (spread * (((2 * count) / (len(vp) - 1)) - 1)), 0),Rgb(1, 1, 1))
        elif (vp != None):
            draw_solid_polygon(vp, map(transform_posn(frame), map(center_and_fill, p)), Posn(0,0), Rgb(1, 1, 1))

    unsquished_circle = overlay_frac(0, scale(0.95, white_circle_bb), circle_bb)

    squished_circle = scale(0.9, quarter_turn_right(stack_frac(1/3, blank_bb, stack(unsquished_circle, blank_bb))))

    default_eye = overlay_frac(0, overlay_frac(0, scale(0.08, circle_bb), scale(0.3, unsquished_circle)), squished_circle)
    final_eye = default_eye
    
    if n < 1:
        return scale(0.08, circle_bb)
    elif n==1:
        return final_eye
    elif n>1:
        for i in range(1, n):
            final_eye = overlay_frac(0, final_eye, rotate(math.pi*(i/n), squished_circle))
        
        return final_eye

# did not manage to find out how to convert all white pixels in squished_circle to become transparent
# was thinking of using rgba but was unable to convert the painter produced by functions to one that can have rgba applied on it
# function allows for change in argument n

show(mangekyou(5))



