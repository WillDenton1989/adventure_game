from models.effects.effect_base import EffectBase

class Damage(EffectBase):
    """this is a class for the damage effect"""

    def __init__(self, max_damage, game_manager):
        EffectBase.__init__(self, game_manager)
        self._max_damage = max_damage

    # public methods

    def execute(self):
        player = self.player
        old_hp = player.hit_points
        new_hp = old_hp - self._max_damage

        player.hit_points = new_hp
        print(f"Damage taken: {self._max_damage}")

    # private methods
