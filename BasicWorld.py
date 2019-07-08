from Place import Place
from Item import Item


class BasicWorld:
    # FIXME refactor world_manager into a module
    def __init__(self, world_manager):
        self.key = Item("Key", "A simple worn metal key.")
        self.hill = Place("Hill", "You walk up a long path to the top of a nearby hill. The air is clear and there is a castle far to the north.", world_manager, [self.key])
        self.grasslands = Place("", "You reach a grasslands area at the foot of a hill to the south. To the north there is a castle.", world_manager)

        self.abandoned_castle_front = Place("Castle Front", "You are at the front of what appears to be a ruined castle. The castle has 4 major towers the nearest ones - those to the southeast and the southwest - are in tatters. The northern towers still appear relatively intact.", world_manager)
        self.abandoned_castle_corner_se = Place("Castle SE tower", "A tower (in shambles) rises upon this corner of the castle.", world_manager)
        self.abandoned_castle_corner_sw = Place("Castle SW tower", "A ruined tower rests above. Moss covers the stones still standing. A few large stones are scattered around the area.", world_manager)
        self.swarshy_swamp = Place("Swarshy Swamp", "Muck and vines lather the faces of the trees.", world_manager)
        self.granite_obelisk = Place("Obelisk of the Lathenheim Fiends", "A shiny black and red tower rises into the swirling purple sky.", world_manager)

        # Set player's initial location
        self.inital_location = self.hill

        # Wire together all of the places
        self.grasslands.attach_to_north_of(self.hill)
        self.abandoned_castle_front.attach_to_north_of(self.grasslands)
        self.abandoned_castle_corner_se.attach_to_east_of(self.abandoned_castle_front)
        self.abandoned_castle_corner_sw.attach_to_west_of(self.abandoned_castle_front)
        self.swarshy_swamp.attach_to_east_of(self.grasslands)
        self.granite_obelisk.attach_to_east_of(self.swarshy_swamp)
