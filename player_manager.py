#player manager
import battle_manager
import input_manager
import event_manager
import game_manager

_player = {
    "name": None,
    "battle_decision": None
}

def initialize():
    event_manager.listen(event_manager.QUIT_EVENT, _quit_event_handler)

def get_player_data():
    global _player
    return _player

def update_player_data(data):
    global _player
    return _player.update(data)

def create_player(player):
    _player["name"] = input_manager.parse_input()

# private methods

def _quit():
    print(f"Farewell {_player['name']}")
    exit()

# event handlers

def _quit_event_handler(event_name, data):
    _quit()
