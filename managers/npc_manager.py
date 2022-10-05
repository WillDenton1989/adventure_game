from models.entities.npc import Npc
from models.name_generator import NameGenerator

class NpcManager:
    def __init__(self):
        self._npcs = []

    # public methods

    def create_npc(self, npc_data):
        name = NameGenerator().new_name(npc_data["character_class"])
        npc_data.update({ "name": name })
        npc = Npc(npc_data)
        self._npcs.append(npc)

        return npc
