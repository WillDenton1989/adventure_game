import yaml

from managers.manager_base import ManagerBase

from models.entities.player import Player
from models.events.input_event import InputEvent
from models.events.inventory_event import InventoryEvent
from models.events.level_event import LevelEvent
from models.events.player_event import PlayerEvent
from models.item import Item

class PlayerManager(ManagerBase):
    def __init__(self, event_dispatcher):
        ManagerBase.__init__(self, event_dispatcher)

        player_data, self._inventory_data = self._load_player_default_data("data/player_data.yaml")
        self._item_manager = None
        self._set_player(player_data)

    def start(self):
        pass

    def process(self):
        pass

    # attribute accessors.

    @property
    def player(self):
        return self._player

    # public methods

    def set_item_manager(self, item_manager):
        self._item_manager = item_manager

    def create_player(self):
        self.event_dispatcher.dispatch(InputEvent(InputEvent.INPUT_PARSE_EVENT, {}))
        self._create_starting_inventory(self._inventory_data)

    # private methods

    def _register_receivers(self):
        self.event_dispatcher.receive(LevelEvent.UPDATE_PLAYER_LOCATION_EVENT, self._update_player_location_event_handler)
        self.event_dispatcher.receive(PlayerEvent.PLAYER_NAME_CHANGE_EVENT, self._player_name_change_event_handler)

    def _unregister_receivers(self):
        pass

    def _load_player_default_data(self, file_name):
        with open(file_name) as f:
            data = yaml.safe_load(f)

        return data["player"], data["starting_inventory"]

    def _set_player(self, player_data):
        self._player = Player(player_data)

    def _create_starting_inventory(self, inventory_data):
        for item_key in inventory_data:
            item = self._item_manager.item_from_key(item_key)
            self.event_dispatcher.dispatch(InventoryEvent(InventoryEvent.ADD_ITEM_TO_INVENTORY_EVENT, { "item": item }))

    def _execute_player_move(self, new_column, new_row):
        self._player.column = new_column
        self._player.row = new_row

    def _handle_game_state_change(self, previous_state, new_state, data):
        pass

    def _change_player_name(self, new_name):
        self._player.name = new_name

    # event handlers

    def _update_player_location_event_handler(self, event):
        self._execute_player_move(event.column, event.row)

    def _player_name_change_event_handler(self, event):
        self._change_player_name(event.new_name)
