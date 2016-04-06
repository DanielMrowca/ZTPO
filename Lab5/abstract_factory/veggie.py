#! python3
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class Veggie(metaclass=ABCMeta):
    @abstractmethod
    def __str__(self):
        return NotImplemented


class BlackOlives(Veggie):
    def __str__(self):
        return "Czarne oliwki"


class Eggplant(Veggie):
    def __str__(self):
        return "Bakłażan"


class Garlic(Veggie):
    def __str__(self):
        return "Czosnek"


class Mushroom(Veggie):
    def __str__(self):
        return "Grzyby"


class Onion(Veggie):
    def __str__(self):
        return "Cebula"


class RedPepper(Veggie):
    def __str__(self):
        return "Czerwona papryka"


class Spinach(Veggie):
    def __str__(self):
        return "Szpinak"