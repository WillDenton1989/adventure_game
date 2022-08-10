import time
import game_commands
import map_parser

TL = 9484
BL = 9492
TR = 9488
BR = 9496
HH = 9472
VV = 9474
EE = 32
PL = 9791

map_1 = [
        [TL, HH, HH, HH, HH, HH, HH, HH, HH, HH, HH, TR],
        [VV, EE, EE, EE, EE, EE, EE, EE, EE, EE, EE, VV],
        [VV, EE, EE, EE, EE, EE, EE, EE, EE, EE, EE, VV],
        [VV, EE, EE, EE, EE, EE, EE, EE, EE, EE, EE, VV],
        [VV, EE, EE, EE, EE, EE, EE, EE, EE, EE, EE, VV],
        [VV, EE, EE, EE, EE, EE, EE, EE, EE, EE, EE, VV],
        [VV, EE, EE, EE, EE, EE, EE, EE, EE, EE, EE, VV],
        [VV, EE, EE, EE, EE, EE, EE, EE, EE, EE, EE, VV],
        [VV, EE, EE, EE, EE, EE, EE, EE, EE, EE, EE, VV],
        [VV, EE, EE, EE, EE, EE, EE, EE, EE, EE, EE, VV],
        [VV, EE, EE, EE, EE, EE, EE, EE, EE, EE, EE, VV],
        [BL, HH, HH, HH, HH, HH, HH, HH, HH, HH, HH, BR]
]

user = {
    "name": None,
    "decision": None,
    "column": 1,
    "row": 1,
    "symbol": chr(PL)
}

objects = [
    user
]

def object_at_coordinate(objects, column, row):
    for object in objects:
        if(object["column"] == column and object["row"] == row):
            return object
    return None

def draw_map(map, objects):
    col_index = 0
    row_index = 0

    for row in map:
        for column in row:
            object = object_at_coordinate(objects, col_index, row_index)

            if(object == None):
                print(chr(column), end = "")
            else:
                print(object["symbol"], end = "")
            col_index += 1

        print("\r")
        row_index += 1
        col_index = 0

def determine_new_coordinates(map, direction, column, row):
    if(direction == "right"):
        return column + 1, row
    elif(direction == "left"):
        return column - 1, row
    elif(direction == "up"):
        return column, row - 1
    elif(direction == "down"):
        return column, row + 1
    else:
        pass # should blow up here!

def is_coordinate_on_map(map, column, row):
    num_rows = len(map)
    num_columns = len(map[0])
    if(column < 0):
        return False
    if(column >= num_columns):
        return False
    if(row < 0):
        return False
    if(row >= num_rows):
        return False
    return True

def execute_user_move(user, new_column, new_row):
    user["column"] = new_column
    user["row"] = new_row

def is_coordinate_passible(map, column, row):
    if(map[column][row] == HH or map[column][row] == VV):
        return False
    elif(map[column][row] == EE):
        return True

def can_player_move_to_coordinate(map, column, row):
    if(is_coordinate_on_map(map, column, row) == False): return False
    if(is_coordinate_passible(map, column, row) == False): return False

    return True

def game_board():
    while(True):
        draw_map(map_1, objects)

        user_input = input("Use the 'k' and 'j' keys to move up and down.\nUse the 'h' and 'l' keys to move left and right.\n")
        user["decision"] = map_parser.parse_user_move(user_input)
        if(user["decision"] == "quit"): game_commands.quit()
        if(user["decision"] == "cont"):
            map_parser.show_controls()
            continue

        new_column, new_row = determine_new_coordinates(map_1, user["decision"], user["column"], user["row"])
        can_move = can_player_move_to_coordinate(map_1, new_column, new_row)
        if(can_move == True):
            execute_user_move(user, new_column, new_row)
