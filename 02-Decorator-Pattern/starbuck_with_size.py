from typing import Protocol
from enum import Enum


class Size(Enum):
    TALL = "TALL"
    GRANDE = "GRANDE"
    VENTI = "VENTI"


# Beverage protocol used as Abstract Base Class
class Beverage(Protocol):
    description: str = ""
    costs_per_size: dict

    def get_description(self) -> str:
        ...

    def cost(self) -> float:
        ...

    @property
    def beverage_size(self) -> Size:
        ...


# used to bridge gap between CondimentItems(Milk, Soy, etc) with Beverage Class
class CondimentDecorator:
    description: str
    costs_per_size: dict

    def __init__(self, beverage: Beverage) -> None:
        self._beverage = beverage

    def get_description(self) -> str:
        raise NotImplementedError

    def cost(self) -> float:
        raise NotImplementedError

    @property
    def beverage_size(self):
        return self._beverage.beverage_size


class Milk(CondimentDecorator):
    costs_per_size = {"TALL": 0.10, "GRANDE": 0.18, "VENTI": 0.25}

    def get_description(self) -> str:
        return self._beverage.get_description() + ", milk"

    def cost(self):
        return self._beverage.cost() + self.costs_per_size[self.beverage_size.name]


class Mocha(CondimentDecorator):
    costs_per_size = {"TALL": 0.20, "GRANDE": 0.40, "VENTI": 0.57}

    def get_description(self) -> str:
        return self._beverage.get_description() + ", mocha"

    def cost(self):
        return self._beverage.cost() + self.costs_per_size[self.beverage_size.name]


class Espresso:
    description = "Espresso"
    costs_per_size = {"TALL": 1.10, "GRANDE": 1.50, "VENTI": 2.10}

    def __init__(self, size: Size):
        self._beverage_size: Size = size

    def get_description(self) -> str:
        return f"{self.description}({self._beverage_size.name})"

    def cost(self):
        return self.costs_per_size[self._beverage_size.name]

    @property
    def beverage_size(self) -> Size:
        return self._beverage_size


if __name__ == "__main__":
    espresso = Mocha(Milk(Espresso(Size.VENTI)))
    print(f"{espresso.cost()} ----- {espresso.get_description()}")
