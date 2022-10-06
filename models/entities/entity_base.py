from abc import ABC, abstractmethod

class EntityBase(ABC):
    """The basics for any entity that will be drawn on the map"""

    def __init__(self, data):
        self._name = data.get("name")
        self._column = data.get("column")
        self._row = data.get("row")
        self._original_symbol = data["symbol"]
        self._events = data.get("events")
        self._updated_symbol = None

    def __lt__(self, other):
        return self._sort_index() > other._sort_index()

    # attribute accessors

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def column(self):
        return self._column

    @column.setter
    def column(self, value):
        self._column = value

    @property
    def row(self):
        return self._row

    @row.setter
    def row(self, value):
        self._row = value

    @property
    def symbol(self):
        if(self._updated_symbol == None):
            return self._original_symbol
        else:
            return self._updated_symbol

    @symbol.setter
    def symbol(self, value):
        self._updated_symbol = value

    @property
    def events(self):
        return self._events

    # private methods

    @abstractmethod
    def _sort_index(self):
        pass
