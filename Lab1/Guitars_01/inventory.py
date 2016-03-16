from guitar import Guitar, GuitarSpec


class Inventory:
    def __init__(self):
        self.guitars = []

    def addGuitar(self, serialNumber, price, spec: GuitarSpec):
        guitar = Guitar(serialNumber, price, spec)
        self.guitars.append(guitar)

    def getGuitar(self, serialNumber):
        """
        Zwraca obiekt gitary jeśli znajdzie gitarę o identycznym numerze seryjnym

        :param serialNumber:
        :return: Guitar | None
        """
        for guitar in self.guitars:
            if guitar.serialNumber == serialNumber:
                return guitar
        return None

    def search(self, searchSpec: GuitarSpec):
        """
        Metoda porównuje wszystkie właściwości obiektu Guitar przekazanego w wywołaniu
        zwraca znalezioną gitarę lub None
        :param guitar:
        :return: Guitar | None
        """
        machingGuitars = []
        for guitar in self.guitars:
            if not guitar.getSpec().matches(searchSpec):
                continue
            machingGuitars.append(guitar)
        return machingGuitars
