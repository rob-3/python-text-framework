from GameObject import GameObject
import UI

class Immovable(GameObject):
    def __init__(self, name, description, identifiers=None):
        super().__init__()
        self.name = name
        self._description = description

        if identifiers is None:
            identifiers = []
        self.identifiers = identifiers
        self.identifiers.append(name.lower())

    def print_description(self):
        '''
        DEPRECATED: Use Immovable.description and then call UI.println()
        yourself.
        '''
        UI.print_in_box(self.name, False)
        UI.println(self._description)

    @property
    def description(self):
        '''
        Returns description of immovable, complete with the name boxed.
        '''
        return_string = ''
        return_string += UI.wrap_in_box(self.name, False)
        return_string += self._description + '\n'
        return return_string

    def on_drop(self, player):
        # FIXME
        raise Exception('You can\'t drop this!')

    def on_pickup(self, player):
        UI.println('You should know you can\'t pick this up.')
