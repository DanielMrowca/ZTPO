#! python3
# -*- coding: utf-8 -*-

from abstract_factory.pizza_type import PizzaType
from abstract_factory.pizza_ingredient_newyork import NewYorkPizzaIngredientFactory
from abstract_factory.pizza_store import PizzaStore
from abstract_factory.pizza import CheesePizza, ClamPizza, PepperoniPizza, VeggiePizza


class NewYorkPizzaStore(PizzaStore):
    def __init__(self):
        self._pizza_list = {PizzaType.Cheese: (CheesePizza, "Pizza serowa z sosem nowojorskim"),
                            PizzaType.Clam: (ClamPizza, "Pizza z małżami w stylu nowojorskim"),
                            PizzaType.Pepperoni: (PepperoniPizza ,"Pizza pepperoni w stylu nowojorskim"),
                            PizzaType.Veggie: (VeggiePizza, "Pizza wegetariańska w stylu nowojorskim")}

    def create_pizza(self, type):
        inredient = NewYorkPizzaIngredientFactory()
        try:
            pizza = self._pizza_list[type][0](inredient)
            pizza._name = self._pizza_list[type][1]
            return pizza
        except KeyError:
            print("[NewYorkPizzaStore]: Wybrany rodzaj pizzy \"{0}\" jest niedostępny".format(type))