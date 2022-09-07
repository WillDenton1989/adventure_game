# constants
from random import randint
import monster_module
import battle_manager
import player_manager
import loot_module
import level_parser
import level_manager
import level_1_characters
import battle_manager
import game_manager
import input_manager

def game_board(player):
    moves = 0

    while(battle_manager.is_someone_dead(player) == False):
        player_manager.divider()
        level_manager.draw_map()

        #take and parse player input.
        print(f"Player hit points: {player['hit_points']}")
        print(f"Moves taken: {moves}")
        player_input = input("Use the 'k' and 'j' keys to move up and down.\nUse the 'h' and 'l' keys to move left and right.\nType 'quit' or 'q' to quit out of the game.\n")
        player["m_decision"] = input_manager.parse_input(player_input)
        if(player["m_decision"] == "quit"): player_manager.quit()
        if(player["m_decision"] == "inventory"):
            loot_module.display_inventory_screen(loot_module.player_inventory, player_manager.player)
            continue
        if(player["m_decision"] == "cont"):
            input_manager.show_controls()
            continue

    if(battle_manager.is_someone_dead(player) == True):
        print(f"\n{player['name']} has perished in the depths of the dungeon, forever lost to its evil...\n")

#game welcome menu
print("Welcome intrepid adventurer! \n\nThis is the Adventure Game!(working title, dont laugh)\n\n")

game_manager.initialize()

game_board(player_manager.player)

#game end
print(f"\n\n{player_manager.player['name']} has finished their Adventure! So far...")
