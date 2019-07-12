from Place import Place, Door
from Item import Item

intro_text = 'You wake up, sprawled on the floor in a small space. You don\'t '
'feel too good and your brain feels foggy.'

closet = Place(name='Closet', description='You appear to be in a storage closet '
        'of some kind.', door_north=Door(description='A simple wooden door.',
            key_id='closet_door'))
hallway1 = Place(name='Hallway', description='You are standing in a hallway.')
hallway2 = Place(name='Hallway', description='You are standing in a hallway.')

closet.north = hallway1
hallway1.east = hallway2

initial_location = closet
