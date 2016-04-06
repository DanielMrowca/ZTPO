#! python3
# -*- coding: utf-8 -*-

from enum import Enum, unique


@unique
class PizzaType(Enum):
    Cheese = "Pizza serowa"
    Clam = "Pizza z małżami"
    Pepperoni = "Pizza pepperoni"
    Veggie = "Pizza wegetariańska"

    def __str__(self):
        return self.value