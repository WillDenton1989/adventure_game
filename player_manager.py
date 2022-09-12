#player manager
import yaml
import battle_manager
import input_manager
import event_manager
import game_manager
import level_manager

_player = {
    "name": None,
    "battle_decision": None
}

def initialize():
    event_manager.listen(event_manager.UPDATE_PLAYER_LOCATION_EVENT, _update_player_location_event_handler)
    # add event handler to catch the level is loaded. That event should contain the player's location.
    # You can set the location then, and add the player to the level manager's objects.
    _set_player()

def get_player_data():
    global _player
    return _player

def update_player_data(data):
    global _player
    return _player.update(data)

def create_player():
    _player["name"] = input_manager.parse_input()

# private methods

def _set_player():
    global _player
    _player = _load_player_data()

def _load_player_data():
    with open("data/player_data.yaml") as f: # hardcoded file no bueno
        data = yaml.safe_load(f)

    return data["player"]

def _execute_player_move(new_column, new_row):
    global _player

    _player["column"] = new_column
    _player["row"] = new_row

# event handlers

def _update_player_location_event_handler(event_name, data):
    _execute_player_move(data["location"]["column"], data["location"]["row"])
