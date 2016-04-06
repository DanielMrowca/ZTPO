#! python3
# -*- coding: utf-8 -*-

from abstract_factory.pizza_ingredient import PizzaIngredientFactory
from abstract_factory.dough import ThinCrustDough
from abstract_factory.sauce import MarinaraSauce
from abstract_factory.cheese import ReggianoCheese
from abstract_factory.veggie import Garlic, Mushroom, Onion, RedPepper
from abstract_factory.meat import SlicdPepperoni
from abstract_factory.seafood import FreshClams


class NewYorkPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        return ThinCrustDough()

    def create_sauce(self):
        return MarinaraSauce()

    def create_cheese(self):
        return ReggianoCheese()

    def create_veggie(self):
        return [Garlic(), Mushroom(), Onion(), RedPepper()]

    def create_meat(self):
        return SlicdPepperoni()

    def create_seafood(self):
        return FreshClams()