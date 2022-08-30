#game_parser.

def show_controls():
    print("""\nType 'attack' or 'a' to try to damage your foe;
Type 'defend' or 'd' to increase your defense rating (max 3);
Type 'quit' or 'q' to exit the adventure game.""")

def parse_player_input(player_input_string):
    if(player_input_string == "quit" or player_input_string == "q"):
        return "quit"
    elif(player_input_string == "attack" or player_input_string == "a"):
        return "attack"
    elif(player_input_string == "defend" or player_input_string == "d"):
        return "defend"
    elif(player_input_string == "inventory" or player_input_string == "i"):
        return "inventory"
    else:
        return "cont"

def parse_inventory_input():
    if(inventory_input == "1"):
        pass
    elif(inventory_input == "2"):
        pass
    elif(inventory_input == "3"):
        pass
    elif(inventory_input == "4"):
        pass
    elif(inventory_input == "5"):
        pass
    else:
        pass


def parse_continue_menu():
    player_cont_input = input(f"Do you wish to continue battling monsters {player['name']}?\nYes/No\n")
    if(player_cont_input == "yes" or player_cont_input == "Yes" or player_cont_input == "y"):
        return "yes"
    elif(player_cont_input == "no" or player_cont_input == "No" or player_cont_input == "n"):
        return "no"
    else:
        return "cont"
