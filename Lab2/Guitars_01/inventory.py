from guitar import Instrument


class Inventory:
    def __init__(self):
        self._inventory = []

    def add_instrument(self, serial_number, price, spec):
        instrument = Instrument(serial_number, price, spec)
        self._inventory.append(instrument)

    @property
    def get(self, serial_number):
        for instr in self._inventory:
            if instr.serial_number == serial_number:
                return instr
        return None

    def search(self, search_spec):
        matching_instruments = []
        for instr in self._inventory:
            if instr.get_spec().matches(search_spec):
                matching_instruments.append(instr)
        return matching_instruments
