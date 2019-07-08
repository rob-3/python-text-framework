import UI

class GameObject:
    def invoke(self, verb, player):
        if verb == "go":
            self.on_go(player)
        elif verb == "look":
            self.on_look(player)
        elif verb == "burn":
            self.on_burn(player)
        elif verb in ["take", "get", "obtain"]:
            self.on_pickup(player)
        elif verb == "drop":
            self.on_drop(player)
        else:
            raise Exception("Verb not defined in GameObject.py")

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

    def print_description(self):
        raise NotImplementedError
    
    def generic_reject(self):
        # TODO improve with multiple responses and random choice
        UI.println("You're not making any sense.")
