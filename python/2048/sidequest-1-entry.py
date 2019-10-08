#
# CS1010X --- Programming Methodology
#
# Sidequest 10.1 Template
#
# Note that written answers are commented out to allow us to run your #
# code easily while grading your problem set.

from random import *
from puzzle import GameGrid

###########
# Helpers #
###########

def accumulate(fn, initial, seq):
    if not seq:
        return initial
    else:
        return fn(seq[0],
                  accumulate(fn, initial, seq[1:]))

def flatten(mat):
    return [num for row in mat for num in row]



###########
# Task 1  #
###########

def new_game_matrix(n):
    matrix = []
    for i in range(n):
        matrix.append([0]*n)
    return matrix

def has_zero(mat):
    return 0 in flatten(mat)

def add_two(mat):
    if has_zero(mat):
        n = len(mat)-1
        placed = False
        while not placed:
            a, b = randint(0, n), randint(0, n)
            if mat[a][b] == 0:
                mat[a][b] = 2
                placed = True
                return mat
            else:
                continue
    else:
        return mat



###########
# Task 2  #
###########

def game_status(mat):
    if 2048 in flatten(mat):
        return "win"
    else:
        if not has_zero(mat):
            n = len(mat)
            for a in range(n):
                if a<n-1:
                    for b in range(n):
                        if b<n-1:
                            if mat[a][b] == mat[a][b+1]:
                                return "not over"
                        if mat[a][b] == mat[a+1][b]:
                            return "not over"
                else:
                    for b in range(n-1):
                        if mat[a][b] == mat[a][b+1]:
                            return "not over"
            return "lose"
        else:
            return "not over"



###########
# Task 3a #
###########

def transpose(mat):
    result = []
    for row in mat:
        for i in range(len(row)):
            try:
                result[i].append(row[i])
            except:
                result.append([row[i],])
    return result



###########
# Task 3b #
###########

def reverse(mat):
    result = []
    for row in mat:
        result.append(row[::-1])
    return result



############
# Task 3ci #
############

def merge_left(mat):
    score = 0
    def merging(row):
        new_row = list(filter(lambda x: x!= 0, row))
        result = [0]
        i = 0
        while i < len(new_row):
            if i == len(new_row)-1:
                result.append(new_row[i])
                i += 1
            elif new_row[i] == new_row[i+1]:
                result.append(new_row[i]*2)
                result[0] += new_row[i]*2
                i += 2
            else:
                result.append(new_row[i])
                i +=1
        return result
            
    result = list(map(merging, mat))
    new_result = []
    for row in result:
        score += row[0]
        new_result.append(row[1:])
    size = len(mat)
    for i in range(size):
        while len(new_result[i]) < size:
            new_result[i].append(0)
    return(new_result, new_result!=mat, score)


#############
# Task 3cii #
#############

def merge_right(mat):
    new_mat, is_valid, score = merge_left(reverse(mat))
    new_mat = reverse(new_mat)
    return (new_mat, is_valid, score)

def merge_up(mat):
    new_mat, is_valid, score = merge_left(transpose(mat))
    new_mat = transpose(new_mat)
    return (new_mat, is_valid, score)

def merge_down(mat):
    new_mat, is_valid, score = merge_left(reverse(transpose(mat)))
    new_mat = transpose(reverse(new_mat))
    return (new_mat, is_valid, score)



###########
# Task 3d #
###########

def text_play():
    def print_game(mat, score):
        for row in mat:
            print(''.join(map(lambda x: str(x).rjust(5), row)))
        print('score: ' + str(score))
    GRID_SIZE = 4
    score = 0
    mat = add_two(add_two(new_game_matrix(GRID_SIZE)))
    print_game(mat, score)
    while True:
        move = input('Enter W, A, S, D or Q: ')
        move = move.lower()
        if move not in ('w', 'a', 's', 'd', 'q'):
            print('Invalid input!')
            continue
        if move == 'q':
            print('Quitting game.')
            return
        move_funct = {'w': merge_up,
                      'a': merge_left,
                      's': merge_down,
                      'd': merge_right}[move]
        mat, valid, score_increment = move_funct(mat)
        if not valid:
            print('Move invalid!')
            continue
        score += score_increment
        mat = add_two(mat)
        print_game(mat, score)
        status = game_status(mat)
        if status == "win":
            print("Congratulations! You've won!")
            return
        elif status == "lose":
            print("Game over. Try again!")
            return

