import yaml

from managers.manager_base import ManagerBase

from models.entities.player import Player
from models.events.inventory_event import InventoryEvent
from models.events.level_event import LevelEvent
from models.events.player_event import PlayerEvent
from models.item import Item
from models.state import State

class PlayerManager(ManagerBase):
    def __init__(self, event_dispatcher, player_template):
        ManagerBase.__init__(self, event_dispatcher)
        self._item_manager = None

        self.create_player(player_template["player"])

    def start(self):
        pass

    def process(self):
        pass

    # attribute accessors.

    @property
    def player(self):
        return self._player

    # public methods

    def create_player(self, player_template):
        self._player = Player(player_template)
        self._dispatch_inventory_data(self.player, player_template)

    # private methods

    def _register_receivers(self):
        self.event_dispatcher.receive(LevelEvent.UPDATE_PLAYER_LOCATION_EVENT, self._update_player_location_event_handler)
        self.event_dispatcher.receive(PlayerEvent.PLAYER_NAME_CHANGE_EVENT, self._player_name_change_event_handler)

    def _unregister_receivers(self):
        pass

    def _change_player_name(self, new_name):
        self._player.name = new_name

    def _dispatch_inventory_data(self, player, player_template):
        player = self.player
        player_id = id(self.player)
        data = { "id" : { "player_id" : player_id }, "inventory" : player_template["inventory"]} # "player_object" : player
        self.event_dispatcher.dispatch(InventoryEvent(InventoryEvent.CREATE_INVENTORY_EVENT, data))

    def _execute_player_move(self, new_column, new_row):
        self._player.column = new_column
        self._player.row = new_row

    def _handle_game_state_change(self, previous_state, new_state, data):
        pass

    # event handlers

    def _update_player_location_event_handler(self, event):
        self._execute_player_move(event.column, event.row)

    def _player_name_change_event_handler(self, event): # DEBUG
        self._change_player_name(event.new_name)
