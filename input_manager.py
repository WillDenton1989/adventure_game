import game_manager
import event_manager
import player_manager

# public methods
def initialize():
    event_manager.listen(event_manager.STATE_CHANGE_EVENT, _state_change_event_handler)

def show_controls():
    if(_game_state() == game_manager.STATE_CHARACTER_CREATION):
        _show_player_creation_controls()
    elif(_game_state() == game_manager.STATE_MOVEMENT):
        _show_movement_controls()
    elif(_game_state() == game_manager.STATE_BATTLE):
        _show_battle_controls()
    else:
        pass

def parse_input():
    show_controls()
    player_input = input(_prompt())

    if(_game_state() == game_manager.STATE_CHARACTER_CREATION):
        return _parse_player_creation(player_input)
    elif(_game_state() == game_manager.STATE_MOVEMENT):
        return _parse_player_movement(player_input)
    elif(_game_state() == game_manager.STATE_BATTLE):
        return _parse_battle_input(player_input)
    else:
        pass

# private methods
def _show_player_creation_controls():
    print("Type in your name and your adventure shall begin!\n")

def _parse_player_creation(input):
    if(input == "dood"):
        print("stuff")
    else:
        pass

    return input

def _prompt():
    if(_game_state() == game_manager.STATE_CHARACTER_CREATION):
        return "A name, liege? "
    elif(_game_state() == game_manager.STATE_MOVEMENT):
        return "? "
    elif(_game_state() == game_manager.STATE_BATTLE):
        return f"\nI await a real command {player_manager.player['name']}: "
    else:
        return "THIS IS BROKEN AND SHOULD NEVER HAPPEN, RAISE AN EXCEPTION HERE!!"

def _game_state():
    return game_manager.game_state()

# private methods

def _show_movement_controls():
    print(f"""Use the 'k' and 'j' keys to move up and down;
Use the 'h' and 'l' keys to move left and right.
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
    elif(input == "i"):
        pass
    elif(input == "quit" or input == "q"):
        event_manager.trigger_event(event_manager.QUIT_EVENT, data)
    else:
        show_controls()

def _show_battle_controls():
    print("""\nType 'attack' or 'a' to try to damage your foe;
Type 'defend' or 'd' to increase your defense rating (max 3);
Type 'quit' or 'q' to exit the adventure game.""")

def _parse_battle_input(input): #changed from parse_battle_input
    if(input == "quit" or input == "q"):
        return "quit"
    elif(input == "attack" or input == "a"):
        return "attack"
    elif(input == "defend" or input == "d"):
        return "defend"
    elif(input == "inventory" or input == "i"):
        return "inventory"
    else:
        return "cont"

def _parse_inventory_input(input):
    if(input == "1"):
        pass
    elif(input == "2"):
        pass
    elif(input == "3"):
        pass
    elif(input == "4"):
        pass
    elif(input == "5"):
        pass
    else:
        pass

# event handlers

def _state_change_event_handler(event, data):
    print(f"GOT HERE: {data}")
