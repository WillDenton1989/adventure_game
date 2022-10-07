from abc import ABC, abstractmethod

import event_manager

ALLOWED_CLASS = "GameManager"

class ManagerBase(ABC):
    """this is the base class for all managers in the game"""

    _game_state = None

    def __init__(self, event_dispatcher):
        event_manager.listen(event_manager.STATE_CHANGE_EVENT, self._state_change_event_handler)
        self._event_dispatcher = event_dispatcher
        self._register_listeners()

    # attribute accessors

    @property
    def game_state(self):
        return ManagerBase._game_state

    @game_state.setter
    def game_state(self, value):
        if(self.__class__.__name__ != ALLOWED_CLASS):
            raise Exception("Only GameManager can do this")
        else:
            ManagerBase._game_state = value

    @property
    def event_dispatcher(self):
        return self._event_dispatcher

    # public methods

    # private methods

    @abstractmethod
    def _register_listeners(self):
        pass

    @abstractmethod
    def _unregister_listeners(self):
        pass

    @abstractmethod
    def _handle_game_state_change(self, previous_state, new_state, data):
        pass

    # event handlers

    def _state_change_event_handler(self, event_name, data):
        self._handle_game_state_change(data["previous_state"], data["new_state"], data)
