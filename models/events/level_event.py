from models.events.event_base import EventBase

class LevelEvent(EventBase):
    DRAW_LEVEL_EVENT = "draw_level_event"
    MOVEMENT_EVENT = "movement_event"
    UPDATE_PLAYER_LOCATION_EVENT = "update_player_location_event"

    def __init__(self, name, data = {}):
        EventBase.__init__(self, name, data)

    # attribute accessors

    @property
    def direction(self):
        return self.data["direction"]

    @property
    def location(self):
        return self.data["location"]

    @property
    def column(self):
        return self.location["column"]

    @property
    def row(self):
        return self.location["row"]
