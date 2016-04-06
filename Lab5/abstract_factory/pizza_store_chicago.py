#! python3
# -*- coding: utf-8 -*-

from abstract_factory.pizza_type import PizzaType
from abstract_factory.pizza_ingredient_chicago import ChicagoPizzaIngredientFactory
from abstract_factory.pizza_store import PizzaStore
from abstract_factory.pizza import CheesePizza, ClamPizza, PepperoniPizza, VeggiePizza


class ChicagoPizzaStore(PizzaStore):
    def __init__(self):
        self._pizza_list = {PizzaType.Cheese: (CheesePizza, "Deep dish pizza w stylu chicagowskim"),
                            PizzaType.Clam: (ClamPizza, "Pizza z małżami w stylu chicagowskim"),
                            PizzaType.Pepperoni: (PepperoniPizza ,"Pizza pepperoni w stylu chicagowskim"),
                            PizzaType.Veggie: (VeggiePizza, "Pizza wegetariańska w stylu chicagowskim")}

    def create_pizza(self, type):
        inredient = ChicagoPizzaIngredientFactory()
        try:
            pizza = self._pizza_list[type][0](inredient)
            pizza._name = self._pizza_list[type][1]
            return pizza
        except KeyError:
            print("[ChicagoPizzaStore]: Wybrany rodzaj pizzy \"{0}\" jest niedostępny".format(type))