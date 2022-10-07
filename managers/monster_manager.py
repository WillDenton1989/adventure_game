from managers.manager_base import ManagerBase

from models.catchphrase_generator import CatchphraseGenerator
from models.entities.monster import Monster
from models.name_generator import NameGenerator

class MonsterManager(ManagerBase):
    def __init__(self, event_dispatcher):
        ManagerBase.__init__(self, event_dispatcher)
        self._monsters = []

    # public methods

    def create_monster(self, monster_data):
        name = NameGenerator().new_name(monster_data["character_class"])
        catchphrase = CatchphraseGenerator().new_phrase(name)
        monster_data.update({ "name": name, "catchphrase": catchphrase })
        monster = Monster(monster_data)
        self._monsters.append(monster)

        return monster

    # private methods

    def _register_listeners(self):
        pass

    def _unregister_listeners(self):
        pass

    def _handle_game_state_change(self, previous_state, new_state, data):
        pass
