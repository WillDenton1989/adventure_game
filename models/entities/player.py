from models.entities.can_battle import CanBattle
from models.entities.entity_base import EntityBase

class Player(EntityBase, CanBattle):
    """builds the player class. will have mix-ins to add functionality"""

    def __init__(self, data):
        EntityBase.__init__(self, data)
        CanBattle.__init__(self, data)

        self._speed = data["speed"]

    # attribute accessors

    @property
    def speed(self):
        return self._speed

    # public methods

    # private methods

    def _sort_index(self):
        return 500
