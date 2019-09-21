
from Place import *
from Item import *
from Container import Container

intro_text = ''


crossroads1=Place(name='Crossroads', description='A windy and secluded path with 4 directions to travel.', things_here=[Trimmer(name='trimmer', description='A metal trimmer for plants.', cut_id='vinewallcutter')])

dark_path=Place(name='Path', description='A normal path leading through a small forest. Something feels wrong with this path, but you can\'t seem to figure out what it is. The path gets darker and darker the deeper you go.')

dark_entrance=Place(name='Deep Forest', description='A somewhat dark and spooky forest. A very dark and speeky forest lies ahead, and you can\'t shake the feeling that you shouldn\'t be here. Strange noises are coming from the dark forest, and the entrance to the dark forest is blocked by a wall of vines.')

dark_forest1=Place(name='Dark Forest', description='', vinewall_east=Vinewall(description='A wall of vines blocking the entrance to the dark forest.', cut_id='vinewallcutter', cut=False))

crossroads1.west = dark_path
dark_path.west = dark_entrance
dark_entrance.west = dark_forest1

initial_location = crossroads1
world_globals = globals()