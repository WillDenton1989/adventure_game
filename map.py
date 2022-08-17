#where the map lives.
import time
import game_commands
import map_parser
import monster_module
import game_functions
import game_parser
import loot_module

TL = 9484
BL = 9492
TR = 9488
BR = 9496
HH = 9472
VV = 9474
EE = 8901
PL = 9791
EN = 7777

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
    game_commands.finish_line,
    monster_module.npc_goblin,
    monster_module.npc_bandit,
    monster_module.npc_dwarf,
    loot_module.loot_chest
]

def npc_coordinates(npc):
    column = npc["column"]
    row = npc["row"]
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

#is this the end?
