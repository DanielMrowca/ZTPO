#! python3
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

class Beverage(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        self._name = "Nieznany napój"
        self._glass = "Nieznana szklanka"

    @property
    def name(self):
        return self._name

    def prepare(self):
        print("|{0:<68}|".format("> Przygotowanie"))
        print("|{0:<68}|".format("-> Nalewanie do szklanki"))
        print("|{0:<68}|".format("--> {0}".format(self._glass)))

    def __str__(self):
        return self._name

class CokeBeverage(Beverage):
    def __init__(self):
        super().__init__()
        self._name = "Coca-Cola"
        self._glass = "Wysoka szklanka"

class FantaBeverage(Beverage):
    def __init__(self):
        super().__init__()
        self._name = "Fanta"
        self._glass = "Niska szklanka"