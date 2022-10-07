from models.events.event_base import EventBase

class LevelEvent(EventBase):
    DRAW_LEVEL_EVENT = "draw_level_event"
    MOVEMENT_EVENT = "movement_event"

    def __init__(self, name, data = {}):
        EventBase.__init__(self, name, data)

    # attribute accessors

    @property
    def direction(self):
        return self.data["direction"]
