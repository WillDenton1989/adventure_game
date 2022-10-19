import yaml

from managers.manager_base import ManagerBase

from models.events.inventory_event import InventoryEvent
from models.events.item_event import ItemEvent
from models.state import State

class InventoryManager(ManagerBase):
    def __init__(self, event_dispatcher):
        ManagerBase.__init__(self, event_dispatcher)

        self._player_inventory = []

    def start(self):
        pass

    def process(self):
        if(self.game_state == State.STATE_INVENTORY):
            self._show_inventory()

    # private methods

    def _register_receivers(self):
        self.event_dispatcher.receive(InventoryEvent.ADD_ITEM_TO_INVENTORY_EVENT, self._add_item_to_inventory_event_handler)
        self.event_dispatcher.receive(InventoryEvent.REMOVE_ITEM_FROM_INVENTORY_EVENT, self._remove_item_from_inventory_event_handler)
        self.event_dispatcher.receive(InventoryEvent.SELECT_ITEM_IN_INVENTORY_EVENT, self._select_item_in_inventory_event_handler)

    def _unregister_receivers(self):
        pass

    def _show_inventory(self):
        print("------------------------------------------------------------------------\n")
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
            item = self._player_inventory[inventory_position]

            print("here is where something would happen with the item you chose")
            self._use_item(item, inventory_position)
        else:
            print("Please select a valid item")

    def _use_item(self, item, inventory_position):
        data = { "item": item, "inventory_position": inventory_position }
        self.event_dispatcher.dispatch(ItemEvent(ItemEvent.USE_ITEM_EVENT, data))

    def _remove_item(self, item, inventory_position):
        if(item.consumable == True):
            self._player_inventory.pop(inventory_position)
        else:
            raise Exception("Item is not consumable")

    def _is_selected_item_in_inventory_range(self, inventory_position):
        return (inventory_position < len(self._player_inventory) - 1)

    def _handle_game_state_change(self, previous_state, new_state, data):
        # _initialize_inventory
        pass

    # event handlers

    def _add_item_to_inventory_event_handler(self, event):
        self._add_item_to_inventory(event.item)

    def _remove_item_from_inventory_event_handler(self, event):
        self._remove_item(event.item, event.inventory_position)

    def _select_item_in_inventory_event_handler(self, event):
        self._select_item(event.inventory_position)
