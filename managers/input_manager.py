from managers.manager_base import ManagerBase

from models.events.battle_event import BattleEvent
from models.events.conversation_event import ConversationEvent
from models.events.game_event import GameEvent
from models.events.inventory_event import InventoryEvent
from models.events.level_event import LevelEvent
from models.events.player_event import PlayerEvent
from models.state import State

class InputManager(ManagerBase):
    def __init__(self, event_dispatcher):
        ManagerBase.__init__(self, event_dispatcher)

    def start(self):
        pass

    def process(self):
        if(self.game_state != State.STATE_GAME_END):
            self._parse_input()

    # private methods

    def _register_receivers(self):
        pass

    def _unregister_receivers(self):
        pass

    def _parse_input(self):
        self._show_controls()
        player_input = input(self._prompt()).strip()

        if(self.game_state == State.STATE_CHARACTER_CREATION):
            return self._parse_player_creation(player_input)
        elif(self.game_state == State.STATE_MOVEMENT):
            return self._parse_player_movement(player_input)
        elif(self.game_state == State.STATE_BATTLE):
            return self._parse_battle_input(player_input)
        elif(self.game_state == State.STATE_CONVERSATION):
            return self._parse_conversation_input(player_input)
        elif(self.game_state == State.STATE_INVENTORY):
            return self._parse_inventory_input(player_input)
        elif(self.game_state == State.STATE_LOOT):
            return self._parse_loot_inventory_input(player_input)
        elif(self.game_state == State.STATE_LEVEL_END):
            return self._parse_level_end_input(player_input)
        else:
            raise Exception(f"Cannot parse input for your current game state: {self.game_state}")

    def _show_controls(self):
        if(self.game_state == State.STATE_CHARACTER_CREATION):
            self._show_player_creation_controls()
        elif(self.game_state == State.STATE_MOVEMENT):
            self._show_movement_controls()
        elif(self.game_state == State.STATE_BATTLE):
            self._show_battle_controls()
        elif(self.game_state == State.STATE_CONVERSATION):
            self._show_conversation_controls()
        elif(self.game_state == State.STATE_INVENTORY):
            self._show_inventory_controls()
        elif(self.game_state == State.STATE_LOOT):
            self._show_loot_inventory_controls()
        elif(self.game_state == State.STATE_LEVEL_END):
            self._show_level_end_controls()
        else:
            exception_string = f"Cannot show controls for your current game state: {self.game_state}"
            raise Exception(exception_string)

    def _prompt(self):
        if(self.game_state == State.STATE_CHARACTER_CREATION):
            return "A name, liege? "
        elif(self.game_state == State.STATE_MOVEMENT or State.STATE_INVENTORY):
            return "? "
        elif(self.game_state == State.STATE_BATTLE):
            return f"\nI await your command: "
        elif(self.game_state == State.STATE_CONVERSATION):
            return "What is your response? "
        else:
            raise Exception("There is no prompt for your current game state.")

    def _show_player_creation_controls(self):
        print("Type in your name and your adventure shall begin!\n")

    def _parse_player_creation(self, input):
        if(input == "dood" or "Dude"):
            print(f"\nSup {input}.\n\nAlright then, lets go!\n")
        else:
            print(f"\nAlright {input}, lets go!\n")

        self.event_dispatcher.dispatch(PlayerEvent(PlayerEvent.PLAYER_NAME_CHANGE_EVENT, { "new_name": input }))

    def _show_movement_controls(self):
        print(f"""Press 'k' and 'j' to move up or down.
Press 'h' and 'l' to move left or right.
Press 'i' to open your inventory. Press 'q' to exit the game.""")

    def _parse_player_movement(self, input):
        data = {}

        if(input == "k"):
            data["direction"] = "up"
            self.event_dispatcher.dispatch(LevelEvent(LevelEvent.MOVEMENT_EVENT, data))
        elif(input == "j"):
            data["direction"] = "down"
            self.event_dispatcher.dispatch(LevelEvent(LevelEvent.MOVEMENT_EVENT, data))
        elif(input == "h"):
            data["direction"] = "left"
            self.event_dispatcher.dispatch(LevelEvent(LevelEvent.MOVEMENT_EVENT, data))
        elif(input == "l"):
            data["direction"] = "right"
            self.event_dispatcher.dispatch(LevelEvent(LevelEvent.MOVEMENT_EVENT, data))
        elif(input == "inventory" or input == "i"):
            self.event_dispatcher.dispatch(InventoryEvent(InventoryEvent.OPEN_INVENTORY_EVENT, data))
        elif(input == "quit" or input == "q"):
            self.event_dispatcher.dispatch(GameEvent(GameEvent.QUIT_EVENT, data))
        else:
            self._parse_input()

    def _show_battle_controls(self):
        print("""Press 'a' to attack. Press 'd' to defend (max 3). Press 'q' to quit.""")

    def _parse_battle_input(self, input):
        data = {}
        if(input == "quit" or input == "q"):
            self.event_dispatcher.dispatch(GameEvent(GameEvent.QUIT_EVENT, data))
        elif(input == "attack" or input == "a"):
            data["command"] = "attack"
            self.event_dispatcher.dispatch(BattleEvent(BattleEvent.BATTLE_COMMAND_EVENT, data))
        elif(input == "defend" or input == "d"):
            data["command"] = "defend"
            self.event_dispatcher.dispatch(BattleEvent(BattleEvent.BATTLE_COMMAND_EVENT, data))
        else:
            self._parse_input()

    def _show_conversation_controls(self):
        print("Use the numbers 1 - 3 to reply")

    def _parse_conversation_input(self, input):
        data = {}
        if(input == "quit" or input == "q"):
            self.event_dispatcher.dispatch(GameEvent(GameEvent.QUIT_EVENT, data))
        elif(input == "1"):
            self.event_dispatcher.dispatch(ConversationEvent(ConversationEvent.END_CONVERSATION_EVENT, data))
        elif(input == "2"):
            self.event_dispatcher.dispatch(ConversationEvent(ConversationEvent.END_CONVERSATION_EVENT, data))
        elif(input == "3"):
            self.event_dispatcher.dispatch(ConversationEvent(ConversationEvent.END_CONVERSATION_EVENT, data))
        else:
            self._parse_input()

    def _show_inventory_controls(self):
        print("To select an item press its corresponding number.\nPress 's' to sort your inventory. Press 'i' to close your inventory.")

    def _parse_inventory_input(self, input):
        data = {}
        if(input == "quit" or input == "q"):
            self.event_dispatcher.dispatch(GameEvent(GameEvent.QUIT_EVENT, data))
        elif(input.isdigit() == True):
            data["inventory_position"] = int(input) - 1
            self.event_dispatcher.dispatch(InventoryEvent(InventoryEvent.SELECT_ITEM_IN_INVENTORY_EVENT, data))
        elif(input == "s" or input == "sort"):
            self.event_dispatcher.dispatch(InventoryEvent(InventoryEvent.SORT_INVENTORY_EVENT, data))
        elif(input == "i" or input == "inventory"):
            self.event_dispatcher.dispatch(InventoryEvent(InventoryEvent.CLOSE_INVENTORY_EVENT, data))
        else:
            self._parse_input()

    def _parse_loot_inventory_input(self, input):
        data = {}
        if(input == "quit" or input == "q"):
            self.event_dispatcher.dispatch(GameEvent(GameEvent.QUIT_EVENT, data))
        elif(input.isdigit() == True):
            data["inventory_position"] = int(input) - 1
            self.event_dispatcher.dispatch(InventoryEvent(InventoryEvent.LOOT_ITEM_IN_INVENTORY_EVENT, data))
        elif(input == "i" or input == "close"): # this will be c in the future but for now i is nicer.
            self.event_dispatcher.dispatch(InventoryEvent(InventoryEvent.CLOSE_INVENTORY_EVENT, data))
        else:
            self._parse_input()

    def _parse_loot_inventory_input(self, input):
        data = {}
        if(input == "quit" or input == "q"):
            self.event_dispatcher.dispatch(GameEvent(GameEvent.QUIT_EVENT, data))
        elif(input.isdigit() == True):
            data["inventory_position"] = int(input) - 1
            self.event_dispatcher.dispatch(InventoryEvent(InventoryEvent.LOOT_ITEM_IN_INVENTORY_EVENT, data))
        elif(input == "i"):            self.event_dispatcher.dispatch(InventoryEvent(InventoryEvent.CLOSE_INVENTORY_EVENT, data))
        else:
            self._parse_input()

    def _show_loot_inventory_controls(self):
        print("Select an item you wish to take. Press 'i' to close this event.")

    def _parse_loot_inventory_input(self, input):
        data = {}
        if(input == "quit" or input == "q"):
            self.event_dispatcher.dispatch(GameEvent(GameEvent.QUIT_EVENT, data))
        elif(input.isdigit() == True):
            data["inventory_position"] = int(input) - 1
            self.event_dispatcher.dispatch(InventoryEvent(InventoryEvent.LOOT_ITEM_IN_INVENTORY_EVENT, data))
        elif(input == "i" or input == "close"): # this will be c in the future but for now i is nicer.
            self.event_dispatcher.dispatch(InventoryEvent(InventoryEvent.CLOSE_INVENTORY_EVENT, data))
        else:
            self._parse_input()

    def _show_level_end_controls(self):
        print("Press 'c' to continue to the next level. Press 'q' to quit the game.")

    def _parse_level_end_input(self, input):
        data = {}
        if(input == "quit" or input == "q"):
            self.event_dispatcher.dispatch(GameEvent(GameEvent.QUIT_EVENT, data))
        elif(input == "c" or input == "continue"):
            self.event_dispatcher.dispatch(LevelEvent(LevelEvent.NEXT_LEVEL_EVENT, data))
        else:
            self._parse_input()

    def _handle_game_state_change(self, previous_state, new_state, data):
        pass

    # event handlers

    def _input_parse_event_handler(self, _event):
        self._parse_input()

    def _input_show_controls_event_handler(self, event_name, data):
        self._show_controls()
