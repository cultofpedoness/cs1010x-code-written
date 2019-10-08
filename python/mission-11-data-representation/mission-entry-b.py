#
# CS1010X --- Programming Methodology
#
# Mission 11b
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

# Collaborator: <your collaborator's matric> <your collaborator's name>

###############
# Mission 11b #
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

# There’s a right way and a wrong way to create a generic complex number. Here are two tries at
# producing 9+10i. Which is the right way?

from generic_arith import *

##first_try = create_complex(9, 10)
##second_try = create_complex(create_ordinary(9), create_ordinary(10))

# What happens when you use the wrong way to produce 9+10i and 3+10i and then try to add
# them? Why does this happen?

# Right way: second_try
# What happens: Error occurs, with the error message Exception: ('Bad tagged \
# datum -- type_tag ', 9)
# Why it happens: This happens because of how real and imag is used to separate
# the real and imaginary parts for operations such as mul(x,y). Thus, without
# each of the real and imaginary numbers having a tag for their type, this
# operation cannot occur and the respective function cannot be called from the
# operation table. The exact bug that occurs is when the type tag is being
# stripped from the number. As the number now has length of 1 (no type tag), it
# results in the Exception from type_tag to give an error message.

##########
# Task 4 #
##########

# Produce expressions that define c2_plus_7i to be the generic complex number whose real part is 2
# and whose imaginary part is 7, and c3_plus_1i to be the generic complex number whose real part
# is 3 and whose imaginary part is 1. Assume that the expression
# >>> csq = square(sub(c2_plus_7i, c3_plus_1i))
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
# c2_plus_7i = create_complex(create_ordinary(2), create_ordinary(7))
# c3_plus_1i = create_complex(create_ordinary(3), create_ordinary(1))

# csq = square(sub(c2_plus_7i, c3_plus_1i))

## Sample ASCII box and pointer diagrams (with 2 components) for your convenience
##    +---+---+---+---+         +---+---+---+---+       +---+---+---+---+
##    |       |       |  -->    |       |       |  -->  |       |       |   
##    +---+---+---+---+         +---+---+---+---+       +---+---+---+---+
##        |                         |                       |       |
##        v                         v                       v       v
##    "complex"                                        "ordinary"  -12
##                          +---+---+---+---+
##                          |       |       |
##                          +---+---+---+---+
##                              |       |
##                              v       v
##                          "ordinary" -35

##########
# Task 5 #
##########

# Within the generic complex number package, the internal add_com function
# handled the addition operation. Why is it not
# possible to name this function "add"?

# Answer: This is because the function "add_com" is stored inside the table of
# operations and will be called through a series of functions starting with
# the function "add". This "add" calls apply_generic which helps to separate the
# tags from the contents and calls for the appropriate add function given the
# type tags. As such, "add" is a more generic function that exists outside of the
# table, while "add_com" is a more specific function within the dictionary to
# be called out when necessary. Since add has been defined already and is used
# for all addition of generic numbers, we cannot name "add_com", which is
# specifically for adding two complex numbers, as "add".

##########
# Task 6 #
##########

from generic_arith import *

# Modify install_complex_package, indicating clearly your modifications.
def install_complex_package():
    def make_com(x, y):
        return tag(repcom(x, y))
    def repcom(x, y):
        return (x, y)
    def real(x):
        return x[0]
    def imag(x):
        return x[1]
    def tag(x):
        return attach_tag("complex", x)

    # add, sub, mul, div: (RepCom, RepCom) -> Generic-Com
    def add_com(x, y):
        return make_com( add(real(x), real(y)),
                         add(imag(x), imag(y)) )
    def sub_com(x, y):
        return make_com( sub(real(x), real(y)),
                         sub(imag(x), imag(y)) )
    def mul_com(x, y):
        return make_com( sub(mul(real(x), real(y)),
                             mul(imag(x), imag(y))),
                         add(mul(real(x), imag(y)),
                             mul(real(y), imag(x))))
    def div_com(x, y):
        com_conj = complex_conjugate(y)
        x_times_com_conj = content(mul_com(x, com_conj))
        y_times_com_conj = content(mul_com(y, com_conj))
        return make_com( div(real(x_times_com_conj), real(y_times_com_conj)),
                         div(imag(x_times_com_conj), real(y_times_com_conj)))
    def complex_conjugate(x):
        return (real(x), negate(imag(x)))

### NEW FUNCTIONS ###

    # negate_com: (RepCom) -> Generic-Com
    def negate_com(x):
        return make_com(negate(real(x)), imag(x))

    # is_zero_rat: (RepCom) -> Boolean
    def is_zero_com(x):
        return is_zero(real(x)) and is_zero(imag(x))

    # is_eq_rat: (RepCom, RepCom) -> Boolean
    def is_eq_com(x, y):
        #return is_zero(sub(real(x), real(y))) and is_zero(sub(imag(x), imag(y)))
        return x == y
    
    put("make", "complex", make_com)
    put("add", ("complex", "complex"), add_com)
    put("sub", ("complex", "complex"), sub_com)
    put("mul", ("complex", "complex"), mul_com)
    put("div", ("complex", "complex"), div_com)

    ### NEW INSERTIONS ###
    put("negate", ("complex",), negate_com)
    put("is_zero", ("complex",), is_zero_com)
    put("is_equal", ("complex", "complex"), is_eq_com)

install_complex_package()

def create_complex(x,y):
    return get("make", "complex")(x, y)

# Change the values for the test variables below
c_neg3_plus_10i = create_complex(create_ordinary(-3), create_ordinary(10))
c1_plus_2i = create_complex(create_ordinary(1), create_ordinary(2))
c1_plus_3i = create_complex(create_ordinary(1), create_ordinary(3))

#################
# Do not change #
#################
def gradeThis():
    if is_equal(sub(c_neg3_plus_10i, mul(c1_plus_2i, c1_plus_3i)),
        add(c1_plus_2i, c1_plus_3i)):
        print("Well done!")
    else:
        print("Please check your solution.")
gradeThis()
