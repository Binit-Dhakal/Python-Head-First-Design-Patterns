"""
This code represent Abstract Factory Pattern: Useful when we want 
to create a collection of related objects
"""

from abc import ABC, abstractmethod
from typing import Optional


# Main Ingridents Abstract Base class
class Sauce(ABC):
    ...


class Dough(ABC):
    ...


class Veggies(ABC):
    ...


class Pepperoni(ABC):
    ...


class Clams(ABC):
    ...


class Cheese(ABC):
    ...


# Concrete Products -> Implement the interface of the Ingridents ABC
ThinCrustDough = type(
    "ThinCrustDough", (Dough,), {"__str__": lambda self: "Thin Crust Dough used"}
)
MarinaraSauce = type(
    "MarinaraSauce", (Sauce,), {"__str__": lambda self: "Marinara Sauce used"}
)
ReggianoCheese = type(
    "ReggianoCheese", (Cheese,), {"__str__": lambda self: "Reggiano Cheese used"}
)
Onion = type("Onion", (Veggies,), {"__str__": lambda self: "Onion used"})
Mushroom = type("Mushroom", (Veggies,), {"__str__": lambda self: "Mushroom used"})
SlicedPepperoni = type(
    "SlicedPepperoni", (Pepperoni,), {"__str__": lambda self: "Sliced Pepperoni used"}
)
FreshClams = type("FreshClams", (Clams,), {"__str__": lambda self: "Fresh Clams used"})


class PizzaIngridentFactory(ABC):
    """
    Abstract class for Ingrident Factories
    """

    @abstractmethod
    def create_dough(self) -> Dough:
        ...

    @abstractmethod
    def create_sauce(self) -> Sauce:
        ...

    @abstractmethod
    def create_veggies(self) -> list[Veggies]:
        ...

    @abstractmethod
    def create_pepperoni(self) -> Pepperoni:
        ...

    @abstractmethod
    def create_clam(self) -> Clams:
        ...

    @abstractmethod
    def create_cheese(self) -> Cheese:
        ...


class NYPizzaIngridentFactory(PizzaIngridentFactory):
    def create_dough(self) -> Dough:
        return ThinCrustDough()

    def create_sauce(self) -> Sauce:
        return MarinaraSauce()

    def create_cheese(self) -> Cheese:
        return ReggianoCheese()

    def create_veggies(self) -> list[Veggies]:
        return [Onion(), Mushroom()]

    def create_pepperoni(self) -> Pepperoni:
        return SlicedPepperoni()

    def create_clam(self) -> Clams:
        return FreshClams()


class Pizza(ABC):
    """Abstract Base Class for Pizza"""

    def __init__(self, ingrident_factory: PizzaIngridentFactory):
        self.ingrident_factory = ingrident_factory
        self._name: str = ""
        self.dough: Optional[Dough] = None
        self.sauce: Optional[Sauce] = None
        self.veggies: list[Veggies] = []
        self.cheese: Optional[Cheese] = None
        self.pepperoni: Optional[Pepperoni] = None
        self.clam: Optional[Clams] = None

    @abstractmethod
    def prepare(self):
        """Prepare Pizza"""

    def bake(self):
        """Bake in oven"""
        print("Bake for 25 minutes at 350")

    def cut(self):
        """Cut the pizza in slices"""
        print("Cutting pizza into diagonal slices")

    def box(self):
        """Box the pizza in nice Objectville packaging"""
        print("Place pizza in official Pizza Store")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @name.getter
    def name(self):
        return self._name

    def __str__(self):
        result = []
        result.append("---- " + self.name + " -----")
        if self.dough:
            result.append(self.dough)

        if self.sauce:
            result.append(self.sauce)

        if self.cheese:
            result.append(self.cheese)

        if self.veggies:
            result.append(" ".join(map(str, self.veggies)))

        if self.clam:
            result.append(self.clam)

        if self.pepperoni:
            result.append(self.pepperoni)

        return "\n".join(map(str, result)) + "\n"


class CheesePizza(Pizza):
    def prepare(self):
        self.dough = self.ingrident_factory.create_dough()
        self.sauce = self.ingrident_factory.create_sauce()
        self.cheese = self.ingrident_factory.create_cheese()


class ClamPizza(Pizza):
    def prepare(self):
        self.dough = self.ingrident_factory.create_dough()
        self.sauce = self.ingrident_factory.create_sauce()
        self.cheese = self.ingrident_factory.create_cheese()
        self.clam = self.ingrident_factory.create_clam()


class VeggiePizza(Pizza):
    def prepare(self):
        self.dough = self.ingrident_factory.create_dough()
        self.sauce = self.ingrident_factory.create_sauce()
        self.cheese = self.ingrident_factory.create_cheese()
        self.veggies = self.ingrident_factory.create_veggies()


class PizzaStore(ABC):
    @abstractmethod
    def create_pizza(self, item: str) -> Optional[Pizza]:
        ...

    def order_pizza(self, type_: str):
        pizza = self.create_pizza(type_)
        if pizza is None:
            return "please provide correct type of pizza you want"
        print(f"--- Making a {pizza.name} ---")
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza


class NYPizzaStore(PizzaStore):
    def create_pizza(self, item: str) -> Optional[Pizza]:
        pizza: Optional[Pizza] = None
        ingrident_factory = NYPizzaIngridentFactory()
        if item == "cheese":
            pizza = CheesePizza(ingrident_factory)
            pizza.name = "New York Style Cheese Pizza"
        elif item == "veggie":
            pizza = VeggiePizza(ingrident_factory)
            pizza.name = "New York Style Veggie Pizza"
        elif item == "clam":
            pizza = ClamPizza(ingrident_factory)
            pizza.name = "New York Style Clam Pizza"

        return pizza


def main():
    ny_store = NYPizzaStore()
    pizza = ny_store.order_pizza("cheese")
    print(f"Ordered {pizza}")

    pizza2 = ny_store.order_pizza("clam")
    print(f"Ordered {pizza2}")


if __name__ == "__main__":
    main()
