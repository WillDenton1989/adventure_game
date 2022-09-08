#this is tha map reader boi.
import yaml
import level_manager
import player_manager
import level_1_characters

# public methods

def build_the_level(level_name, symbol_dict):
    string_map = _load_map("data/" + level_name + ".txt")
    map_key_dict = _load_dictionary_yaml(symbol_dict)
    usable_map = _check_map(string_map, map_key_dict)
    _load_objects("data/" + level_name + "_objects.yaml")

    level_manager.set_current_level(usable_map)

    return usable_map

# private methods

def _set_player(data):
    player_stats = _load_player_data()

    player_manager.update_player_data(data['location'])
    player_manager.update_player_data(player_stats)
    level_manager.add_player(player_manager.get_player_data())

def _load_player_data():
    with open("data/player_data.yaml") as f: # hardcoded file no bueno
        data = yaml.safe_load(f)

    return data["player"]

def _add_npc(data):
    npc_data = _load_npcs(data["key"])
    npc_data.update(data["location"])

    level_manager.add_object(npc_data)

def _add_monster(data):
    npc_data = _load_npcs(data["key"])
    npc_data.update(data["location"])

    level_manager.add_object(npc_data, data["events"])

def _add_treasure(data):
    npc_data = _load_npcs(data["key"])
    npc_data.update(data["location"])

    level_manager.add_object(npc_data)

def _add_finish_line(data):
    npc_data = _load_npcs(data["key"])
    npc_data.update(data["location"])

    level_manager.add_object(npc_data)

def _load_npcs(key):
    with open("data/npc_data.yaml") as f: # hardcoded filename no bueno
        data = yaml.safe_load(f)

    return data[key]

def _check_map(string_map, map_key_dict):
    if(_is_it_square(string_map) == True):
        square_map = _parse_string_map(string_map, map_key_dict)
        return square_map
    else:
        print("The map you provided is not square.")
        return None

def _is_it_square(string_map):
    if(len(string_map) != len(string_map[0])):
        return False
    else:
        return True

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

def _parse_string_map(map, dictionary):
    map_list = []
    for line in map:
        list = []
        for character in line:
            new_value = dictionary.get(character)
            list.append(new_value)
        map_list.append(list)
    return map_list

def _load_objects(filename):
    with open(filename) as f:
        data = yaml.safe_load(f)

        for object in data["objects"]:
            if(object["object_name"] == "player_start"):
                _set_player(object)
            elif(object["object_name"] == "monster"):
                _add_monster(object)
            elif(object["object_name"] == "treasure"):
                _add_treasure(object)
            elif(object["object_name"] == "finish_line"):
                _add_finish_line(object)
            elif(object["object_name"] == "npc"):
                _add_npc(object)
            else:
                pass # look at throwing exceptions!!!

    return data
