#! python3
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

class Pizza(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        self._name = "Nieznana pizza"
        self._dough = None
        self._sauce = None
        self._cheese = None
        self._veggie = None
        self._meat = None
        self._seafood = None

    @property
    def name(self):
        return self._name

    def prepare(self):
        print("|{0:<68}|".format("> Przygotowanie -- AF"))

        if self._dough is not None:
            print("|{0:<68}|".format("-> Wyrabianie ciasta"))
            print("|{0:<68}|".format("--> {0}".format(self._dough)))

        if self._sauce is not None:
            print("|{0:<68}|".format("-> Dodawanie sosu"))
            print("|{0:<68}|".format("--> {0}".format(self._sauce)))

        if self._cheese is not None:
            print("|{0:<68}|".format("-> Dodawanie sera"))
            print("|{0:<68}|".format("--> {0}".format(self._cheese)))

        if self._veggie is not None:
            print("|{0:<68}|".format("-> Dodawanie warzyw"))
            for i in self._veggie:
                print("|{0:<68}|".format("--> {0}".format(i)))

        if self._meat is not None:
            print("|{0:<68}|".format("-> Dodawanie mięsa"))
            print("|{0:<68}|".format("--> {0}".format(self._meat)))

        if self._seafood is not None:
            print("|{0:<68}|".format("-> Dodawanie owoców morza"))
            print("|{0:<68}|".format("--> {0}".format(self._seafood)))

    def bake(self):
        print("|{0:<68}|".format("> Pieczenie przez 25 minut w 180 C"))

    def cut(self):
        print("|{0:<68}|".format("> Krojenie pizzy w diagonalne kawałk"))

    def box(self):
        print("|{0:<68}|".format("> Pakowanie pizzy do firmowego opakowania PizzaStore"))

    def __str__(self):
        return self._name


class CheesePizza(Pizza):
    def __init__(self, ingredient):
        super().__init__()
        self._ingredient = ingredient

    def prepare(self):
        self._dough = self._ingredient.create_dough()
        self._cheese = self._ingredient.create_cheese()
        self._sauce = self._ingredient.create_sauce()
        super().prepare()


class ClamPizza(Pizza):
    def __init__(self, ingredient):
        super().__init__()
        self._ingredient = ingredient

    def prepare(self):
        self._dough = self._ingredient.create_dough()
        self._cheese = self._ingredient.create_cheese()
        self._sauce = self._ingredient.create_sauce()
        self._seafood = self._ingredient.create_seafood()
        super().prepare()


class PepperoniPizza(Pizza):
    def __init__(self, ingredient):
        super().__init__()
        self._ingredient = ingredient

    def prepare(self):
        self._dough = self._ingredient.create_dough()
        self._cheese = self._ingredient.create_cheese()
        self._sauce = self._ingredient.create_sauce()
        self._veggie = self._ingredient.create_veggie()
        self._meat = self._ingredient.create_meat()
        super().prepare()


class VeggiePizza(Pizza):
    def __init__(self, ingredient):
        super().__init__()
        self._ingredient = ingredient

    def prepare(self):
        self._dough = self._ingredient.create_dough()
        self._cheese = self._ingredient.create_cheese()
        self._sauce = self._ingredient.create_sauce()
        self._veggie = self._ingredient.create_veggie()
        super().prepare()