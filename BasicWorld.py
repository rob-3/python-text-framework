from World import Place
from Item import Item

intro_text = ''

key = Item("Key", "A simple worn metal key.")
hill = Place("Hill", "You walk up a long path to the top of a nearby hill. The air is clear and there is a castle far to the north.", [key])
grasslands = Place("", "You reach a grasslands area at the foot of a hill to the south. To the north there is a castle.")

abandoned_castle_front = Place("Castle Front", "You are at the front of what appears to be a ruined castle. The castle has 4 major towers the nearest ones - those to the southeast and the southwest - are in tatters. The northern towers still appear relatively intact.")
abandoned_castle_corner_se = Place("Castle SE tower", "A tower (in shambles) rises upon this corner of the castle.")
abandoned_castle_corner_sw = Place("Castle SW tower", "A ruined tower rests above. Moss covers the stones still standing. A few large stones are scattered around the area.")
swarshy_swamp = Place("Swarshy Swamp", "Muck and vines lather the faces of the trees.")
granite_obelisk = Place("Obelisk of the Lathenheim Fiends", "A shiny black and red tower rises into the swirling purple sky.")

# Set player's initial location
inital_location = hill

# Wire together all of the places
hill.north = grasslands
grasslands.north = abandoned_castle_front
abandoned_castle_front.east = abandoned_castle_corner_se
abandoned_castle_front.west = abandoned_castle_corner_sw
grasslands.east = swarshy_swamp
swarshy_swamp.east = granite_obelisk
