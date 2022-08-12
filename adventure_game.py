#constants

from random import randint
import game_parser
import monster_module
import game_functions
import game_commands
import map_parser
import map

def game_board(player, game_map, objects):
    while(game_functions.is_player_dead(player) == False):
        map.draw_map(game_map, objects)

        player_input = input("Use the 'k' and 'j' keys to move up and down.\nUse the 'h' and 'l' keys to move left and right.\nType 'quit' or 'q' to quit out of the game.\n")
        player["m_decision"] = map_parser.parse_player_move(player_input)
        if(player["m_decision"] == "quit"): game_commands.quit()
        if(player["m_decision"] == "cont"):
            map_parser.show_controls()
            continue

        new_column, new_row = map.determine_new_coordinates(game_map, player["m_decision"], player["column"], player["row"])
        can_move = map.can_player_move_to_coordinate(game_map, new_column, new_row)
        if(can_move == True):
            map.execute_player_move(player, new_column, new_row)

        goblin_location = map.npc_coordinates(monster_module.npc_goblin)
        bandit_location = map.npc_coordinates(monster_module.npc_bandit)

        player_location = new_column, new_row

        print(goblin_location, player_location)
        goblin_trigger = game_functions.battle_trigger(player_location, goblin_location)
        bandit_trigger = game_functions.battle_trigger(player_location, bandit_location)

        if(goblin_trigger == True):
            game_functions.battle(game_commands.player, monster_module.npc_goblin, game_functions.attack, game_functions.defend, game_parser.parse_player_input, monster_module.enemy_npc_choice, game_commands.quit)
        if(bandit_trigger == True):
            game_functions.battle(game_commands.player, monster_module.npc_bandit, game_functions.attack, game_functions.defend, game_parser.parse_player_input, monster_module.enemy_npc_choice, game_commands.quit)

    print(f"\n{game_commands.player['name']} has perished in the depths of the dungeon, forever lost to its evil...\n")


#game welcome menu
print("Welcome intrepid adventurer! \n\nThis is the Adventure Game!(working title, dont laugh)\n\n")
game_commands.player["name"] = game_commands.player_name()
print(f"\nAlright {game_commands.player['name']}. lets go!")

#map stuffs
game_board(game_commands.player, map.map_1, map.objects)

#battle start

#game end
print(f"\n\n{game_commands.player['name']} has finished their Adventure! So far...")
