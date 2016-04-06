#! python3
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class Seafood(metaclass=ABCMeta):
    @abstractmethod
    def __str__(self):
        return NotImplemented


class FreshClams(Seafood):
    def __str__(self):
        return "Świerze małże z Long Island Sound"


class FrozenClams(Seafood):
    def __str__(self):
        return "Mrożone małże z zatoki Chesapeake"