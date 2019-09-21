import UI
from Place import *
from Item import *
from Player import *
from World import *

class AJWorld(World):
    def __init__(self):
        # all init for rooms/items goes here
        self.place1 = Place(name='Place', description='A nice place')
        self.item1 = Item(name='Item', description='An item')
        
        # you can also create things inline to put them inside of rooms
        # however, they will no longer be available to the debugger without a
        # prefix if you choose to do this (of course you can still access them
        # from .get()ing them from the place)
        self.place2 = Place(name='Place2', description='A very nice place',
                things_here=[Item(name='Item2', description='Item in a room!')])
                
        self.cabin_livingroom = Place(name='Cabin Living Room', description='In the main room of the log cabin, there is a lit fireplace that crackles as it gives off heat, and there are two chairs next to the fireplace.  You see your friend\'s dead body on the ground, and you are reminded of his gruesome death.', things_here=[Key(name='key', description='A simple worn metal key.', key_id='cabin_door')])
        
        self.cabin_exterior = Place(name='Cabin Exterior', description='The ground around the cabin is muddy, but a gravel path leads to the front door of the cabin. To the west is a thick wall of trees.', door_north=Door(description='A worn front door to the log cabin.', key_id='cabin_door', locked=True))
        
        self.cabin_bedroom1 = Place(name='Cabin Bedroom', description='The bedroom has a large bed with a drawer beside it.  A candle-lit table is at the end of the room.')
      
        self.cabin_shed = Place(name='Shed', description='A simple wood shed with a variety of tools.', door_west=Door(description='A large, simple door to the shed.', key_id='cabin_door', locked=True), things_here=[Battery(name='battery', description='A small flashlight battery.', battery_id='flashlight'), Flashlight(name='flashlight', description='A small flashlight battery.', battery_id='flashlight')])
        
        self.cabin_bedroom2 = Place(name='Cabin Bedroom', description='The bedroom has a large bed and a table with a chair on it.  There is also a storage closet on the north wall of the room.', door_north=Door(description='A small closet door.', key_id='cabin_door', locked = True))
        
        self.cabin_closet = Place(name='Closet', description='A small closet with space for items.', things_here=[Key(name='key', description='A small metal key with no obvious function', key_id='mineshaft_entrance')])

        self.crossroads1=Place(name='Crossroads', description='A windy and secluded path with 4 directions to travel.', things_here=[Trimmer(name='trimmer', description='A metal trimmer for plants.', cut_id='vinewallcutter')])

        self.dark_path=Place(name='Path', description='A normal path leading through a small forest. Something feels wrong with this path, but you can\'t seem to figure out what it is. The path gets darker and darker the deeper you go.')

        self.dark_entrance=Place(name='Deep Forest', description='A somewhat dark and spooky forest. A very dark and speeky forest lies ahead, and you can\'t shake the feeling that you shouldn\'t be here. Strange noises are coming from the dark forest, and the entrance to the dark forest is blocked by a wall of vines.')

        self.dark_forest1=Place(name='Dark Forest', description='', vinewall_east=Vinewall(description='A wall of vines blocking the entrance to the dark forest.', cut_id='vinewallcutter', cut=False))
        
        self.cabin_exterior.north = cabin_livingroom
        self.cabin_livingroom.west = cabin_bedroom1
        self.cabin_shed.west = cabin_exterior
        self.cabin_livingroom.east = cabin_bedroom2
        self.cabin_bedroom2.north = cabin_closet
        self.cabin_exterior.south = crossroads1
        self.crossroads1.west = dark_path
        self.dark_path.west = dark_entrance
        self.dark_entrance.west = dark_forest1
        
        # remove the line below in your subclass
        raise NotImplementedError()

    def start_adventure(self, player):
        '''
        You should do any one-time prints here and set the initial location of
        the player. Suggested code is below.
        '''
        UI.println('Game beginning')

        # this line is important if you want debugging to work
        player.world = self

        player.location = self.cabin_livingroom

        # set the breakout condition to when you want to end the game
        while True:
            player.location.on_enter(player)

        self.end_adventure(player)

        # remove the line below in your subclass
        raise NotImplementedError()

    def end_adventure(self, player):
        '''
        Called when the adventure is ended. Put any final messages you want here
        like credits.
        '''
        # remove the line below in your subclass
        raise NotImplementedError()

if __name__ == '__main__':
    AJWorld().start_adventure(Player())