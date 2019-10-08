from hungry_games_classes import *
from engine import *
from contest_engine import *
from collections import OrderedDict
import json
import gui_simulation

class Match(object):
    def __init__(self, tribute_classes, rounds_info):
        self.scores = OrderedDict()

        tributes = self.tributes(tribute_classes)
        survival_bonus = (len(tributes) - 2) * 50 
        for tribute in tributes:
            self.scores[tribute] = 0

        self.rounds = list(map(lambda round_info: Round(self.tributes(tribute_classes), survival_bonus, *round_info), rounds_info))


    def tributes(self, tribute_classes):
        instances = []
        for cls, name in tribute_classes:
            instance = cls(name, 200)
            instances.append(instance)

            # Give everyone a knife
            knife = Weapon("Knife", 5, 10)
            instance.inventory.append(knife)
        return instances

    def simulate(self):
        for r in self.rounds:
            r.simulate()
            for tribute in r.scores:
                self.scores[tribute] += r.scores[tribute]

    def text_simulate_all(self):
        self.simulate()
        self.print_output()

    def gui_simulate_round(self, roundId):
        if roundId < 0 or roundId >= len(self.rounds):
            raise Exception("Invalid round")

        r = self.rounds[roundId]
        r.gui_simulate()


    def print_output(self):
        for i, rnd in enumerate(self.rounds):
            print('===== Round {} ====='.format(i+1))
            rnd.print_output()

    def output(self):
        def score():
            scores = OrderedDict()
            for tribute in self.scores.keys():
                scores[tribute.get_name()] = self.scores[tribute]
            return scores

        rounds = list(map(lambda round: round.json_output(), self.rounds))
        return {'scores': score(), 'rounds': rounds}

    def json_output(self):
        return json.dumps(self.output(), sort_keys=True, indent=2)


class Round(object):
    def __init__(self, tributes, survival_bonus, game_map, game_config):
        self.tributes = tributes
        self.game_map = game_map
        self.game_config = game_config
        self.bonus = survival_bonus
        self.simulated = False

    def simulate(self):
        game = ContestEngine(self.game_map, self.game_config)
        for tribute in self.tributes:
            game.add_tribute(tribute)

        game.start()

        self.simulated = True
        self.events = GAME_LOGGER.events
        self.map_states = GAME_LOGGER.map_states
        self.time = len(self.events) - 1
        self.scores = self.score_events()

    def gui_simulate(self):
        if not self.simulated:
            self.simulate()
        gui_simulation.animate_game_events(self.game_map.size, self.events, self.map_states)

    def score_events(self):
        if not self.simulated:
            raise Exception('Round not simulated')

        scores = OrderedDict()
        for tribute in self.tributes:
            scores[tribute] = 0

        for i in range(1, self.time+1):
            for event in self.events[i]:
                if event[0] == 'KILLED' and isinstance(event[1], Tribute):
                    if isinstance(event[2], Tribute):
                        scores[event[1]] += 50
                    elif type(event[2]) == WildAnimal:
                        scores[event[1]] += 20
                    elif type(event[2]) == Animal:
                        scores[event[1]] += 10

        # Calculate survived scores
        survivor_events = list(filter(lambda event: event[0] == 'SURVIVED', self.events[self.time]))
        for event in survivor_events:
            scores[event[1]] += self.bonus // len(survivor_events)

        return scores

    def print_output(self):
        if not self.simulated:
            raise Exception('Round not simulated')

        GAME_LOGGER.print_events(self.events)

    def json_output(self):
        if not self.simulated:
            raise Exception('Round not simulated')

        def json_tuple(tup):
            output = []
            for item in tup:
                if isinstance(item, NamedObject):
                    output.append(item.json_output())
                elif isinstance(item, tuple):
                    output.append(json_tuple(item))
                else:
                    output.append(item)
            return tuple(output)

        def json_score():
            scores = OrderedDict()
            for tribute in self.scores.keys():
                scores[tribute.get_name()] = self.scores[tribute]
            return scores

        def json_config():
            def json_map():
                return {'size': self.game_map.size, 'wrap': self.game_map.wrap == 1}

            items = []
            for itemClass, qty in self.game_config.item_counts.items():
                items.append({'type': itemClass.__name__, 'qty': qty})

            periodic_events = []
            for periodic_event in self.game_config.periodic_events:
                periodic_events.append({'description': periodic_event[2], 'interval': periodic_event[0]})

            return {'items': items, 'max_steps': self.game_config.steps, 'periodic_events': periodic_events, 'map': json_map()}

        def json_history():
            def json_map(i):
                map_state = OrderedDict()
                for j in range(len(self.map_states[i])):
                    for k in range(len(self.map_states[i][j])):
                        map_state[self.map_states[i][j][k].get_name()] = self.map_states[i][j][k].json_output()
                return map_state

            def json_events(i):
                events = []
                for event in self.events[i]:
                    events.append(json_tuple(event))
                return events
            history = []
            for i in range(self.time):
                history.append({'map': json_map(i), 'events': json_events(i+1)})

            return history

        return {'scores': json_score(), 'history': json_history(), 'config': json_config()};
