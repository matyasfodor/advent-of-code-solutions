class Ingredient(object):
    def __init__(self, capacity, durability, flavor, texture, calories):
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories

    def get_amount(self, amount):
        return Ingredient(**{key: value * amount for key, value in self.__dict__.iteritems()})

    def get_full_score(self):
        score = 1
        for ingredient_property in ['capacity', 'durability', 'flavor', 'texture']:
            score *= max(self.__dict__[ingredient_property], 0)
        return score

    def __add__(self, other):
        properties = {}
        for key in self.__dict__:
            properties[key] = self.__dict__[key] + other.__dict__[key]
        return Ingredient(**properties)

    @classmethod
    def parse_line(cls, line):
        _, rest_data = line.split(': ')
        property_points = [entry.split() for entry in rest_data.split(', ')]
        kwargs = {entry_pair[0]: int(entry_pair[1]) for entry_pair in property_points}
        return cls(**kwargs)

    @classmethod
    def empty_ingredient(cls):
        return cls(0, 0, 0, 0, 0)