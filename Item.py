from GameObject import GameObject
import UI

class Item(GameObject):
    def __init__(self, name, description, identifiers=None):
        super().__init__()
        self.name = name
        self.description = description

        if identifiers is None:
            identifiers = []
        self.identifiers = identifiers
        self.identifiers.append(name.lower())
    
    def on_burn(self, player):
        UI.println('This is not something you should burn.')

    def on_go(self, player):
        UI.println('You\'re there.')

    def print_description(self):
        UI.print_in_box(self.name, False)
        UI.println(self.description)

    def on_drop(self, player):
        # FIXME else
        if player.has(self):
            player.give(self)
            player.location.take(self)
            UI.println('Dropped.')

    def on_pickup(self, player):
        # FIXME else
        if self in player.location.things_here:
            player.take(self)
            player.location.give(self)
            UI.println('Taken.')
