import UI

class GameObject:
    def __init__(self):
        self.interact = {
            'look': self.on_look,
        }
        self.identifiers = []

    def on_look(self, player):
        self.print_description()

    def print_description(self):
        raise NotImplementedError

    def is_called(self, string):
        for identifier in self.identifiers:
            if identifier == string:
                return True
        return False

    # for debug shell
    def __str__(self):
        self.print_description()
        return None
