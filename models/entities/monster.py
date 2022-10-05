from models.entities.entity_base import EntityBase
from models.entities.battleable import Battleable

class Monster(EntityBase, Battleable):
    """basic monster class"""

    def __init__(self, data):
        EntityBase.__init__(self, data)
        Battleable.__init__(self, data)
        self._catchphrase = data["catchphrase"]

    # attribute accessors

    @property
    def catchphrase(self):
        return self._catchphrase
