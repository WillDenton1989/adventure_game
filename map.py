#where the map lives.
import time
import game_commands
import map_parser
import monster_module
import battle_manager
import game_parser
import loot_module
import map_reader
import yaml
import data
import level_1_characters
import event_manager

objects = []
events = []

def add_object(object, events=[]):
    objects.append(object)

    for event_name in events:
        _add_event(event_name, object)

def add_player(player):
    add_object(player)

def open_yaml_file(filename):
    with open(filename, 'r') as file:
        doc = yaml.safe_load(file)
    return doc

def load_player_data(yaml_file):
    data = open_yaml_file(yaml_file)

    game_commands.player.update(data['player'])

def npc_coordinates(npc):
    column = npc["column"]
    row = npc["row"]
    return column, row

def object_at_coordinate(objects, column, row):
    for object in objects:
        if(object["column"] == column and object["row"] == row):
            return object
    return None

def draw_map(map, objects):
    col_index = 0
    row_index = 0

    for row in map:
        for column in row:
            object = object_at_coordinate(objects, col_index, row_index)
            if(object == None):
                print(chr(column), end = "")
            else:
                print(chr(object["symbol"]), end = "")
            col_index += 1
        print("\r")
        row_index += 1
        col_index = 0

def determine_new_coordinates(map, direction, column, row):
    if(direction == "right"):
        return column + 1, row
    elif(direction == "left"):
        return column - 1, row
    elif(direction == "up"):
        return column, row - 1
    elif(direction == "down"):
        return column, row + 1
    else:
        pass

def is_coordinate_on_map(map, column, row):
    num_rows = len(map)
    num_columns = len(map[0])
    if(column < 0):
        return False
    if(column >= num_columns):
        return False
    if(row < 0):
        return False
    if(row >= num_rows):
        return False
    return True

def execute_player_move(player, new_column, new_row):
    player["column"] = new_column
    player["row"] = new_row

    _trigger_events(new_column, new_row)

def is_coordinate_passable(map, column, row):
    if(map[row][column] == 8901):
        return True
    else:
        return False

def can_player_move_to_coordinate(map, column, row):
    if(is_coordinate_on_map(map, column, row) == False): return False
    if(is_coordinate_passable(map, column, row) == False): return False

    return True

# private methods

def _add_event(event_name, data):
    location = { "row": data["row"], "column": data["column"] }
    events.append({ "event_name": event_name, "data": data, "location": location })

def _trigger_events(column, row):
    for event in events:
        if(event["location"]["column"] == column and event["location"]["row"] == row):
            event_manager.publish_event(event["event_name"], event["data"])
