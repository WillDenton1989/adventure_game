from managers.manager_base import ManagerBase

from models.entities.npc import Npc
from models.name_generator import NameGenerator

class NpcManager(ManagerBase):
    def __init__(self, event_dispatcher):
        ManagerBase.__init__(self, event_dispatcher)
        self._npcs = []

    # public methods

    def create_npc(self, npc_data):
        name = NameGenerator().new_name(npc_data["character_class"])
        npc_data.update({ "name": name })
        npc = Npc(npc_data)
        self._npcs.append(npc)

        return npc

    # private methods

    def _register_listeners(self):
        pass

    def _unregister_listeners(self):
        pass

    def _handle_game_state_change(self, previous_state, new_state, data):
        pass
