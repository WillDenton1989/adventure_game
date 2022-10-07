from models.events.event_base import EventBase

class ConversationEvent(EventBase):
    CONVERSATION_EVENT = "conversation_event"
    END_CONVERSATION_EVENT = "end_conversation_event"

    def __init__(self, name, data = {}):
        EventBase.__init__(self, name, data)

    # attribute accessors

    @property
    def entity(self):
        return self.data["inventory_position"]

    @property
    def player(self):
        return self.data["item"]
