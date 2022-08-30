#constants

from random import randint
import monster_module
import game_functions
import game_commands
import game_parser
import loot_module
import map_reader
import map_parser
import map

def game_board(player, game_map, objects):
    moves = 0

    map.load_character_locations('data/player_data.yaml', 'data/npc_data.yaml')

    while(game_functions.is_someone_dead(player) == False):
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

        #sets the coordinate of various characters on the map.
        player_location = new_column, new_row
        goblin_location = map.npc_coordinates(monster_module.npc_goblin)
        goblin_two_location = map.npc_coordinates(monster_module.npc_goblin_two)
        bandit_location = map.npc_coordinates(monster_module.npc_bandit)
        chest_location = map.npc_coordinates(loot_module.loot_chest)
        finish_line_location = map.npc_coordinates(game_commands.finish_line)

        #booleans for if the player occupies the same coordinate as another character. maybe turn this into a list?
        goblin_trigger = game_functions.event_trigger(player_location, goblin_location)
        goblin_two_trigger = game_functions.event_trigger(player_location, goblin_two_location)
        bandit_trigger = game_functions.event_trigger(player_location, bandit_location)
        chest_trigger = game_functions.event_trigger(player_location, chest_location)
        finish_line_trigger = game_functions.event_trigger(player_location, finish_line_location)

        if(goblin_trigger == True):
            game_functions.battle(game_commands.player, monster_module.npc_goblin, game_functions.attack, game_functions.defend, game_parser.parse_player_input, monster_module.enemy_npc_choice, game_commands.quit)
        if(goblin_two_trigger == True):
            game_functions.battle(game_commands.player, monster_module.npc_goblin_two, game_functions.attack, game_functions.defend, game_parser.parse_player_input, monster_module.enemy_npc_choice, game_commands.quit)
        if(bandit_trigger == True):
            game_functions.battle(game_commands.player, monster_module.npc_bandit, game_functions.attack, game_functions.defend, game_parser.parse_player_input, monster_module.enemy_npc_choice, game_commands.quit)
        if(chest_trigger == True):
            print("\nGreat chest ahead. Sadly there is no loot here.\n") #run chest screen here

        if(finish_line_trigger == True):
            print(f"\nCongratulations {game_commands.player['name']}!\nIt took you {moves} moves to escape the bleak and terrible dungeon!\n")
            break

    if(game_functions.is_someone_dead(player) == True):
        print(f"\n{player['name']} has perished in the depths of the dungeon, forever lost to its evil...\n")

#game welcome menu
print("Welcome intrepid adventurer! \n\nThis is the Adventure Game!(working title, dont laugh)\n\n")
game_commands.player["name"] = game_commands.player_name()
print(f"\nAlright {game_commands.player['name']}. lets go!")

#map stuffs
game_board(game_commands.player, map_reader.dungeon_map, map.objects)

#game end
print(f"\n\n{game_commands.player['name']} has finished their Adventure! So far...")
