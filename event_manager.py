# Events. probably need to clean this up in the near future.
CREATE_ENTITY_EVENT = "create_entity_event"
ENTITIES_UPDATED_EVENT = "entities_updated_event"

ADD_PLAYER_TO_LEVEL_EVENT = "add_player_event"
STATE_CHANGE_EVENT = "state_change_event"

# private variables

_event_listeners = []
_callbacks = set([])

# public methods

def trigger_event(event_name, data={}):
    global _event_listeners

    for event_listener in _event_listeners:
        if(event_listener["event_name"] == event_name):
            event_listener["callback"](event_name, data)

def listen(event_name, callback):
    _ensure_unique_callback(callback)
    _event_listeners.append({ "event_name": event_name, "callback": callback })

# private methods

def _ensure_unique_callback(callback):
    global _callbacks
    if(callback in _callbacks):
        raise Exception("Added listener twice")

    _callbacks.add(callback)
