#where the inventory lives.
import yaml
import player_manager
import event_manager
import game_manager
import input_manager

# public methods

def initialize():
    event_manager.listen(event_manager.STATE_CHANGE_EVENT, _state_change_event_handler)

# private methods

def _initialize_inventory(player, inventory):
    _manage_inventory(inventory)

def _display_inventory(inventory):
    print("\n------------------------------------------------------------------------\n")
    print("Here is your inventory:\n")

    print(f"""    1) -{inventory['space_1']}
    2) -{inventory['space_2']}
    3) -{inventory['space_3']}""")

    print("\n------------------------------------------------------------------------\n")

def _manage_inventory(inventory):
    _display_inventory(inventory)
    print("what would you like to use?")
    input_manager.parse_input()

# event handlers

def _state_change_event_handler(event_name, data):
    if(data["new_state"] == game_manager.STATE_INVENTORY):
        inventory_data = data["event_data"]
        _initialize_inventory(player_manager.get_player_data(), player_manager.get_player_inventory())

def _inventory_command_event_handler(event_name, data):
    pass
