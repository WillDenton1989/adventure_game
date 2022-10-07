from models.events.event_base import EventBase

class ItemEvent(EventBase):
    USE_ITEM_EVENT = "use_item_event"

    def __init__(self, name, data = {}):
        EventBase.__init__(self, name, data)

    # attribute accessors

    @property
    def inventory_position(self):
        return self.data["inventory_position"]

    @property
    def item(self):
        return self.data["item"]
