#! python3
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class Meat(metaclass=ABCMeta):
    @abstractmethod
    def __str__(self):
        return NotImplemented


class SlicdPepperoni(Meat):
    def __str__(self):
        return "Plasterki Pepperoni"