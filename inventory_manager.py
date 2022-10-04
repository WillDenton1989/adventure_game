#where the inventory lives.
import yaml
import player_manager
import event_manager
import game_manager
import input_manager
from models.inventory import Inventory

_player_inventory = []
_game_manager = None

# public methods

def initialize(game_manager):
    global _game_manager
    event_manager.listen(event_manager.STATE_CHANGE_EVENT, _state_change_event_handler)
    event_manager.listen(event_manager.ADD_ITEM_TO_INVENTORY_EVENT, _add_item_to_inventory_event_handler)
    event_manager.listen(event_manager.SELECT_ITEM_IN_INVENTORY_EVENT, _inventory_command_event_handler)

    _game_manager = game_manager

# private methods

def _display_inventory():
    global _player_inventory

    print("\n------------------------------------------------------------------------\n")
    print("Here is your inventory:\n")
    element_number = 1

    if(len(_player_inventory) == 0):
        print("Your inventory is empty.")
    else:
        for item in _player_inventory:
                print(f"{element_number}" + ") - " + f"{item}")
                element_number += 1

    print("\n------------------------------------------------------------------------\n")

def _inventory_screen():
    _display_inventory()
    input_manager.parse_input()
    _inventory_continue()

def _add_item_to_inventory(item):
    global _player_inventory
    return _player_inventory.append(item)

def _inventory_continue(): # this function is necessary for _inventory_screen to work until the gameboard loop is reworked.
    if(_game_state() == game_manager.GameManager.STATE_INVENTORY):
        _inventory_screen()

def _game_state():
    global _game_manager
    return _game_manager.game_state

def _select_item(inventory_position):
    if(_is_selected_item_in_inventory_range(inventory_position) == True):
        print("here is where something would happen with the item you chose")
        _use_item(inventory_position)
        _remove_consumable_item(inventory_position)
    else:
        print("Please select a valid item")

def _use_item(inventory_position):
    global _player_inventory
    consumable_item_data = {}
    equip_item_data = {}
    if(_is_item_consumable(inventory_position) == True):
        consumable_item_data["item_choice"] = _player_inventory[inventory_position]
        event_manager.trigger_event(event_manager.TRIGGER_CONSUME_ITEM_EFFECT_EVENT, consumable_item_data)
    elif(_is_item_equipable(inventory_position) == True):
        _player_inventory[inventory_position]
        print("here is where an equipable item trigger would happen.")
        # event_manager.trigger_event(event_manager.TRIGGER_EQUIP_ITEM_EFFECT_EVENT, equip_item_data)
    else:
        print("That is not a useable item brother man.")

def equip_item():
    pass

def unequip_item():
    pass

def _remove_consumable_item(inventory_position):
    global _player_inventory
    if(_is_item_consumable(inventory_position) == True):
        _player_inventory.pop(inventory_position)
    else:
        pass

def _is_selected_item_in_inventory_range(inventory_position):
    global _player_inventory
    if(inventory_position > len(_player_inventory) - 1):
        return False
    else:
        return True

def _is_item_consumable(inventory_position):
    global _player_inventory
    if(_player_inventory[inventory_position].consumable == True):
        return True
    else:
        return False

def _is_item_equipable(inventory_position):
    global _player_inventory
    if(_player_inventory[inventory_position].equipable == True):
        return True
    else:
        return False

# event handlers

def _state_change_event_handler(event_name, data):
    if(data["new_state"] == game_manager.GameManager.STATE_INVENTORY):
        _inventory_screen()

def _add_item_to_inventory_event_handler(event_name, item_object_data):
    _add_item_to_inventory(item_object_data)

def _inventory_command_event_handler(event_name, data):
    _select_item(data["choice"])
