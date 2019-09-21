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

        self.interact['pickup'] = self.on_pickup
        self.interact['take'] = self.on_pickup
        self.interact['get'] = self.on_pickup
        self.interact['obtain'] = self.on_pickup
        self.interact['drop'] = self.on_drop
        self.interact['burn'] = self.on_burn

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
class Flashlight(Item):
    def __init__(self, description, battery_id, identifiers=None, name='Flashlight'):
        super().__init__(name, description, identifiers)
        self.battery_id = battery_id
class Key(Item):
    def __init__(self, description, key_id, identifiers=None, name='Key'):
        super().__init__(name, description, identifiers)
        self.key_id = key_id
class Battery(Item):
    def __init__(self, description, battery_id, identifiers=None, name='Battery'):
        super().__init__(name, description, identifiers)
        self.battery_id = battery_id
class Trimmer(Item):
    def __init__(self, description, cut_id, identifiers=None, name='Trimmer'):
        super().__init__(name, description, identifiers)
        self.cut_id = cut_id
