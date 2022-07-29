#parser.

def show_controls():
    print("""\nType 'attack' or 'a' to try to damage your foe;
Type 'defend' or 'd' to try to defend against an attack;
Type 'quit' or 'q' to exit the adventure game.\n""")

def parse_player_input(player_input_string):
    if(player_input_string == "quit" or player_input_string == "q"):
        return "quit"
    elif(player_input_string == "attack" or player_input_string == "a"):
        return "attack"
    elif(player_input_string == "defend" or player_input_string == "d"):
        return "defend"
    else:
        show_controls()
