from abc import ABC, abstractmethod


class BadKirbyInterface(ABC):
    @abstractmethod
    def be_round(self):
        pass

    @abstractmethod
    def be_cute(self):
        pass

    @abstractmethod
    def turn_into_pink_ball(self):
        pass


class BadBlueKirby(BadKirbyInterface):
    def be_round(self):
        return "I am round"

    def be_cute(self):
        return "I am cute"

    def turn_into_pink_ball(self):
        return "I can't be pink though..."


print("BAD EXAMPLE - ISP Violation:")
blue_kirby = BadBlueKirby()
print(f"Blue Kirby: {blue_kirby.be_round()}")
print(f"Blue Kirby: {blue_kirby.be_cute()}")
print(f"Blue Kirby: {blue_kirby.turn_into_pink_ball()}")
print("Blue Kirby can't turn into a pink ball but has to implement it!")
