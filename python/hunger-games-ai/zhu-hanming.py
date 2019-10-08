#
# CS1010X --- Programming Methodology
#
# Contest 15.1 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hungry_games_classes import *
from contest_simulation import *
import random


class Player(Tribute):
    def __init__(self, name, health):
        super().__init__(name, health)
        self.last_direction = ""
        
    def next_action(self):
        vicinity = self.objects_around()
        ## Surroundings
        living_vicinity = list(filter(lambda x: isinstance(x, LivingThing), vicinity))
        tribute_vicinity = list(filter(lambda x: isinstance(x, Tribute), living_vicinity))
        wild_vicinity = list(filter(lambda x: isinstance(x, WildAnimal), living_vicinity))
        thing_vicinity = list(filter(lambda x: isinstance(x, Thing), vicinity))
        melee_vicinity = list(filter(lambda x: type(x) == Weapon, thing_vicinity))
        ranged_vicinity = list(filter(lambda x: type(x) == RangedWeapon, thing_vicinity))
        ammo_vicinity = list(filter(lambda x: type(x) == Ammo, thing_vicinity))
        medicine_vicinity = list(filter(lambda x: type(x) == Medicine, thing_vicinity))
        exits = self.get_exits()
        if self.last_direction:
            if self.last_direction=="NORTH":
                exits.remove("SOUTH")
            elif self.last_direction=="SOUTH":
                exits.remove("NORTH")
            elif self.last_direction=="EAST":
                exits.remove("WEST")
            elif self.last_direction=="WEST":
                exits.remove("EAST")

        ## Self
        weapons = list(self.get_weapons())
        melee_weapons = list(filter(lambda x: type(x) == Weapon, weapons))
        ranged_weapons = list(filter(lambda x: type(x) == RangedWeapon, weapons))
        ammo = list(filter(lambda x: isinstance(x, Ammo), self.get_inventory()))
        food = list(self.get_food())
        hunger = self.get_hunger()
        health = self.get_health()
        medicine = list(self.get_medicine())

        if health<20 and medicine and not tribute_vicinity and not wild_vicinity:
            medicine.sort(key = lambda x: x.get_medicine_value(), reverse = True)
            if medicine[0].get_medicine_value() >0:
                return ("EAT", medicine[0])

        elif health<20 and not tribute_vicinity and not wild_vicinity and medicine_vicinity:
            medicine_vicinity.sort(key = lambda x: x.get_medicine_value(), reverse = True)
            if medicine_vicinity[0].get_medicine_value() >0:
                return ("TAKE", medicine_vicinity[0])
        
        if hunger >= 70 and not tribute_vicinity and food and melee_weapons:
            food.sort(key = lambda x: x.get_food_value(), reverse = True)
            if food[0].get_food_value() > 0:
                return ("EAT", food[0])


        ## Next is the priority to get melee weapons. Ranged weapons tend to be unreliable due to
        ## the need for ammo, which often only lasts 1 shot. Though powerful, it's very unreliable.
        
        if not melee_weapons: ## If I have no melee weapons
            if melee_vicinity: ## and I see one, my priority is to pick it up
                melee_vicinity.sort(key = lambda x: x.min_damage(), reverse = True)
                return ("TAKE", melee_vicinity[0])
            else: ## Else if there's nothing for me to pick up
                if tribute_vicinity: ## If there's a tribute around
                    if ranged_weapons: ## I can consider using my ranged weapon, but only if certain conditions are met
                        ranged_weapons.sort(key = lambda x: x.min_damage(), reverse = True) ## Let's run through my weapons from strongest to weakest
                        for r_weapon in ranged_weapons:
                            if r_weapon.shots_left() >0: ## If there's a loaded ranged weapon 
                                tribute_vicinity.sort(key = lambda x: x.get_health()) ## ranking my tributes from lowest to highest health
                                for tribute in tribute_vicinity:
                                    if tribute.get_health() <= r_weapon.max_damage(): ## if the tribute's health is lower than my lowest dmg
                                        return ("ATTACK", tribute, r_weapon) ## Kill him
                                ## return ("ATTACK", tribute_vicinity[0], r_weapon) ## Uncomment to allow aiming for lowest health tribute

                        ## If the condition to hit him has not been met (aka 1HKO)
                        should_run = False
                        for tribute in tribute_vicinity: ## Run away if the tribute poses a threat
                            tribute_weapon = tribute.get_weapons()
                            for weapon in tribute_weapon:
                                if type(weapon) == Weapon: ## if he has a melee weapon
                                    should_run = True
                                    break
                                elif type(weapon) == RangedWeapon: ## or a loaded ranged weapon
                                    if weapon.shots_left() > 0:
                                        should_run = True
                                        break
                        if should_run: ## run away
                            if exits:
                                index = random.randint(0, len(exits)-1)
                                direction = exits[index]
                                self.last_direction = direction
                                return ("GO", direction)
                        if ammo: ## if I'm safe and I have ammo to load
                            for r_weapon in ranged_weapons:
                                for ammunition in ammo:
                                    if ammunition.weapon_type() == r_weapon.get_name():
                                        return ("LOAD", r_weapon, ammunition) ## load the appropriate weapon
                        if ammo_vicinity: ## if there's ammo nearby to pick up and I'm safe
                            for r_weapon in ranged_weapons:
                                for ammunition in ammo_vicinity:
                                    if ammunition.weapon_type() == r_weapon.get_name():
                                        return ("TAKE", ammunition) ## pick up ammo that I can use
                                    
                        if exits: ## If there's nothing to do that can help me fight back, just continue moving
                            index = random.randint(0, len(exits)-1)
                            direction = exits[index]
                            self.last_direction = direction
                            return ("GO", direction)

                    else: ## If no melee and no ranged weapon
                        should_run = False
                        for tribute in tribute_vicinity: ## once again check if I'm in danger
                            tribute_weapon = tribute.get_weapons()
                            for weapon in tribute_weapon:
                                if type(weapon) == Weapon:
                                    should_run = True
                                    break
                                elif type(weapon) == RangedWeapon:
                                    if weapon.shots_left() > 0:
                                        should_run = True
                                        break
                        if should_run: ## Run away if the tribute poses a threat
                            if exits:
                                index = random.randint(0, len(exits)-1)
                                direction = exits[index]
                                self.last_direction = direction
                                return ("GO", direction)

                        if ranged_vicinity: ## If there's a ranged weapon nearby, just pick it up.
                            ranged_vicinity.sort(key = lambda x: x.min_damage(), reverse = True)
                            return ("TAKE", ranged_vicinity[0])

                        if exits: ## If I have absolutely nothing, time to move on
                            index = random.randint(0, len(exits)-1)
                            direction = exits[index]
                            self.last_direction = direction
                            return ("GO", direction)

                else:  ## if no melee weapon to pick up and no tribute
                    if ranged_weapons:
                        ranged_weapons.sort(key = lambda x: x.min_damage(), reverse = True)
                        
                        ## Actually there is no need to sort, as my code will only ever pick up one ranged
                        ## weapon for each player/tribute. But this is just in case.
                        
                        if ammo: ## if I have ammunition
                            for r_weapon in ranged_weapons:
                                for ammunition in ammo:
                                    if ammunition.weapon_type() == r_weapon.get_name():
                                        return ("LOAD", r_weapon, ammunition) ## load the weapon
                        if ammo_vicinity: ## if there's ammo nearby
                            for r_weapon in ranged_weapons:
                                for ammunition in ammo_vicinity:
                                    if ammunition.weapon_type() == r_weapon.get_name():
                                        return ("TAKE", ammunition) ## pick up ammo that I can use
                        if exits: ## If I have absolutely nothing, time to move on
                            index = random.randint(0, len(exits)-1)
                            direction = exits[index]
                            self.last_direction = direction
                            return ("GO", direction)
                    else:
                        if ranged_vicinity: ## If there's a ranged weapon nearby, just pick it up.
                            ranged_vicinity.sort(key = lambda x: x.min_damage(), reverse = True)
                            return ("TAKE", ranged_vicinity[0])
                        else:
                            if exits: ## If I have absolutely nothing, time to move on
                                index = random.randint(0, len(exits)-1)
                                direction = exits[index]
                                self.last_direction = direction
                                return ("GO", direction)


        else: ## if I have a melee weapon
            if melee_vicinity: ## but there's a better melee weapon!
                melee_vicinity.sort(key = lambda x: x.min_damage(), reverse = True)
                melee_weapons.sort(key = lambda x: x.min_damage(), reverse = True)
                if melee_vicinity[0].min_damage() > melee_weapons[0].min_damage():
                    return ("TAKE", melee_vicinity[0]) ### pick it upppp
            if living_vicinity: ## if there's a living creature nearby
                melee_weapons.sort(key = lambda x: x.min_damage(), reverse = True)
                if tribute_vicinity: ## If there's a tribute nearby
                    tribute_vicinity.sort(key = lambda x: x.get_health())
                    if len(tribute_vicinity)==1: ## If I'm only facing off against one person
                        if tribute_vicinity[0].get_health() <= melee_weapons[0].min_damage(): ## 1HKO with melee if possible
                            return ("ATTACK", tribute_vicinity[0], melee_weapons[0]) 
                        elif ranged_weapons: ## else I try to 1HKO with ranged
                            ranged_weapons.sort(key = lambda x: x.min_damage(), reverse = True)
                            for r_weapon in ranged_weapons:
                                if r_weapon.shots_left()>0:
                                    for tribute in tribute_vicinity:
                                        if tribute.get_health()<=r_weapon.min_damage(): ## if the tribute has lower health than my ranged dmg
                                            return ("ATTACK", tribute, r_weapon) ## kill
                        else:
                            for tribute in tribute_vicinity:
                                if max(list(map(lambda x: x.max_damage(), list(tribute.get_weapons())))) > health:
                                    if exits: ## if the guy has a weapon that can potentially one-shot me, run away
                                        index = random.randint(0, len(exits)-1)
                                        direction = exits[index]
                                        self.last_direction = direction
                                        return ("GO", direction)
                                            
                    else: ## If there's more than 1 enemy
                        for tribute in tribute_vicinity:
                            if max(list(map(lambda x: x.max_damage(), list(tribute.get_weapons())))) > health:
                                if exits: ## if the guy has a weapon that can potentially one-shot me, run away
                                    index = random.randint(0, len(exits)-1)
                                    direction = exits[index]
                                    self.last_direction = direction
                                    return ("GO", direction)
                        for tribute in tribute_vicinity: ## If I am relatively safe, let me try to balance things out
                            if tribute.get_health()>health: ## if my health is lower than the other person's health
                                for r_weapon in ranged_weapons:
                                    if r_weapon.shots_left()>0:
                                        return ("ATTACK", tribute, r_weapon) ## Use the high dmg ranged weapon as a game changer

                    for tribute in tribute_vicinity:## Else if cannot 1HKO and no need for any game changer, I will prioritise the tributes accordingly
                        weps = list(tribute.get_weapons())
                        for wep in weps:
                            if type(wep) == RangedWeapon:
                                if wep.shots_left() >0:
                                    return ("ATTACK", tribute, melee_weapons[0]) ## Attack those possessing ranged_weapons first
                            elif type(wep) == Weapon:
                                return ("ATTACK", tribute, melee_weapons[0]) ## then attack those with melee weapons
                    return ("ATTACK", tribute_vicinity[0], melee_weapons[0]) ## if no danger just hit the lowest health fella

                if wild_vicinity:
                    wild_vicinity.sort(key = lambda x: x.get_damage(), reverse= True)
                    return ("ATTACK", wild_vicinity[0], melee_weapons[0]) ## hit any wild animals

                return ("ATTACK", living_vicinity[0], melee_weapons[0]) ## hit any remaining animals, likely no danger

            if ranged_weapons: ## If I have a ranged weapon and there's no living creature
                ranged_weapons.sort(key = lambda x: x.min_damage(), reverse = True)
                
                if ammo: ## if I have ammunition
                    for r_weapon in ranged_weapons:
                        for ammunition in ammo:
                            if ammunition.weapon_type() == r_weapon.get_name():
                                return ("LOAD", r_weapon, ammunition) ## load the appropriate weapon
                if ammo_vicinity: ## if there's ammo nearby
                    for r_weapon in ranged_weapons:
                        for ammunition in ammo_vicinity:
                            if ammunition.weapon_type() == r_weapon.get_name():
                                return ("TAKE", ammunition) ## pick up ammo that I can use
            elif not ranged_weapons and ranged_vicinity: ## else if I have no ranged weapon but can pick up one
                ranged_vicinity.sort(key = lambda x: x.min_damage(), reverse = True)
                return ("TAKE", ranged_vicinity[0]) ## pick up the best

            if thing_vicinity: ## if there are non-living things nearby
                food_vicinity = list(filter(lambda x: isinstance(x, Food), thing_vicinity))
                if food_vicinity: ## go for the food
                    food_vicinity.sort(key = lambda x: x.get_food_value(), reverse = True)
                    if food_vicinity[0].get_food_value() >=10:
                        return ("TAKE", food_vicinity[0]) ## pickup the good food
                    elif len(food)<3: ## pickup to stockpile at least 3 food items
                        return ("TAKE", food_vicinity[0])
            if exits: ## if nothing else continue searching
                index = random.randint(0, len(exits)-1)
                direction = exits[index]
                self.last_direction = direction
                return ("GO", direction)
                
        return None ## should not occur by right, but this is a catch-all


