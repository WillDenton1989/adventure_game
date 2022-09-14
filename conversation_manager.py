# where the conversation lives.
import event_manager
import game_manager
import player_manager
import npc_manager

conversation = {}

def initialize():
    event_manager.listen(event_manager.STATE_CHANGE_EVENT, _state_change_event_handler)
    event_manager.listen(event_manager.CONVERSATION_EVENT, _conversation_command_event_handler)

def _conversation():
    print("this is where the conversation will begin")

# private methods

def _initialize_conversation(player, npc):

    conversation["player"] = player
    conversation["npc"] = npc

    npc["name"] = npc_manager.name_generator(npc["class"]) + " the " + npc["class"]

    print(f"\n{player['name']} has encountered the legendary {npc['name']}!!!\n")

    _run_conversation()

def _run_conversation():
    pass
# event handlers

def _state_change_event_handler(event_name, data):
    if(data["new_state"] == game_manager.STATE_CONVERSATION):
        conversation_data = data["event_data"]
        _initialize_conversation(player_manager.get_player_data(), conversation_data)

def _conversation_command_event_handler(event_name, data):
    pass
