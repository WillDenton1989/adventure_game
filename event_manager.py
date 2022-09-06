#where the events live.
import yaml

#start_battle_event
BATTLE_EVENT = "battle_event"
STATE_CHANGE_EVENT = "state_change" # maybe?
END_BATTLE_EVENT = "end_battle"
MOVEMENT_EVENT = "movement_event"

_event_listeners = []

def trigger_event(event_name, data={}):
    for event_listener in _event_listeners:
        if(event_listener["event_name"] == event_name):
            event_listener["callback"](event_name, data)

def listen(event_name, callback):
    _event_listeners.append({ "event_name": event_name, "callback": callback })
