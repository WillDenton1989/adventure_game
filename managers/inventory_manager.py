import yaml

import event_manager

from managers.manager_base import ManagerBase

from models.events.inventory_event import InventoryEvent
from models.state import State

class InventoryManager(ManagerBase):
    count = 0
    def __init__(self, event_dispatcher):
        ManagerBase.__init__(self, event_dispatcher)
        self._player_inventory = []

    # private methods

    def _register_listeners(self):
        event_manager.listen(event_manager.ADD_ITEM_TO_INVENTORY_EVENT, self._add_item_to_inventory_event_handler)
        self.event_dispatcher.receive(InventoryEvent.SELECT_ITEM_IN_INVENTORY_EVENT, self._inventory_select_event_handler)

    def _unregister_listeners(self):
        pass

    def _show_inventory(self):
        while(self.game_state == State.STATE_INVENTORY):
            self._show_inventory_text()
            event_manager.trigger_event(event_manager.INPUT_PARSE_EVENT, {})

    def _show_inventory_text(self):
        print("\n------------------------------------------------------------------------\n")
        print("Here is your inventory:\n")
        element_number = 1

        if(len(self._player_inventory) == 0):
            print("Your inventory is empty.")
        else:
            for item in self._player_inventory:
                    print(f"{element_number}" + ") - " + f"{item}")
                    element_number += 1

        print("\n------------------------------------------------------------------------\n")

    def _add_item_to_inventory(self, item):
        return self._player_inventory.append(item)

    def _select_item(self, inventory_position):
        if(self._is_selected_item_in_inventory_range(inventory_position) == True):
            print("here is where something would happen with the item you chose")
            self._use_item(inventory_position)
            self._remove_consumable_item(inventory_position)
        else:
            print("Please select a valid item")

    def _use_item(self, inventory_position):
        consumable_item_data = {}
        equip_item_data = {}
        if(self._is_item_consumable(inventory_position) == True):
            consumable_item_data["item_choice"] = self._player_inventory[inventory_position]
            event_manager.trigger_event(event_manager.TRIGGER_CONSUME_ITEM_EFFECT_EVENT, consumable_item_data)
        elif(self._is_item_equipable(inventory_position) == True):
            self._player_inventory[inventory_position]
            print("here is where an equipable item trigger would happen.")
        else:
            print("That is not a useable item brother man.")

    def _remove_consumable_item(self, inventory_position):
        if(self._is_item_consumable(inventory_position) == True):
            self._player_inventory.pop(inventory_position)
        else:
            pass

    def _is_selected_item_in_inventory_range(self, inventory_position):
        if(inventory_position > len(self._player_inventory) - 1):
            return False
        else:
            return True

    def _is_item_consumable(self, inventory_position):
        if(self._player_inventory[inventory_position].consumable == True):
            return True
        else:
            return False

    def _is_item_equipable(self, inventory_position):
        if(self._player_inventory[inventory_position].equipable == True):
            return True
        else:
            return False

    def _handle_game_state_change(self, previous_state, new_state, data):
        self._show_inventory()

    # event handlers

    def _add_item_to_inventory_event_handler(self, event_name, item_object_data):
        self._add_item_to_inventory(item_object_data)

    def _inventory_select_event_handler(self, event):
        self._select_item(event.inventory_position)
