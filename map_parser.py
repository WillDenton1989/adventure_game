#this is the map parser

def show_controls():
    print("""Use the 'k' and 'j' keys to move up and down;
Use the 'h' and 'l' keys to move left and right.""")

def parse_user_move(user_input):
    if(user_input == "k"):
        return "up"
    elif(user_input == "j"):
        return "down"
    elif(user_input == "h"):
        return "left"
    elif(user_input == "l"):
        return "right"
    elif(user_input == "quit" or user_input == "q"):
        return "quit"
    else:
        return "cont"
