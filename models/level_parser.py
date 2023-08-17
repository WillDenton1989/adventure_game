import yaml

from models.level import Level

class LevelParser:
    """parses the level and level objects from yaml data"""

    def __init__(self):
        pass

    # attribute accessors

    # public methods

    def build_the_level(self, level_name, symbol_dict): # DEBUG FILE location
        string_map = self._load_map("data/" + level_name + ".txt")
        map_key_dict = self._load_dictionary_yaml("data/" + symbol_dict + ".yaml")
        entity_templates = self._load_level_objects("data/" + level_name + "_entities.yaml")
        level = Level(string_map, map_key_dict, entity_templates)

        return level

    # private methods

    def _load_level_objects(self, filename):
        with open(filename) as f:
            data = yaml.safe_load(f)

        return data

    def _load_map(self, filename):
        map_list = []
        with open(filename) as map:
            for line in map:
                x = line.split()
                map_list.append(x)
            return map_list

    def _load_dictionary_yaml(self, filename):
        with open(filename) as f:
            data = yaml.safe_load(f)

        return data
