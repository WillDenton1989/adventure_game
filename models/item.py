# this is where the item model shall live.

class Item:
    """builds the basics for items"""

    VALID_TYPES = ["junk", "consumable", "weapon", "armor", "treasure"]

    def __init__(self, display_name = None, VALID_TYPES = 0, effects = None, weight = 1, value = 1, consumable = False, equipable = False):
        self._display_name = display_name
        self._type = VALID_TYPES
        self._effects = effects
        self._weight = weight
        self._value = value
        self._consumable = consumable
        self._equipable = equipable


    def __str__(self):
        return f"{self._display_name}"

    # Attribute accessors

    @property
    def consumable(self):
        return self._consumable

    @property
    def equipable(self):
        return self._equipable

    @property
    def effects(self):
        return self._effects

    @property
    def weight(self):
        return self._weight
