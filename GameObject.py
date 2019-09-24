import UI

class GameObject:
    def __init__(self):
        self.interact = {
            'look': self.on_look,
        }
        self.identifiers = []
        self.description = ""

    def on_look(self, player):
        UI.println(self.description)

    def is_called(self, string):
        for identifier in self.identifiers:
            if identifier == string:
                return True
        return False

    # for debug shell
    def __str__(self):
        return self.description
