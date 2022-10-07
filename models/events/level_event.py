from models.events.event_base import EventBase

class LevelEvent(EventBase):
    DRAW_LEVEL_EVENT = "draw_level_event"

    def __init__(self, name, data = {}):
        EventBase.__init__(self, name, data)
