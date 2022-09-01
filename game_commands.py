#game commands or whatever i shall inevitably change this file to.
import monster_module
import battle_manager
import game_parser

player = {
    "name": None,
    "battle_decision": None,
    "m_decision": None
}

def player_name():
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
    elif player["name"] == "foobar":
        print("Sounds like a foofoo barbar name ngl...")
    else:
        print("\nHeh funny name.")
    return player["name"]

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
