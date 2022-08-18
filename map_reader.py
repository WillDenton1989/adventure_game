#this is tha map reader boi
import json

def load_map_key_dictionary(filename):
    with open(filename) as f:
        data = f.read()
    dict = json.loads(data)
    return dict

def load_map(filename):
    map_list = []
    map = open(filename)
    for line in map:
        x = line.split()
        map_list.append(x)
    return map_list

def parse_string_map(map, dictionary):
    #why is map list a bad variable name btw?
    map_list = []
    for line in map:
        list = []
        for character in line:
            new_value = dictionary.get(character)
            list.append(new_value)
        map_list.append(list)
    return map_list

def is_it_square(string_map):
    if(len(string_map) != len(string_map[0])):
        return False
    else:
        return True

def check_map(string_map, map_key_dict):
    if(is_it_square(string_map) == True):
        square_map = parse_string_map(string_map, map_key_dict)
        return square_map
    else:
        print("The map you provided is not square.")
        return None
        
#change the arg of load_map to the name of the text file you wish to use as the map.
string_map = load_map('map.txt')
#loads map key dictionary from a text file. make sure its actually an appropriate dictionary.
map_key_dict = load_map_key_dictionary('map_symbol_dictionary.txt')
#parse string map will use a symbol dictionary to parse the loaded map into a viable map.
usable_map = check_map(string_map, map_key_dict)

# example of keys dictionary.
# map_key_dict = {
#     "TL": 9484,
#     "BL": 9492,
#     "TR": 9488,
#     "BR": 9496,
#     "HH": 9472,
#     "VV": 9474,
#     "EE": 8901
#     }

# example of map
# map_1 = [
#         [TL, HH, HH, HH, HH, HH, HH, HH, HH, HH, HH, TR],
#         [VV, EE, EE, EE, EE, EE, EE, EE, EE, EE, EE, VV],
#         [VV, EE, EE, EE, EE, EE, EE, EE, EE, EE, EE, VV],
#         [VV, EE, EE, EE, EE, EE, EE, EE, EE, EE, EE, VV],
#         [VV, EE, EE, EE, TL, HH, HH, TR, EE, EE, EE, VV],
#         [VV, EE, EE, EE, VV, EE, EE, EE, EE, EE, EE, VV],
#         [VV, EE, EE, EE, VV, EE, EE, VV, EE, EE, EE, VV],
#         [VV, EE, EE, EE, BL, HH, HH, BR, EE, EE, EE, VV],
#         [VV, EE, EE, EE, EE, EE, EE, EE, EE, EE, EE, VV],
#         [VV, EE, EE, EE, EE, EE, EE, EE, EE, EE, EE, VV],
#         [VV, EE, EE, EE, EE, EE, EE, EE, EE, EE, EE, VV],
#         [BL, HH, HH, HH, HH, HH, HH, HH, HH, HH, HH, BR]
# ]
