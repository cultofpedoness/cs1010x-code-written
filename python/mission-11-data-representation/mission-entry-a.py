#
# CS1010X --- Programming Methodology
#
# Mission 11a
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

# Collaborator: <your collaborator's matric> <your collaborator's name>

###############
# Mission 11a #
###############

##########
# Task 1 #
##########

# With these operations, compound generic operations can be defined, such as
# def square(x):
#   return mul(x, x)

# (a) What are the types of the input and output of the generic square operation?
# Answer: (Generic Number) -> Generic Number

# (b) Why would we prefer to define square in the above way, rather than:
# def square(x):
#    return apply_generic("square", x)
# Answer: We would need to define the function "square" for each type of number/
# for each number package, to ensure that the correct output is given for that
# type of number when squared and to tag it accordingly etc. basically we need
# to add stuff to every single package installed, when we can easily achieve
# the same effect using mul, which has already been defined in each package.

##########
# Task 2 #
##########
# In the ordinary number package, a generic number operator is indexed by the
# name of the operator and a tuple of strings. For example, the add operator is
# indexed by ’add_ord’ and (’ordinary’, ’ordinary’); negation is indexed by
# ’negate_ord’ and (’ordinary’, ).
# In contrast, the constructor that creates an ordinary number is indexed by
# ’make_ord’ and just a string ’ordinary’. Explain why we have such a difference.

# Hint: Consider the differences in the process of the creation of a Generic-Num,
# such as create_ordinary, and the operations we can apply on Generic-Num, such
# as add. How is make_ord invoked, and how is add_ord invoked?

# Answer: create_ordinary goes straight to the get function, which calls for
# the function stored at _operation_table["make"][type], and executing it.
# In this case, the type is thus a simple string that denotes the type, such as
# "ordinary" or "rational".

# However, the other operation functions such as add_ord or negate_ord are all
# called through apply_generic, which basically iterates through the inputs as
# *args and identifies the tags of the inputs, before calling the appropriate
# function in the dictionary using a tuple of the tags. This makes sense as
# operations such as add or subtract requires 2 inputs/generic numbers to take
# place, and the types of these 2 numbers affect the function to be carried out.
# For operations like negate, which only requires 1 input and thus tag, the same
# process of iterating through the numbers to identify tags is carried out,
# with the resultant tuple of tags used to call the respective index,
# hence the function is stored under a tuple of tags, even if there is only one
# tag.


##########
# Task 3 #
##########

# There’s a right way and a wrong way to create a generic rational number. Here are two tries at
# producing 9/10. Which is the right way?

from generic_arith import *

first_try = create_rational(9, 10)
second_try = create_rational(create_ordinary(9), create_ordinary(10))

# What happens when you use the wrong way to produce 9/10 and 3/10 and then try to add
# them? Why does this happen?

# Right way: second_try
# What happens: Error occurs, with the error message Exception: ('Bad tagged \
# datum -- type_tag ', 9)
# Why it happens: This happens because of how denom and numer is used to separate
# the numerator and denominator for operations such as mul(x,y). Thus, without
# each of the numerator and denominator having a tag for their type, this
# operation cannot occur and the respective function cannot be called from the
# operation table. The exact bug that occurs is when the type tag is being
# stripped from the number. As the number now has length of 1 (no type tag), it
# results in the Exception from type_tag to give an error message.

##########
# Task 4 #
##########

# Produce expressions that define r2_7 to be the generic rational number whose numerator part is
# 2 and whose denominator part is 7, and r3_1 to be the generic rational number whose numerator
# is 3 and whose denominator is 1. Assume that the expression
# >>> csq = square(sub(r2_7, r3_1))
# is evaluated. Draw a box and pointer diagram that represents csq.

# As an example, the following is a box and pointer diagram that represents x, a Generic-
# Ord number:
# x = create_ordinary(5)
#
#         +---+---+---+---+
# x  -->  |       |       |
#         +---+---+---+---+
#             |       |
#             v       v
#         "ordinary"  5

