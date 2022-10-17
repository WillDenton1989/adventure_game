from abc import ABC, abstractmethod

from models.events.game_event import GameEvent

ALLOWED_CLASS = "GameManager"

class ManagerBase(ABC):
    """this is the base class for all managers in the game"""

    _game_state = None

    def __init__(self, event_dispatcher):
        self._event_dispatcher = event_dispatcher
        self.event_dispatcher.receive(GameEvent.STATE_CHANGE_EVENT, self._state_change_event_handler)
        self._register_receivers()

    @abstractmethod
    def start(self):
        # this is where any one time operation is run.
        pass

    @abstractmethod
    def process(self):
        # looks at the game state, if the game state aligns
        # with the manager then run code here.
        # otherwise pass, may need a loop
        pass

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
    def _register_receivers(self):
        pass

    @abstractmethod
    def _unregister_receivers(self):
        pass

    @abstractmethod
    def _handle_game_state_change(self, previous_state, new_state, data):
        pass

    # event handlers

    def _state_change_event_handler(self, event):
        self._handle_game_state_change(event.previous_state, event.new_state, event.data)
