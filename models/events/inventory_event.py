from models.events.event_base import EventBase

class InventoryEvent(EventBase):
    OPEN_INVENTORY_EVENT = "open_inventory_event"
    CLOSE_INVENTORY_EVENT = "close_inventory_event"
    SELECT_ITEM_IN_INVENTORY_EVENT = "select_item_in_inventory_event"
    ADD_ITEM_TO_INVENTORY_EVENT = "add_item_to_inventory_event"
    REMOVE_ITEM_FROM_INVENTORY_EVENT = "remove_item_from_inventory_event"
    CREATE_INVENTORY_EVENT = "create_inventory_event"

    def __init__(self, name, data = {}):
        EventBase.__init__(self, name, data)

    # attribute accessors

    @property
    def entity_id(self):
        return self.data["id"]

    @property
    def inventory(self):
        return self.data["inventory"]

    @property
    def inventory_position(self):
        return self.data["inventory_position"]

    @property
    def item(self):
        return self.data["item"]
