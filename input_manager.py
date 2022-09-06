import game_manager
import event_manager

# public methods
def initialize():
    event_manager.listen(event_manager.STATE_CHANGE_EVENT, _state_change_event_handler)

def show_controls():
    if(game_manager.game_state == game_manager.STATE_CHARACTER_CREATION):
        _show_player_creation_controls()
    elif(game_manager.game_state == game_manager.STATE_MOVEMENT):
        _show_movement_controls()
    elif(game_manager.game_state == game_manager.STATE_BATTLE):
        _show_battle_controls()
    else:
        pass

def parse_input(input):
    if(game_manager.game_state() == game_manager.STATE_CHARACTER_CREATION):
        return _parse_player_creation(input)
    elif(game_manager.game_state() == game_manager.STATE_MOVEMENT):
        return _parse_player_movement(input)
    elif(game_manager.game_state() == game_manager.STATE_BATTLE):
        return _parse_battle_input(input)
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

# private methods

def _show_movement_controls():
    print(f"""Use the 'k' and 'j' keys to move up and down;
Use the 'h' and 'l' keys to move left and right.
Type 'quit' or 'q' to quit out of the game.""")

def _parse_player_movement(input):
    if(input == "k"):
        return "up"
    elif(input == "j"):
        return "down"
    elif(input == "h"):
        return "left"
    elif(input == "l"):
        return "right"
    elif(input == "i"):
        return "inventory"
    elif(input == "quit" or input == "q"):
        return "quit"
    else:
        return "cont"

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
