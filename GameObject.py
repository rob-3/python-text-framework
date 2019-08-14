import UI

class GameObject:
    def __init__(self):
        self.interact = {
            'look': self.on_look,
        }

    def on_look(self, player):
        self.print_description()

    def print_description(self):
        raise NotImplementedError
