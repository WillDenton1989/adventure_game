#battle manager
from random import randint
from managers.input_manager import InputManager
import event_manager
from models.name_generator import NameGenerator
from models.catchphrase_generator import CatchphraseGenerator
from models.state import State

SYMBOL_DEAD = "corpse"

_player_decision = None
_monster_decision = None
_battle = {}
_round = 0

# public methods

def initialize():
    event_manager.listen(event_manager.STATE_CHANGE_EVENT, _state_change_event_handler)
    event_manager.listen(event_manager.BATTLE_COMMAND_EVENT, _battle_command_event_handler)

def is_someone_dead(character):
    if(character.hit_points <= 0):
        return True
    else:
        return False

# private methods

def _initialize_battle(data):
    player, monster = data["player"], data["entity"]
    if(_check_for_loot(monster) == True): return

    player.prepare_for_battle()
    monster.prepare_for_battle()

    _round = 0
    _battle["player"] = player
    _battle["monster"] = monster

    print(f"\n{player.name} is fighting the legendary {monster.name}!!!\n")
    print(monster.catchphrase)
    _run_battle()

def _check_for_loot(monster):
    if(is_someone_dead(monster) == True):
        event_manager.trigger_event(event_manager.END_BATTLE_EVENT)
        print(f"\nThe corpse of {monster.name} lies before you, broken and shamed\nFor now there is no loot to be had... begone!")
        return True
    return False

def _run_battle():
    global _round

    _round += 1
    player, monster = _battle["player"], _battle["monster"]

    print(f"\n\nRound {_round}: {player.name} - {player.hit_points}, {monster.name} - {monster.hit_points}")
    print(f"\n{player.name}: defense: {player.defense} attack: {player.attack_power}, {monster.name}: defense: {monster.defense} attack: {monster.attack_power}")
    event_manager.trigger_event(event_manager.INPUT_PARSE_EVENT, {})

def _handle_player_decision(decision):
    global _player_decision
    global _monster_decision

    _player_decision = decision
    _monster_decision = _enemy_npc_choice()
    _execute_battle_round()

def _enemy_npc_choice():
    x = randint(1, 10)
    if(x <= 7):
        return "attack"
    else:
        return "defend"

def _execute_battle_round():
    player, monster = _battle["player"], _battle["monster"]
    global _player_decision
    global _monster_decision

    _execute_defends(player, monster, _player_decision, _monster_decision)
    _execute_attacks(player, monster, _player_decision, _monster_decision)

    print(f"\n{player.name} chooses to {_player_decision}, {monster.name} chooses to {_monster_decision}")

    if(_player_death(player, monster) == False and _monster_death(player, monster) == False):
        _run_battle()

def _execute_defends(player, monster, player_decision, monster_decision):
    if(player_decision == "defend"):
        player.defense = _defend(player.defense, player.defense_scalar)

    if(monster_decision == "defend"):
        monster.defense = _defend(monster.defense, monster.defense_scalar)

def _execute_attacks(player, monster, player_decision, monster_decision):
    if(player_decision == "attack"):
        monster.hit_points = _attack(player.attack_power, monster.hit_points, monster.defense)

    if(monster_decision == "attack"):
        player.hit_points = _attack(monster.attack_power, player.hit_points, player.defense)

def _defend(original_defense, defense_scalar):
    new_defense = original_defense + defense_scalar
    if(new_defense == 4):
        return original_defense
    else:
        return new_defense

def _attack(attack_power, hit_points, defense):
    attack_roll = randint(1, attack_power)
    attack_value =  max(0, attack_roll - defense)
    return hit_points - attack_value

def _monster_death(player, monster):
    if(is_someone_dead(monster) == True):
        print(f"\n\n{monster.name} has been slain")
        monster.symbol = SYMBOL_DEAD
        event_manager.trigger_event(event_manager.END_BATTLE_EVENT)
        return True
    return False

def _player_death(player, monster):
    if(is_someone_dead(player) == True):
        print(f"\n\n{player.name} has been slain by {monster.name}")
        return True
    return False

# event handlers

def _state_change_event_handler(event_name, data):
    if(data["new_state"] == State.STATE_BATTLE):
        battle_data = data["event_data"]
        _initialize_battle(data["event_data"])

def _battle_command_event_handler(event_name, data):
    _handle_player_decision(data["command"])
