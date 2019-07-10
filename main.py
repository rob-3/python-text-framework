"""
The main game class.
"""
import UI
import NewWorld as world
from Player import Player

# TODO allow player to pick a world from many options

def main():
    """
    The main function that is called when the game starts.
    """
    UI.println("Welcome to my game!")

    player = Player(100, [], world.initial_location)
    UI.println(world.intro_text)
    while True:
        player.location.on_enter(player)
    # FIXME no exit condition


if __name__ == "__main__":
    main()
