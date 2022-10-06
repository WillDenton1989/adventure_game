from models.entities.entity_base import EntityBase

class Treasure(EntityBase):

    def __init__(self, data):
        EntityBase.__init__(self, data)

    # private methods

    def _sort_index(self):
        return 100
