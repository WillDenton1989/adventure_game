#technically battle functions but oh well
import game_commands
import monster_module
import parser
from random import randint

def round_counter(round):
    return + 1

def is_someone_dead(player, monster):
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

def battle(player, monster, attack, defend, round_counter, parse_player_input, enemy_npc_choice, quit):
    print(f"\nAlright {player['name']}. lets go!")
    print(f"\n{player['name']} is fighting a monstrous {monster['name']}")
    monster_module.monster_catchphrase_generator(monster, monster_module.monster_generator)
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
