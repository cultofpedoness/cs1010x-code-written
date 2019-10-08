#
# CS1010X --- Programming Methodology
#
# Mission 7 - Sidequest 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from lazy_susan import *

##########
# Task 1 #
##########

def solve_trivial_2(table):
    table_state = get_table_state(table)
    moves = ()
    for coin in table_state:
        if coin == 1:
            moves += (1,)
        else:
            moves += (0,)
    flip_coins(table, moves)
        

# test:
t2_1 = create_table(2)
solve_trivial_2(t2_1)
print(check_solved(t2_1))


########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

##t2_1_run = create_table(2)
##run(t2_1_run, solve_trivial_2)

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

##t2_1_susan = create_table(2)
##Susan(t2_1_susan)

########################################################





##########
# Task 2 #
##########

def solve_trivial_4(table):
    table_state = get_table_state(table)
    moves = ()
    for coin in table_state:
        if coin == 1:
            moves += (1,)
        else:
            moves += (0,)
    flip_coins(table, moves)

# test:
t4_2 = create_table(4)
solve_trivial_4(t4_2)
print(check_solved(t4_2))


########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

##t4_2_run = create_table(4)
##run(t4_2_run, solve_trivial_4)

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

##t4_2_susan = create_table(4)
##Susan(t4_2_susan)

########################################################





##########
# Task 3 #
##########

def solve_2(table):
    flip_coins(table, (0,1))
    if not check_solved(table):
        flip_coins(table,(0,1))

# test:
t2_3 = create_table(2)
solve_2(t2_3)
print(check_solved(t2_3))


########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

t2_3_run = create_table(2)
run(t2_3_run, solve_2)

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

# t2_3_susan = create_table(2)
# Susan(t2_3_susan)

########################################################





##########
# Task 4 #
##########

def solve_4(table):
    move_a = (1,0,1,0)
    move_b = (1,1,0,0)
    move_c = (1,0,0,0)

    moveset = (move_a, move_b, move_a, move_c, move_a, move_b, move_a)

    for move in moveset:
        flip_coins(table, move)
        if check_solved(table) == True:
            break

# test:
t4_4 = create_table(4)
solve_4(t4_4)
print(check_solved(t4_4))


########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

##t4_4_run = create_table(4)
##run(t4_4_run, solve_4)

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

# t4_4_susan = create_table(4)
# Susan(t4_4_susan)

########################################################





##########
# Task 5 #
##########

def solve(table):
    size = get_table_size(table)
    i = 0
    while size>1:
        size /= 2
        i += 1
    moveset = ((1,),)
    next_moveset = ()
    for i in range(0,i):
        for move in moveset:
            next_moveset += (move*2,)
        moveset_original = moveset
        moveset = next_moveset
        next_moveset = ()
        for row in moveset_original:
            moveset+= (row + (0,)*len(row),)
    if len(moveset)>1:
        moveset = moveset[1:]

    prev_sequence = ()
    sequence = (0,)
    next_sequence = ()

    for a in range(0, int(get_table_size(table)/2)-1):
        next_sequence = sequence + (a*2+1,) + sequence + \
                        (a*2+2,) + sequence + (a*2+1,) + sequence
        prev_sequence = sequence
        sequence = next_sequence
    if get_table_size(table) == 2:
        sequence *= 2

    for num in sequence:
        flip_coins(table, moveset[num])
        if check_solved(table):
            break
        

# test:
##t1_5 = create_table(1)
##solve(t1_5)
##print(check_solved(t1_5))
##
##t2_5 = create_table(2)
##solve(t2_5)
##print(check_solved(t2_5))
##
##t4_5 = create_table(4)
##solve(t4_5)
##print(check_solved(t4_5))
##
##t8_5 = create_table(8)
##solve(t8_5)
##print(check_solved(t8_5))
##
##t16_5 = create_table(16)
##solve(t16_5)
##print(check_solved(t16_5))

# Note: It is not advisable to execute run() if the table is large.
