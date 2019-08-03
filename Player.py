'''
The Player character in the game.
'''
from GameObject import GameObject
import UI

class Player(GameObject):
    def __init__(self, hp, inventory, starting_location):
        super().__init__()
        # FIXME name
        self.name = '[Player name]'
        self.description = 'It\'s you, what did you expect?'
        self.identifiers = ['me', 'myself', 'i']
        self.hp = hp
        self.inventory = inventory
        self.location = starting_location

    def move_to(self, location):
        self.location = location

    @property
    def north(self):
        return self.location.north

    @property
    def east(self):
        return self.location.east

    @property
    def south(self):
        return self.location.south

    @property
    def west(self):
        return self.location.west

    def is_here(self, location):
        return bool(self.location == location)

    def get_all_things(self):
        all_things = []
        # Get everything in this location
        all_things.extend(self.location.things_here)
        # Add inventory
        all_things.extend(self.inventory)
        # Get this location
        all_things.append(self.location)
        # Get the player himself
        all_things.append(self)
        return all_things

    def on_burn(self, player):
        UI.println('Are you masochistic?')

    def on_go(self, player):
        UI.println('You are already with yourself.')

    def print_description(self):
        UI.println(self.description)

    def take(self, item):
        self.inventory.append(item)

    def give(self, item):
        # FIXME else
        if item in self.inventory:
            self.inventory.remove(item)

    def has(self, item):
        return bool(item in self.inventory)
