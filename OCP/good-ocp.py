class Vehicle:
    def can_fly(self):
        return False


class Car(Vehicle):
    pass


class FlyingCar(Vehicle):
    def can_fly(self):
        return True


print("\nGOOD EXAMPLE - OCP Compliant:")
good_regular_car = Car()
good_flying_car = FlyingCar()
print(f"Regular car can fly: {good_regular_car.can_fly()}")
print(f"Flying car can fly: {good_flying_car.can_fly()}")
print("To add a new car type, we only need to inherit from the Vehicle class!")
