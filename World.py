"""
World Module
------------
This module defines a Place class and a WorldManager for managing relationships
between Places.
"""
from dataclasses import dataclass

from GameObject import GameObject
import UI
import WordParser as wp

class Place(GameObject):
    def __init__(self, name, description, things_here=None):
        self.description = description

        if things_here is None:
            things_here = []
        self.things_here = things_here
        self.identifiers = ["here", "around", name]
        self.name = name

    def contains_thing(self, game_object):
        """
        This implementation relies on the fact that game_object.location is
        actually updated as it changes.
        """
        return bool(game_object.location == self)

    def on_burn(self, player):
        if player.is_here(self):
            UI.println("What kind of pyromaniac are you?")
        else:
            # FIXME
            UI.println("Too far away.")

    def on_look(self, player):
        if player.is_here(self):
            self.print_description()
        else:
            # FIXME
            UI.println("Too far away.")

    def print_description(self):
        UI.print_in_box(self.name)
        UI.println(self.description)
        for index, item in enumerate(self.things_here):
            if index == 0:
                UI.println()
            UI.println(f"There is a {item.name.lower()} here.")
        UI.println()
        if self.north is not None:
            UI.println("There is an exit to the north.")
        if self.east is not None:
            UI.println("There is an exit to the east.")
        if self.south is not None:
            UI.println("There is an exit to the south.")
        if self.west is not None:
            UI.println("There is an exit to the west.")

    def on_go(self, player):
        player.move_to(self)

    def on_enter(self, player):
        # TODO should we be adding player to things_here?
        self.print_description()
        while player.is_here(self):
            wp.process_input(UI.prompt(), player)

    @property
    def north(self):
        return get_place_north_of(self)

    @north.setter
    def north(self, place):
        attach(place, "north", self)

    @property
    def east(self):
        return get_place_east_of(self)

    @east.setter
    def east(self, place):
        attach(place, "east", self)

    @property
    def south(self):
        return get_place_south_of(self)

    @south.setter
    def south(self, place):
        attach(place, "south", self)

    @property
    def west(self):
        return get_place_west_of(self)

    @west.setter
    def west(self, place):
        attach(place, "west", self)

    def take(self, item):
        self.things_here.append(item)

    def give(self, item):
        # FIXME else
        if item in self.things_here:
            self.things_here.remove(item)

def get_opposite_direction(direction):
    if direction == "north":
        return "south"
    elif direction == "east":
        return "west"
    elif direction == "south":
        return "north"
    elif direction == "west":
        return "east"
    else:
        return None



_exits = []

def attach(place1, direction, place2):
    """
    Creates two exit objects: one heading in $direction from $place2 to
    $place1, and the other heading in $direction.opposite from $place1 to
    $place2.
    """
    my_exit = Exit(place2, direction, place1)
    opposite_exit = Exit(place1, get_opposite_direction(direction), place2)
    _exits.append(my_exit)
    _exits.append(opposite_exit)

def get_place(direction, origin):
    # There should only be one exit that matches the criteria
    # FIXME check for other places and raise exception
    for my_exit in _exits:
        if my_exit.direction == direction and my_exit.origin == origin:
            return my_exit.destination
    return None

def get_place_north_of(origin):
    return get_place("north", origin)

def get_place_east_of(origin):
    return get_place("east", origin)

def get_place_south_of(origin):
    return get_place("south", origin)

def get_place_west_of(origin):
    return get_place("west", origin)

@dataclass
class Exit:
    origin: Place
    direction: str
    destination: Place
