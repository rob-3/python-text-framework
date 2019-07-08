"""
Fully implemented
"""
from dataclasses import dataclass
from Place import Place

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


@dataclass
class Exit:
    origin: Place
    direction: str
    destination: Place

class WorldManager:
    def __init__(self):
        self._exits = []

    def attach(self, place1, direction, place2):
        """
        Creates two exit objects: one heading in $direction from $place2 to
        $place1, and the other heading in $direction.opposite from $place1 to
        $place2.
        """
        exit = Exit(place2, direction, place1)
        opposite_exit = Exit(place1, get_opposite_direction(direction), place2)
        self._exits.append(exit)
        self._exits.append(opposite_exit)

    def get_place(self, direction, origin):
        # There should only be one exit that matches the criteria
        # FIXME check for other places and raise exception
        for my_exit in self._exits:
            if my_exit.direction == direction and my_exit.origin == origin:
                return my_exit.destination

    def get_place_north_of(self, origin):
        return self.get_place("north", origin)

    def get_place_east_of(self, origin):
        return self.get_place("east", origin)

    def get_place_south_of(self, origin):
        return self.get_place("south", origin)

    def get_place_west_of(self, origin):
        return self.get_place("west", origin)
