'''
The main game class.
'''
import UI
from Player import Player

# import your world here
from World import World

# TODO allow player to pick a world from many options

def main():
    '''
    The main function that is called when the game starts.
    '''
    player = Player(100, [])
    # change this line to use your constructor
    world = World()
    world.start_adventure(player)

if __name__ == '__main__':
    main()
