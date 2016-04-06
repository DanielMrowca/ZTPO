#! python3
# -*- coding: utf-8 -*-

from factory_method.pizza import Pizza


class CheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self._name = "Pizza serowa z sosem nowojorskim"
        self._dough = "Cienkie ciasto ciasto"
        self._sauce = "Sos Marinara"

        self._toppings.append("Tarty ser Reggiano")


class ClamPizza(Pizza):
    def __init__(self):
        super().__init__()
        self._name = "Pizza z małżmi w stylu nowojorskim"
        self._dough = "Cienkie ciasto ciasto"
        self._sauce = "Sos Marinara"

        self._toppings.append("Tarty ser Reggiano")
        self._toppings.append("Świeże małże z Long Island Sound")


class PepperoniPizza(Pizza):
    def __init__(self):
        super().__init__()
        self._name = "Pizza pepperoni w stylu nowojorskim"
        self._dough = "Cienkie ciasto ciasto"
        self._sauce = "Sos Marinara"

        self._toppings.append("Tarty ser Reggiano")
        self._toppings.append("Plasterki pepperoni")
        self._toppings.append("Czosnek")
        self._toppings.append("Cebula")
        self._toppings.append("Grzyby")
        self._toppings.append("Czerwona papryka")


class VeggiePizza(Pizza):
    def __init__(self):
        super().__init__()
        self._name = "Pizza wegetariańska w stylu nowojorskim"
        self._dough = "Cienkie ciasto ciasto"
        self._sauce = "Sos Marinara"

        self._toppings.append("Tarty ser Reggiano")
        self._toppings.append("Czosnek")
        self._toppings.append("Cebula")
        self._toppings.append("Grzyby")
        self._toppings.append("Czerwona papryka")