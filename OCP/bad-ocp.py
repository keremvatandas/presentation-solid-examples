class BadCar:
    def __init__(self, type):
        self.type = type

    def can_fly(self):
        # When a new car type is added, we need to change this method
        if self.type == "regular":
            return False
        elif self.type == "flying":
            return True
        # New type added, we need to change this method
        return False


print("BAD EXAMPLE - OCP Violation:")
bad_regular_car = BadCar("regular")
bad_flying_car = BadCar("flying")
print(f"Regular car can fly: {bad_regular_car.can_fly()}")
print(f"Flying car can fly: {bad_flying_car.can_fly()}")
print("To add a new car type, we need to change the BadCar class!")
