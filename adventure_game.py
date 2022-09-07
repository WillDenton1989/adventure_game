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

        #take and parse player input.
        print(f"Player hit points: {player['hit_points']}")
        print(f"Moves taken: {moves}")
        # player_input = input("Use the 'k' and 'j' keys to move up and down.\nUse the 'h' and 'l' keys to move left and right.\nType 'quit' or 'q' to quit out of the game.\n")
        input_manager.parse_input()

    if(battle_manager.is_someone_dead(player) == True):
        print(f"\n{player['name']} has perished in the depths of the dungeon, forever lost to its evil...\n")

#game welcome menu
print("Welcome intrepid adventurer! \n\nThis is the Adventure Game!(working title, dont laugh)\n\n")

game_manager.initialize()

game_board(player_manager.player)

#game end
print(f"\n\n{player_manager.player['name']} has finished their Adventure! So far...")
