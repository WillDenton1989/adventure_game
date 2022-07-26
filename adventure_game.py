#constants

from random import randint
import parser

player = {
    "name": None,
    "hit_points": 9,
    "attack_power": 5,
    "defense": 1,
    "decision": None
    }

monster = {
    "hit_points": 8,
    "attack_power": 5,
    "defense": 1,
    "decision": None
    }

name = None
round = -1

# game commands

def user_name():
    name = input("So tell me your name and your adventure shall begin!\n").strip()

    if name == "quit":
        exit()
    elif name == "Bill":
        print("\nWhats up homie :D")
    elif name == "Mike":
        print("\nThe master returns!")
    elif name == "Scott":
        print("\nIt's you! great...")
    elif name == "Gary":
        print("\nOwO it's Gary! UwU xD")
    elif name == "motherfucker":
        print("\nWhat aint no country i ever heard of. they speak english in what?")
    elif name == "boobs":
        print("\nMmmmmmm those are nice")
    else:
        print("\nHeh funny name.")
    return name

def quit():
    print(f"You are a pussy ass bitch")
    print(f"Farewell {name}")
    exit()

def round_counter(round):
    return round + 1

def monsters_choice():
    x = randint(1, 10)
    if(x <= 6):
        return "attack"
    else:
        return "defend"

#game functions

def is_someone_dead(player, monster, name):
    if(monster["hit_points"] <= 0):
        print(f"\n{name} has slain the beast!")
        return True
    elif(player["hit_points"] <= 0):
        print(f"\n{name} has been slain by the beast!")
        return True
    else:
        return False

def defend(original_defense, round):
    new_defense = original_defense + 1
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
name = user_name()
print(f"\nAlright {name}. lets go!")
parser.show_controls()

while(is_someone_dead(player, monster, name) == False):
    round = round_counter(round)

    print(f"\n\nRound {round_counter(round)}: monster - {monster['hit_points']}, player - {player['hit_points']}")
    print(f"\nplayer defense: {player['defense']}, monster defense {monster['defense']}")

    # 1) player input
    player_input_string = input(f"I await your command {name}: ")
    player["decision"] = parser.parse_player_input(player_input_string)

    # 2) gather monster input
    monster["decision"] = monsters_choice()

    # 3) execute defends
    if(player["decision"] == "defend"):
        player["defense"] = defend(player["defense"], round)

    if(monster["decision"] == "defend"):
        monster["defense"] = defend(monster["defense"], round)

    # 4) execute attacks
    if(player["decision"] == "attack"):
        monster["hit_points"] = attack(player["attack_power"], monster["hit_points"], monster["defense"])

    if(monster["decision"] == "attack"):
        player["hit_points"] = attack(monster["attack_power"], player["hit_points"], player["defense"])

    # 5) quit out
    if(player["decision"] == "quit"):
        quit()

    print(f"\nThe player chooses to {player['decision']}, The Monster choses to {monster['decision']}")

print(f"\n\n{name} has finished the Adventure! So far...")
