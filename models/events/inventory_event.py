from models.events.event_base import EventBase

class InventoryEvent(EventBase):
    OPEN_INVENTORY_EVENT = "open_inventory_event"

    def __init__(self, name, data = {}):
        EventBase.__init__(self, name, data)
