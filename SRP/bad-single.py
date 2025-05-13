class Performer:
    def __init__(self, name):
        self.name = name

    def sing(self):
        return f"{self.name} is singing a beautiful song."

    def dance(self):
        return f"{self.name} is dancing with amazing moves."


# Usage
kirby_bad = Performer("Pink Kirby")
print(kirby_bad.sing())
print(kirby_bad.dance())