#######################################
# Testing Code
#######################################

# We only execute code inside the if statement if this file is
# not being imported into another file
if __name__ == '__main__':
    def qualifer_map(size, wrap):
        game_config = GameConfig()
        game_config.set_item_count(Weapon, 10)
        game_config.set_item_count(RangedWeapon, 10)
        game_config.set_item_count(Food, 10)
        game_config.set_item_count(Medicine, 10)
        game_config.set_item_count(Animal, 10)
        game_config.steps = 1000

        def spawn_wild_animals(game):
            for i in range(3):
                animal = DefaultItemFactory.create(WildAnimal)
                game.add_object(animal[0])
                GAME_LOGGER.add_event("SPAWNED", animal[0])
        game_config.add_periodic_event(20, spawn_wild_animals, "Spawn Wild Animals")

        return (GameMap(size, wrap=wrap), game_config)

    # Create 6 AI Clones
    tributes = []
    for i in range(6):
        # An AI is represented by a tuple, with the Class as the first element,
        # and the name of the AI as the second
        ai = (Player, "AI" + str(i))
        tributes.append(ai)

    # Qualifier Rounds
    # Uncomments to run more rounds, or modify the rounds list
    # to include more rounds into the simulation
    # (Note: More rounds = longer simulation!)
    rounds = [qualifer_map(4, False),
              #qualifer_map(4, False),
              #qualifer_map(4, False),
              qualifer_map(4, True),
              #qualifer_map(4, True),
              #qualifer_map(4, True),
             ]



    match = Match(tributes, rounds)
    print("Simulating matches... might take a while")

    # Simulate without the graphics
    # match.text_simulate_all()

    # Simulate a specific round with the graphics
    # Due to limitation in the graphics framework,
    # can only simulate one round at a time
    # Round id starts from 0
    match.gui_simulate_round(0)
