import sys

from managers.battle_manager import BattleManager
from managers.conversation_manager import ConversationManager
from managers.entity_manager import EntityManager
from managers.hud_manager import HudManager
from managers.input_manager import InputManager
from managers.inventory_manager import InventoryManager
from managers.item_manager import ItemManager
from managers.level_manager import LevelManager
from managers.manager_base import ManagerBase

from models.event_dispatcher import EventDispatcher
from models.events.battle_event import BattleEvent
from models.events.conversation_event import ConversationEvent
from models.events.game_event import GameEvent
from models.events.inventory_event import InventoryEvent
from models.events.level_event import LevelEvent
from models.state import State

class GameManager(ManagerBase):
    """The Great Eye, ever watchful. Its gaze pierces cloud, shadow, earth and game_file."""

    def __init__(self):
        event_dispatcher = EventDispatcher()
        ManagerBase.__init__(self, event_dispatcher)
        self.game_state = State.STATE_CHARACTER_CREATION
        self._turns = 0

        self._initialize_managers()

    def start(self):
        self._register_manager_starts()

        self.process()

    def process(self):
        while(self.game_state != State.STATE_GAME_END):
            self._increment_turn()
            self._player_death()
            self._run_manager_processes()
            if(self.game_state == State.STATE_CHARACTER_CREATION):
                self._transition_to_movement()

    # attribute accessors

    @property
    def turns(self):
        return self._turns

    @property
    def player(self):
        return self._entity_manager.player

    # private methods

    def _initialize_managers(self):
        self._item_manager = ItemManager(self.event_dispatcher, self)
        self._inventory_manager = InventoryManager(self.event_dispatcher, self._item_manager)
        self._entity_manager = EntityManager(self.event_dispatcher)
        self._input_manager = InputManager(self.event_dispatcher)
        self._battle_manager = BattleManager(self.event_dispatcher)
        self._level_manager = LevelManager(self.event_dispatcher, self)
        self._conversation_manager = ConversationManager(self.event_dispatcher)
        self._hud_manager = HudManager(self.event_dispatcher, self)

    def _register_receivers(self):
        self.event_dispatcher.receive(BattleEvent.BATTLE_EVENT, self._battle_started_handler)
        self.event_dispatcher.receive(BattleEvent.END_BATTLE_EVENT, self._battle_ended_handler)

        self.event_dispatcher.receive(ConversationEvent.CONVERSATION_EVENT, self._conversation_started_handler)
        self.event_dispatcher.receive(ConversationEvent.END_CONVERSATION_EVENT, self._conversation_ended_handler)

        self.event_dispatcher.receive(InventoryEvent.OPEN_INVENTORY_EVENT, self._inventory_opened_handler)
        self.event_dispatcher.receive(InventoryEvent.CLOSE_INVENTORY_EVENT, self._inventory_closed_handler)
        self.event_dispatcher.receive(InventoryEvent.LOOT_EVENT, self._loot_event_handler)

        self.event_dispatcher.receive(GameEvent.QUIT_EVENT, self._quit_event_handler)
        self.event_dispatcher.receive(GameEvent.GAME_FINISH_EVENT, self._game_finish_event_handler)

    def _unregister_receivers(self):
        pass

    def _register_manager_starts(self):
        self._entity_manager.start()
        self._item_manager.start()
        self._inventory_manager.start()
        self._battle_manager.start()
        self._level_manager.start()
        self._conversation_manager.start()
        self._input_manager.start()
        self._hud_manager.start()

    def _run_manager_processes(self):
        self._hud_manager.process()
        self._level_manager.process()
        self._entity_manager.process()
        self._inventory_manager.process()
        self._item_manager.process()
        self._battle_manager.process()
        self._conversation_manager.process()
        self._input_manager.process() # this should always be last in the order.

    def _set_state(self, new_state, event_data = []):
        previous_state = self.game_state
        self.game_state = new_state
        self._dispatch_state_change(previous_state, new_state, event_data)

    def _dispatch_state_change(self, previous_state, new_state, event_data):
        data = { "previous_state": previous_state, "new_state": new_state, "event_data": event_data }
        self.event_dispatcher.dispatch(GameEvent(GameEvent.STATE_CHANGE_EVENT, data))

    def _transition_to_movement(self):
        self._set_state(State.STATE_MOVEMENT)
        self._level_manager.set_level('level_1', 'data/symbols_dictionary.yaml')

    def _increment_turn(self):
        if(self.game_state == State.STATE_MOVEMENT):
            self._turns += 1

    def _quit(self):
        print(f"Farewell {self.player.name}")
        sys.exit(0)

    def _player_death(self):
        if(self.player.hit_points <= 0):
            self._line_formating()
            print(f"\n{self.player.name} has been lost in the depths of the dungeon, succumbing to its evil.")
            if(self.turns <=1):
                print(f"\nAnd it only took {self.player.name} {self._turns} turn to perish miserably.\n")
            else:
                print(f"\nAnd it only took {self.player.name} {self._turns} turns to perish miserably.\n")
            self._line_formating()
            self._set_state(State.STATE_GAME_END, {})

    def _game_finish_line(self):
        self._line_formating()
        print(f"\nCongratulations {self.player.name}!\n\nYou escaped the bleak and terrible dungeon in {self._turns} turns!\n")
        print(f"{self.player.name} has finished their Adventure! So far...\n")
        self._line_formating()
        self._set_state(State.STATE_GAME_END, {})

    def _line_formating(self):
        # probaly just need something like curses. but for now this helps.
        print("------------------------------------------------------------------------")

    def _handle_game_state_change(self, previous_state, new_state, data):
        pass

    def _start_battle(self, monster):
        data = { "player": self.player, "monster": monster }
        self._set_state(State.STATE_BATTLE, data)

    def _start_conversation(self, conversation_data):
        conversation_data.update({ "player": self.player })
        self._set_state(State.STATE_CONVERSATION, conversation_data)

    def _start_loot(self, entity_loot_data):
        self._set_state(State.STATE_LOOT, entity_loot_data)

    # event handlers

    def _battle_started_handler(self, event):
        self._start_battle(event.monster)

    def _battle_ended_handler(self, _event):
        print("Here in battle ended event handler.") # DEBUG
        self._set_state(State.STATE_MOVEMENT)

    def _inventory_opened_handler(self, _event):
        self._set_state(State.STATE_INVENTORY)

    def _inventory_closed_handler(self, _event):
        self._set_state(State.STATE_MOVEMENT)

    def _loot_event_handler(self, event):
        self._start_loot(event.entity)

    def _conversation_started_handler(self, event):
        self._start_conversation(event.data)

    def _conversation_ended_handler(self, _event):
        self._set_state(State.STATE_MOVEMENT)

    def _quit_event_handler(self, _event):
        self._quit()

    def _game_finish_event_handler(self, event):
        self._game_finish_line()
