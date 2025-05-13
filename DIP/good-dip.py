class Footwear:
    def description(self):
        pass


class PinkBoots(Footwear):
    def description(self):
        return "these unique pink boots"


class BlueShoes(Footwear):
    def description(self):
        return "these cool blue shoes"


class GreenSandals(Footwear):
    def description(self):
        return "these comfy green sandals"


class GoodKirby:
    def __init__(self, footwear):
        # Kirby doesn't depend on the concrete class, it depends on the abstract interface
        # Footwear is injected from the outside (Dependency Injection)
        self.footwear = footwear

    def walk(self):
        return f"I can walk with {self.footwear.description()} given to me lol"


print("\nGOOD EXAMPLE - DIP Compliant:")
kirby_with_pink_boots = GoodKirby(PinkBoots())
kirby_with_blue_shoes = GoodKirby(BlueShoes())
kirby_with_green_sandals = GoodKirby(GreenSandals())

print(f"Kirby with pink boots: {kirby_with_pink_boots.walk()}")
print(f"Kirby with blue shoes: {kirby_with_blue_shoes.walk()}")
print(f"Kirby with green sandals: {kirby_with_green_sandals.walk()}")
print("Kirby can now walk with any footwear type!")
