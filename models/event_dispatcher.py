import sys

from models.events.battle_event import BattleEvent
from models.events.conversation_event import ConversationEvent
from models.events.game_event import GameEvent

class EventDispatcher:
    def __init__(self):
        self._event_listeners = []
        self._callbacks = set([])

    def __str__(self):
        return f" Event listeners: {self._event_listeners}"

    # public methods

    def dispatch(self, event):
        for event_listener in self._event_listeners:
            if(event_listener["event_name"] == event.name):
                event_listener["callback"](event)

    def receive(self, event_name, callback):
        self._ensure_unique_callback(event_name, callback)
        self._event_listeners.append({ "event_name": event_name, "callback": callback })

    def clear_receivers(self):
        self._event_listeners.clear()

    def event_from_string(self, event_string, data):
        classname, event_constant = event_string.split("#")
        klass = self._constantize(classname)
        event_name = klass.__dict__[event_constant]

        return klass(event_name, data)

    # private methods

    def _ensure_unique_callback(self, event_name, callback):
        if(callback in self._callbacks):
            raise Exception(f"Listener already added: {callback.__name__} for {event_name}")

        self._callbacks.add(callback)

    def _constantize(self, classname):
        return getattr(sys.modules[__name__], classname)
