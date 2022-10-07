from managers.battle_manager import BattleManager
from managers.conversation_manager import ConversationManager
from managers.entity_manager import EntityManager
import event_manager
from managers.input_manager import InputManager
from managers.inventory_manager import InventoryManager
from managers.item_manager import ItemManager
from managers.level_manager import LevelManager
from managers.manager_base import ManagerBase
from models.state import State

class GameManager(ManagerBase):
    """Herald ye, i am the god of this game. All shall tremeble at mine approach. My gaze pierces cloud, shadow, earth and flesh."""

    def __init__(self):
        ManagerBase.__init__(self)
        self.game_state = State.STATE_CHARACTER_CREATION
        self._initialize_managers()
        self._start()

    # attribute accessors

    def get_player_manager(self):
        return self.player

    @property
    def battle_manager(self):
        return self._battle_manager

    @property
    def player(self):
        return self._entity_manager.player

    # private methods

    def _initialize_managers(self):
        self._entity_manager = EntityManager()
        self._input_manager = InputManager()
        self._item_manager = ItemManager(self)
        self._inventory_manager = InventoryManager()
        self._battle_manager = BattleManager()
        self._level_manager = LevelManager(self)
        self._conversation_manager = ConversationManager()

    def _register_listeners(self):
        event_manager.listen(event_manager.BATTLE_EVENT, self._battle_started_handler)
        event_manager.listen(event_manager.END_BATTLE_EVENT, self._battle_ended_handler)

        event_manager.listen(event_manager.CONVERSATION_EVENT, self._conversation_started_handler)
        event_manager.listen(event_manager.END_CONVERSATION_EVENT, self._conversation_ended_handler)

        event_manager.listen(event_manager.OPEN_INVENTORY_EVENT, self._inventory_opened_handler)
        event_manager.listen(event_manager.CLOSE_INVENTORY_EVENT, self._inventory_closed_handler)

        event_manager.listen(event_manager.QUIT_EVENT, self._quit_event_handler)
        event_manager.listen(event_manager.GAME_FINISH_EVENT, self._game_finish_event_handler)

    def _unregister_listeners(self):
        pass

    def _set_state(self, new_state, event_data = []):
        previous_state = self.game_state
        self.game_state = new_state
        self._dispatch_state_change(previous_state, new_state, event_data)

    def _dispatch_state_change(self, previous_state, new_state, event_data):
        data = { "previous_state": previous_state, "new_state": new_state, "event_data": event_data }
        event_manager.trigger_event(event_manager.STATE_CHANGE_EVENT, data)

    def _start(self):
        self._entity_manager.player_manager.set_item_manager(self._item_manager)
        self._entity_manager.create_player()
        self._transition_to_movement()

    def _transition_to_movement(self):
        self._set_state(State.STATE_MOVEMENT)
        self._level_manager.set_level('level_1', 'data/symbols_dictionary.yaml')

    def _quit(self):
        print(f"Farewell {self.player.name}")
        exit()

    def _game_end(self):
        print(f"\nCongratulations {self.player.name}!\n\nYou have escaped the bleak and terrible dungeon!\n")
        print(f"\n{self.player.name} has finished their Adventure! So far...\n")
        exit()

    def _handle_game_state_change(self, previous_state, new_state, data):
        pass

    def _start_battle(self, battle_data):
        battle_data.update({ "player": self.player })
        self._set_state(State.STATE_BATTLE, battle_data)

    def _start_conversation(self, conversation_data):
        conversation_data.update({ "player": self.player })
        self._set_state(State.STATE_CONVERSATION, conversation_data)

    # event handlers

    def _battle_started_handler(self, event, data):
        self._start_battle(data)

    def _battle_ended_handler(self, event, data):
        self._set_state(State.STATE_MOVEMENT, data)

    def _inventory_opened_handler(self, event, data):
        self._set_state(State.STATE_INVENTORY, data)

    def _inventory_closed_handler(self, event, data):
        self._set_state(State.STATE_MOVEMENT, data)

    def _conversation_started_handler(self, event, data):
        self._start_conversation(data)

    def _conversation_ended_handler(self, event, data):
        self._set_state(State.STATE_MOVEMENT, data)

    def _quit_event_handler(self, event_name, data):
        self._quit()

    def _game_finish_event_handler(self, event_name, data):
        self._game_end()
