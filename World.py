import UI
from Place import Place
from Item import Item

class World():
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

        player.location = self.place1

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
