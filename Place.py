"""
Place Module
------------
This module defines a Place class
"""
from dataclasses import dataclass

from GameObject import GameObject
import UI
import WordParser as wp

class Place(GameObject):
    def __init__(self, name, description, things_here=None, north=None,
            east=None, south=None, west=None):
        self.description = description

        if things_here is None:
            things_here = []
        self.things_here = things_here
        self.identifiers = ["here", "around", name]
        self.name = name
        self._north = north
        self._east = east
        self._south = south
        self._west = west

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
        return self._north

    @north.setter
    def north(self, place):
        if self._north is not place:
            self._north = place
            place.south = self

    @property
    def east(self):
        return self._east

    @east.setter
    def east(self, place):
        if self._east is not place:
            self._east = place
            place.west = self

    @property
    def south(self):
        return self._south

    @south.setter
    def south(self, place):
        if self._south is not place:
            self._south = place
            place.north = self

    @property
    def west(self):
        return self._west

    @west.setter
    def west(self, place):
        if self._west is not place:
            self._west = place
            place.east = self

    def take(self, item):
        self.things_here.append(item)

    def give(self, item):
        # FIXME else
        if item in self.things_here:
            self.things_here.remove(item)
