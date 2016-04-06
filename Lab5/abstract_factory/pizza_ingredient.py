#! python3
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class PizzaIngredientFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_dough(self):
        return NotImplemented

    @abstractmethod
    def create_sauce(self):
        return NotImplemented

    @abstractmethod
    def create_cheese(self):
        return NotImplemented

    @abstractmethod
    def create_veggie(self):
        return NotImplemented

    @abstractmethod
    def create_meat(self):
        return NotImplemented

    @abstractmethod
    def create_seafood(self):
        return NotImplemented