#
# CS1010X --- Programming Methodology
#
# Mission 5
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph import *

##########
# Task 1 #
##########

def connect_ends(curve1, curve2):
    x_translate = -(x_of(curve1(1))-x_of(curve2(0)))
    y_translate = -(y_of(curve1(1))-y_of(curve2(0)))
    return connect_rigidly(translate(x_translate, y_translate)(curve1), curve2)


##draw_connected(200, translate(0.2, 0.2)(arc))
##def connect_ends(curve1, curve2):
####    x_can_be_scaled = True
####    y_can_be_scaled = True
####    try:
####        x_scale = 1/(x_of(curve1(1))/x_of(curve2(0)))
####    except:
####        x_translate = -(x_of(curve1(1))-x_of(curve2(0)))
####        x_can_be_scaled = False
####    try:
####        y_scale = 1/(y_of(curve1(1))/y_of(curve2(0)))
####    except:
####        y_translate = -(y_of(curve1(1))-y_of(curve2(0)))
####        y_can_be_scaled = False
##    def connected_curve(t):
##        if t<0.5:
##            if x_can_be_scaled:
##                if y_can_be_scaled:
##                    return scale_xy(x_scale, y_scale)(curve1(2*t))
##                else:
##                    return translate(1, y_translate)(scale_xy(x_scale, 1)(curve1(2*t)))
##            else:
##                if y_can_be_scaled:
##                    return translate(x_translate, 1)(scale_xy(1, y_scale)(curve1(2*t)))
##                else:
##                    return translate(x_translate, y_translate)(curve1(2*t))
##        else:
##            return curve2(2*t-1)
##    return connected_curve

#draw_connected_scaled(200, connect_ends(arc, unit_line))

##########
# Task 2 #
##########

def gosperize ( curve ):
    scaled_curve = scale ( sqrt (2)/2)( curve )
    left_curve = rotate (pi/4)( scaled_curve )
    right_curve = translate (0.5,0.5)( rotate (-pi/4)( scaled_curve ))
    return connect_rigidly ( left_curve , right_curve )

def gosper_curve ( level ):
    return repeated ( gosperize , level )( unit_line )

def show_connected_gosper ( level ):
    squeezed_curve = squeeze_curve_to_rect (-0.5, -0.5, 1.5, 1.5) \
                     ( gosper_curve ( level ))
    draw_connected (200 , squeezed_curve )

##show_connected_gosper(1)

def show_points_gosper(level, num_points, initial_curve):
    def gosper_init_curve(lvl):
        return repeated (gosperize, lvl)(initial_curve)
    squeezed_curve = squeeze_curve_to_rect(-0.5, -0.5, 1.5, 1.5)\
                     (gosper_init_curve(level))
    draw_points(num_points, squeezed_curve)

##show_points_gosper(7, 1000, arc)

##########
# Task 3 #
##########

def your_gosper_curve_with_angle(level, angle_at_level):
    if level == 0:
        return unit_line
    else:
        return your_gosperize_with_angle(angle_at_level(level))(your_gosper_curve_with_angle(level-1, angle_at_level))

def your_gosperize_with_angle(theta):
    def inner_gosperize(curve_fn):
        return put_in_standard_position(connect_ends(rotate(theta)(curve_fn), rotate(-theta)(curve_fn)))
    return inner_gosperize

# testing
draw_connected(200, gosper_curve_with_angle(10, lambda lvl: pi/4))
draw_connected(200, gosper_curve(10))
draw_connected(200, your_gosper_curve_with_angle(10, lambda lvl: pi/4))
#draw_connected(200, your_gosper_curve_with_angle(5, lambda lvl: (pi/(2+lvl))/(pow(1.3, lvl))))
