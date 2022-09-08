import battle_manager
import player_manager
import level_manager
import battle_manager
import game_manager
import input_manager

def game_board(player):
    moves = 0

    while(battle_manager.is_someone_dead(player) == False):
        print("------------------------------------------------------------------------")
        level_manager.draw_map()

        # ghetto hud for now.
        print(f"{player['name']} hit points: {player['hit_points']}")
        print(f"Moves taken: {moves}")
        print(game_manager._game_state)

        input_manager.parse_input()

        moves = moves + 1

    if(battle_manager.is_someone_dead(player) == True):
        print(f"\n{player['name']} has perished in the depths of the dungeon, forever lost to its evil...\n")

def game_intro_message():
    print("\nWelcome intrepid adventurer! \n\nThis is the Adventure Game!(working title, dont laugh)\n\n")

def game_over_message():
    player_data = player_manager.get_player_data()
    print(f"\n\n{player_data['name']} has finished their Adventure! So far...")

# the cool running

game_intro_message()

game_manager.initialize()
game_board(player_manager.get_player_data())

game_over_message()

# is this the end?
