# where the conversation lives.
import event_manager
import game_manager
import npc_manager
import input_manager

_game_manager = None

def initialize(game_manager):
    global _game_manager
    _game_manager = game_manager
    event_manager.listen(event_manager.STATE_CHANGE_EVENT, _state_change_event_handler)
    event_manager.listen(event_manager.CONVERSATION_EVENT, _conversation_command_event_handler)

# private methods

def _run_conversation():
    # dwarf dialogue should come from a yaml file
    print("hello buddy! Whats your name?")
    input_manager.parse_input()

    # player dialogue choices should also come from a yaml file

# event handlers

def _initialize_conversation(player, npc):
    print(f"\n{player.name} has encountered the legendary {npc.name}!!!\n")
    _run_conversation()

def _state_change_event_handler(event_name, data):
    global _game_manager
    if(data["new_state"] == game_manager.GameManager.STATE_CONVERSATION):
        conversation_data = data["event_data"]
        _initialize_conversation(_game_manager.get_player_manager().player, conversation_data)

def _conversation_command_event_handler(event_name, data):
    pass
