#player manager
import battle_manager
import input_manager
import game_manager

player = {
    "name": None,
    "battle_decision": None,
    "m_decision": None
}

def initialize():
    pass

def create_player(player):
    input_manager.show_controls()
    #player_name(player)
    input_manager.parse_input(player_name(player))


def player_name(player):
    player["name"] = input().strip()
    print(f"\nAlright {player['name']}, lets go!")

def continue_menu():
    pass

def quit():
    print(f"Farewell {player['name']}")
    exit()

def game_end():
    print(f"\n\n{player['name']} has finished their Adventure! So far...")
    exit()

def divider():
    print("------------------------------------------------------------------------")
