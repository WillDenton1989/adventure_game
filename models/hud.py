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
        self._line_formating()
        print(f"Player: {self.player.name} | Hit-Points: {self.player.hit_points} | Turn: {self.turns} | STATE:  {self.game_state}")
        self._line_formating()

    # private methods

    def _line_formating(self):
        # probaly just need something like curses. but for now this helps.
        print("------------------------------------------------------------------------")
