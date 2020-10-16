import UI
from Place import *
from Item import *
from Container import Container
from Player import Player

intro_text = 'You wake up. You\'re slumped against a wooden wall. As you rise to your feet and begin to assess your surroundings, you almost lose your balance and tumble back to the ground. After a moment, your vision clears.'


cabin_exterior = Place(name='Cabin Exterior', description='The ground around the cabin is muddy, but a gravel path leads to the front door of the cabin. To the west is a thick wall of trees.', door_north=Door(description='A worn front door to the log cabin.', key_id='cabin_door', locked=True))

cabin_livingroom = Place(name='Cabin Living Room', description='In the main room of the log cabin, there is a lit fireplace that crackles as it gives off heat, and there are two chairs next to the fireplace.', things_here=[Key(name='key', description='A simple worn metal key.', key_id='cabin_door')])

cabin_bedroom1 = Place(name='Cabin Bedroom', description='The bedroom has a large bed with a drawer beside it.  A candle-lit table is at the end of the room.')

cabin_shed = Place(name='Shed', description='A simple wood shed with a variety of tools.', door_west=Door(description='A large, simple door to the shed.', key_id='cabin_door', locked=True), things_here=[Battery(name='battery', description='A small flashlight battery.', battery_id='flashlight'), Flashlight(name='flashlight', description='A small flashlight battery.', battery_id='flashlight')])

cabin_bedroom2 = Place(name='Cabin Bedroom', description='The bedroom has a large bed and a table with a chair on it.  There is also a storage closet on the north wall of the room.', door_north=Door(description='A small closet door.', key_id='cabin_door', locked = True))

cabin_closet = Place(name='Closet', description='A small closet with space for items.', things_here=[Key(name='key', description='A small metal key with no obvious function', key_id='mineshaft_entrance')])


cabin_exterior.north = cabin_livingroom
cabin_livingroom.west = cabin_bedroom1
cabin_shed.west = cabin_exterior
cabin_livingroom.east = cabin_bedroom2
cabin_bedroom2.north = cabin_closet

initial_location = cabin_livingroom

def start_adventure(player):
    UI.println(intro_text)
    player.globals = globals()

    player.location = initial_location

    while True:
        player.location.on_enter(player)

    # when done end adventure
    end_adventure()

def end_adventure():
    '''
    Clean up the game here, display any last messages, write to disk, etc
    '''

if __name__ == '__main__':
    start_adventure(Player())
