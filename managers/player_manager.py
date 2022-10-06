import yaml
import item_manager
import event_manager
from models.item import Item
from models.entities.player import Player
from managers.manager_base import ManagerBase
from managers.input_manager import InputManager

class PlayerManager(ManagerBase):
    def __init__(self):
        ManagerBase.__init__(self)

        event_manager.listen(event_manager.UPDATE_PLAYER_LOCATION_EVENT, self._update_player_location_event_handler)
        player_data, self._inventory_data = self._load_player_default_data("data/player_data.yaml")

        self._set_player(player_data)

    # attribute accessor bois.

    @property
    def player(self):
        return self._player

    # public methods

    def create_player(self):
        event_manager.trigger_event(event_manager.INPUT_PARSE_EVENT, {})
        self._create_starting_inventory(self._inventory_data)

    # private methods

    def _register_listeners(self):
        event_manager.listen(event_manager.PLAYER_NAME_CHANGE_EVENT, self._player_name_change_event_handler)

    def _unregister_listeners(self):
        pass

    def _load_player_default_data(self, file_name):
        with open(file_name) as f:
            data = yaml.safe_load(f)

        return data["player"], data["starting_inventory"]

    def _set_player(self, player_data):
        self._player = Player(player_data)

    def _create_starting_inventory(self, inventory_data):
        for item_key in inventory_data:
            item = item_manager.item_from_key(item_key)

            object_item = Item(item["display_name"], item["type"], item["effects"], item["weight"], item["value"], item["consumable"], item["equipable"])

            event_manager.trigger_event(event_manager.ADD_ITEM_TO_INVENTORY_EVENT, object_item)

    def _execute_player_move(self, new_column, new_row):
        self._player.column = new_column
        self._player.row = new_row

    def _handle_game_state_change(self, previous_state, new_state):
        pass

    def _change_player_name(self, new_name):
        self._player.name = new_name

    # event handlers

    def _update_player_location_event_handler(self, event_name, data):
        self._execute_player_move(data["location"]["column"], data["location"]["row"])

    def _player_name_change_event_handler(self, event_name, data):
        self._change_player_name(data["name"])
