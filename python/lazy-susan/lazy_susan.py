import turtle
from math import *
from random import random, randrange
from time import sleep

###############
## Susan GUI ##
###############

class Coin(turtle.Turtle):
    def __init__(self, init=None):
        '''Initialize Coin in random state'''
        super().__init__(shape="circle")
        self.penup()
        self.onclick(self.click)
        self.__clicked = False
        # Edit: Integrate ADT and GUI (Pass ADT state to GUI)
        self.__state = random() > 0.5 if init is None else bool(init)
        # self.__state = random() > 0.5
        # End Edit

    def get_state(self):
        '''Returns state of Coin'''
        return self.__state

    def get_color(self):
        '''Returns color of Coin'''
        if Susan.debug:
            return "white" if self.get_state() else "black"
        else:
            return "red" if self.__clicked else "black"

    def reset_click(self):
        '''Resets click status of Coin'''
        self.__clicked = False

    def flip(self):
        '''Flips current state of Coin'''
        self.__state = not self.__state

    def set_color(self):
        '''Set color of Coin based on state'''
        self.fillcolor(self.get_color())

    def click(self, x=0, y=0):
        '''Method when triggered by click'''
        self.__clicked = not self.__clicked
        self.flip()
        self.set_color()

class SusanTable(turtle.Turtle):
    def __init__(self, tn):
        '''Stores n Coins in a list'''
        # Edit: Integrate ADT and GUI (Pass ADT state to GUI)
        self.__pos = list(map(lambda x: Coin(not x), tn.get_state())) \
                     if type(tn) is Table else [Coin() for i in range(tn)]
        # self.__pos = [Coin() for i in range(tn)]
        # End Edit
        self.tableADT = tn
        super().__init__()
        self.hideturtle()

    def get_coin(self, i):
        '''Returns coin in ith position'''
        return self.__pos[i]

    def is_ended(self, turn):
        '''Returns boolean if the game is ended'''
        ended = len(set(map(lambda x: x.get_state(), self.__pos))) == 1
        if ended:
            self.write("You won in {} turns!".format(turn),
                       align='center',
                       font=('Consolas', 22, 'bold'))
            print("You won in {} turns!".format(turn))
        return ended

    def randomly_rotate(self):
        '''Randomly rotates coins on the table'''
        for i in range(int(random()*len(self.__pos))):
            self.__pos.append(self.__pos.pop(0))
        
    def randomly_rotate_animate(self, screen):
        '''Animates the rotation of the coins'''
        screen.tracer(0)
        frames = 100
        # EASE IN ANIMATION
        for t in range(frames//2):
            offset = 2*pi*(2*t/frames)**3
            for i, coin in enumerate(self.__pos):
                angle = 2*pi*i/len(self.__pos) + offset
                coin.goto(sin(angle), cos(angle))
            screen.update()
        # APPLY ACTUAL RANDOM ROTATION
        self.randomly_rotate()
        self.refresh_display()
        # EASE OUT ANIMATION
        for t in range(frames//2):
            offset = 2*pi*(1+(2*t/frames-1)**3)
            for i, coin in enumerate(self.__pos):
                angle = 2*pi*i/len(self.__pos) + offset
                coin.goto(sin(angle), cos(angle))
            screen.update()
        screen.tracer(1)

    def refresh_display(self):
        '''Refreshes display, usually after rotating'''
        for coin in self.__pos:
            coin.reset_click()
            coin.set_color()
            
    # Edit: Integrate ADT and GUI (update ADT with GUI state)
    def ADTupdate(self):
        if type(self.tableADT) is Table:
            self.tableADT.GUIupdate(list(map(lambda x: not x.get_state(), self.__pos)))
    # End Edit

class Susan(turtle._Screen):
    debug = False # class variable
    def __init__(self, tn, auto=[], delay=1):
        super().__init__()
        turtle.Turtle._screen = self
        self.setworldcoordinates(-2, -2, 2, 2)
        self.tracer(0)
        if delay==0:
            self.tracer = lambda *args: None
            self.update = lambda *args: None
        # Edit: Integrate ADT and GUI (enable Table interfacing)
        n = get_table_size(tn) if type(tn) is Table else tn
        # n = tn
        # End Edit
        self.game = SusanTable(tn)
        self.size = n
        self.turn = 0
        self.game.randomly_rotate_animate(self)

        if not auto: # Manual play
            self.onkeypress(self.check_selection, "space")
            self.onkeypress(self.toggle_debugger, "d")
            self.listen()
            self.tracer(1)
        else:
            def helper(auto):
                '''helper function to repeat instructions once exhausted'''
                while True:
                    yield from auto
            Susan.debug = True # show coin states
            auto = helper(auto)
            max_iterations = 50000 # max number of tries
            while max_iterations > 0:
                max_iterations -= 1
                instruction = next(auto)
                if len(instruction) == n:
                    for i in range(n):
                        if instruction[i] == "1":
                            self.game.get_coin(i).click()
                    if self.check_selection():
                        break
                    sleep(delay)
                else:
                    print("{} not of correct length".format(instruction))

    def check_selection(self):
        '''Check if game is ended, otherwise, rotate'''
        self.turn += 1
        ended = self.game.is_ended(self.turn)
        # Edit: Integrate ADT and GUI (update ADT with GUI state)
        self.game.ADTupdate()
        # End Edit
        if not ended:
            self.game.randomly_rotate_animate(self)
        else:
            self.onkeypress(None, "space")
        return ended

    def toggle_debugger(self):
        '''toggle debug on/off, to see coin states'''
        Susan.debug = not Susan.debug
        self.game.refresh_display()

###############
## Susan ADT ##
###############

class TableCoin(object):

    def __init__(self, init=None):
        # Edit: Integrate ADT and GUI (Update ADT with GUI state)
        self.__state = bool(randrange(0,2)) if init is None else init
        # self.__state = bool(randrange(0,2))
        # End Edit

    def flip(self):
        self.__state = not self.__state

    def get_state(self):
        return self.__state

class Table(object):    

    def __init__(self, size):
        self.turn = 0
        self.display = False
        self.size = size
        self.__state = [TableCoin() for i in range(size)]
        
    def rotate(self):
        self.turn += 1
        for i in range(randrange(0, self.size)):
            self.__state.append(self.__state.pop(0))
        if self.display:
            print(" "*(7 + self.size*3), end="\\\n")
            print(" "*(8 + self.size*3), end="\\")
            print("-> {} (rotated)".format(self.get_state()))

    def flip(self, position):
        self.__state[position].flip()

    def is_solved(self):
        return len(set(map(lambda c: c.get_state(), self.__state))) == 1

    def run(self, solver):
        self.display = True
        self.print_state()
        self.rotate()
        solver(self)
        self.display = False

    def print_state(self, move=None):
        if not self.display: return
        print("{:>5d}:".format(self.turn), end=" ")
        print(self.get_state(), end="")
        print("" if move is None else "<--- {}".format(move))

    def get_state(self):
        return tuple(map(lambda c: int(c.get_state()), self.__state))

    # Edit: Integrate ADT and GUI (Update ADT with GUI state)
    def GUIupdate(self, statelist):
        self.__state = list(map(lambda x: TableCoin(x), statelist))
        self.turn += 1
    # End Edit


#########################
## Susan ADT Interface ##
#########################

def create_table(size):
    return Table(size)

def get_table_size(table):
    return table.size

def get_table_state(table):
    return table.get_state()

def check_solved(table):
    return bool(table.is_solved())

def flip_coins(table, move=None):
    if move is None:
        move = ()
        for i in range(get_table_size(table)):
            if randrange(0,2):
                table.flip(i)
                move += (1,)
            else:
                move += (0,)
    else:
        for i in range(len(move)):
            if move[i]:
                table.flip(i)
    table.print_state(tuple(move))
    if check_solved(table) == True:
        pass
    else:
        table.rotate()
    
def run(table, solver):
    return table.run(solver)
