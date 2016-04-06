#! python3
# -*- coding: utf-8 -*-

import sys

if len(sys.argv) == 2:
    if sys.argv[1] == "factory_method":
        from factory_method.pizza_type import PizzaType
        from factory_method.pizza_store_chicago import ChicagoPizzaStore
        from factory_method.pizza_store_newyork import NewYorkPizzaStore
    elif sys.argv[1] == "abstract_factory":
        from abstract_factory.pizza_type import PizzaType
        from abstract_factory.pizza_store_chicago import ChicagoPizzaStore
        from abstract_factory.pizza_store_newyork import NewYorkPizzaStore
    else:
        sys.exit()
else:
    sys.exit()


chicago_store = ChicagoPizzaStore()
newyork_store = NewYorkPizzaStore()

def make_order(order_number, store, pizza_type):
    print("{0}".format("-" * 70))
    print("|{0:^68}|".format("Zamówienie nr {0:2d}".format(order_number)))
    print("{0}".format("-" * 70))
    pizza = store.order_pizza(pizza_type)
    print("{0}".format("-" * 70))
    print("|{0:^68}|".format("{0} <--> do odbioru".format(pizza)))
    print("{0}".format("-" * 70))
    print("")

make_order(1, newyork_store, PizzaType.Cheese)
make_order(2, chicago_store, PizzaType.Cheese)
make_order(3, newyork_store, PizzaType.Clam)
make_order(4, chicago_store, PizzaType.Clam)
make_order(5, newyork_store, PizzaType.Pepperoni)
make_order(6, chicago_store, PizzaType.Pepperoni)
make_order(7, newyork_store, PizzaType.Veggie)
make_order(8, chicago_store, PizzaType.Veggie)