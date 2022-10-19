from managers.manager_base import ManagerBase

from models.hud import Hud
from models.state import State

class HudManager(ManagerBase):
    def __init__(self, event_dispatcher, game_manager):
        ManagerBase.__init__(self, event_dispatcher)
        self._game_manager = game_manager
        self._hud = Hud(self._game_manager)

    def start(self):
        pass

    def process(self):
        if(self.game_state != State.STATE_GAME_END):
            self.hud.display_hud()

    # attribute accessors

    @property
    def hud(self):
        return self._hud

    # public methods

    # private methods

    def _register_receivers(self):
        pass

    def _unregister_receivers(self):
        pass

    def _handle_game_state_change(self, previous_state, new_state, data):
        pass
