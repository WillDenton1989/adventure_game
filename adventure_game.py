import battle_manager
from player_manager import PlayerManager
import level_manager
import battle_manager
from game_manager import GameManager
import input_manager
# import item_manager

_player = None

def game_board(player):
    moves = 0

    # need to fix this sometime soon. tis leaky
    # we really really really really really need to fix this loop soon.
    # i know i gave a little push back at first but now its bothering me.
    # add one check everytime this leaks. # of times: |||||, ||||
    while(battle_manager.is_someone_dead(player) == False):

        print("------------------------------------------------------------------------")
        level_manager.draw_map()

        # ghetto hud for now.
        print(f"{player['name']} hit points: {player['hit_points']}")
        print(f"Moves taken: {moves}")
        print(GameManager._game_state)

        input_manager.parse_input()

        moves = moves + 1

    if(battle_manager.is_someone_dead(player) == True):
        print(f"\n{player['name']} has perished in the depths of the dungeon, forever lost to its evil...\n")

def game_intro_message():
    print("\nWelcome intrepid adventurer! \n\nThis is the Adventure Game!(working title, dont laugh)\n\n")

# the cool running

game_intro_message()

# game_manager.initialize()
GameManager()

_player = GameManager._player_manager.get_player_data

game_board(_player)

# is this the end?
