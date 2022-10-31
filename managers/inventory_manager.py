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

    def start(self):
        pass

    def process(self):
        if(self.game_state == State.STATE_INVENTORY):
            self._show_inventory(self._player_id)
        elif(self.game_state == State.STATE_LOOT):
            self._show_inventory(self._player_id)
            self._inspect_entities_inventory(self._lootable_entity_id)

    # private methods

    def _register_receivers(self):
        self.event_dispatcher.receive(InventoryEvent.CREATE_INVENTORY_EVENT, self._create_inventory_event_handler)
        self.event_dispatcher.receive(InventoryEvent.LOOT_ITEM_IN_INVENTORY_EVENT, self._select_entities_item_event_handler)
        self.event_dispatcher.receive(InventoryEvent.SORT_INVENTORY_EVENT, self._sort_inventory_event_handler)

        self.event_dispatcher.receive(InventoryEvent.REMOVE_ITEM_FROM_INVENTORY_EVENT, self._remove_item_from_inventory_event_handler)
        self.event_dispatcher.receive(InventoryEvent.SELECT_ITEM_IN_INVENTORY_EVENT, self._select_item_in_inventory_event_handler)

    def _unregister_receivers(self):
        pass

    def _initialize_loot_event(self, lootable_entity):
        self._lootable_entity = lootable_entity
        entity_id = id(lootable_entity)
        self._lootable_entity_id = str(entity_id)

    def _create_inventory(self, id, inventory_data):
        starting_inventory = self._create_starting_inventory(inventory_data)
        if("player_id" in id):
            self._player_id = str(id["player_id"])
            self._inventories.update({ self._player_id : starting_inventory })
        elif("monster_id" in id):
            monster_id = str(id["monster_id"])
            self._inventories.update({ monster_id : starting_inventory })
        elif("treasure_id" in id):
            chest_id = str(id["treasure_id"])
            self._inventories.update({ chest_id : starting_inventory })
        else:
            raise Exception(f"Issue with creating an inventory for this entity ID: {id}, Inventory data: {inventory_data}")

    def _create_starting_inventory(self, inventory_data):
        starting_inventory = []
        if(inventory_data == None): return starting_inventory

        for item_key in inventory_data:
            item = self._item_manager.item_from_key(item_key)
            starting_inventory.append(item)

        return starting_inventory

    def _inspect_entities_inventory(self, lootable_entity):
        self._show_inventory(lootable_entity)

    def _show_inventory(self, id):
        print("------------------------------------------------------------------------\n")
        element_number = 1

        if(id == self._player_id):
            print("Here is your inventory:\n")
        else:
            print("These are the items you find:\n")

        if(len(self._inventories[id]) == 0):
            if(id == self._player_id):
                print("Your inventory is empty.")
            else:
                print("This inventory is empty.")
        else:
            for item in self._inventories[id]:
                    print(f"{element_number}" + ") - " + f"{item}")
                    element_number += 1

        print("\n------------------------------------------------------------------------\n")

    def _select_item(self, inventory_position, id):
        if(self._is_selected_item_in_inventory_range(inventory_position, id) == True):
            item = self._inventories[id][inventory_position]
            if(item.consumable == True):
                self._use_item(item, inventory_position)
            elif(item.equipable == True):
                if(item.equiped == False):
                    self._equip_item(item, inventory_position)
                elif(item.equiped == True):
                    self._unequip_item(item, inventory_position)
                else:
                    raise Exception("Issue with equipment in select item.")
            else:
                print("This item is neither consumable nor equipable.")
        else:
            print("Please select a valid item")

    def _use_item(self, item, inventory_position):
        print(f"You consume {item}")
        data = { "item": item, "inventory_position": inventory_position }
        self.event_dispatcher.dispatch(ItemEvent(ItemEvent.USE_ITEM_EVENT, data))

    def _equip_item(self, item, inventory_position):
        print(f"You equiped: {item}")
        item.equiped = True

        data = { "item": item }
        self.event_dispatcher.dispatch(ItemEvent(ItemEvent.EQUIP_ITEM_EVENT, data))

    def _unequip_item(self, item, inventory_position):
        item.equiped = False
        print(f"You un-equiped: {item}")

        data = { "item": item }
        self.event_dispatcher.dispatch(ItemEvent(ItemEvent.UNEQUIP_ITEM_EVENT, data))

    def _remove_item(self, item, inventory_position, id):
        if(item.consumable == True):
            self._inventories[id].pop(inventory_position)
        else:
            raise Exception("Item is not consumable")

    def _is_selected_item_in_inventory_range(self, inventory_position, id):
        return (inventory_position < len(self._inventories[id]))

    def _select_entities_item(self, inventory_position, id):
        if(self._is_selected_item_in_inventory_range(inventory_position, id) == True):
            item = self._inventories[id][inventory_position]

            self._take_selected_item(id, self._player_id, inventory_position, item)
        else:
            print("Please select a valid item")

    def _take_selected_item(self, entity_id, player_id, inventory_position, item):
        self._inventories[player_id].append(item)
        self._inventories[entity_id].pop(inventory_position)

    def _store_selected_item(self):
        pass

<<<<<<< HEAD
    def _sort_player_inventory(self, id):
        self._inventories[id].sort(reverse=True, key=lambda x: x.display_name)

=======
>>>>>>> a99a85f (adds loot events)
    def _handle_game_state_change(self, previous_state, new_state, data):
        if(data["new_state"] == State.STATE_LOOT):
            self._initialize_loot_event(data["event_data"])

    # event handlers

    def _create_inventory_event_handler(self, event):
        self._create_inventory(event.entity_id, event.inventory)

    def _select_item_in_inventory_event_handler(self, event):
        self._select_item(event.inventory_position, self._player_id)

    def _remove_item_from_inventory_event_handler(self, event):
        self._remove_item(event.item, event.inventory_position, self._player_id)

<<<<<<< HEAD
    def _sort_inventory_event_handler(self, _event):
        self._sort_player_inventory(self._player_id)

    def _select_entities_item_event_handler(self, event):
        self._select_entities_item(event.inventory_position, self._lootable_entity_id)
=======
    def _select_entities_item_event_handler(self, event):
        self._select_entities_item(event.inventory_position, self._lootable_entity)
>>>>>>> a99a85f (adds loot events)
