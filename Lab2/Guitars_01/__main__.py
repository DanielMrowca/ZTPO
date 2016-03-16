#!python3
# -*- coding: utf-8 -*-
__author__ = 'Daniel'

from guitar import InstrumentSpec, InstrumentType, Builder, Type, Wood
from inventory import Inventory
from copy import deepcopy

def initialize_inventory(invent):
    prop = dict()
    prop["instrumentType"] = InstrumentType.GUITAR
    prop["builder"] = Builder.COLLINGS
    prop["model"] = "CJ"
    prop["type"] = Type.ACOUSTIC
    prop["numStrings"] = 6
    prop["topWood"] = Wood.INDIAN_ROSEWOOD
    prop["backWood"] = Wood.SITKA
    invent.add_instrument("11277", 3999.95, InstrumentSpec(deepcopy(prop)))

    prop["builder"] = Builder.MARTIN
    prop["model"] = "D-18"
    prop["topWood"] = Wood.MAHOGANY
    prop["backWood"] = Wood.OAK
    invent.add_instrument("122784", 5495.95, InstrumentSpec(deepcopy(prop)))

    prop["builder"] = Builder.FENDER
    prop["model"] = "Stratocastor"
    prop["type"] = Type.ELECTRIC
    prop["topWood"] = Wood.ALDER
    prop["backWood"] = Wood.ALDER
    invent.add_instrument("V95693", 1499.95, InstrumentSpec(deepcopy(prop)))
    invent.add_instrument("V9512", 1549.95, InstrumentSpec(deepcopy(prop)))

    prop["builder"] = Builder.GIBSON
    prop["model"] = "Les Paul"
    prop["topWood"] = Wood.MAPLE
    prop["backWood"] = Wood.MAPLE
    invent.add_instrument("70108276", 2295.95, InstrumentSpec(deepcopy(prop)))

    prop["model"] = "SG '61 Reissue"
    prop["topWood"] = Wood.MAHOGANY
    prop["backWood"] = Wood.MAHOGANY
    invent.add_instrument("82765501", 1890.95, InstrumentSpec(deepcopy(prop)))

    prop["instrumentType"] = InstrumentType.MANDOLIN
    prop["type"] = Type.ACOUSTIC
    prop["model"] = "F-5G"
    prop["backWood"] = Wood.MAPLE
    prop["topWood"] = Wood.MAPLE
    prop["numStrings"]  # usunigcie zbgdnego pola
    invent.add_instrument("9019920", 5495.99, InstrumentSpec(deepcopy(prop)))

    prop["instrumentType"] = InstrumentType.BANJO
    prop["model"] = "RB-) Wreath"
    del prop["topWood"]  # usunigcie zbgdnego pola
    prop["numStrings"] = 5
    invent.add_instrument("8900231", 2945.95, InstrumentSpec(deepcopy(prop)))


if __name__ == "__main__":
    print("Inicjalizacja magazynu")
    inventory = Inventory()
    initialize_inventory(inventory)
    print("OK")
    print("Zapytanie\n")
    bronek_props = {'builder': Builder.GIBSON, 'backWood': Wood.MAPLE}
    what_bronek_likes_spec = InstrumentSpec(bronek_props)
    matching_instruments = inventory.search(what_bronek_likes_spec)
    if len(matching_instruments) > 0:
        print("Bronku, moze zainteresują Cię następujące instrumenty:")
        for inst in matching_instruments:
            mySpec = inst.get_spec()
            print('Na przykład ' + str(mySpec.get_prop('instrumentType')) +
                ' o następujących właściwościach: ')
            for p in mySpec.get_props().keys():
                if p == "instrumentType":
                    continue
                print("	{}: {}".format(p, mySpec.get_prop(p)))
            print("	Ten instrument - " + str(mySpec.get_prop('instrumentType')) +
                " - jest w naszym sklepie dostępny za " + str(inst.price) +
                " PLN\n---")
    else:
        print("Przykro mi, Bronku, nie znalazłem nic dla Ciebie.")
