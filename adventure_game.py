# constants

from random import randint
import monster_module
import battle_manager
import game_commands
import game_parser
import loot_module
import map_reader
import map_parser
import map
import event_parser
import level_1_characters
import battle_manager

def game_board(player, game_map, objects):
    moves = 0

    while(battle_manager.is_someone_dead(player) == False):
        game_commands.divider()
        map.draw_map(game_map, objects)

        #take and parse player input.
        print(f"Player hit points: {player['hit_points']}")
        print(f"Moves taken: {moves}")
        player_input = input("Use the 'k' and 'j' keys to move up and down.\nUse the 'h' and 'l' keys to move left and right.\nType 'quit' or 'q' to quit out of the game.\n")
        player["m_decision"] = map_parser.parse_player_move(player_input)
        if(player["m_decision"] == "quit"): game_commands.quit()
        if(player["m_decision"] == "inventory"):
            loot_module.display_inventory_screen(loot_module.player_inventory, game_commands.player)
            continue
        if(player["m_decision"] == "cont"):
            map_parser.show_controls()
            continue

        #takes desired direction and checks the coordinates and if valid executes them.
        new_column, new_row = map.determine_new_coordinates(game_map, player["m_decision"], player["column"], player["row"])
        can_move = map.can_player_move_to_coordinate(game_map, new_column, new_row)
        if(can_move == True):
            map.execute_player_move(player, new_column, new_row)
        moves = moves + 1

    if(battle_manager.is_someone_dead(player) == True):
        print(f"\n{player['name']} has perished in the depths of the dungeon, forever lost to its evil...\n")

#game welcome menu
print("Welcome intrepid adventurer! \n\nThis is the Adventure Game!(working title, dont laugh)\n\n")
game_commands.player["name"] = game_commands.player_name()
print(f"\nAlright {game_commands.player['name']}. lets go!")

#map stuffs
dungeon_map = map_reader.build_the_level('level_1', 'data/symbols_dictionary.yaml')# TODO - this should be in adventure.py / owo it is tho
battle_manager.initialize()

game_board(game_commands.player, dungeon_map, map.objects)

#game end
print(f"\n\n{game_commands.player['name']} has finished their Adventure! So far...")
