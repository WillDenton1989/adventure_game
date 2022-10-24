import ctypes
import yaml

from managers.manager_base import ManagerBase

from models.events.inventory_event import InventoryEvent
from models.events.item_event import ItemEvent
from models.state import State

class InventoryManager(ManagerBase):
    def __init__(self, event_dispatcher, item_manager):
        ManagerBase.__init__(self, event_dispatcher)
        self._item_manager = item_manager
        self._inventories = {}

        self._monster_ids = []
        self._treasure_ids = []
        self._entity_ids = []

    def start(self):
        pass

    def process(self):
        if(self.game_state == State.STATE_INVENTORY):
            self._show_inventory(self._player_id)

    # private methods

    def _register_receivers(self):
        self.event_dispatcher.receive(InventoryEvent.CREATE_INVENTORY_EVENT, self._create_inventory_event_handler)

        self.event_dispatcher.receive(InventoryEvent.ADD_ITEM_TO_INVENTORY_EVENT, self._add_item_to_inventory_event_handler)
        self.event_dispatcher.receive(InventoryEvent.REMOVE_ITEM_FROM_INVENTORY_EVENT, self._remove_item_from_inventory_event_handler)
        self.event_dispatcher.receive(InventoryEvent.SELECT_ITEM_IN_INVENTORY_EVENT, self._select_item_in_inventory_event_handler)

    def _unregister_receivers(self):
        pass

    def _create_inventory(self, id, inventory_data):
        starting_inventory = self._create_starting_inventory(inventory_data)
        if("player_id" in id):
            self._player_id = str(id["player_id"])
            self._inventories.update({ self._player_id : starting_inventory })
        elif("monster_id" in id):
            self._monster_ids.append(id["monster_id"])
            monster_id = str(id["monster_id"])
            self._inventories.update({ monster_id : starting_inventory })
        elif("treasure_id" in id):
            self._treasure_ids.append(id["treasure_id"])
            chest_id = str(id["treasure_id"])
            self._inventories.update({ chest_id : starting_inventory })
        else:
            self._entity_ids.append(id)
            entity_id = str(id)
            self._inventories.update({ entity_id : starting_inventory })

    def _create_starting_inventory(self, inventory_data):
        starting_inventory = []

        for item_key in inventory_data:
            item = self._item_manager.item_from_key(item_key)
            starting_inventory.append(item)

        return starting_inventory

    def _show_inventory(self, id):
        print("------------------------------------------------------------------------\n")
        print("Here is your inventory:\n")
        element_number = 1
        # print(self._inventories) #DEBUG
        if(len(self._inventories[id]) == 0):
            print("Your inventory is empty.")
        else:
            for item in self._inventories[id]:
                    print(f"{element_number}" + ") - " + f"{item}")
                    element_number += 1

        print("\n------------------------------------------------------------------------\n")

    def _select_item(self, inventory_position, id):
        if(self._is_selected_item_in_inventory_range(inventory_position, id) == True):
            item = self._inventories[id][inventory_position]

            self._use_item(item, inventory_position)
        else:
            print("Please select a valid item")

    def _use_item(self, item, inventory_position):
        data = { "item": item, "inventory_position": inventory_position }
        self.event_dispatcher.dispatch(ItemEvent(ItemEvent.USE_ITEM_EVENT, data))

    def _remove_item(self, item, inventory_position, id):
        if(item.consumable == True):
            self._inventories[id].pop(inventory_position)
        else:
            raise Exception("Item is not consumable")

    def _is_selected_item_in_inventory_range(self, inventory_position, id):
        return (inventory_position < len(self._inventories[id]) - 1)

    def _handle_game_state_change(self, previous_state, new_state, data):
        # _initialize_inventory
        pass

    # event handlers

    def _create_inventory_event_handler(self, event):
        self._create_inventory(event.entity_id, event.inventory)

    def _add_item_to_inventory_event_handler(self, event):
        self._add_item_to_inventory(event.item)

    def _remove_item_from_inventory_event_handler(self, event):
        self._remove_item(event.item, event.inventory_position, self._player_id)

    def _select_item_in_inventory_event_handler(self, event):
        self._select_item(event.inventory_position, self._player_id)
