from models.events.event_base import EventBase

class BattleEvent(EventBase):
    BATTLE_EVENT = "battle_event"
    BATTLE_COMMAND_EVENT = "battle_command_event"
    END_BATTLE_EVENT = "end_battle_event"

    def __init__(self, name, data = {}):
        EventBase.__init__(self, name, data)

    # attribute accessors

    @property
    def player(self):
        return self.data["player"]

    @property
    def monster(self):
        return self.data["entity"]

    @property
    def command(self):
        return self.data["command"]
