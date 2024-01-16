from abc import ABC, abstractmethod


class Pizza(ABC):
    """Abstract base class for Pizza"""

    @abstractmethod
    def prepare(self):
        """Prepare pizza"""

    @abstractmethod
    def bake(self):
        """Bake pizza in oven"""

    @abstractmethod
    def cut(self):
        """Cut pizza in slices"""

    @abstractmethod
    def box(self):
        """Box the pizza in nice Objectvilles packaging"""


## We will create 4 concrete Pizza class
class NYStyleCheesePizza(Pizza):
    """Concrete class for New York Style Cheese Pizza"""

    def prepare(self):
        print("Preparing NYStyleCheesePizza")

    def bake(self):
        print("Baking NYStyleCheesePizza")

    def cut(self):
        print("Cut NYStyleCheesePizza")

    def box(self):
        print("Box NYStyleCheesePizza")


class NYStylePepperoniPizza(Pizza):
    """Concrete class of New York Style Pepperoni Pizza"""

    def prepare(self):
        print("Preparing NYStylePepperoniPizza")

    def bake(self):
        print("Baking NYStylePepperoniPizza")

    def cut(self):
        print("Prepare slices of NYStylePepperoniPizza")

    def box(self):
        print("Package NYStylePepperoniPizza in nice box")


class ChicagoStyleCheesePizza(Pizza):
    """Concrete class of Chicago Style Cheese Pizza"""

    def prepare(self):
        print("Preparing ChicagoStyleCheesePizza")

    def bake(self):
        print("Baking ChicagoStyleCheesePizza")

    def cut(self):
        print("Prepare slices of ChicagoStyleCheesePizza")

    def box(self):
        print("Package ChicagoStyleCheesePizza in nice box")


class ChicagoStylePepperoniPizza(Pizza):
    """Concrete class of Chicago Style Pepperoni Pizza"""

    def prepare(self):
        print("Preparing ChicagoStylePepperoniPizza")

    def bake(self):
        print("Baking ChicagoStylePepperoniPizza")

    def cut(self):
        print("Prepare slices of ChicagoStylePepperoniPizza")

    def box(self):
        print("Package ChicagoStylePepperoniPizza in nice box")


class PizzaStore(ABC):
    """
    Abstract class for pizza store.
    All our regional store is going to inherit this
    """

    @abstractmethod
    def create_pizza(self, type: str) -> Pizza:
        """Create Pizza is in this method"""

    def order_pizza(self, type: str) -> Pizza:
        """Ordering Pizza is handled by this method"""
        pizza = self.create_pizza(type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza


class PizzaTypeNotAvailable(Exception):
    pass


class NYPizzaStore(PizzaStore):
    def create_pizza(self, type: str) -> Pizza:
        if type == "cheese":
            return NYStyleCheesePizza()
        elif type == "pepperoni":
            return NYStylePepperoniPizza()
        else:
            raise PizzaTypeNotAvailable


class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, type: str) -> Pizza:
        if type == "cheese":
            return ChicagoStyleCheesePizza()
        elif type == "pepperoni":
            return ChicagoStylePepperoniPizza()
        else:
            raise PizzaTypeNotAvailable


def main():
    pizza_store = NYPizzaStore()
    pizza_store.order_pizza("pepperoni")


if __name__ == "__main__":
    main()
