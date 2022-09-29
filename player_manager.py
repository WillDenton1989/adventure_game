#player manager
import yaml
import battle_manager
import input_manager
import event_manager
import game_manager
import level_manager
import item_manager
from models import item_model

_player = {
    "name": None,
    "battle_decision": None
}

def initialize():
    event_manager.listen(event_manager.UPDATE_PLAYER_LOCATION_EVENT, _update_player_location_event_handler)
    player_data, inventory_data = _load_player_default_data()
    _set_player(player_data)
    _create_starting_inventory(inventory_data)

def get_player_data():
    global _player
    return _player

def update_player_data(data):
    global _player
    return _player.update(data)

def change_player_data(key, value):
    global _player
    _player[key] = value
    return _player


def create_player():
    _player["name"] = input_manager.parse_input()

# private methods

def _load_player_default_data():
    with open("data/player_data.yaml") as f: # hardcoded file no bueno
        data = yaml.safe_load(f)

    return data["player"], data["starting_inventory"]

def _set_player(player_data):
    global _player
    _player = player_data

def _create_starting_inventory(inventory_data):
    for item_key in inventory_data:

        item = item_manager.item_from_key(item_key)

        object_item = item_model.Item(item["display_name"], item["type"], item["effect"], item["weight"], item["value"], item["consumable"], item["equipable"])

        event_manager.trigger_event(event_manager.ADD_ITEM_TO_INVENTORY_EVENT, object_item)

def _execute_player_move(new_column, new_row):
    global _player

    _player["column"] = new_column
    _player["row"] = new_row

# event handlers

def _update_player_location_event_handler(event_name, data):
    _execute_player_move(data["location"]["column"], data["location"]["row"])
