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



@unique
class Style(Enum):
    A = 0
    B = 1
    ANY = 2

    def __str__(self):
        names = ('Style A', 'Style B', 'Niekoreslony')
        return names[self.value]


@unique
class InstrumentType(Enum):
    GUITAR = 0
    BANJO = 1
    DOBRO = 2
    FIDDLE = 3
    BASS = 4
    MANDOLIN = 5
    ANY = 6

    def __str__(self):
        names = ('Gitara', 'Banjo', 'Dobro', 'Skrzypce', 'Gitara basowa',
            'Mandolina', 'Niekoreslony')
        return names[self.value]


class InstrumentSpec:
    def __init__(self, prop: dict):
        if prop is None:
            self._prop = dict()
        else:
            self._prop = prop

    def get_prop(self, name):
        if name in self._prop.keys():
            return self._prop[name]
        else:
            return None

    def get_props(self):
        return self._prop

    def matches(self, other_spec) -> bool:
        for k in other_spec.get_props().keys():
            if self._prop[k] != other_spec.get_prop(k):
                return False
        return True


class Instrument:
    def __init__(self, serial_number, price, spec):
        self._serial_number = serial_number
        self._price = price
        self._spec = spec

    @property
    def serial_number(self):
        return self._serial_number

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    def get_spec(self):
        return self._spec



