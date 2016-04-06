#! python3
# -*- coding: utf-8 -*-

from factory_method.pizza_type import PizzaType
from factory_method.beverage_type import BeverageType
from factory_method.beverage import CokeBeverage, FantaBeverage
from factory_method.pizza_store import PizzaStore
from factory_method.pizza_chicago import (CheesePizza, ClamPizza, PepperoniPizza, VeggiePizza)


class ChicagoPizzaStore(PizzaStore):
    def __init__(self):
        self._pizza_list = {PizzaType.Cheese: CheesePizza,
                            PizzaType.Clam: ClamPizza,
                            PizzaType.Pepperoni: PepperoniPizza,
                            PizzaType.Veggie: VeggiePizza}
        self._beverage_list = {BeverageType.Coke: CokeBeverage,
                               BeverageType.Fanta: FantaBeverage}

    def create_pizza(self, type):
        try:
            return self._pizza_list[type]()
        except KeyError:
            print("[ChicagoPizzaStore]: Wybrany rodzaj pizzy \"{0}\" jest niedostępny".format(type))

    def create_beverage(self, type):
        try:
            return self._beverage_list[type]()
        except KeyError:
            print("[ChicagoPizzaStore]: Wybrany rodzaj napoju \"{0}\" jest niedostępny".format(type))