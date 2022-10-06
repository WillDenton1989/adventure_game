#!python3

import battle_manager
import level_manager
import battle_manager
from game_manager import GameManager
import input_manager
from models.state import State

_player = None

def game_board(player, game_manager):
    moves = 0

    while(battle_manager.is_someone_dead(player) == False):

        if(game_manager.game_state == State.STATE_MOVEMENT):
            print("------------------------------------------------------------------------")
            level_manager.draw_level()

            # ghetto hud for now.
            print(f"{player.name} hit points: {player.hit_points}")
            print(f"Moves taken: {moves}")
            print(f"STATE:  {game_manager.game_state}")

            input_manager.parse_input()

            moves = moves + 1

    if(battle_manager.is_someone_dead(player) == True):
        print(f"\n{player.name} has perished in the depths of the dungeon, forever lost to its evil...\n")

def game_intro_message():
    print("\nWelcome intrepid adventurer! \n\nThis is the Adventure Game!(working title, dont laugh)\n\n")

# the cool running

game_intro_message()

_game_manager = GameManager()
_player = _game_manager.player

game_board(_player, _game_manager)

# is this the end?
