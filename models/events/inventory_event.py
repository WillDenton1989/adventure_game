from models.events.event_base import EventBase

class InventoryEvent(EventBase):
    OPEN_INVENTORY_EVENT = "open_inventory_event"
    CLOSE_INVENTORY_EVENT = "close_inventory_event"
    SELECT_ITEM_IN_INVENTORY_EVENT = "select_item_in_inventory_event"

    def __init__(self, name, data = {}):
        EventBase.__init__(self, name, data)

    # attribute accessors

    @property
    def inventory_position(self):
        return self.data["inventory_position"]
