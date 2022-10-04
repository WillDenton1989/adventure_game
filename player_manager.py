import yaml
import battle_manager
import input_manager
import event_manager
import game_manager
import level_manager
import item_manager
from models.item import Item

class PlayerManager:
    """this is the player manager class"""

    _player = {
        "name": None,
        "battle_decision": None
    }

    def __init__(self):
        event_manager.listen(event_manager.UPDATE_PLAYER_LOCATION_EVENT, self._update_player_location_event_handler)
        player_data, inventory_data = self._load_player_default_data("data/player_data.yaml") # hard coded file, probably no beuno
        self._set_player(player_data)
        self._create_starting_inventory(inventory_data)

    # attribute accessor bois.

    @property
    def get_player_data(self):
        return self._player

    def update_player_data(self, data_1):
        return self._player.update(data_1)

    @property
    def change_player_data(self, key, value):
        self._player[key] = value
        return self._player

    @property
    def create_player(self):
        self._player["name"] = input_manager.parse_input()

    # private methods

    def _load_player_default_data(self, file_name):
        with open(file_name) as f:
            data = yaml.safe_load(f)

        return data["player"], data["starting_inventory"]

    def _set_player(self, player_data):
        self._player = player_data

    def _create_starting_inventory(self, inventory_data):
        for item_key in inventory_data:

            item = item_manager.item_from_key(item_key)

            object_item = Item(item["display_name"], item["type"], item["effects"], item["weight"], item["value"], item["consumable"], item["equipable"])

            event_manager.trigger_event(event_manager.ADD_ITEM_TO_INVENTORY_EVENT, object_item)

    def _execute_player_move(self, new_column, new_row):

        self._player["column"] = new_column
        self._player["row"] = new_row

    # event handlers

    def _update_player_location_event_handler(self, event_name, data):
        self._execute_player_move(data["location"]["column"], data["location"]["row"])