# FILL IN YOUR ANSWERS HERE:
# r2_7 = create_rational(create_ordinary(2), create_ordinary(7))
# r3_1 = create_rational(create_ordinary(3), create_ordinary(1))

# csq = square(sub(r2_7, r3_1))

## Sample ASCII box and pointer diagrams (with 2 components) for your convenience
##            +---+---+---+---+         +---+---+---+---+       +---+---+---+---+
##            |       |       |  -->    |       |       |  -->  |       |       |   
##            +---+---+---+---+         +---+---+---+---+       +---+---+---+---+
##                |                         |                       |       |
##                v                         v                       v       v
##            "rational"                                        "ordinary"  49
##                                  +---+---+---+---+
##                                  |       |       |
##                                  +---+---+---+---+
##                                      |       |
##                                      v       v
##                                  "ordinary" 361


##########
# Task 5 #
##########

# Within the generic rational number package, the internal add_rat function
# handled the addition operation. Why is it not
# possible to name this function "add"?

# Answer: This is because the function "add_rat" is stored inside the table of
# operations and will be called through a series of functions starting with
# the function "add". This "add" calls apply_generic which helps to separate the
# tags from the contents and calls for the appropriate add function given the
# type tags. As such, "add" is a more generic function that exists outside of the
# table, while "add_rat" is a more specific function within the dictionary to
# be called out when necessary. Since add has been defined already and is used
# for all addition of generic numbers, we cannot name "add_rat", which is
# specifically for adding two rational numbers, as "add".

##########
# Task 6 #
##########

from generic_arith import *

# Modify install_rational_package, indicating clearly your modifications.
def install_rational_package():
    def make_rat(x, y):
        return tag(reprat(x, y))
    def reprat(x, y):
        return (x, y)
    def numer(x):
        return x[0]
    def denom(x):
        return x[1]
    def tag(x):
        return attach_tag("rational", x)

    # add, sub, mul, div: (RepRat, RepRat) -> Generic-Rat
    def add_rat(x, y):
        return make_rat( add(mul(numer(x), denom(y)),
                             mul(denom(x), numer(y))),
                         mul(denom(x), denom(y)) )
    def sub_rat(x, y):
        return make_rat( sub(mul(numer(x), denom(y)),
                             mul(denom(x), numer(y))),
                         mul(denom(x), denom(y)) )
    def mul_rat(x, y):
        return make_rat( mul(numer(x), numer(y)),
                         mul(denom(x), denom(y)) )
    def div_rat(x, y):
        return make_rat( mul(numer(x), denom(y)),
                         mul(denom(x), numer(y)) )

### NEW FUNCTIONS ###

    # negate_rat: (RepRat) -> Generic-Rat
    def negate_rat(x):
        return make_rat(negate(numer(x)), denom(x))

    # is_zero_rat: (RepRat) -> Boolean
    def is_zero_rat(x):
        return is_zero(numer(x))

    # is_eq_rat: (RepRat, RepRat) -> Boolean
    def is_eq_rat(x, y):
        return is_zero(sub(mul(numer(x), denom(y)), mul(denom(x), numer(y))))
    
    put("make", "rational", make_rat)
    put("add", ("rational", "rational"), add_rat)
    put("sub", ("rational", "rational"), sub_rat)
    put("mul", ("rational", "rational"), mul_rat)
    put("div", ("rational", "rational"), div_rat)
    put("negate", ("rational",), negate_rat)
    put("is_zero", ("rational",), is_zero_rat)
    put("is_equal", ("rational", "rational"), is_eq_rat)
    
install_rational_package()

def create_rational(x, y):
    return get("make", "rational")(x, y)

# Change the values for the test variables below
r1_2 = create_rational(create_ordinary(1), create_ordinary(2))
r2_4 = create_rational(create_ordinary(2), create_ordinary(4))
r1_8 = create_rational(create_ordinary(1), create_ordinary(8))

#################
# Do not change #
#################
def gradeThis():
    if is_equal(sub(r1_2, mul(r2_4, r1_2)), add(r1_8, r1_8)):
        print("Well done!")
    else:
        print("Please check your solution.")
gradeThis()
