#this is the map parser

def show_controls():
    print("""Use the 'w' and 's' keys to move up and down;
Use the 'a' and 'd' keys to move left and right.""")

def parse_user_move(user_input):
    if(user_input == "w"):
        return "up"
    elif(user_input == "s"):
        return "down"
    elif(user_input == "a"):
        return "left"
    elif(user_input == "d"):
        return "right"
    elif(user_input == "quit" or user_input == "q"):
        return "quit"
    else:
        return "cont"
