import battle_manager
import player_manager
import level_manager
import battle_manager
import game_manager
import input_manager

def game_board(player):
    moves = 0

    # need to fix this sometime soon. tis leaky
    # we really really really really really need to fix this loop now.
    # i know i gave a little push back but now it bothers me. 
    while(battle_manager.is_someone_dead(player) == False):
        print("------------------------------------------------------------------------")
        level_manager.draw_map()

        # ghetto hud for now.
        # print(level_manager._events
        print(f"{player['name']} hit points: {player['hit_points']}")
        print(f"Moves taken: {moves}")
        print(game_manager._game_state)

        input_manager.parse_input()

        moves = moves + 1

    if(battle_manager.is_someone_dead(player) == True):
        print(f"\n{player['name']} has perished in the depths of the dungeon, forever lost to its evil...\n")

def game_intro_message():
    print("\nWelcome intrepid adventurer! \n\nThis is the Adventure Game!(working title, dont laugh)\n\n")

# the cool running

game_intro_message()

game_manager.initialize()
game_board(player_manager.get_player_data())

# is this the end?
