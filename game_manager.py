import battle_manager
import player_manager
import event_manager
import input_manager
import level_parser
import level_manager
import conversation_manager
import inventory_manager
import item_manager

STATE_CHARACTER_CREATION = "state_character_creation"
STATE_MOVEMENT = "state_movement"
STATE_BATTLE = "state_battle"
STATE_CONVERSATION = "state_conversation"
STATE_INVENTORY = "state_inventory"

_game_state = None

def initialize():
    global _game_state
    _game_state = STATE_CHARACTER_CREATION

    _initialize_managers()
    _register_listeners()

    player_manager.create_player()
    _transition_to_movement()

def game_state():
    global _game_state
    return _game_state

# private methods

def _transition_to_movement():
    _set_state(STATE_MOVEMENT)
    dungeon_map = level_parser.build_the_level('level_1', 'data/symbols_dictionary.yaml')

def _initialize_managers():
    battle_manager.initialize() # we need to do any other managers initializations here!! :)
    player_manager.initialize()
    input_manager.initialize()
    level_manager.initialize()
    conversation_manager.initialize()
    inventory_manager.initialize()
    item_manager.initialize()

def _register_listeners():
    event_manager.listen(event_manager.BATTLE_EVENT, _battle_started_handler)
    event_manager.listen(event_manager.END_BATTLE_EVENT, _battle_ended_handler)

    event_manager.listen(event_manager.CONVERSATION_EVENT, _conversation_started_handler)
    event_manager.listen(event_manager.END_CONVERSATION_EVENT, _conversation_ended_handler)

    event_manager.listen(event_manager.OPEN_INVENTORY_EVENT, _inventory_opened_handler)
    event_manager.listen(event_manager.CLOSE_INVENTORY_EVENT, _inventory_closed_handler)

    event_manager.listen(event_manager.QUIT_EVENT, _quit_event_handler)
    event_manager.listen(event_manager.GAME_FINISH_EVENT, _game_finish_event_handler)

def _set_state(new_state, event_data = []):
    global _game_state

    previous_state = _game_state
    _game_state = new_state
    _dispatch_state_change(previous_state, new_state, event_data)

def _dispatch_state_change(previous_state, new_state, event_data):
    data = { "previous_state": previous_state, "new_state": new_state, "event_data": event_data }

    event_manager.trigger_event(event_manager.STATE_CHANGE_EVENT, data)

def _quit():
    player = player_manager.get_player_data()
    print(f"Farewell {player['name']}")
    exit()

def _game_over():
    player_data = player_manager.get_player_data()
    print(f"\nCongratulations {player_data['name']}!\n\nYou have escaped the bleak and terrible dungeon!\n")
    print(f"\n{player_data['name']} has finished their Adventure! So far...\n")
    # should put the game over screen here when i make that.
    # also what should be here is the portal, either the trigger will be here or ill make another trigger for it.
    exit()

# event handlers

def _battle_started_handler(event, data):
    _set_state(STATE_BATTLE, data)

def _battle_ended_handler(event, data):
    _set_state(STATE_MOVEMENT, data)

def _inventory_opened_handler(event, data):
    _set_state(STATE_INVENTORY, data)

def _inventory_closed_handler(event, data):
    _set_state(STATE_MOVEMENT, data)

def _conversation_started_handler(event, data):
    _set_state(STATE_CONVERSATION, data)

def _conversation_ended_handler(event, data):
    _set_state(STATE_MOVEMENT, data)

def _quit_event_handler(event_name, data):
    _quit()

def _game_finish_event_handler(event_name, data):
    _game_over()
