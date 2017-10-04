import sys

sys.path.append('..')


class Recipe(object):

    def __init__(self, name, items):
        self.name = name
        self.description = ''
        self.items = []

    def __repr__(self):
        return 'Recipe: ' + name + ', '.join(item for item in self.items)

