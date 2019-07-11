from GameObject import GameObject
import UI

class Immovable(GameObject):
    def __init__(self, name, description, identifiers=None):
        self.name = name
        self.description = description

        if identifiers is None:
            identifiers = []
        self.identifiers = identifiers
        self.identifiers.append(name.lower())

    def print_description(self):
        UI.print_in_box(self.name, False)
        UI.println(self.description)

    def on_drop(self, player):
        # FIXME
        raise Exception('You can\'t drop this!')


    def on_pickup(self, player):
        UI.println('You should know you can\'t pick this up.')
