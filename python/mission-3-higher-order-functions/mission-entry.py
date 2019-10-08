#
# CS1010X --- Programming Methodology
#
# Mission 3
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

###########
# Task 1a #
###########

def compose(f, g):
    return lambda x:f(g(x))

def thrice(f):
    return compose(f, compose(f, f))

def repeated(f, n):
    if n == 0:
        return identity
    else:
        return compose(f, repeated(f, n - 1))

# Your answer here:
# n = 9

###########
# Task 1b #
###########

identity = lambda x: x
add1 = lambda x: x + 1
sq = lambda x: x**2

# (i) print(thrice(thrice)(add1)(6))
# Explanation: It prints 33. This is because thrice(thrice)(add1) results in thrice(thrice(thrice(add1))(6),
# which results in 27 + 6 = 33.

# (ii) print(thrice(thrice)(identity)(compose))
# Explanation: It returns the function location of compose. This is because thrice(thrice)(identity)(compose)
# results in thrice(thrice(thrice(identity(compose))), which basically identifies compose 27 times, and as
# identify returns x for argument x, it returns the function compose itself, and printing it will print its
# where it is saved.

# (iii) print(thrice(thrice)(sq)(1))
# Explanation: It returns 1, for the reasons mentioned above, it returns 1 squared 27 times, which is still 1.

# (iv) print(thrice(thrice)(sq)(2))
# Explanation: It will attempt to return 2^(2^27). However, as this number is way too large, it will take too
# long to execute (and will not execute completely in the end) and will print nothing. 


###########
# Task 2a #
###########

def combine(f, op ,n):
    result = f(0)
    for i in range(n):
        result = op(result, f(i))
    return result

def smiley_sum(t):
    def f(x):
        if x == 1:
            return 1
        elif x>1:
            return 2*(x**2)
        else:
            return 0

    def op(x, y):
        return x + y

    n  = t+1

    # Do not modify this return statement
    return combine(f, op, n)

###########
# Task 2b #
###########

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def combine(f, op ,n):
    result = f(0)
    for i in range(n):
        result = op(result, f(i))
    return result

def new_fib(n):
    def f(x):
        a,b = 0,1
        for i in range(x-1):
            a,b = b,a+b
        return a

    def op(x, y):
        return y

    return combine(f, op, n+1)

# Your answer here:






