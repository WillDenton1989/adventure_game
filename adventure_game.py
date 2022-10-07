#!python3

import event_manager
from managers.game_manager import GameManager
from models.state import State

def game_board(game_manager):
    moves = 0
    player = None
    battle_manager = game_manager.battle_manager

    while(battle_manager.is_someone_dead(player := game_manager.player) == False):
        if(game_manager.game_state == State.STATE_MOVEMENT):
            print("------------------------------------------------------------------------")
            event_manager.trigger_event(event_manager.DRAW_LEVEL_EVENT, {})

            # ghetto hud for now.
            print(f"{player.name} hit points: {player.hit_points}")
            print(f"Moves taken: {moves}")
            print(f"STATE:  {game_manager.game_state}")

            event_manager.trigger_event(event_manager.INPUT_PARSE_EVENT, {})

            moves = moves + 1

    if(battle_manager.is_someone_dead(player) == True):
        print(f"\n{player.name} has perished in the depths of the dungeon, forever lost to its evil...\n")

def game_intro_message():
    print("\nWelcome intrepid adventurer! \n\nThis is the Adventure Game!(working title, dont laugh)\n\n")

# the cool running

game_intro_message()

_game_manager = GameManager()

game_board(_game_manager)

# is this the end?