# UNCOMMENT THE FOLLOWING LINE TO TEST YOUR GAME
#text_play()


# How would you test that the winning condition works?
# Your answer:
#


##########
# Task 4 #
##########

def make_state(matrix, total_score):
    return [matrix, total_score]

def get_matrix(state):
    return state[0]

def get_score(state):
    return state[1]

def make_new_game(n):
    matrix = new_game_matrix(n)
    matrix = add_two(matrix)
    matrix = add_two(matrix)
    return make_state(matrix, 0)

def move(fn, state):
    new_matrix, is_valid, add_score = fn(get_matrix(state))
    if is_valid == False:
        return (state, is_valid)
    else:
        new_matrix = add_two(new_matrix)
        return (make_state(new_matrix, get_score(state)+add_score), is_valid)


def left(state):
    return move(merge_left, state)

def right(state):
    return move(merge_right, state)

def up(state):
    return move(merge_up, state)

def down(state):
    return move(merge_down, state)


# Do not edit this #
game_logic = {
    'make_new_game': make_new_game,
    'game_status': game_status,
    'get_score': get_score,
    'get_matrix': get_matrix,
    'up': up,
    'down': down,
    'left': left,
    'right': right,
    'undo': lambda state: (state, False)
}

# UNCOMMENT THE FOLLOWING LINE TO START THE GAME (WITHOUT UNDO)
#gamegrid = GameGrid(game_logic)




#################
# Optional Task #
#################

###########
# Task 5i #
###########

def make_new_record(mat, increment):
    return [mat, increment]

def get_record_matrix(record):
    return record[0]

def get_record_increment(record):
    return record[1]

############
# Task 5ii #
############

def make_new_records():
    return []

def push_record(new_record, stack_of_records):
    if len(stack_of_records) == 4:
        new_stack = stack_of_records[1:]
        new_stack.append(new_record)
        return new_stack
    elif len(stack_of_records) < 4:
        new_stack = stack_of_records
        new_stack.append(new_record)
        return new_stack

def is_empty(stack_of_records):
    return type(stack_of_records)==list and len(stack_of_records)==0

def pop_record(stack_of_records):
    if is_empty(stack_of_records):
        return (None, None, stack_of_records)
    else:
        return (get_record_matrix(stack_of_records[-2]), get_record_increment\
                (stack_of_records[-1]), stack_of_records[:-1])
            
#############
# Task 5iii #
#############

# COPY AND UPDATE YOUR FUNCTIONS HERE
def make_state(matrix, total_score, records):
    return [matrix, total_score, records]

def get_matrix(state):
    return state[0]

def get_score(state):
    return state[1]

def make_new_game(n):
    matrix = new_game_matrix(n)
    matrix = add_two(matrix)
    matrix = add_two(matrix)
    records = make_new_records()
    return make_state(matrix, 0, records)

def move(fn, state):
    records = get_records(state)
    if is_empty(records):
        records = push_record(make_new_record(get_matrix(state), 0), records)
    new_matrix, is_valid, add_score = fn(get_matrix(state))
    if is_valid == False:
        return (state, is_valid)
    else:
        new_matrix = add_two(new_matrix)
        records = push_record(make_new_record(new_matrix, add_score), records)
        return (make_state(new_matrix, get_score(state)+add_score, records), is_valid)

def left(state):
    return move(merge_left, state)

def right(state):
    return move(merge_right, state)

def up(state):
    return move(merge_up, state)

def down(state):
    return move(merge_down, state)


# NEW FUNCTIONS TO DEFINE
def get_records(state):
    return state[2]

def undo(state):
    if len(get_records(state))<2:
        return (state, False)
    else:
        prev_mat, prev_incre, new_records = pop_record(get_records(state))
        new_score = get_score(state) - prev_incre
        return (make_state(prev_mat, new_score, new_records), True)


# UNCOMMENT THE FOLLOWING LINES TO START THE GAME (WITH UNDO)
game_logic = {
    'make_new_game': make_new_game,
    'game_status': game_status,
    'get_score': get_score,
    'get_matrix': get_matrix,
    'up': up,
    'down': down,
    'left': left,
    'right': right,
    'undo': undo
}
gamegrid = GameGrid(game_logic)
