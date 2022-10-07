class EffectBase:
    """this the base class for effects. They should all inherit from this class."""

    EFFECT_TYPE = ["heal", "damage", "attack_damage", "defense", "mana"]

    def __init__(self, game_manager):
        self._game_manager = game_manager

    # attribute accessors

    @property
    def game_manager(self):
        return self._game_manager

    @property
    def player(self):
        return self._game_manager.player

    # public methods

    # private methods
