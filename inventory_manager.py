#where the inventory lives.
import yaml
import player_manager
import event_manager
import game_manager
import input_manager

_player_inventory = []

# public methods

def initialize():
    event_manager.listen(event_manager.STATE_CHANGE_EVENT, _state_change_event_handler)
    event_manager.listen(event_manager.ADD_ITEM_TO_INVENTORY_EVENT, _add_item_to_inventory_event_handler)
    event_manager.listen(event_manager.INVENTORY_COMMAND_EVENT, _inventory_command_event_handler)

# private methods

def _initialize_inventory(player, inventory):
    pass

def _display_inventory():
    global _player_inventory

    print("\n------------------------------------------------------------------------\n")
    print("Here is your inventory:\n")
    element_number = 1

    for item in _player_inventory:
        print(f"{element_number}" + ") - " + f"{item['display_name']}")
        element_number += 1

    print("\n------------------------------------------------------------------------\n")

def _inventory_screen():
    _display_inventory()
    input_manager.parse_input()
    # _display_inventory()
    _inventory_continue()

def _add_item_to_inventory(item):
    global _player_inventory
    return _player_inventory.append(item)

def _inventory_continue():
    if(_game_state() == game_manager.STATE_INVENTORY):
        _inventory_screen()

def _game_state():
    return game_manager.game_state()

def _handle_inventory_command(data):
    print("here is where something would happen with the item you chose")
    pass

# event handlers

def _state_change_event_handler(event_name, data):
    if(data["new_state"] == game_manager.STATE_INVENTORY):
        _inventory_screen()

def _add_item_to_inventory_event_handler(event_name, data):
    _add_item_to_inventory(data["item"])

def _inventory_command_event_handler(event_name, data):
    _handle_inventory_command(data["choice"])
