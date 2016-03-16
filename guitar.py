from enum import Enum, unique

@unique
class Type(Enum):
    ACOUSTIC = 0
    ELECTRIC = 1

    def __str__(self):
        names = ['akustyczna', 'elektryczna']
        return names[self.value]

@unique
class Builder(Enum):
    FENDER = 0
    MARTIN = 1
    GIBSON = 2
    COLLINGS = 3
    OLSON = 4
    RAYAN = 5
    PRS = 6
    ANY = 7

    def __str__(self):
        names = ['Fender', 'Martin', 'Gibson', 'Collings', 'Olson', 'Rayan', 'PRS', 'nieokreślony']
        return names[self.value]

@unique
class Wood(Enum):
    INDIAN_ROSEWOOD = 0
    BRASILIAN_ROSEWOOD = 1
    MAHOGANY = 2
    MAPLE = 3
    EBONY = 4
    CEDAR = 5
    OAK = 6
    ALDER = 7
    SITKA = 8

    def __str__(self):
        names = ['palisander indyjski', 'palisander brazylijski', 'mahoń', 'klon', 'heban', 'cedr', 'dąb', 'olcha',
                 'sitka']
        return names[self.value]


class GuitarSpec:
    def __init__(self, builder: Builder, model, type: Type, backWood: Wood, topWood: Wood, strings: int):
        if isinstance(type, Type):
            self._type = type
        else:
            print("bledny typ")
        self._model = model
        self._builder = builder
        self._topWood = topWood
        self._backWood = backWood
        self._strings = strings

    def getBuilder(self) -> Builder:
        return self._builder

    def getModel(self):
        return self._model

    def getType(self) -> Type:
        return self._type

    def getBackWood(self) -> Wood:
        return self._backWood

    def getTopWood(self) -> Wood:
        return self._topWood

    def getStrings(self):
        return self._strings

    def matches(self, other) -> bool:
        if other.getBuilder() != self.getBuilder():
            return False
        model = other.getModel()
        if not (model is None) and (model != "") and (model.lower() != self.getModel().lower()):
            return False
        if other.getType() != self.getType():
            return False
        if other.getBackWood() != self.getBackWood():
            return False
        if other.getTopWood() != self.getTopWood():
            return False
        if other.getStrings() != self.getStrings():
            return False
        return True


class Guitar:
    def __init__(self, serialNumber, price, spec: GuitarSpec):
        self._serialNumber = serialNumber
        self._price = price
        self._spec = spec

    def getSerialNumber(self) -> str:
        return self._serialNumber

    def getPrice(self):
        return self._price

    def setPrice(self, value):
        self._price = value

    def getSpec(self) -> GuitarSpec:
        return self._spec