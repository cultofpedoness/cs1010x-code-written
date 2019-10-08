#
# CS1010X --- Programming Methodology
#
# Mission 14 Template
#
# Note that written answers should be commented out to allow us to run your
# code easily while grading your problem set.

from hungry_games import *
import random



#################################################################################
#                                                                               #
# PASTE YOUR MISSION 13 CODE HERE                                               #
#                                                                               #
#################################################################################

class Weapon(Thing):

    ###########
    # Task 1a #
    ###########

    def __init__(self, name, min_dmg, max_dmg):
        super().__init__(name)
        self.min = min_dmg
        self.max = max_dmg


    ###########
    # Task 1b #
    ###########

    def min_damage(self):
        return self.min

    def max_damage(self):
        return self.max

    ###########
    # Task 1c #
    ###########

    def damage(self):
        return random.randint(self.min, self.max)

class Ammo(Thing):

    ###########
    # Task 2a #
    ###########
    def __init__(self, name, weapon, quantity):
        super().__init__(name)
        self.weapon = weapon
        self.quantity = quantity


    ###########
    # Task 2b #
    ###########
    def get_quantity(self):
        return self.quantity


    ###########
    # Task 2c #
    ###########
    def weapon_type(self):
        return self.weapon.name


    ###########
    # Task 2d #
    ###########
    def remove_all(self):
        self.quantity = 0


class RangedWeapon(Weapon):

    ###########
    # Task 3a #
    ###########
    def __init__(self, name, min_dmg, max_dmg):
        super().__init__(name, min_dmg, max_dmg)
        self.shots = 0


    ###########
    # Task 3b #
    ###########
    def shots_left(self):
        return self.shots


    ###########
    # Task 3c #
    ###########
    def load(self, ammo):
        if ammo.weapon_type() == self.name:
            self.shots += ammo.get_quantity()
            ammo.remove_all()
        else:
            pass


    ###########
    # Task 3d #
    ###########
    def damage(self):
        if self.shots == 0:
            return 0
        else:
            self.shots -= 1
            return super().damage()

###########
# Task 4a #
###########
class Food(Thing):
    def __init__(self, name, food_value):
        super().__init__(name)
        self.food_value = food_value

    def get_food_value(self):
        return self.food_value


###########
# Task 4b #
###########
class Medicine(Food):
    def __init__(self, name, food_value, medicine_value):
        super().__init__(name, food_value)
        self.medicine_value = medicine_value

    def get_medicine_value(self):
        return self.medicine_value

##############
# Task 5a&b  #
##############
class Animal(LivingThing):
    def __init__(self, name, health, food_value, *threshold):
        if len(threshold) == 0:
            super().__init__(name, health, random.randint(0, 4))
        else:
            super().__init__(name, health, threshold[0])
        self.food_value = food_value

    def get_food_value(self):
        return self.food_value

    def go_to_heaven(self):
        drop = Food(self.name + " meat", self.food_value)
        self.get_place().add_object(drop)
        super().go_to_heaven()




#################################################################################
#                                                                               #
# MISSION 14                                                                    #
# TESTING CODE IS BELOW ALL THE TASKS                                           #
#                                                                               #
#################################################################################


#############
##  Task 1 ##
#############

class Tribute(Person):


    ############
    #  Task 1a #
    ############
    def __init__(self, name, health):
        # Tributes will not move by themselves, so set threshold to -1
        super().__init__(name, health, -1)
        # add hunger property
        self.hunger = 0




    ############
    #  Task 1b #
    ############
    def get_hunger(self):
        return self.hunger



    ############
    #  Task 1c #
    ############
    def add_hunger(self, hunger_value):
        self.hunger += hunger_value
        if self.hunger >=100:
            self.go_to_heaven()



    ############
    #  Task 1d #
    ############
    def reduce_hunger(self, hunger_value):
        if hunger_value > self.hunger:
            self.hunger = 0
        else:
            self.hunger -= hunger_value



    #############
    ##  Task 2 ##
    #############
    def eat(self, food):
        if food in self.get_inventory():
            if isinstance(food, Food):
                self.reduce_hunger(food.get_food_value())
                if type(food) == Medicine:
                    self.health += food.get_medicine_value()
                    if self.health > 100:
                        self.health = 100
                self.remove_item(food)
        
                




    ############
    #  Task 3a #
    ############
    def get_weapons(self):
        return tuple(filter(lambda x: isinstance(x, Weapon), self.get_inventory()))




    ############
    #  Task 3b #
    ############
    def get_food(self):
        return tuple(filter(lambda x: isinstance(x, Food), self.get_inventory()))




    ############
    #  Task 3c #
    ############
    def get_medicine(self):
        return tuple(filter(lambda x: type(x) == Medicine, self.get_inventory()))




    #############
    ##  Task 4 ##
    #############
    def attack(self, living_thing, weapon):
        if weapon in self.get_weapons():
            if living_thing in self.objects_around():
                living_thing.health -= weapon.damage()
                if living_thing.health <=0:
                    living_thing.go_to_heaven()



