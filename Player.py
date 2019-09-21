'''
The Player character in the game.
'''
from GameObject import GameObject
import UI
from Item import *
from functional import forEach

class Player(GameObject):
    def __init__(self, inventory=None):
        super().__init__()
        # FIXME name
        self.name = '[Player name]'
        self.description = 'It\'s you, what did you expect?'
        self.identifiers = ['me', 'myself', 'i']
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory
        self.location = None

        self.interact['burn'] = self.on_burn
        self.interact['go'] = self.on_go
        self.interact['i'] = self.view_inventory

    def view_inventory(self, player):
        if self.inventory == []:
            UI.println('There is nothing in your inventory.')
        else:
            UI.print_in_box('Inventory', True)
            def describe(go):
                go.print_description()
            forEach(self.inventory, describe)

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

    def has_key(self, key_id):
        for item in self.inventory:
            if isinstance(item, Key) and item.key_id == key_id:
                return True
        return False
    def has_tool(self, cut_id):
        for item in self.inventory:
            if isinstance(item, Trimmer) and item.cut_id == cut_id:
                return True