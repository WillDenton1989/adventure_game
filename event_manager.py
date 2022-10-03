#where the events live.

# Events. probably need to clean this up in the near future.
ADD_PLAYER_TO_LEVEL_EVENT = "add_player_event"
STATE_CHANGE_EVENT = "state_change_event"

BATTLE_EVENT = "battle_event"
BATTLE_COMMAND_EVENT = "battle_command_event"
END_BATTLE_EVENT = "end_battle_event"

MOVEMENT_EVENT = "movement_event"
UPDATE_PLAYER_LOCATION_EVENT = "update_player_location_event"

OPEN_INVENTORY_EVENT = "open_inventory event"
CLOSE_INVENTORY_EVENT = "close_inventory_event"

SELECT_ITEM_IN_INVENTORY_EVENT = "select_item_in_inventory_event"

TRIGGER_CONSUME_ITEM_EFFECT_EVENT = "trigger_consume_item_effect_event"
TRIGGER_EQUIP_ITEM_EFFECT_EVENT = "trigger_equip_item_effect_event"

ADD_ITEM_TO_INVENTORY_EVENT = "add_item_to_inventory_event"
REMOVE_ITEM_FROM_INVENTORY_EVENT = "remove_item_from_inventory_event"

CONVERSATION_EVENT = "conversation_event"
CONVERSATION_INPUT_EVENT = "conversation_input_event"
END_CONVERSATION_EVENT = "end_conversation_event"

QUIT_EVENT = "quit_event"
GAME_FINISH_EVENT = "game_finish_event"

_event_listeners = []

# methods

def trigger_event(event_name, data={}):
    for event_listener in _event_listeners:
        if(event_listener["event_name"] == event_name):
            event_listener["callback"](event_name, data)

def listen(event_name, callback):
    _event_listeners.append({ "event_name": event_name, "callback": callback })
