from game_manager import GameManager
import event_manager
from player_manager import PlayerManager

_game_manager = None

# public methods

def initialize(game_manager):
    global _game_manager

    _game_manager = game_manager

def show_controls():
    if(_game_state() == GameManager.STATE_CHARACTER_CREATION):
        _show_player_creation_controls()
    elif(_game_state() == GameManager.STATE_MOVEMENT):
        _show_movement_controls()
    elif(_game_state() == GameManager.STATE_BATTLE):
        _show_battle_controls()
    elif(_game_state() == GameManager.STATE_CONVERSATION):
        _show_conversation_controls()
    elif(_game_state() == GameManager.STATE_INVENTORY):
        _show_inventory_controls()
    else:
        raise Exception("cannot show controls for your current game state.")

def parse_input():
    show_controls()
    player_input = input(_prompt()).strip()

    if(_game_state() == GameManager.STATE_CHARACTER_CREATION):
        return _parse_player_creation(player_input)
    elif(_game_state() == GameManager.STATE_MOVEMENT):
        return _parse_player_movement(player_input)
    elif(_game_state() == GameManager.STATE_BATTLE):
        return _parse_battle_input(player_input)
    elif(_game_state() == GameManager.STATE_CONVERSATION):
        return _parse_conversation_input(player_input)
    elif(_game_state() == GameManager.STATE_INVENTORY):
        return _parse_inventory_input(player_input)
    else:
        raise Exception("cannot parse input for your current game state.")

# private methods

def _game_state():
    global _game_manager
    return _game_manager.game_state

def _player_data():
    global _game_manager
    return _game_manager.get_player_manager().player

def _show_player_creation_controls():
    print("Type in your name and your adventure shall begin!\n")

def _parse_player_creation(input):
    if(input == "dood"):
        print(f"\nSup {input}.\n\nAlright then, lets go!\n")
    else:
        print(f"\nAlright {input}, lets go!\n")

    return input

def _prompt():
    if(_game_state() == GameManager.STATE_CHARACTER_CREATION):
        return "A name, liege? "
    elif(_game_state() == GameManager.STATE_MOVEMENT):
        return "? "
    elif(_game_state() == GameManager.STATE_BATTLE):
        player = _player_data()
        return f"\nI await your command {player.name}: "
    elif(_game_state() == GameManager.STATE_CONVERSATION):
        return "What is your response? "
    elif(_game_state() == GameManager.STATE_INVENTORY):
        return "Select the item you wish to use, dude. "
    else:
        raise Exception("there is no prompt for your current game state.")

def _show_movement_controls():
    print(f"""Use the 'k' and 'j' keys to move up and down;
Use the 'h' and 'l' keys to move left and right.
Type 'inventory' or 'i' to open the inventory screen.
Type 'quit' or 'q' to quit out of the game.""")

def _parse_player_movement(input):
    data = {}

    if(input == "k"):
        data["direction"] = "up"
        event_manager.trigger_event(event_manager.MOVEMENT_EVENT, data)
    elif(input == "j"):
        data["direction"] = "down"
        event_manager.trigger_event(event_manager.MOVEMENT_EVENT, data)
    elif(input == "h"):
        data["direction"] = "left"
        event_manager.trigger_event(event_manager.MOVEMENT_EVENT, data)
    elif(input == "l"):
        data["direction"] = "right"
        event_manager.trigger_event(event_manager.MOVEMENT_EVENT, data)
    elif(input == "inventory" or input == "i"):
        event_manager.trigger_event(event_manager.OPEN_INVENTORY_EVENT, data)
    elif(input == "quit" or input == "q"):
        event_manager.trigger_event(event_manager.QUIT_EVENT, data)
    else:
        show_controls()

def _show_battle_controls():
    print("""\nType 'attack' or 'a' to try to damage your foe;
Type 'defend' or 'd' to increase your defense rating (max 3);
Type 'quit' or 'q' to exit the adventure game.""")

def _parse_battle_input(input):
    data = {}
    if(input == "quit" or input == "q"):
        event_manager.trigger_event(event_manager.QUIT_EVENT, data)
    elif(input == "attack" or input == "a"):
        data["command"] = "attack"
        event_manager.trigger_event(event_manager.BATTLE_COMMAND_EVENT, data)
    elif(input == "defend" or input == "d"):
        data["command"] = "defend"
        event_manager.trigger_event(event_manager.BATTLE_COMMAND_EVENT, data)
    else:
        show_controls()

def _show_conversation_controls():
    print("Use the numbers 1 - 3 to reply")

def _parse_conversation_input(input):
    data = {}
    if(input == "quit" or input == "q"):
        event_manager.trigger_event(event_manager.QUIT_EVENT, data)
    elif(input == "1"):
        pass
    elif(input == "2"):
        pass
    elif(input == "3"):
        event_manager.trigger_event(event_manager.END_CONVERSATION_EVENT, data)
    else:
        pass

def _show_inventory_controls():
    print("Press 'i' to close your inventory.")

def _parse_inventory_input(input):
    data = {}
    if(input == "quit" or input == "q"):
        event_manager.trigger_event(event_manager.QUIT_EVENT, data)
    elif(input.isdigit() == True):
        data["choice"] = int(input) - 1
        event_manager.trigger_event(event_manager.SELECT_ITEM_IN_INVENTORY_EVENT, data)
    elif(input == "i"):
        event_manager.trigger_event(event_manager.CLOSE_INVENTORY_EVENT, data)
    else:
        parse_input()

# event handlers
