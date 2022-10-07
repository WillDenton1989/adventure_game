
class EventBase:
    def __init__(self, name, data = {}):
        self._data = data
        self._name = name

    # attribute accessors

    @property
    def name(self):
        return self._name

    @property
    def data(self):
        return self._data
