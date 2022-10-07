from models.events.event_base import EventBase

class InputEvent(EventBase):
    INPUT_PARSE_EVENT = "input_parse_event"

    def __init__(self, name, data = {}):
        EventBase.__init__(self, name, data)
