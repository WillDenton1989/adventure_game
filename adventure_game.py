#constants

from random import randint
import parser
import monster_module

player = {
    "name": None,
    "hit_points": 9,
    "attack_power": 5,
    "defense": 1,
    "defense_scalar": 1,
    "decision": None
    }

monster = monster_module.monster_generator()

#round = -1

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

def continue_menu(player):
    player_input_string = input(f"Do you wish to continue battling monsters {player['name']}?\nyes/no\n")
    if(player_input_string == "yes" or player_input_string == "y"):
        monster = monster_module.monster_generator()
        player["hit_points"] = 9
        player["defense"] = 1
        return battle(player, monster, attack, defend, round_counter, parser.parse_player_input, enemy_npc_choice, quit)
    elif(player_input_string == "no" or player_input_string == "n"):
        return game_end()
    else:
        return exit()

def quit():
    print(f"You are a pussy ass bitch")
    print(f"Farewell {player['name']}")
    exit()

def game_end():
    print(f"\n\n{player['name']} has finished their Adventure! So far...")
    exit()

def round_counter(round):
    return + 1

def enemy_npc_choice():
    x = randint(1, 10)
    if(x <= 7):
        return "attack"
    else:
        return "defend"

#game functions

def is_someone_dead(player, monster,):
    if(monster["hit_points"] <= 0):
        print(f"\n{player['name']} has slain {monster['name']}!")
        return True
    elif(player["hit_points"] <= 0):
        print(f"\n{player['name']} has been slain by {monster['name']}!")
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

def battle(player, monster, attack, defend, round_counter, parse_player_input, enemy_npc_choice, quit,):
    print(f"\nAlright {player['name']}. lets go!")
    print(f"\n{player['name']} is fighting a monsterous {monster['name']}")
    #monster_module.monster_catchphrase_generator(monster, monster_module.monster_generator)
    parser.show_controls()
    while(is_someone_dead(player, monster,) == False):
        round = -1
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

        print(f"\n{player['name']} chooses to {player['decision']}, The {monster['name']} choses to {monster['decision']}")

# Main
print("Welcome intrepid adventurer! \n\nThis is the Adventure Game!(working title, dont laugh)\n\n")
player["name"] = user_name()

#battle start
battle(player, monster, attack, defend, round_counter, parser.parse_player_input, enemy_npc_choice, quit)

while(is_someone_dead(player, monster) == True):
    continue_menu(player)


print(f"\n\n{player['name']} has finished their Adventure! So far...")
