#where the map lives.
import time
import game_commands
import map_parser
import monster_module
import game_functions
import game_parser

TL = 9484
BL = 9492
TR = 9488
BR = 9496
HH = 9472
VV = 9474
EE = 8901
PL = 9791
EN = None

map_1 = [
        [TL, HH, HH, HH, HH, HH, HH, HH, HH, HH, HH, TR],
        [VV, EE, EE, EE, EE, EE, EE, EE, EE, EE, EE, VV],
        [VV, EE, EE, EE, EE, EE, EE, EE, EE, EE, EE, VV],
        [VV, EE, EE, EE, EE, EE, EE, EE, EE, EE, EE, VV],
        [VV, EE, EE, EE, TL, HH, HH, TR, EE, EE, EE, VV],
        [VV, EE, EE, EE, VV, EE, EE, EE, EE, EE, EE, VV],
        [VV, EE, EE, EE, VV, EE, EE, VV, EE, EE, EE, VV],
        [VV, EE, EE, EE, BL, HH, HH, BR, EE, EE, EE, VV],
        [VV, EE, EE, EE, EE, EE, EE, EE, EE, EE, EE, VV],
        [VV, EE, EE, EE, EE, EE, EE, EE, EE, EE, EE, VV],
        [VV, EE, EE, EE, EE, EE, EE, EE, EE, EE, EE, VV],
        [BL, HH, HH, HH, HH, HH, HH, HH, HH, HH, HH, BR]
]

user = game_commands.player
#monster = monster_module.monster_generator

goblin = monster_module.npc_goblin
bandit = monster_module.npc_bandit
# rand_monster_selection = monster_module.monster_generator()
# rand_monster = rand_monster_selection

objects = [
    user,
    goblin,
    bandit
]

def npc_coordinates(monster):
    column = monster["column"]
    row = monster["row"]
    return column, row

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

def is_coordinate_passable(map, column, row):
    if(map[row][column] == EE):
        return True
    else:
        return False

def can_player_move_to_coordinate(map, column, row):
    if(is_coordinate_on_map(map, column, row) == False): return False
    if(is_coordinate_passable(map, column, row) == False): return False

    return True

def game_board():
    while(True):
        draw_map(map_1, objects)

        user_input = input("Use the 'k' and 'j' keys to move up and down.\nUse the 'h' and 'l' keys to move left and right.\nType 'quit' or 'q' to quit out of the game.\n")
        user["m_decision"] = map_parser.parse_user_move(user_input)
        if(user["m_decision"] == "quit"): game_commands.quit()
        if(user["m_decision"] == "cont"):
            map_parser.show_controls()
            continue

        new_column, new_row = determine_new_coordinates(map_1, user["m_decision"], user["column"], user["row"])
        can_move = can_player_move_to_coordinate(map_1, new_column, new_row)
        if(can_move == True):
            execute_user_move(user, new_column, new_row)

        npc_location = npc_coordinates(goblin)
        player_location = new_column, new_row
        print(npc_location, player_location)
        trigger = game_functions.battle_trigger(player_location, npc_location)

        if(trigger == True):
            game_functions.battle(game_commands.player, game_commands.monster, game_functions.attack, game_functions.defend, game_parser.parse_player_input, monster_module.enemy_npc_choice, game_commands.quit)
