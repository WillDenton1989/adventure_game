class Hud:
    """this is a class for the heads up display or HUD. will dsiplay relavent information based on game state."""

    def __init__(self, game_manager):
        self._game_manager = game_manager

    # attribute accessors

    @property
    def player(self):
        return self._game_manager.player

    @property
    def turns(self):
        return self._game_manager.turns

    @property
    def game_state(self):
        return self._game_manager.game_state

    # public methods

    def display_hud(self):
        self._line_formating_a()
        print(f"Player: {self.player.name} | HP/Max-HP: {self.player.hit_points}/{self.player.max_hit_points} | AttkPwr: {self.player.attack_power} | Def: {self.player.defense} | Turn: {self.turns}\nSTATE: {self.game_state}")
        self._line_formating_a()

    # private methods

    def _line_formating_a(self):
        print("------------------------------------------------------------------------")

    def _line_formating_b(self):
        print("\n------------------------------------------------------------------------")

    def _line_formating_c(self):
        print("------------------------------------------------------------------------\n")

    def _line_formating_d(self):
        print("\n------------------------------------------------------------------------\n")
