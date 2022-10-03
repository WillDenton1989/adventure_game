# maybe a class for effects?

class Effect:
    """this is a class for making effects"""

    EFFECT_TYPE = ["heal", "damage", "attack_damage", "defense", "mana"]

    def __init__(self, EFFECT_TYPE):
        self._effect_type = EFFECT_TYPE
