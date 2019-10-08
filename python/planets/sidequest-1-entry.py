#
# CS1010S --- Programming Methodology
#
# Sidequest 8.1 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from planets import *
from math import *

# Set up the environment of the simulation
planets = (Earth, Mars, Moon)

plot_planets(planets, Mars)

##########
# Task 1 #
##########
# a)
# Follows trigonometry angle.
# E.g. 0 degree -> East
# E.g. 90 degree -> North
def get_velocity_component(angle, velocity):
    return(velocity*cos(radians(angle)), velocity*sin(radians(angle)))

print(get_velocity_component(30, 50)) #(43.30127018922194, 24.999999999999996)
# note that the exact values of each component may differ slightly due to differences in precision

# b)
def calculate_total_acceleration(planets, current_x, current_y):
    x_acc = ()
    y_acc = ()
    for planet in planets:
        x_dist = get_x_coordinate(planet) - current_x
        y_dist = get_y_coordinate(planet) - current_y
        mass = get_mass(planet)
        base = (G*mass)/((sqrt((x_dist)**2 + (y_dist)**2))**3)
        acc_x = x_dist * base
        acc_y = y_dist * base
        x_acc += (acc_x,)
        y_acc += (acc_y,)
        
    return (sum(x_acc),sum(y_acc))        
    
print(calculate_total_acceleration(planets, 0.1, 0.1)) #(-1511.54410020574, -1409.327982470404)

# c)
# Do not change the return statement
def f(t, Y):
    ax, ay = calculate_total_acceleration(planets, Y[0], Y[1])
    vx, vy = Y[2], Y[3]
    return np.array([vx, vy, ax, ay])

np.set_printoptions(precision=3)
print(f(0.5, [0.1, 0.1, 15.123, 20.211])) #[ 15.123 20.211 -1511.544 -1409.328]

##########
# Task 2 #
##########

# Uncomment and change the input parameters to alter the path of the spacecraft
vx, vy = get_velocity_component(81, 27.17)


##############################################################################################
# Uncomment the following line to start the plot
start_spacecraft_animation(vx, vy, f)
