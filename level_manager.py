#where the map lives.
import time
import player_manager
import monster_module
import battle_manager
import input_manager
import loot_module
import yaml
import data
import level_1_characters
import event_manager
import input_manager

_objects = []
_events = []
_current_level = None
_player = None

def initialize():
    event_manager.listen(event_manager.MOVEMENT_EVENT, _movement_event_handler)

# event_manager.trigger_event(event_manager.MOVEMENT_EVENT, data)

def add_object(object, _events=[]):
    _objects.append(object)

    for event_name in _events:
        _add_event(event_name, object)

def add_player(player):
    global _player
    add_object(player)
    _player = player

def set_current_level(level):
    global _current_level

    _current_level = level

def open_yaml_file(filename):
    with open(filename, 'r') as file:
        doc = yaml.safe_load(file)
    return doc

def load_player_data(yaml_file):
    data = open_yaml_file(yaml_file)

    player_manager.player.update(data['player'])

def draw_map():
    global _objects

    col_index = 0
    row_index = 0

    for row in _current_level:
        for column in row:
            object = _object_at_coordinate(_objects, col_index, row_index)
            if(object == None):
                print(chr(column), end = "")
            else:
                print(chr(object["symbol"]), end = "")
            col_index += 1
        print("\r")
        row_index += 1
        col_index = 0

def determine_new_coordinates(direction, column, row):
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

def execute_player_move(player, new_column, new_row):
    player["column"] = new_column
    player["row"] = new_row

    _trigger__events(new_column, new_row)

def can_player_move_to_coordinate(column, row):
    if(_is_coordinate_on_map(_current_level, column, row) == False): return False
    if(_is_coordinate_passable(_current_level, column, row) == False): return False

    return True

# private methods

def _player_move(direction):
    global _player
    new_column, new_row = determine_new_coordinates(direction, _player["column"], _player["row"])

    if(can_player_move_to_coordinate(new_column, new_row) == True):
        execute_player_move(_player, new_column, new_row)
    else:
        print("You can't move there, hoe")

def _add_event(event_name, data):
    location = { "row": data["row"], "column": data["column"] }
    _events.append({ "event_name": event_name, "data": data, "location": location })

def _trigger__events(column, row):
    for event in _events:
        if(event["location"]["column"] == column and event["location"]["row"] == row):
            event_manager.trigger_event(event["event_name"], event["data"])

def _is_coordinate_on_map(map, column, row):
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

def _is_coordinate_passable(map, column, row):
    if(map[row][column] == 8901):
        return True
    else:
        return False

def _object_at_coordinate(_objects, column, row):
    for object in _objects:
        if(object["column"] == column and object["row"] == row):
            return object

    return None

# event handlers

def _movement_event_handler(event_name, data):
    _player_move(data["direction"])
