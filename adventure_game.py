#constants

from random import randint
import game_parser
import monster_module
import game_functions
import game_commands
import map_parser
import map

#game welcome menu
print("Welcome intrepid adventurer! \n\nThis is the Adventure Game!(working title, dont laugh)\n\n")
game_commands.player["name"] = game_commands.user_name()
print(f"\nAlright {game_commands.player['name']}. lets go!")

#map stuffs
map.game_board()

#battle start

#game end
print(f"\n\n{game_commands.player['name']} has finished their Adventure! So far...")
