import event_manager
from managers.input_manager import InputManager
from managers.manager_base import ManagerBase
from models.state import State

class ConversationManager(ManagerBase):
    def __init__(self):
        ManagerBase.__init__(self)

    # private methods

    def _register_listeners(self):
        event_manager.listen(event_manager.CONVERSATION_EVENT, self._conversation_command_event_handler)

    def _unregister_listeners(self):
        pass

    def _run_conversation(self):
        print("hello buddy! Whats your name?")
        event_manager.trigger_event(event_manager.INPUT_PARSE_EVENT, {})

    def _initialize_conversation(self, data):
        npc = data["entity"]
        player = data["player"]
        print(f"\n{player.name} has encountered the legendary {npc.name}!!!\n")
        self._run_conversation()

    def _handle_game_state_change(self, previous_state, new_state, data):
        if(new_state == State.STATE_CONVERSATION):
            conversation_data = data["event_data"]
            self._initialize_conversation(conversation_data)

    # event handlers

    def _conversation_command_event_handler(self, event_name, data):
        pass
