class BadKirby:
    def __init__(self):
        # Kirby directly depends on PinkBoots
        # There is a direct dependency on the concrete class
        self.boots = PinkBoots()

    def walk(self):
        return f"I can walk with {self.boots.description()}"


class PinkBoots:
    def description(self):
        return "these unique pink boots"


print("BAD EXAMPLE - DIP Violation:")
kirby = BadKirby()
print(f"Kirby: {kirby.walk()}")
print("Kirby directly depends on PinkBoots and can't use other footwear!")
