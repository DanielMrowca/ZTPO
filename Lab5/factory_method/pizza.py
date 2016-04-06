#! python3
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

class Pizza(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        self._name = "Nieznana pizza"
        self._dough = "Nieznane ciasto"
        self._sauce = "Nieznany sos"
        self._toppings = []

    @property
    def name(self):
        return self._name

    def prepare(self):
        print("|{0:<68}|".format("> Przygotowanie"))
        print("|{0:<68}|".format("-> Wyrabianie ciasta"))
        print("|{0:<68}|".format("--> {0}".format(self._dough)))
        print("|{0:<68}|".format("-> Dodawanie sosu"))
        print("|{0:<68}|".format("--> {0}".format(self._sauce)))
        print("|{0:<68}|".format("-> Dodawanie dodatków:"))

        for i in self._toppings:
            print("|{0:<68}|".format("--> {0}".format(i)))

    def bake(self):
        print("|{0:<68}|".format("> Pieczenie przez 25 minut w 180 C"))

    def cut(self):
        print("|{0:<68}|".format("> Krojenie pizzy w diagonalne kawałk"))

    def box(self):
        print("|{0:<68}|".format("> Pakowanie pizzy do firmowego opakowania PizzaStore"))

    def __str__(self):
        return self._name