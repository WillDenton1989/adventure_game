class CanEquip:
    def __init__(self):
        self._equpipment = {}

    # attribute accessors

    @property
    def equipment(self):
        return self._equipment

    @equipment.setter
    def equipment(self, value):
        return self._equpment.update(value)

    @property
    def max_hit_points(self):
        return self._max_hit_points

    @property
    def hit_points(self):
        return self._hit_points

    @hit_points.setter
    def hit_points(self, value):
        self._hit_points = value

    @property
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

    # private methods
