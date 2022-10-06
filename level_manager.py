# where the map lives.
import battle_manager
from managers.input_manager import InputManager
import yaml
import event_manager
from models.state import State

_game_manager = None
_state = None
_level_class = None

# public methods

def initialize(game_manager):
    global _game_manager
    _game_manager = game_manager
    _register_listeners()

def set_current_level(original_level):
    global _current_level

    _current_level = original_level

def set_level(level):
    global _level_class

    _level_class = level

def draw_level():
    global _level_class

    map = _level_class.drawable_map()
    for row in map:
        for column in row:
            print(chr(column), end = "")
        print("\r")

# private methods

def _register_listeners():
    event_manager.listen(event_manager.MOVEMENT_EVENT, _movement_event_handler)
    event_manager.listen(event_manager.ENTITIES_UPDATED_EVENT, _entities_updated_event_handler)
    event_manager.listen(event_manager.STATE_CHANGE_EVENT, _state_change_event_handler)

def _trigger_level_events(column, row):
    global _level_class
    triggered_events = _level_class.events_for(column, row)
    for event in triggered_events:
        event_manager.trigger_event(event["event_name"], event["data"])

def _move(direction):
    global _level_class
    player = _game_manager.player
    new_column, new_row = _determine_new_coordinates(direction, player.column, player.row)

    if(_level_class.can_move_to(new_column, new_row) == True):
        data = { "location": { "column": new_column, "row": new_row } }
        event_manager.trigger_event(event_manager.UPDATE_PLAYER_LOCATION_EVENT, data)
        _trigger_level_events(new_column, new_row)
    else:
        print("You can't move there, hoe")
    pass

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

def _update_entities(updated_entities):
    global _level_class

    _level_class.update_entities(updated_entities)


def _set_state(new_state):
    global _state
    _state = new_state

# event handlers

def _movement_event_handler(event_name, data):
    _move(data["direction"])

def _entities_updated_event_handler(event_name, data):
    _update_entities(data["updated_entities"])

def _state_change_event_handler(event_name, data):
    _set_state(data["new_state"])
