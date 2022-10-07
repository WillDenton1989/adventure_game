#!python3

from managers.game_manager import GameManager
from models.events.level_event import LevelEvent
from models.events.input_event import InputEvent
from models.state import State

def game_board(game_manager):
    moves = 0
    player = None
    battle_manager = game_manager.battle_manager

    while(battle_manager.is_someone_dead(player := game_manager.player) == False):
        if(game_manager.game_state == State.STATE_MOVEMENT):
            print("------------------------------------------------------------------------")
            game_manager.event_dispatcher.dispatch(LevelEvent(LevelEvent.DRAW_LEVEL_EVENT, {}))

            # ghetto hud for now.
            print(f"{player.name} hit points: {player.hit_points}")
            print(f"Moves taken: {moves}")
            print(f"STATE:  {game_manager.game_state}")

            game_manager.event_dispatcher.dispatch(InputEvent(InputEvent.INPUT_PARSE_EVENT, {}))

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
