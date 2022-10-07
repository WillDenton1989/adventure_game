
class EventDispatcher:
    def __init__(self):
        self._event_listeners = []
        self._callbacks = set([])

    # public methods

    def dispatch(self, event):
        for event_listener in self._event_listeners:
            if(event_listener["event_name"] == event.name):
                event_listener["callback"](event)

    def receive(self, event_name, callback):
        self._ensure_unique_callback(event_name, callback)
        self._event_listeners.append({ "event_name": event_name, "callback": callback })

    # private methods

    def _ensure_unique_callback(self, event_name, callback):
        if(callback in self._callbacks):
            raise Exception(f"Listener already added: {callback.__name__} for {event_name}")

        self._callbacks.add(callback)
