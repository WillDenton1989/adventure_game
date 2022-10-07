from models.entities.battleable import Battleable
from models.entities.entity_base import EntityBase

class Player(EntityBase, Battleable):
    """builds the player class. will have mix-ins to add functionality"""

    def __init__(self, data):
        EntityBase.__init__(self, data)
        Battleable.__init__(self, data)
        self._speed = data["speed"]

    # attribute accessors

    @property
    def speed(self):
        return self._speed

    # public methods

    # private methods

    def _sort_index(self):
        return 500
