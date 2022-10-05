import battle_manager
from player_manager import PlayerManager
import event_manager
import input_manager
import level_parser
import level_manager
import conversation_manager
import inventory_manager
import item_manager
from managers.entity_manager import EntityManager

class GameManager:
    """Herald ye, i am the gay manager of this game all shall tremeble at mine approach. My gaze pierces cloud, shadow, earth and flesh."""

    STATE_CHARACTER_CREATION = "state_character_creation"
    STATE_MOVEMENT = "state_movement"
    STATE_BATTLE = "state_battle"
    STATE_CONVERSATION = "state_conversation"
    STATE_INVENTORY = "state_inventory"

    _game_state = None
    _player_manager = None
    _entity_manager = None

    def __init__(self):
        GameManager._game_state = GameManager.STATE_CHARACTER_CREATION
        self._initialize_managers()
        self._register_listeners()
        self._transition_to_movement()

    # attribute accessors

    def get_player_manager(self):
        return self._player_manager

    def get_manager(self):
        pass

    @property
    def game_state(self):
        return self._game_state

    # private methods

    def _transition_to_movement(self):
        self._set_state(GameManager.STATE_MOVEMENT)
        dungeon_map = level_parser.build_the_level('level_1', 'data/symbols_dictionary.yaml')

    def _initialize_managers(self):
        self._entity_manager = EntityManager()
        battle_manager.initialize(self)
        item_manager.initialize(self)
        inventory_manager.initialize(self)
        input_manager.initialize(self)
        self._player_manager = PlayerManager()
        level_manager.initialize(self)
        conversation_manager.initialize(self)

    def _register_listeners(self):
        event_manager.listen(event_manager.BATTLE_EVENT, self._battle_started_handler)
        event_manager.listen(event_manager.END_BATTLE_EVENT, self._battle_ended_handler)

        event_manager.listen(event_manager.CONVERSATION_EVENT, self._conversation_started_handler)
        event_manager.listen(event_manager.END_CONVERSATION_EVENT, self._conversation_ended_handler)

        event_manager.listen(event_manager.OPEN_INVENTORY_EVENT, self._inventory_opened_handler)
        event_manager.listen(event_manager.CLOSE_INVENTORY_EVENT, self._inventory_closed_handler)

        event_manager.listen(event_manager.QUIT_EVENT, self._quit_event_handler)
        event_manager.listen(event_manager.GAME_FINISH_EVENT, self._game_finish_event_handler)

    def _set_state(self, new_state, event_data = []):
        previous_state = GameManager._game_state
        GameManager._game_state = new_state
        self._dispatch_state_change(previous_state, new_state, event_data)

    def _dispatch_state_change(self, previous_state, new_state, event_data):
        data = { "previous_state": previous_state, "new_state": new_state, "event_data": event_data }

        event_manager.trigger_event(event_manager.STATE_CHANGE_EVENT, data)

    def _quit(self):
        player = self._player_manager.player
        print(f"Farewell {player.name}")
        exit()

    def _game_end(self):
        player_data = self._player_manager.player
        print(f"\nCongratulations {player_data.name}!\n\nYou have escaped the bleak and terrible dungeon!\n")
        print(f"\n{player_data.name} has finished their Adventure! So far...\n")
        exit()

    def _game_over(self):
        pass

    # event handlers

    def _battle_started_handler(self, event, data):
        self._set_state(GameManager.STATE_BATTLE, data)

    def _battle_ended_handler(self, event, data):
        self._set_state(GameManager.STATE_MOVEMENT, data)

    def _inventory_opened_handler(self, event, data):
        self._set_state(GameManager.STATE_INVENTORY, data)

    def _inventory_closed_handler(self, event, data):
        self._set_state(GameManager.STATE_MOVEMENT, data)

    def _conversation_started_handler(self, event, data):
        self._set_state(GameManager.STATE_CONVERSATION, data)

    def _conversation_ended_handler(self, event, data):
        self._set_state(GameManager.STATE_MOVEMENT, data)

    def _quit_event_handler(self, event_name, data):
        self._quit()

    def _game_finish_event_handler(self, event_name, data):
        self._game_end()
