from managers.input_manager import InputManager
from managers.manager_base import ManagerBase

from models.events.conversation_event import ConversationEvent
from models.events.input_event import InputEvent
from models.state import State

class ConversationManager(ManagerBase):
    def __init__(self, event_dispatcher):
        ManagerBase.__init__(self, event_dispatcher)

    # private methods

    def _register_receivers(self):
        self.event_dispatcher.receive(ConversationEvent.CONVERSATION_EVENT, self._conversation_command_event_handler)

    def _unregister_receivers(self):
        pass

    def _run_conversation(self):
        print("hello buddy! Whats your name?")
        self.event_dispatcher.dispatch(InputEvent(InputEvent.INPUT_PARSE_EVENT, {}))

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

    def _conversation_command_event_handler(self, _event):
        pass
