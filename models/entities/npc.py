from models.entities.entity_base import EntityBase

class Npc(EntityBase):
    def __init__(self, data):
        EntityBase.__init__(self, data)

    # attribute accessors

    # public methods
    
    # private methods

    def _sort_index(self):
        return 200
