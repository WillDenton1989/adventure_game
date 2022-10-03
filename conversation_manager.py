# where the conversation lives.
import event_manager
import game_manager
import player_manager
import npc_manager
import input_manager

conversation = {}

def initialize():
    event_manager.listen(event_manager.STATE_CHANGE_EVENT, _state_change_event_handler)
    event_manager.listen(event_manager.CONVERSATION_EVENT, _conversation_command_event_handler)

def initialize_conversation(player, npc):
    npc["name"] = npc_manager.name_generator(npc["character_class"]) + " the " + npc["character_class"]
    print(f"\n{player['name']} has encountered the legendary {npc['name']}!!!\n")
    _run_conversation()

# private methods

def _run_conversation():
    # dwarf dialogue should come from a yaml file
    print("hello buddy! Whats your name?")
    input_manager.parse_input()

    # player dialogue choices should also come from a yaml file

# event handlers

def _state_change_event_handler(event_name, data):
    if(data["new_state"] == game_manager.GameManager.STATE_CONVERSATION):
        conversation_data = data["event_data"]
        initialize_conversation(player_manager.get_player_data(), conversation_data)

def _conversation_command_event_handler(event_name, data):
    pass
