from hungry_games_classes import *
from engine import GameEngine
import os, sys

class ContestEngine(GameEngine):
    def start(self):
        GAME_LOGGER.reset()
        self.prev_tributes = self.tributes

        for event in self.config.periodic_events:
            self.add_periodic_event(*event)

        # Disable print to stdout
        stdout = sys.stdout
        f = open(os.devnull, 'w')
        sys.stdout = f

        for i in range(self.config.steps):
            self.tick()

            tributes = list(filter(lambda obj: isinstance(obj, Tribute), self.clock_list))
            if len(tributes) <= 1:
                break

            self.prev_tributes = tributes

        # If we only have one survivor, we have a winner
        if len(tributes) == 1:
            GAME_LOGGER.add_event("SURVIVED", tributes[0])

        # If all the tributes died in the last round, we will divide the score
        # amongst all that survived till that round
        else:
            for tribute in self.prev_tributes:
                GAME_LOGGER.add_event("SURVIVED", tribute)

        # Re-enable print to stdout
        sys.stdout = stdout