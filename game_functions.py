#technically battle functions but oh whale
#eventually revamp cobat system including defend and eventually add weapons and armor.
from random import randint
import game_commands
import monster_module
import game_parser

def is_someone_dead(character):
    if(character["hit_points"] <= 0):
        return True
    else:
        return False

# def game_over_screen():

def defend(original_defense, defense_scalar):
    new_defense = original_defense + defense_scalar
    #create a defense cap constant.
    #
    if(new_defense == 4):
        return original_defense
    else:
        return new_defense

def attack(attack_power, hit_points, defense):
    attack_roll = randint(1, attack_power)
    attack_value =  max(0, attack_roll - defense)
    return hit_points - attack_value

def battle(player, monster, attack, defend, parse_player_input, enemy_npc_choice, quit):
    if(is_someone_dead(monster) == True):
        return print(f"\nThe corpse of {monster['name']} lies before you, broken and shamed\nFor now there is no loot to be had... begone!")

    print(f"\n{player['name']} is fighting the legendary {monster['name']}!!!\n")
    monster_module.monster_catchphrase_generator(monster)
    game_parser.show_controls()
    round = -1

    while(is_someone_dead(player) == False and is_someone_dead(monster) == False):
        round = round + 1

        print(f"\n\nRound {round}: {monster['name']} - {monster['hit_points']}, {player['name']} - {player['hit_points']}")
        print(f"\n{player['name']} defense: {player['defense']} attack: {player['attack_power']}, {monster['name']} defense: {monster['defense']} attack: {monster['attack_power']}")

        # 1) player input
        player_input_string = input(f"I await your command {player['name']}: ")
        player["battle_decision"] = game_parser.parse_player_input(player_input_string)
        while(player["battle_decision"] == "cont"):
            game_parser.show_controls()
            player_input_string = input(f"\nI await a real command {player['name']}: ")
            player["battle_decision"] = game_parser.parse_player_input(player_input_string)

        # 2) gather monster input
        monster["battle_decision"] = enemy_npc_choice()

        # 3) execute defends
        if(player["battle_decision"] == "defend"):
            player["defense"] = defend(player["defense"], player["defense_scalar"])

        if(monster["battle_decision"] == "defend"):
            monster["defense"] = defend(monster["defense"], monster["defense_scalar"])

        # 4) execute attacks
        if(player["battle_decision"] == "attack"):
            monster["hit_points"] = attack(player["attack_power"], monster["hit_points"], monster["defense"])

        if(monster["battle_decision"] == "attack"):
            player["hit_points"] = attack(monster["attack_power"], player["hit_points"], player["defense"])

        # 5) open inventory
        #inventory code will go here.

        # 6) quit out
        if(player["battle_decision"] == "quit"):
            quit()

        print(f"\n{player['name']} chooses to {player['battle_decision']}, {monster['name']} chooses to {monster['battle_decision']}")

        #battle resolution
        if(is_someone_dead(monster) == True):
            print(f"\n\n{monster['name']} has been slain")
            monster['symbol'] = 120
        if(is_someone_dead(player) == True):
            print(f"\n\n{player['name']} has been slain by {monster['name']}")

def event_trigger(player_location, npc_location):
    if(player_location == npc_location):
        return True
    else:
        return False