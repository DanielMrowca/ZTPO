#! python3
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class Cheese(metaclass=ABCMeta):
    @abstractmethod
    def __str__(self):
        return NotImplemented


class MozzarellaCheese(Cheese):
    def __str__(self):
        return "Tarty ser Mozzarella"


class ParmesanCheese(Cheese):
    def __str__(self):
        return "Tarty ser Parmezan"


class ReggianoCheese(Cheese):
    def __str__(self):
        return "Tarty ser Reggiano"