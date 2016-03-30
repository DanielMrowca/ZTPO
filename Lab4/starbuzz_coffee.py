#! python3
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from price_list_data import price_list


class Beverage(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        self._description = "Nieznany napój"
        self._cost = price_list[self.__class__.__name__]

    @property
    def description(self):
        return self._description

    @property
    def cost(self):
        return self._cost


class HouseBlend(Beverage):
    def __init__(self):
        super().__init__()
        self._description = "Mieszanka firmowa"


class DarkRoast(Beverage):
    def __init__(self):
        super().__init__()
        self._description = "Ciemno palona"


class Decaf(Beverage):
    def __init__(self):
        super().__init__()
        self._description = "Bezkofeinowa"


class Espresso(Beverage):
    def __init__(self):
        super().__init__()
        self._description = "Espresso"


class BlackTea(Beverage):
    def __init__(self):
        super().__init__()
        self._description = "Czarna herbata"


class GreenTea(Beverage):
    def __init__(self):
        super().__init__()
        self._description = "Zielona herbata"


class Condiment(Beverage):
    @abstractmethod
    def __init__(self, beverage: Beverage):
        super().__init__()
        self._beverage = beverage

    @property
    def description(self):
        return "{}, {}".format(self._beverage.description, self._description)

    @property
    def cost(self):
        return self._beverage.cost + self._cost


class SteamedMilk(Condiment):
    def __init__(self, beverage: Beverage):
        super().__init__(beverage)
        self._description = "spienione mleko"


class Mocha(Condiment):
    def __init__(self, beverage: Beverage):
        super().__init__(beverage)
        self._description = "czekolada"


class Soy(Condiment):
    def __init__(self, beverage: Beverage):
        super().__init__(beverage)
        self._description = "mleko sojowe"


class Whip(Condiment):
    def __init__(self, beverage: Beverage):
        super().__init__(beverage)
        self._description = "bita śmietana"


class Cinnamon(Condiment):
    def __init__(self, beverage: Beverage):
        super().__init__(beverage)
        self._description = "cynamon"


class Honey(Condiment):
    def __init__(self, beverage: Beverage):
        super().__init__(beverage)
        self._description = "miód"


class Sugar(Condiment):
    def __init__(self, beverage: Beverage):
        super().__init__(beverage)
        self._description = "cukier"