from models.entities.monster import Monster
from models.name_generator import NameGenerator
from models.catchphrase_generator import CatchphraseGenerator

class MonsterManager:

    def __init__(self):
        self._monsters = []

    # public methods

    def create_monster(self, monster_data):
        name = NameGenerator().new_name(monster_data["character_class"])
        catchphrase = CatchphraseGenerator().new_phrase(name)
        monster_data.update({ "name": name, "catchphrase": catchphrase })
        monster = Monster(monster_data)
        self._monsters.append(monster)

        return monster
