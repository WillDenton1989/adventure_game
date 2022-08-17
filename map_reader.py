#this is tha map reader boi

TL = 9484
BL = 9492
TR = 9488
BR = 9496
HH = 9472
VV = 9474
EE = 8901

PL = 9791
EN = 7777

def load_map(filename):
    map_list = []
    map = open(filename)
    for line in map:
        x = line.split()
        map_list.append(x)
    return map_list

string_map = load_map('map.txt')

map_key_dict = {
    "TL": 9484,
    "BL": 9492,
    "TR": 9488,
    "BR": 9496,
    "HH": 9472,
    "VV": 9474,
    "EE": 8901
    }

def parse_string_map(map, dictionary):
    map_list = []
    for line in map:
        list = []
        for character in line:
            new_value = dictionary.get(character)
            list.append(new_value)
        map_list.append(list)
    return map_list

usable_map = parse_string_map(string_map, map_key_dict)
#print(usable_map)
#the end?
