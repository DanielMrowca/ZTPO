#! python3
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class Sauce(metaclass=ABCMeta):
    @abstractmethod
    def __str__(self):
        return NotImplemented


class MarinaraSauce(Sauce):
    def __str__(self):
        return "Sos Marinara"


class PlumTomatoSauce(Sauce):
    def __str__(self):
        return "Sos z pomidorów śliwkowych"