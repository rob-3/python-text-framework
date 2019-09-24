from functools import reduce
from GameObject import GameObject

class Container(GameObject):
    def __init__(self, things):
        super().__init__()
        if things is not None:
            self.things = things
        else:
            self.things = []

    def get(self, string):
        '''
        Takes a string which is checked against all identifiers in the
        Container. An array of any matching items is returned. An empty array
        will be returned if no objects match.
        '''
        # FIXME prevent "" from being matched just to be defensive
        def function(accum, new_elem):
            if isinstance(new_elem, Container):
                matching_contents = reduce(function, new_elem, [])
                accum.append(matching_contents)
            if new_elem.is_called(string):
                accum.append(new_elem)
            return accum
        things = reduce(function, self.things, [])
        return things

    def print_description(self):
        raise NotImplementedError()
