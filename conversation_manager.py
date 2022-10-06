# where the conversation lives.
import event_manager
from managers.input_manager import InputManager
from models.state import State

def initialize():
    event_manager.listen(event_manager.STATE_CHANGE_EVENT, _state_change_event_handler)
    event_manager.listen(event_manager.CONVERSATION_EVENT, _conversation_command_event_handler)

# private methods

def _run_conversation():
    # dwarf dialogue should come from a yaml file
    print("hello buddy! Whats your name?")
    event_manager.trigger_event(event_manager.INPUT_PARSE_EVENT, {})

    # player dialogue choices should also come from a yaml file

def _initialize_conversation(data):
    npc = data["entity"]
    player = data["player"]
    print(f"\n{player.name} has encountered the legendary {npc.name}!!!\n")
    _run_conversation()

# event handlers

def _state_change_event_handler(event_name, data):
    if(data["new_state"] == State.STATE_CONVERSATION):
        conversation_data = data["event_data"]
        _initialize_conversation(conversation_data)

def _conversation_command_event_handler(event_name, data):
    pass
