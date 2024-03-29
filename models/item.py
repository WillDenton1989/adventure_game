class Item:
    """Builds the basic Item class. This was also my first class. :D"""

    def __init__(self, item_data):
        self._display_name = item_data["display_name"]
        self._effects = item_data.get("effects")
        self._modifier = item_data.get("modifier")
        self._modifier_value = item_data.get("modifier_value")
        self._weight = item_data["weight"]
        self._value = item_data["value"]
        self._consumable = item_data["consumable"]
        self._equipable = item_data["equipable"]
        self._equiped = False

    def __str__(self):
        if(self.equiped == True):
            return f"{self._display_name} - Equiped"
        else:
            return f"{self._display_name}"

    def __lt__(self, other):
        pass

    # Attribute accessors

    @property
    def display_name(self):
        return self._display_name

    @property
    def consumable(self):
        return self._consumable

    @property
    def equipable(self):
        return self._equipable

    @property
    def equiped(self):
        return self._equiped

    @equiped.setter
    def equiped(self, value):
        self._equiped = value

    @property
    def effects(self):
        return self._effects

    @property
    def modifier(self):
        return self._modifier

    @property
    def modifier_value(self):
        return self._modifier_value

    @property
    def weight(self):
        return self._weight

    # public methods

    # private methods
