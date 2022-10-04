class EffectBase:
    """this is a class for making effects"""

    EFFECT_TYPE = ["heal", "damage", "attack_damage", "defense", "mana"]

    def __init__(self, game_manager):
        self._game_manager = game_manager

    @property
    def game_manager(self):
        return self._game_manager

    @property
    def player_manager(self):
        return self._game_manager.get_player_manager()
