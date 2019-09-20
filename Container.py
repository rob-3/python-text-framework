from GameObject import GameObject
import HigherOrderFunction as hof

class NoSuchGameObjectInContainerException(Exception):
    pass

class Container(GameObject):
    def __init__(self, things):
        super().__init__()
        if things is not None:
            self.things = things
        else:
            self.things = []

    def has_thing_called(self, game_object):
        '''
        Checks if there is game_object is in self.things with identifier
        game_object
        '''
        maybe_thing = hof.find(self.things, lambda thing: bool(thing is game_object))
        if maybe_thing is not None:
            return True
        return False

    def get(self, string):
        thing = hof.find(self.things, lambda thing: thing.is_called(string))
        if thing is not None:
            return thing
        else:
            raise NoSuchGameObjectInContainerException(f'Tried to get a '
            '"{string}" from {self.things}')

    def print_description(self):
        raise NotImplementedError()
