#! python3
# -*- coding: utf-8 -*-

from enum import Enum, unique


@unique
class BeverageType(Enum):
    Coke = "Coca-Cola"
    Fanta = "Fanta"

    def __str__(self):
        return self.value