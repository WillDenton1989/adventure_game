#constants

from random import randint
import parser
import monster_module
import game_functions
import game_commands

#game welcome menu
print("Welcome intrepid adventurer! \n\nThis is the Adventure Game!(working title, dont laugh)\n\n")
game_commands.player["name"] = game_commands.user_name()
#battle start
game_functions.battle(game_commands.player, game_commands.monster, game_functions.attack, game_functions.defend, parser.parse_player_input, monster_module.enemy_npc_choice, quit)
#Continue menu loop
while(game_functions.is_someone_dead(game_commands.player, game_commands.monster) == True):
    game_commands.continue_menu(game_commands.player, game_commands.monster)
#game end
print(f"\n\n{game_commands.player['name']} has finished their Adventure! So far...")
