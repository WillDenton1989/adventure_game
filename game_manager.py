import battle_manager
import player_manager
import event_manager
import input_manager
import level_parser
import level_manager

STATE_CHARACTER_CREATION = "state_character_creation"
STATE_MOVEMENT = "state_movement"
STATE_BATTLE = "state_battle"

_game_state = None

def initialize():
    global _game_state
    _game_state = STATE_CHARACTER_CREATION

    _initialize_managers()
    _register_listeners()

    player_manager.create_player(player_manager.get_player_data()) # and then change game state to STATE_MOVEMENT after player is created
    _transition_to_movement()

def game_state():
    global _game_State
    return _game_state

def _transition_to_movement():
    _set_state(STATE_MOVEMENT)
    dungeon_map = level_parser.build_the_level('level_1', 'data/symbols_dictionary.yaml')

def _initialize_managers():
    battle_manager.initialize() # we need to do any other managers initializations here!! :)
    player_manager.initialize()
    input_manager.initialize()
    level_manager.initialize()

def _set_state(new_state, event_data = []):
    global _game_state

    previous_state = _game_state
    _game_state = new_state
    _dispatch_state_change(previous_state, new_state, event_data)

def _dispatch_state_change(previous_state, new_state, event_data):
    data = { "previous_state": previous_state, "new_state": new_state, "event_data": event_data }

    event_manager.trigger_event(event_manager.STATE_CHANGE_EVENT, data)

def _register_listeners():
    event_manager.listen(event_manager.BATTLE_EVENT, _battle_started_handler)
    event_manager.listen(event_manager.END_BATTLE_EVENT, _battle_ended_handler)

# event handlers

def _battle_started_handler(event, data):
    _set_state(STATE_BATTLE, data)

def _battle_ended_handler(event, data):
    _set_state(STATE_MOVEMENT, data)
