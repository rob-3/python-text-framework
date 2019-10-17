'''
Place Module
------------
This module defines a Place class
'''
from Container import Container
from Immovable import Immovable
import UI
import WordParser as wp

class Place(Container):
    def __init__(self, name, description, things_here=None, north=None,
            east=None, south=None, west=None, door_north=None, door_east=None,
            door_south=None, door_west=None):
        super().__init__(things_here)
        self.description = description

        if things_here is None:
            things_here = []
        self.things = things_here
        self.identifiers = ['here', 'around', name]
        self.name = name
        self.places = {'north': north, 'east': east, 'south': south, 'west': west}
        self.doors = {'north': door_north, 'east': door_east, 'south': door_south, 'west': door_west}
        # FIXME appends doors to things_here
        # FIXME lists for direction refs and doors

        self.interact['go'] = self.on_go
        self.interact['burn'] = self.on_burn

    def on_burn(self, player):
        if player.is_here(self):
            UI.println('What kind of pyromaniac are you?')
        else:
            # FIXME
            UI.println('Too far away.')

    def on_look(self, player):
        if player.is_here(self):
            self.print_description()
        else:
            # FIXME
            UI.println('Too far away.')

    def print_description(self):
        UI.print_in_box(self.name, True)
        UI.println(self.description)

        for index, item in enumerate(self.things):
            if index == 0:
                UI.println()
            UI.println(f'There is a {item.name.lower()} here.')

        # This avoids a double print of door and direction for exits
        directions_accounted_for = {'north': False, 'east': False, 'south':
                False, 'west': False}
        # We want a leading blank line to help with readability
        UI.println()

        for direction, door in self.doors.items():
            if door is not None:
                if door.closed:
                    UI.println(f'There is a closed door to the {direction}.')
                else:
                    UI.println(f'There is an open door to the {direction}.')
                directions_accounted_for[direction] = True
        for direction, place in self.places.items():
            if not directions_accounted_for[direction] and place is not None:
                UI.println(f'There is an exit to the {direction}.')

    def on_go(self, player):
        player.move_to(self)

    def on_enter(self, player):
        # TODO should we be adding player to things_here?
        self.print_description()
        while player.is_here(self):
            wp.process_input(UI.prompt(), player)

    @property
    def north(self):
        if self.doors['north'] is not None:
            return self.doors['north']
        return self.places['north']

    @north.setter
    def north(self, place):
        if self.places['north'] is not place:
            self.places['north'] = place
            place.south = self
            # Door handling
            if self.doors['north'] is not None:
                self.doors['north'].origin = self
                self.doors['north'].destination = place
                place.doors['south'] = self.doors['north']
            elif place.doors['south'] is not None:
                place.doors['south'].origin = place
                place.doors['south'].destination = self
                self.doors['north'] = place.doors['south']
                
    @property
    def east(self):
        if self.doors['east'] is not None:
            return self.doors['east']
        return self.places['east']

    @east.setter
    def east(self, place):
        if self.places['east'] is not place:
            self.places['east'] = place
            place.west = self
            # Door handling
            if self.doors['east'] is not None:
                self.doors['east'].origin = self
                self.doors['east'].destination = place
                place.doors['west'] = self.doors['east']
            elif place.doors['west'] is not None:
                place.doors['west'].origin = place
                place.doors['west'].destination = self
                self.doors['east'] = place.doors['west']
                
    @property
    def south(self):
        if self.doors['south'] is not None:
            return self.doors['south']
        return self.places['south']

    @south.setter
    def south(self, place):
        if self.places['south'] is not place:
            self.places['south'] = place
            place.north = self
            # Door handling
            if self.doors['south'] is not None:
                self.doors['south'].origin = self
                self.doors['south'].destination = place
                place.doors['north'] = self.doors['south']
            elif place.doors['north'] is not None:
                place.doors['north'].origin = place
                place.doors['north'].destination = self
                self.doors['south'] = place.doors['north']
                
    @property
    def west(self):
        if self.doors['west'] is not None:
            return self.doors['west']
        return self.places['west']

    @west.setter
    def west(self, place):
        if self.places['west'] is not place:
            self.places['west'] = place
            place.east = self
            # Door handling
            if self.doors['west'] is not None:
                self.doors['west'].origin = self
                self.doors['west'].destination = place
                place.doors['east'] = self.doors['west']
            elif place.doors['east'] is not None:
                place.doors['east'].origin = place
                place.doors['east'].destination = self
                self.doors['west'] = place.doors['east']
                
    def take(self, item):
        self.things.append(item)

    def give(self, item):
        # FIXME else
        if item in self.things:
            self.things.remove(item)

    @property
    def things_here(self):
        return self.things + [door for door in self.doors.values() if door is not None]

class Door(Immovable):
    def __init__(self, description, key_id, closed=True, locked=False, identifiers=None, name='Door'):
        super().__init__(name, description, identifiers)
        self.key_id = key_id
        self.description = description
        self.name = name
        self.origin = None
        self.destination = None
        self.locked = locked
        self.closed = closed

        self.interact['unlock'] = self.on_unlock
        self.interact['lock'] = self.on_lock
        self.interact['open'] = self.on_open
        self.interact['close'] = self.on_close
        self.interact['go'] = self.on_go

    def on_unlock(self, player):
        if not self.locked:
            UI.println('The door is already unlocked.')
        elif player.has_key(self.key_id):
            self.locked = False
            UI.println('The door is now unlocked.')
        else:
            UI.println('You don\'t have the proper key to unlock this door.')

    def on_lock(self, player):
        if self.locked:
            UI.println('The door is already locked.')
        elif player.has_key(self.key_id):
            self.locked = True
            UI.println('The door is now locked.')
        else:
            UI.println('You don\'t have the proper key to unlock this door.')

    def other_side(self, place):
        if place is None:
            raise PassedWrongPlaceToDoorException()
        if place is self.origin:
            return self.destination
        elif place is self.destination:
            return self.origin
        else:
            raise PassedWrongPlaceToDoorException()

    def on_go(self, player):
        if self.closed:
            UI.println('The door is closed.')
        else:
            self.other_side(player.location).on_go(player)

    def on_open(self, player):
        if self.closed:
            if self.locked:
                UI.println('The door is locked.')
            else:
                self.closed = False
                UI.println('The door is now open.')
        else:
            UI.println('The door is already open.')

    def on_close(self, player):
        if self.closed:
            UI.println('The door is already closed.')
        elif self.locked:
            UI.println('The door is locked, so you cannot close it.')
        else:
            self.closed = True 
            UI.println('The door is now closed.')

class PassedWrongPlaceToDoorException(Exception):
    pass
