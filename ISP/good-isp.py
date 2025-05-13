from abc import ABC, abstractmethod


class BaseKirbyInterface(ABC):
    @abstractmethod
    def be_round(self):
        pass

    @abstractmethod
    def be_cute(self):
        pass


class PinkKirbyInterface(BaseKirbyInterface):
    @abstractmethod
    def turn_into_pink_ball(self):
        pass


class BlueKirbyInterface(BaseKirbyInterface):
    @abstractmethod
    def turn_into_blue_ball(self):
        pass


class GoodPinkKirby(PinkKirbyInterface):
    def be_round(self):
        return "I am round"

    def be_cute(self):
        return "I am cute"

    def turn_into_pink_ball(self):
        return "I turned into a pink ball!"


class GoodBlueKirby(BlueKirbyInterface):
    def be_round(self):
        return "I am round"

    def be_cute(self):
        return "I am cute"

    def turn_into_blue_ball(self):
        return "I turned into a blue ball! Dope!"


print("\nGOOD EXAMPLE - ISP Compliant:")
pink_kirby = GoodPinkKirby()
blue_kirby = GoodBlueKirby()

print("Pink Kirby:")
print(f"- {pink_kirby.be_round()}")
print(f"- {pink_kirby.be_cute()}")
print(f"- {pink_kirby.turn_into_pink_ball()}")

print("\nBlue Kirby:")
print(f"- {blue_kirby.be_round()}")
print(f"- {blue_kirby.be_cute()}")
print(f"- {blue_kirby.turn_into_blue_ball()}")
print("Each Kirby type only implements what it can do!")
