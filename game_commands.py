#game commands or whatever i shall inevitably change this file to.
import monster_module
import game_functions
import game_parser

player = {
    "name": None,
    "hit_points": 10,
    "attack_power": 5,
    "defense": 1,
    "defense_scalar": 1,
    "battle_decision": None
    }

monster = monster_module.monster_generator()

def user_name():
    player["name"] = input("So tell me your name and your adventure shall begin!\n").strip()

    if player["name"] == "quit":
        exit()
    elif player["name"] == "Bill":
        print("\nWhats up homie :D")
    elif player["name"] == "Mike":
        print("\nThe master returns!")
    elif player["name"] == "Scott":
        print("\nIt's you! great...")
    elif player["name"] == "Gary":
        print("\nOwO it's Gary! UwU xD")
    elif player["name"] == "motherfucker":
        print("\nWhat aint no country i ever heard of. they speak english in what?")
    elif player["name"] == "boobs":
        print("\nMmmmmmm Boobs")
    elif player["name"] == "dood":
        print("\nSup dood :)")
    elif player["name"] == "dad":
        print("Oh no. I hope you dont encounter... him...")
    else:
        print("\nHeh funny name.")
    return player["name"]

def continue_menu(player, monster):
    player_input_string = input(f"Do you wish to continue battling monsters {player['name']}?\nyes/no\n")
    if(player_input_string == "yes" or player_input_string == "y"):
        monster = monster_module.monster_generator()
        player.update({"hit_points": 10})
        player.update({"defense": 1})
        return game_functions.battle(player, monster, game_functions.attack, game_functions.defend, game_parser.parse_player_input, monster_module.enemy_npc_choice, quit)
    elif(player_input_string == "no" or player_input_string == "n"):
        return game_end()
    else:
        return continue_menu(player, monster)

def quit():
    print(f"Farewell {player['name']}")
    exit()

def game_end():
    print(f"\n\n{player['name']} has finished their Adventure! So far...")
    exit()

def dad_fred_paradox(player, monster):
    if(player["name"] == "dad" and monster["name"] == "Bandit Fred the Dadfucker"):
        monster["attack_power"] = 10
