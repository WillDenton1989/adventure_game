from models.effects.effect_base import EffectBase

class Defense(EffectBase):
    """this is a class for defense effect"""

    def __init__(self, max_defense, game_manager):
        EffectBase.__init__(self, game_manager)
        self._max_defense = max_defense

    # public methods

    def execute(self):
        player = self.player
        old_defense = player.defense
        new_defense = old_defense + self._max_defense

        player.defense = new_defense
        print(f"\nOld Defense: {old_defense} | New Defense: {new_defense}")

    # private methods
