"""
The main game class.
"""
import UI
from BasicWorld import BasicWorld
from Player import Player


def main():
    """
    The main function that is called when the game starts.
    """
    UI.println("Welcome to my game!")

    # TODO allow player to pick a world from many options
    world = BasicWorld()
    player = Player(100, [], world.inital_location)
    while True:
        player.location.on_enter(player)
    # FIXME no exit condition


if __name__ == "__main__":
    main()
