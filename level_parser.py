import yaml

from models.events.entity_event import EntityEvent
from models.events.level_event import LevelEvent
from models.level import Level

_event_dispatcher = None

# public methods

def initialize(event_dispatcher):
    global _event_dispatcher

    _event_dispatcher = event_dispatcher

def build_the_level(level_name, symbol_dict):
    string_map = _load_map("data/" + level_name + ".txt")
    map_key_dict = _load_dictionary_yaml(symbol_dict)
    level = Level(string_map, map_key_dict)
    return level

def build_the_objects(level_name):
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
    global _event_dispatcher

    data = { "location": object["location"] }
    _event_dispatcher.dispatch(LevelEvent(LevelEvent.UPDATE_PLAYER_LOCATION_EVENT, data))

def _add_entity(entity_data):
    data = { "entity_data": entity_data }
    _event_dispatcher.dispatch(EntityEvent(EntityEvent.CREATE_ENTITY_EVENT, data))

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
