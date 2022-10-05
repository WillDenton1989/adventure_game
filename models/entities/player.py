from models.entities.entity_base import EntityBase
from models.entities.battleable import Battleable

class Player(EntityBase, Battleable):
    """builds the basic player class"""

    def __init__(self, data):
        EntityBase.__init__(self, data)
        Battleable.__init__(self, data)

        self._speed = data["speed"]

    # accessors

    @property
    def speed(self):
        return self._speed
