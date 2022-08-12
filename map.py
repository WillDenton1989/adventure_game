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

objects = [
    game_commands.player,
    monster_module.npc_goblin,
    monster_module.npc_bandit
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
        pass

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

def execute_player_move(player, new_column, new_row):
    player["column"] = new_column
    player["row"] = new_row

def is_coordinate_passable(map, column, row):
    if(map[row][column] == EE):
        return True
    else:
        return False

def can_player_move_to_coordinate(map, column, row):
    if(is_coordinate_on_map(map, column, row) == False): return False
    if(is_coordinate_passable(map, column, row) == False): return False

    return True

# def game_board(player):
#     while(game_functions.is_player_dead(player) == False):
#         draw_map(map_1, objects)
#
#         player_input = input("Use the 'k' and 'j' keys to move up and down.\nUse the 'h' and 'l' keys to move left and right.\nType 'quit' or 'q' to quit out of the game.\n")
#         player["m_decision"] = map_parser.parse_player_move(player_input)
#         if(player["m_decision"] == "quit"): game_commands.quit()
#         if(player["m_decision"] == "cont"):
#             map_parser.show_controls()
#             continue
#
#         new_column, new_row = determine_new_coordinates(map_1, player["m_decision"], player["column"], player["row"])
#         can_move = can_player_move_to_coordinate(map_1, new_column, new_row)
#         if(can_move == True):
#             execute_player_move(player, new_column, new_row)
#
#         goblin_location = npc_coordinates(goblin)
#         bandit_location = npc_coordinates(bandit)
#
#         player_location = new_column, new_row
#         print(goblin_location, player_location)
#         goblin_trigger = game_functions.battle_trigger(player_location, goblin_location)
#         bandit_trigger = game_functions.battle_trigger(player_location, bandit_location)
#
#         if(goblin_trigger == True):
#             game_functions.battle(game_commands.player, goblin, game_functions.attack, game_functions.defend, game_parser.parse_player_input, monster_module.enemy_npc_choice, game_commands.quit)
#         if(bandit_trigger == True):
#             game_functions.battle(game_commands.player, bandit, game_functions.attack, game_functions.defend, game_parser.parse_player_input, monster_module.enemy_npc_choice, game_commands.quit)
#
#     print(f"\n{game_commands.player['name']} has perished in the depths of the dungeon, forever lost to its evil...\n")

#is this the end?
