#constants

from random import randint
import parser

player = {
    "name": None,
    "hit_points": 9,
    "attack_power": 5,
    "defense": 1,
    "defense_scalar": 1,
    "decision": None
    }

monster = {
    "name": "Orc",
    "hit_points": 8,
    "attack_power": 5,
    "defense": 1,
    "defense_scalar": .5,
    "decision": None
    }

round = -1

# game commands

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
    else:
        print("\nHeh funny name.")
    return player["name"]

def quit():
    print(f"You are a pussy ass bitch")
    print(f"Farewell {player['name']}")
    exit()

def round_counter(round):
    return round + 1

def enemy_npc_choice():
    x = randint(1, 10)
    if(x <= 7):
        return "attack"
    else:
        return "defend"

#game functions

def is_someone_dead(player, monster,):
    if(monster["hit_points"] <= 0):
        print(f"\n{player['name']} has slain the beast!")
        return True
    elif(player["hit_points"] <= 0):
        print(f"\n{player['name']} has been slain by the beast!")
        return True
    else:
        return False

def defend(original_defense, defense_scalar):
    new_defense = original_defense + defense_scalar
    if(new_defense == 4):
        return original_defense
    else:
        return new_defense

def attack(attack_power, hit_points, defense):
    attack_roll = randint(1, attack_power)
    attack_value =  max(0, attack_roll - defense)
    return hit_points - attack_value

# Main
print("Welcome intrepid adventurer! \n\nThis is the Adventure Game!(working title, dont laugh)\n\n")
player["name"] = user_name()
#future return point
print(f"\nAlright {player['name']}. lets go!")
print(f"\n{player['name']} is fighting a monsterous {monster['name']}")
parser.show_controls()

#battle start
while(is_someone_dead(player, monster,) == False):
    round = round_counter(round)

    print(f"\n\nRound {round}: {monster['name']} - {monster['hit_points']}, {player['name']} - {player['hit_points']}")
    print(f"\nplayer defense: {player['defense']}, enemy defense {monster['defense']}")

    # 1) player input
    player_input_string = input(f"I await your command {player['name']}: ")
    player["decision"] = parser.parse_player_input(player_input_string)

    # 2) gather monster input
    monster["decision"] = enemy_npc_choice()

    # 3) execute defends
    if(player["decision"] == "defend"):
        player["defense"] = defend(player["defense"], player["defense_scalar"])

    if(monster["decision"] == "defend"):
        monster["defense"] = defend(monster["defense"], monster["defense_scalar"])

    # 4) execute attacks
    if(player["decision"] == "attack"):
        monster["hit_points"] = attack(player["attack_power"], monster["hit_points"], monster["defense"])

    if(monster["decision"] == "attack"):
        player["hit_points"] = attack(monster["attack_power"], player["hit_points"], player["defense"])

    # 5) quit out
    if(player["decision"] == "quit"):
        quit()

    print(f"\n{player['name']} chooses {player['decision']}, The {monster['name']} choses to {monster['decision']}")

print(f"\n\n{player['name']} has finished their Adventure! So far...")
