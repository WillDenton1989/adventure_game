from models.entities.can_battle import CanBattle
from models.entities.entity_base import EntityBase

class Monster(EntityBase, CanBattle):
    def __init__(self, data):
        EntityBase.__init__(self, data)
        CanBattle.__init__(self, data)
        self._catchphrase = data["catchphrase"]

    # attribute accessors

    @property
    def catchphrase(self):
        return self._catchphrase

    # public methods

    # private method

    def _sort_index(self):
        return 300
