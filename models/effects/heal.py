from models.effects.effect_base import EffectBase

class Heal(EffectBase):
    """this is a class for healing effect"""

    def __init__(self, max_heal, game_manager):
        super().__init__(game_manager) # ask Mike about if we're still using this right?
        self._max_heal = max_heal

    # public methods

    def execute(self):
        player = self.player
        max_hp = player.max_hit_points
        old_hp = player.hit_points
        new_hp = old_hp + self._max_heal

        if(new_hp > max_hp):
            player.hit_points = max_hp
            print(f"{old_hp}, {max_hp}")
        else:
            player.hit_points = new_hp
            print(f"{old_hp}, {new_hp}")

    # private methods
