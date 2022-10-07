from models.events.event_base import EventBase

class GameEvent(EventBase):
    QUIT_EVENT = "quit_event"

    def __init__(self, name, data = {}):
        EventBase.__init__(self, name, data)
