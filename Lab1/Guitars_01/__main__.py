#!python3
# -*- coding: utf-8 -*-
__author__ = 'Wojtek'

from guitar import Guitar, GuitarSpec, Type, Builder, Wood
from inventory import Inventory


def initializeInventory(inventory):
    '''
    Załadowanie gitar do magazynu
    '''
    inventory.addGuitar("11277", 3999.95, GuitarSpec(Builder.COLLINGS, "CJ", Type.ACOUSTIC,
                        Wood.INDIAN_ROSEWOOD, Wood.SITKA, 8))
    inventory.addGuitar("V95693", 1499.95, GuitarSpec(Builder.FENDER, "Stratocastor", Type.ELECTRIC,
                        Wood.ALDER, Wood.ALDER, 12))
    inventory.addGuitar("V9512", 1549.95, GuitarSpec(Builder.FENDER, "Stratocastor", Type.ELECTRIC,
                        Wood.ALDER, Wood.ALDER, 12))
    inventory.addGuitar("122784", 5495.95, GuitarSpec(Builder.MARTIN, "D-18", Type.ACOUSTIC,
                        Wood.MAHOGANY, Wood.OAK, 8))
    inventory.addGuitar("76531", 6295.95, GuitarSpec(Builder.MARTIN, "OM-28", Type.ACOUSTIC,
                        Wood.BRASILIAN_ROSEWOOD, Wood.OAK, 8))
    inventory.addGuitar("70108276", 2295.95, GuitarSpec(Builder.GIBSON, "Les Paul", Type.ELECTRIC,
                        Wood.MAHOGANY, Wood.MAPLE, 12))
    inventory.addGuitar("82765501", 1890.95, GuitarSpec(Builder.GIBSON, "SG '61 Reissue", Type.ELECTRIC,
                        Wood.MAHOGANY, Wood.MAHOGANY, 8))
    inventory.addGuitar("77023", 6275.95, GuitarSpec(Builder.MARTIN, "D-28", Type.ACOUSTIC,
                        Wood.INDIAN_ROSEWOOD, Wood.OAK, 8))
    inventory.addGuitar("1092", 12995.95, GuitarSpec(Builder.OLSON, "SJ", Type.ACOUSTIC,
                        Wood.INDIAN_ROSEWOOD, Wood.CEDAR, 12))
    inventory.addGuitar("566-62", 8999.95, GuitarSpec(Builder.RAYAN, "Cathedral", Type.ACOUSTIC,
                        Wood.EBONY, Wood.CEDAR, 8))
    inventory.addGuitar("6 29584", 2100.95, GuitarSpec(Builder.PRS, "Dave Navarro Signature", Type.ELECTRIC,
                        Wood.MAHOGANY, Wood.MAPLE, 8))


if __name__ == "__main__":
    print("Inicjalizacja magazynu")
    inventory = Inventory()
    initializeInventory(inventory)
    print("OK")
    print("Zapytanie\n")
    whatEveLikes = GuitarSpec(Builder.FENDER, "stratocastor", Type.ELECTRIC, Wood.ALDER, Wood.ALDER, 12)

    matchingGuitars = inventory.search(whatEveLikes)
    if len(matchingGuitars) > 0:
        print("Ewo, może spodobają Ci się gitary:")
        for guitar in matchingGuitars:
            print("""{} model {}:
                {}
                {} - tył i boki
                {} - góra
                Możesz już mieć za: {}""".format(guitar.getSpec().getBuilder(),
                                                 guitar.getSpec().getModel(),
                                                 guitar.getSpec().getType(),
                                                 guitar.getSpec().getBackWood(),
                                                 guitar.getSpec().getTopWood(),
                                                 guitar.getPrice()))
    else:
        print("Przykro mi, Ewo, nie znalazłem nic dla Ciebie.")
