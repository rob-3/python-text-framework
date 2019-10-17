import UI
from Place import Place
from Item import Item
from Player import Player

# all init for rooms/items goes here
place1 = Place(name='Place', description='A nice place')
item1 = Item(name='Item', description='An item')

# you can also create things inline to put them inside of rooms
# however, they will no longer be available to the debugger without a
# prefix if you choose to do this (of course you can still access them
# from .get()ing them from the place)
place2 = Place(name='Place2', description='A very nice place',
        things_here=[Item(name='Item2', description='Item in a room!')])

def start_adventure(player):
    '''
    You should do any one-time prints here and set the initial location of
    the player. Suggested code is below.
    '''
    UI.println('Game beginning')

    # this line is important if you want debugging to work
    player.globals = globals()

    # set initial location of player
    player.location = place1

    # attaches place2 to the north of place1
    place1.north = place2

    # this is equivalent to the above
    # you only need one or the other
    place2.south = place1

    # set the breakout condition to when you want to end the game
    while True:
        player.location.on_enter(player)

    end_adventure(player)

def end_adventure(player):
    '''
    Called when the adventure is ended. Put any final messages you want here
    like credits.
    '''

if __name__ == '__main__':
    start_adventure(Player())
