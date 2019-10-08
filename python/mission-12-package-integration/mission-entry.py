#
# CS1010X --- Programming Methodology
#
# Mission 12
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

# Collaborator: <your collaborator's name>, <11a/11b>

from generic_arith_min import *

###########################
# Rational Number Package #
###########################

# Copy and paste the install_rational_package procedure from Mission
# 11a below and complete the tasks below for this mission.

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


    ###########
    # Task 1a #
    ###########
    def repord_to_reprat(x):
        return (create_ordinary(x), create_ordinary(1))

    ###########
    # Task 2a #
    ###########
    def RRmethod_to_ORmethod(method):
        return lambda ord, rat: method(repord_to_reprat(ord), rat)


    def RRmethod_to_ROmethod(method):
        return lambda rat, ord: method(rat, repord_to_reprat(ord))

    ###########
    # Task 3a #
    ###########
    put("add", ("ordinary", "rational"), RRmethod_to_ORmethod(add_rat))
    put("sub", ("ordinary", "rational"), RRmethod_to_ORmethod(sub_rat))
    put("mul", ("ordinary", "rational"), RRmethod_to_ORmethod(mul_rat))
    put("div", ("ordinary", "rational"), RRmethod_to_ORmethod(div_rat))
    put("is_equal", ("ordinary", "rational"), RRmethod_to_ORmethod(is_eq_rat))

    put("add", ("rational", "ordinary"), RRmethod_to_ROmethod(add_rat))
    put("sub", ("rational", "ordinary"), RRmethod_to_ROmethod(sub_rat))
    put("mul", ("rational", "ordinary"), RRmethod_to_ROmethod(mul_rat))
    put("div", ("rational", "ordinary"), RRmethod_to_ROmethod(div_rat))
    put("is_equal", ("rational", "ordinary"), RRmethod_to_ROmethod(is_eq_rat))
    
install_rational_package()

def create_rational(x,y):
    return get("make","rational")(x,y)

###########################
# Complex Number Package  #
###########################

# Copy and paste the install_complex_package procedure from Mission
# 11b below and complete the tasks below for this mission.

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
        return make_com(negate(real(x)), negate(imag(x)))

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


    ###########
    # Task 1b #
    ###########
    def repord_to_repcom(x):
        return (create_ordinary(x), create_ordinary(0))

    ###########
    # Task 2b #
    ###########
    def CCmethod_to_OCmethod(method):
        return lambda ord, com: method(repord_to_repcom(ord), com)


    def CCmethod_to_COmethod(method):
        return lambda com, ord: method(com, repord_to_repcom(ord))

    ###########
    # Task 3b #
    ###########
    put("add", ("ordinary", "complex"), CCmethod_to_OCmethod(add_com))
    put("sub", ("ordinary", "complex"), CCmethod_to_OCmethod(sub_com))
    put("mul", ("ordinary", "complex"), CCmethod_to_OCmethod(mul_com))
    put("div", ("ordinary", "complex"), CCmethod_to_OCmethod(div_com))
    put("is_equal", ("ordinary", "complex"), CCmethod_to_OCmethod(is_eq_com))

    put("add", ("complex", "ordinary"), CCmethod_to_COmethod(add_com))
    put("sub", ("complex", "ordinary"), CCmethod_to_COmethod(sub_com))
    put("mul", ("complex", "ordinary"), CCmethod_to_COmethod(mul_com))
    put("div", ("complex", "ordinary"), CCmethod_to_COmethod(div_com))
    put("is_equal", ("complex", "ordinary"), CCmethod_to_COmethod(is_eq_com))

install_complex_package()

def create_complex(x,y):
    return get("make","complex")(x,y)


#################
# Do not change #
#################

n3 = create_ordinary(3)
r3_1 = create_rational(create_ordinary(3), create_ordinary(1))
r2_7 = create_rational(create_ordinary(2), create_ordinary(7))

def gradeThis_rational_package():
    rationalA = is_equal(n3, r3_1)
    rationalB = is_equal(sub(add(n3, r2_7), r2_7), n3)
    if rationalA and rationalB:
        print("Well done! Your install_rational_package is complete!")
    else:
        print("Please check your solution for install_rational_package.")

n3 = create_ordinary(3)
c3_plus_0i = create_complex(create_ordinary(3), create_ordinary(0))
c2_plus_7i = create_complex(create_ordinary(2), create_ordinary(7))

def gradeThis_complex_package():
    complexA = is_equal(n3, c3_plus_0i)
    complexB = is_equal(sub(add(n3, c2_plus_7i), c2_plus_7i), n3)
    if complexA and complexB:
        print("Well done! Your install_complex_package is complete!")
    else:
        print("Please check your solution for install_complex_package.")

gradeThis_rational_package()
gradeThis_complex_package()
