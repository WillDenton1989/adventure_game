from models.events.event_base import EventBase

class GameEvent(EventBase):
    QUIT_EVENT = "quit_event"
    GAME_FINISH_EVENT = "game_finish_event"
    STATE_CHANGE_EVENT = "state_change_event"
    # GAME_END_EVENT = "game_end_event"

    def __init__(self, name, data = {}):
        EventBase.__init__(self, name, data)

    # attribute accessors

    @property
    def new_state(self):
        return self.data["new_state"]

    @property
    def previous_state(self):
        return self.data["previous_state"]
