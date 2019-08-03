import UI

class GameObject:
    def __init__(self):
        self.interact = {
            'go': self.on_go,
            'look': self.on_look,
            'burn': self.on_burn,
            'take': self.on_pickup,
            'get': self.on_pickup,
            'obtain': self.on_pickup,
            'drop': self.on_drop,
            'open': self.on_open,
            'close': self.on_close
        }

    def on_burn(self, player):
        self.generic_reject()

    def on_go(self, player):
        self.generic_reject()

    def on_look(self, player):
        self.print_description()

    def on_pickup(self, player):
        self.generic_reject()

    def on_drop(self, player):
        self.generic_reject()

    def on_open(self, player):
        self.generic_reject()

    def on_close(self, player):
        self.generic_reject()

    def on_unlock(self, player):
        self.generic_reject()

    def on_lock(self, player):
        self.generic_reject()

    def print_description(self):
        raise NotImplementedError

    def generic_reject(self):
        # TODO improve with multiple responses and random choice
        UI.println('You\'re not making any sense.')
