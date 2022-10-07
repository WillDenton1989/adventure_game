from random import randint

import event_manager

from managers.input_manager import InputManager
from managers.manager_base import ManagerBase

from models.battle import Battle
from models.state import State

SYMBOL_DEAD = "corpse"

class BattleManager(ManagerBase):
    def __init__(self):
        ManagerBase.__init__(self)
        self._battle = None

    # public methods

    def is_someone_dead(self, character):
        if(character.hit_points <= 0):
            return True
        else:
            return False

    # private methods

    def _register_listeners(self):
        event_manager.listen(event_manager.BATTLE_COMMAND_EVENT, self._battle_command_event_handler)

    def _unregister_listeners(self):
        pass

    def _initialize_battle(self, data):
        player, monster = data["player"], data["entity"]
        if(self._check_for_loot(monster) == True): return

        player.prepare_for_battle()
        monster.prepare_for_battle()
        self._battle = Battle(player, monster)

        print(f"\n{player.name} is fighting the legendary {monster.name}!!!\n")
        print(monster.catchphrase)
        self._run_battle()

    def _check_for_loot(self, monster):
        if(self.is_someone_dead(monster) == True):
            event_manager.trigger_event(event_manager.END_BATTLE_EVENT)
            print(f"\nThe corpse of {monster.name} lies before you, broken and shamed\nFor now there is no loot to be had... begone!")
            return True
        return False

    def _run_battle(self):
        self._battle.round += 1

        print(self._battle)
        event_manager.trigger_event(event_manager.INPUT_PARSE_EVENT, {})

    def _handle_player_decision(self, decision):
        self._battle.player_decision = decision
        self._battle.monster_decision = self._enemy_npc_choice()
        self._execute_battle_round()

    def _enemy_npc_choice(self):
        x = randint(1, 10)
        if(x <= 7):
            return "attack"
        else:
            return "defend"

    def _execute_battle_round(self):
        player, monster = self._battle.player, self._battle.monster
        player_decision, monster_decision = self._battle.player_decision, self._battle.monster_decision

        self._execute_defends(player, monster, player_decision, monster_decision)
        self._execute_attacks(player, monster, player_decision, monster_decision)

        print(self._battle.decision_text())

        if(self._player_death(player, monster) == False and self._monster_death(player, monster) == False):
            self._run_battle()

    def _execute_defends(self, player, monster, player_decision, monster_decision):
        if(player_decision == "defend"):
            player.defense = self._defend(player.defense, player.defense_scalar)

        if(monster_decision == "defend"):
            monster.defense = self._defend(monster.defense, monster.defense_scalar)

    def _execute_attacks(self, player, monster, player_decision, monster_decision):
        if(player_decision == "attack"):
            monster.hit_points = self._attack(player.attack_power, monster.hit_points, monster.defense)

        if(monster_decision == "attack"):
            player.hit_points = self._attack(monster.attack_power, player.hit_points, player.defense)

    def _defend(self, original_defense, defense_scalar):
        new_defense = original_defense + defense_scalar
        if(new_defense == 4):
            return original_defense
        else:
            return new_defense

    def _attack(self, attack_power, hit_points, defense):
        attack_roll = randint(1, attack_power)
        attack_value =  max(0, attack_roll - defense)
        return hit_points - attack_value

    def _monster_death(self, player, monster):
        if(self.is_someone_dead(monster) == True):
            print(f"\n\n{monster.name} has been slain")
            monster.symbol = SYMBOL_DEAD
            event_manager.trigger_event(event_manager.END_BATTLE_EVENT)
            return True
        return False

    def _player_death(self, player, monster):
        if(self.is_someone_dead(player) == True):
            print(f"\n\n{player.name} has been slain by {monster.name}")
            return True
        return False

    def _handle_game_state_change(self, previous_state, new_state, data):
        pass

    # event handlers

    def _state_change_event_handler(self, event_name, data):
        if(data["new_state"] == State.STATE_BATTLE):
            battle_data = data["event_data"]
            self._initialize_battle(data["event_data"])

    def _battle_command_event_handler(self, event_name, data):
        self._handle_player_decision(data["command"])
