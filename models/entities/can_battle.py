from models.entities.can_be_modified import CanBeModified

class CanBattle(CanBeModified):
    def __init__(self, data):
        CanBeModified.__init__(self, data)

        self._max_hit_points = data["max_hit_points"]
        self._hit_points = data["hit_points"]
        self._attack_power = data["attack_power"]
        self._base_defense = data["defense"]
        self._defense_scalar = data["defense_scalar"]
        self._accumulated_scale_defense = 0

    # attribute accessors

    @property
    @CanBeModified.modifiable_attribute
    def max_hit_points(self):
        return self._max_hit_points

    @property
    def hit_points(self):
        return self._hit_points

    @hit_points.setter
    def hit_points(self, value):
        self._hit_points = value

    @property
    @CanBeModified.modifiable_attribute
    def attack_power(self):
        return self._attack_power

    @attack_power.setter
    def attack_power(self, value):
        self._attack_power = value

    @property
    def defense(self):
        return self._base_defense + self._accumulated_scale_defense

    @defense.setter
    def defense(self, value):
        self._accumulated_scale_defense = value - self._base_defense

    @property
    def defense_scalar(self):
        return self._defense_scalar

    # public methods

    def prepare_for_battle(self):
        self._accumulated_scale_defense = 0

    # private methods