#############
##  Task 5 ##
#############
# You can either draw it here or attach a image file when you submit.




################
# Testing Code #
################


def test_task1():
    print("===== Task 1b ======")
    cc = Tribute("Chee Chin", 100)
    print(cc.get_hunger())          # 0

    print("===== Task 1c ======")
    Base = Place("base")
    cc = Tribute("Chee Chin", 100)
    Base.add_object(cc)
    print(cc.get_place().get_name())    # base
    cc.add_hunger(50)
    print(cc.get_hunger())              # 50
    cc.add_hunger(50)                   # Chee Chin went to heaven!
    print(cc.get_hunger())              # 100
    print(cc.get_place().get_name())    # Heaven

    print("===== Task 1d ======")
    cc = Tribute("Chee Chin", 100)
    cc.add_hunger(10)
    print(cc.get_hunger())          # 10
    cc.reduce_hunger(20)
    print(cc.get_hunger())          # 0

# Uncomment to test task 1
test_task1()

def test_task2():
    print("===== Task 2 ======")
    cc = Tribute("Chee Chin", 100)
    chicken = Food("chicken", 5)
    aloe_vera = Medicine("aloe vera", 2, 5)

    Base = Place("base")
    Base.add_object(cc)
    Base.add_object(chicken)
    Base.add_object(aloe_vera)

    cc.reduce_health(10)
    cc.add_hunger(4)
    print(named_col(cc.get_inventory()))    # []

    cc.eat(chicken)
    print(cc.get_hunger())                  # 4

    cc.take(chicken)                        # Chee Chin took chicken
    cc.take(aloe_vera)                      # Chee Chin took aloe vera
    print(named_col(cc.get_inventory()))    # ['chicken', 'aloe vera']

    cc.eat(aloe_vera)
    print(cc.get_health())                  # 95
    print(cc.get_hunger())                  # 2

    print(named_col(cc.get_inventory()))    # ['chicken']

    cc.eat(chicken)
    print(cc.get_health())                  # 95
    print(cc.get_hunger())                  # 0
    print(named_col(Base.get_objects()))    # ['Chee Chin']

# Uncomment to test task 2
test_task2()

def test_task3():
    print("===== Task 3 ======")
    cc = Tribute("Chee Chin", 100)
    chicken = Food("chicken", 5)
    aloe_vera = Medicine("aloe vera", 2, 5)
    bow = RangedWeapon("bow", 4, 10)
    sword = Weapon("sword", 2, 5)

    Base = Place("base")
    Base.add_object(cc)
    Base.add_object(chicken)
    Base.add_object(aloe_vera)
    Base.add_object(bow)
    Base.add_object(sword)

    cc.take(bow)                           # Chee Chin took bow
    cc.take(sword)                         # Chee Chin took sword
    cc.take(chicken)                       # Chee Chin took chicken
    cc.take(aloe_vera)                     # Chee Chin took aloe_vera

    print(named_col(cc.get_inventory()))   # ['bow', 'sword', 'chicken', 'aloe vera']
    print(named_col(cc.get_weapons()))     # ('bow', 'sword')
    print(named_col(cc.get_food()))        # ('chicken', 'aloe vera')
    print(named_col(cc.get_medicine()))    # ('aloe vera',)

# Uncomment to test task 3
test_task3()

def test_task4():
    print("===== Task 4 ======")
    Base = Place("base")
    cc = Tribute("Chee Chin", 100)
    sword = Weapon("sword", 10, 10)
    bear = Animal("bear", 20, 10)

    Base.add_object(cc)
    Base.add_object(sword)
    Base.add_object(bear)

    print(bear.get_health())                # 20

    cc.attack(bear, sword)
    print(bear.get_health())                # 20

    cc.take(sword)                          # Chee Chin took sword
    cc.attack(bear, sword)
    print(bear.get_health())                # 10

    cc.attack(bear, sword)                  # bear went to heaven
    print(named_col(Base.get_objects()))    # ['Chee Chin', 'bear meat']

# Uncomment to test task 4
test_task4()
