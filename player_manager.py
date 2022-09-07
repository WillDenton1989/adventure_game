#player manager
import battle_manager
import input_manager
import event_manager
import game_manager

player = {
    "name": None,
    "battle_decision": None
}

def initialize():
    event_manager.listen(event_manager.QUIT_EVENT, _quit_event_handler)

def create_player(player):
    input_manager.show_controls()
    player["name"] = input_manager.parse_input()

# private methods

def _quit():
    print(f"Farewell {player['name']}")
    exit()

# event handlers

def _quit_event_handler(event_name, data):
    _quit()
