from models.events.event_base import EventBase

class PlayerEvent(EventBase):
    PLAYER_NAME_CHANGE_EVENT = "player_name_change_event"

    def __init__(self, name, data = {}):
        EventBase.__init__(self, name, data)

    # attribute accessors

    @property
    def new_name(self):
        return self.data["new_name"]
