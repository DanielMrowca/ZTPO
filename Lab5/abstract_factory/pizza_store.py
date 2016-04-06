#! python3
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class PizzaStore(metaclass=ABCMeta):
    @abstractmethod
    def create_pizza(self, type):
        return NotImplemented

    def order_pizza(self, type):
        pizza = self.create_pizza(type)

        #try:
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        #except AttributeError:
        #    print("[PizzaStore]: Wystąpił błąd podczas realizacji zmówienia")

        return pizza