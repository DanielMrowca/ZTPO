#! python3
# -*- coding: utf-8 -*-
from starbuzz_coffee import *

orders = []

orders.append(Espresso())

orders.append(DarkRoast())
orders[-1] = Mocha(orders[-1])
orders[-1] = Mocha(orders[-1])
orders[-1] = Whip(orders[-1])

orders.append(HouseBlend())
orders[-1] = Soy(orders[-1])
orders[-1] = Mocha(orders[-1])
orders[-1] = SteamedMilk(orders[-1])

orders.append(Decaf())
orders[-1] = SteamedMilk(orders[-1])

orders.append(BlackTea())
orders[-1] = Cinnamon(orders[-1])
orders[-1] = Sugar(orders[-1])

orders.append(GreenTea())
orders[-1] = Honey(orders[-1])
orders[-1] = Honey(orders[-1])
orders[-1] = Honey(orders[-1])
orders[-1] = Honey(orders[-1])
orders[-1] = Honey(orders[-1])

print("""
----------------
--- Rachunek ---
----------------
""")

sBillForm = """-> Zamówienie nr {0}:
{1} <- {2:4.2f} zł"""

for index, order in enumerate(orders):
    print(sBillForm.format(index, order.description, order.cost))