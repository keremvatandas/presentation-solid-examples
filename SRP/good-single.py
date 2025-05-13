class Singer:
    def __init__(self, name):
        self.name = name

    def sing(self):
        return f"{self.name} is singing a beautiful song."


class Dancer:
    def __init__(self, name):
        self.name = name

    def dance(self):
        return f"{self.name} is dancing with amazing moves."


# Usage
singer = Singer("Blue Jigglypuff (Singer)")
print(singer.sing())

dancer = Dancer("Purple Jigglypuff (Dancer)")
print(dancer.dance())
