import UI
import WordParser as wp
from GameObject import GameObject

class Place(GameObject):
    def __init__(self, name, description, world_manager, things_here=None):
        self.description = description

        if things_here is None:
            things_here = []
        self.things_here = things_here
        self.world_manager = world_manager
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

    def attach_to_north_of(self, place):
        self.world_manager.attach(self, "north", place)

    def attach_to_east_of(self, place):
        self.world_manager.attach(self, "east", place)

    def attach_to_south_of(self, place):
        self.world_manager.attach(self, "south", place)

    def attach_to_west_of(self, place):
        self.world_manager.attach(self, "west", place)

    @property
    def north(self):
        return self.world_manager.get_place_north_of(self)

    @property
    def east(self):
        return self.world_manager.get_place_east_of(self)

    @property
    def south(self):
        return self.world_manager.get_place_south_of(self)

    @property
    def west(self):
        return self.world_manager.get_place_west_of(self)

    def take(self, item):
        self.things_here.append(item)

    def give(self, item):
        # FIXME else
        if item in self.things_here:
            self.things_here.remove(item)
