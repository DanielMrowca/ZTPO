#! python3
# -*- coding: utf-8 -*-

from abstract_factory.pizza_ingredient import PizzaIngredientFactory
from abstract_factory.dough import ThickCrustDough
from abstract_factory.sauce import PlumTomatoSauce
from abstract_factory.cheese import MozzarellaCheese
from abstract_factory.veggie import BlackOlives, Spinach, Eggplant
from abstract_factory.meat import SlicdPepperoni
from abstract_factory.seafood import FrozenClams


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        return ThickCrustDough()

    def create_sauce(self):
        return PlumTomatoSauce()

    def create_cheese(self):
        return MozzarellaCheese()

    def create_veggie(self):
        return [BlackOlives(), Spinach(), Eggplant()]

    def create_meat(self):
        return SlicdPepperoni()

    def create_seafood(self):
        return FrozenClams()