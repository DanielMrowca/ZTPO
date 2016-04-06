#! python3
# -*- coding: utf-8 -*-

from factory_method.pizza import Pizza


class CheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self._name = "Deep dish pizza w stylu chicagowskim"
        self._dough = "Ekstra grube ciasto"
        self._sauce = "Sos z pomidorów śliwkowych"

        self._toppings.append("Tarty ser Mozzarella")

    def cut(self):
        print("|{0:<68}|".format("> Krojenie pizzy w prostkątne kawałk"))


class ClamPizza(Pizza):
    def __init__(self):
        super().__init__()
        self._name = "Pizza z małżami w stylu chicagowskim"
        self._dough = "Ekstra grube ciasto"
        self._sauce = "Sos z pomidorów śliwkowych"

        self._toppings.append("Tarty ser Mozzarella")
        self._toppings.append("Mrożone małże z zatoki Chesapeake")

    def cut(self):
        print("|{0:<68}|".format("> Krojenie pizzy w prostkątne kawałk"))


class PepperoniPizza(Pizza):
    def __init__(self):
        super().__init__()
        self._name = "Pizza pepperoni w stylu chicagowskim"
        self._dough = "Ekstra grube ciasto"
        self._sauce = "Sos z pomidorów śliwkowych"

        self._toppings.append("Tarty ser Mozzarella")
        self._toppings.append("Czarne oliwki")
        self._toppings.append("Szpinak")
        self._toppings.append("Bakłażan")
        self._toppings.append("Plasterki pepperoni")

    def cut(self):
        print("|{0:<68}|".format("> Krojenie pizzy w prostkątne kawałk"))


class VeggiePizza(Pizza):
    def __init__(self):
        super().__init__()
        self._name = "Pizza wegetariańska w stylu chicagowskim"
        self._dough = "Ekstra grube ciasto"
        self._sauce = "Sos z pomidorów śliwkowych"

        self._toppings.append("Tarty ser Mozzarella")
        self._toppings.append("Czarne oliwki")
        self._toppings.append("Szpinak")
        self._toppings.append("Bakłażan")

    def cut(self):
        print("|{0:<68}|".format("> Krojenie pizzy w prostkątne kawałk"))