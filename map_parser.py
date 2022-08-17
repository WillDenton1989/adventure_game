#this is the map parser

def show_controls():
    print(f"""Use the 'k' and 'j' keys to move up and down;
Use the 'h' and 'l' keys to move left and right.
Type 'quit' or 'q' to quit out of the game.""")

def parse_player_move(player_input):
    if(player_input == "k"):
        return "up"
    elif(player_input == "j"):
        return "down"
    elif(player_input == "h"):
        return "left"
    elif(player_input == "l"):
        return "right"
    elif(player_input == "quit" or player_input == "q"):
        return "quit"
    else:
        return "cont"
