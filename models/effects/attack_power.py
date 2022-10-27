from models.effects.effect_base import EffectBase

class AttackPower(EffectBase):
    """this is a class for the attack power effect"""

    def __init__(self, attack_power, game_manager):
        EffectBase.__init__(self, game_manager)
        self._max_attack_power = attack_power

    # public methods

    def execute(self):
        player = self.player
        old_attack_power = player.attack_power
        new_attack_power = old_attack_power + self._max_attack_power

        player.attack_power = new_attack_power
        print(f"\nOld attack power: {old_attack_power} | New attack power: {new_attack_power}")

    def remove(self):
        player = self.player
        old_attack_power = player.attack_power
        new_attack_power = old_attack_power - self._max_attack_power

        player.attack_power = new_attack_power
        print(f"\nOld attack power: {old_attack_power} | New attack power: {new_attack_power}")

    # private methods
