class Battle:
    def __init__(self, player, monster):
        self._player = player
        self._monster = monster
        self._round = 0
        self._player_decision = None
        self._monster_decision = None

    # refactor this in the battle display refactor DEBUG
    def __str__(self):
        return f"""\nRound {self.round}: {self.player.name} HP: {self.player.hit_points} | {self.monster.name} HP: {self.monster.hit_points}
{self.player.name}: Attack: {self.player.attack_power} Defense: {self.player.defense} | {self.monster.name}: Attack: {self.monster.attack_power} Defense: {self.monster.defense}"""

    # attribute accessors

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, value):
        self._player = value

    @property
    def monster(self):
        return self._monster

    @monster.setter
    def monster(self, value):
        self._monster = value

    @property
    def round(self):
        return self._round

    @round.setter
    def round(self, value):
        self._round = value

    @property
    def player_decision(self):
        return self._player_decision

    @player_decision.setter
    def player_decision(self, value):
        self._player_decision = value

    @property
    def monster_decision(self):
        return self._monster_decision

    @monster_decision.setter
    def monster_decision(self, value):
        self._monster_decision = value

    # public methods

    def decision_text(self):
        return f"\n{self.player.name} chooses to {self.player_decision} | {self.monster.name} chooses to {self.monster_decision}"

    # private methods
