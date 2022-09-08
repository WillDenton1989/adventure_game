#battle manager
#eventually revamp combat system including defend and eventually add weapons and armor.
from random import randint
import player_manager
import monster_module
import input_manager
import event_manager
import game_manager

def initialize():
    event_manager.listen(event_manager.STATE_CHANGE_EVENT, _state_change_event_handler)

def is_someone_dead(character):
    if(character["hit_points"] <= 0):
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

# private methods

def _start_battle(player, monster, attack, defend, parse_input, enemy_npc_choice):
    # stand in for what should probably be a looting event. for now it just lets you go back to the corpse without restarting the battle
    if(is_someone_dead(monster) == True):
        event_manager.trigger_event(event_manager.END_BATTLE_EVENT)
        return print(f"\nThe corpse of {monster['name']} lies before you, broken and shamed\nFor now there is no loot to be had... begone!")

    monster["name"] = monster_module.name_generator() + " the " + monster["class"]

    print(f"\n{player['name']} is fighting the legendary {monster['name']}!!!\n")
    monster_module.monster_catchphrase_generator(monster)
    input_manager.show_controls()#input_manager.show_battle_controls()
    round = -1

    while(is_someone_dead(player) == False and is_someone_dead(monster) == False):
        round = round + 1

        print(f"\n\nRound {round}: {monster['name']} - {monster['hit_points']}, {player['name']} - {player['hit_points']}")
        print(f"\n{player['name']}: defense: {player['defense']} attack: {player['attack_power']}, {monster['name']}: defense: {monster['defense']} attack: {monster['attack_power']}")

        # 1) player input
        player["battle_decision"] = input_manager.parse_input()
        if(player["battle_decision"] == "cont"):
            continue

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
        # inventory code will go here.

        # 6) quit out
        if(player["battle_decision"] == "quit"):
            quit()

        print(f"\n{player['name']} chooses to {player['battle_decision']}, {monster['name']} chooses to {monster['battle_decision']}")

        # battle resolution
        if(is_someone_dead(monster) == True):
            print(f"\n\n{monster['name']} has been slain")
            monster['symbol'] = 120
            event_manager.trigger_event(event_manager.END_BATTLE_EVENT)

        if(is_someone_dead(player) == True):
            print(f"\n\n{player['name']} has been slain by {monster['name']}")

# event handlers

def _state_change_event_handler(event_name, data):
    if(data["new_state"] == game_manager.STATE_BATTLE):
        battle_data = data["event_data"]
        _start_battle(player_manager.get_player_data(), battle_data, attack, defend, input_manager.parse_input, monster_module.enemy_npc_choice)
