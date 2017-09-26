"""Class that create recipe object"""


class Recipe(object):
    """Recipe object class"""

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.ingredients = []    