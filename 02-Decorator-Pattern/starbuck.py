from abc import ABC, abstractmethod


# Abstract Beverage Class: define a set of method that subclasses must implement
class Beverage(ABC):
    _description: str = "Unknown Beverage"

    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def cost(self) -> float:
        pass


# Main Decorator component containg pointer to the Beverage class and forward all
# component method to the Beverage pointer
class CondimentDecorator(Beverage):
    def __init__(self, beverage: Beverage) -> None:
        self._beverage = beverage

    def get_description(self) -> str:
        return self._description

    def cost(self) -> float:
        raise NotImplementedError


class Milk(CondimentDecorator):
    def get_description(self) -> str:
        return self._beverage.get_description() + ", milk"

    def cost(self):
        return self._beverage.cost() + 0.20


class Mocha(CondimentDecorator):
    def get_description(self):
        return self._beverage.get_description() + ", mocha"

    def cost(self):
        return self._beverage.cost() + 0.30


class Soy(CondimentDecorator):
    def get_description(self):
        return self._beverage.get_description() + ", soy"

    def cost(self):
        return self._beverage.cost() + 0.35


class HouseBlend(Beverage):
    _description = "House Blend"

    def get_description(self):
        return self._description

    def cost(self):
        return 10.03


if __name__ == "__main__":
    house_blend = Mocha(Soy(HouseBlend()))

    print(f"{house_blend.cost()} --- {house_blend.get_description()}")
