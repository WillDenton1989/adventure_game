#this is tha map reader boi.
import yaml
import level_manager
import player_manager
import event_manager
from models.level import Level

# public methods

def initialize():
    pass

def build_the_level(level_name, symbol_dict):
    string_map = _load_map("data/" + level_name + ".txt")
    map_key_dict = _load_dictionary_yaml(symbol_dict)
    level = Level(string_map, map_key_dict)

    level_manager.set_level(level)
    _load_objects("data/" + level_name + "_objects.yaml")

# private methods

def _load_objects(filename):
    with open(filename) as f:
        data = yaml.safe_load(f)

        for object in data["objects"]:
            if(object["object_name"] == "player_start"):
                _add_player(object)
            else:
                _add_entity(object)

    return data

def _add_player(object):
    data = { "location": object["location"] }
    event_manager.trigger_event(event_manager.UPDATE_PLAYER_LOCATION_EVENT, data)

def _add_entity(entity_data):
    data = { "entity_data": entity_data }
    event_manager.trigger_event(event_manager.CREATE_ENTITY_EVENT, data)

def _load_map(filename):
    map_list = []
    map = open(filename)
    for line in map:
        x = line.split()
        map_list.append(x)
    return map_list

def _load_dictionary_yaml(filename):
    with open(filename) as f:
        data = yaml.safe_load(f)

    return data
