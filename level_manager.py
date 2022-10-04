# where the map lives.
import player_manager
import battle_manager
import input_manager
import yaml
import event_manager
import input_manager
import game_manager

_objects = []
_events = []
_current_level = None

def initialize():
    event_manager.listen(event_manager.MOVEMENT_EVENT, _movement_event_handler)

def add_object(object, _events=[]):
    _objects.append(object)

    for event_name in _events:
        _add_event(event_name, object)

def set_current_level(level):
    global _current_level

    _current_level = level

def open_yaml_file(filename):
    with open(filename, 'r') as file:
        doc = yaml.safe_load(file)
    return doc

def load_player_data(yaml_file):
    data = open_yaml_file(yaml_file)

    player_manager.update_player_data(data['player'])

def draw_map():
    global _objects
    objects_to_draw = [game_manager.GameManager._player_manager.get_player_data]
    objects_to_draw.extend(_objects)

    col_index = 0
    row_index = 0

    for row in _current_level:
        for column in row:
            object = _object_at_coordinate(objects_to_draw, col_index, row_index)
            if(object == None):
                print(chr(column), end = "")
            else:
                print(chr(object["symbol"]), end = "")
            col_index += 1
        print("\r")
        row_index += 1
        col_index = 0

# private methods

def _add_event(event_name, data):
    location = { "row": data["row"], "column": data["column"] }
    _events.append({ "event_name": event_name, "data": data, "location": location })

def _trigger_level_events(column, row):
    for event in _events:
        if(event["location"]["column"] == column and event["location"]["row"] == row):
            event_manager.trigger_event(event["event_name"], event["data"])

def _determine_new_coordinates(direction, column, row):
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

def _can_player_move_to_coordinate(column, row):
    if(_is_coordinate_on_map(_current_level, column, row) == False): return False
    if(_is_coordinate_passable(_current_level, column, row) == False): return False

    return True

def _move(direction):
    _player = game_manager.GameManager._player_manager.get_player_data
    new_column, new_row = _determine_new_coordinates(direction, _player["column"], _player["row"])

    if(_can_player_move_to_coordinate(new_column, new_row) == True):
        data = { "location": { "column": new_column, "row": new_row } }
        event_manager.trigger_event(event_manager.UPDATE_PLAYER_LOCATION_EVENT, data)
        _trigger_level_events(new_column, new_row)
    else:
        print("You can't move there, hoe")
    pass

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
    _move(data["direction"])
