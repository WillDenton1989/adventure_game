#this is tha map reader boi

map_key_dict = {
    "TL": 9484,
    "BL": 9492,
    "TR": 9488,
    "BR": 9496,
    "HH": 9472,
    "VV": 9474,
    "EE": 8901
    }

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

#change the arg of load_map to the name of the text file you wish to use as the map.
string_map = load_map('map.txt')
#parse string map will use a symbol dictionary to parse the loaded map into a viable map.
usable_map = parse_string_map(string_map, map_key_dict)
