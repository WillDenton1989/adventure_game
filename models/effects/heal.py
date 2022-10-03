class Heal:
    """this is a class for healing effect"""

    def __init__(self, max_heal, game_manager):
        self._max_heal = max_heal
        self._game_manager = game_manager

    def execute(self):
        user = self._player_manager().get_player_data()

        max_hp = user["max_hit_points"]
        old_hp = user["hit_points"]
        new_hp = old_hp + self._max_heal

        if(new_hp > max_hp):
            self._player_manager().change_player_data("hit_points", max_hp)
            print(f"{old_hp}, {max_hp}")
        else:
            self._player_manager().change_player_data("hit_points", new_hp)
            print(f"{old_hp}, {new_hp}")

    # private methods

    def _player_manager(self):
        return self._game_manager.get_player_manager()
