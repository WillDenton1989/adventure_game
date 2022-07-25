# constants

from random import randint
import parser

name = None

player_hit_points = 15
monster_hit_points = 14

player_defense = 1
monster_defense = 1

# player_attack_power = randint(1, 4)
player_attack_power = 5
monster_attack_power = 4

player_decision = None
monster_decision = None

round = 0

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
    print(f"Farewell {name}")
    exit()

def monsters_choice():
    x = randint(1, 10)
    if(x <= 6):
        return "attack"
    else:
        return "defend"

#game functions

def is_someone_dead():
    if(monster_hit_points <= 0):
        print(f"{name} has slain the beast!")
        return True
    elif(player_hit_points <= 0):
        print(f"{name} has been slain by the beast!")
        return True
    else:
        return False

def defend(original_defense):
    return original_defense + 1

def attack(attack_power, hit_points, defense):
    attack_roll = randint(1, attack_power)
    attack_value =  max(0, attack_roll - defense)
    return hit_points - attack_value

# Main

print("Welcome intrepid adventurer! \n\nThis is the Adventure Game!(working title, dont laugh)\n\n")
name = user_name()
print(f"\nAlright {name}. lets go!")
parser.show_controls()
while(is_someone_dead() == False):
    round = round + 1

    print(f"\n\nRound {round}: monster - {monster_hit_points}, player - {player_hit_points}")
    print(f"\nplayer defense: {player_defense}, monster defense {monster_defense}")

    # 1) player input
    player_input_string = input(f"I await your command {name}: ")
    player_decision = parser.parse_player_input(player_input_string)

    # 2) gather monster input
    monster_decision = monsters_choice()

    # 3) execute defends
    if(player_decision == "defend"):
        player_defense = defend(player_defense)

    if(monster_decision == "defend"):
        monster_defense = defend(monster_defense)

    # 4) execute attacks
    if(player_decision == "attack"):
        monster_hit_points = attack(player_attack_power, monster_hit_points, monster_defense)

    if(monster_decision == "attack"):
        player_hit_points = attack(monster_attack_power, player_hit_points, player_defense)

    print(player_decision, monster_decision)


print(f"\n\n{name} has finished the Adventure! So far...")
