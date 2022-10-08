from models.events.event_base import EventBase

class EntityEvent(EventBase):
    CREATE_ENTITY_EVENT = "create_entity_event"
    ENTITIES_UPDATED_EVENT = "entities_updated_event"

    def __init__(self, name, data = {}):
        EventBase.__init__(self, name, data)

    # attribute accessors

    @property
    def entity_data(self):
        return self.data["entity_data"]

    @property
    def updated_entities(self):
        return self.data["updated_entities"]
