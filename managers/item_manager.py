import yaml
# from playsound import playsound

from managers.manager_base import ManagerBase

from models.effects.attack_power import AttackPower
from models.effects.damage import Damage
from models.effects.defense import Defense
from models.effects.heal import Heal
from models.events.inventory_event import InventoryEvent
from models.events.item_event import ItemEvent
from models.item import Item

class ItemManager(ManagerBase):
    def __init__(self, event_dispatcher, game_manager):
        ManagerBase.__init__(self, event_dispatcher)

        self._game_manager = game_manager
        self._item_templates = self._load_item_templates("data/game_data/items.yaml") # DEBUG FILE location

    def start(self):
        pass

    def process(self):
        pass

    # public methods

    def item_from_key(self, key):
        template = self._item_templates[key]
        return Item(template)

    # private methods

    def _register_receivers(self):
        self.event_dispatcher.receive(ItemEvent.USE_ITEM_EVENT, self._use_item_event_handler)
        self.event_dispatcher.receive(ItemEvent.EQUIP_ITEM_EVENT, self._equip_item_event_handler)
        self.event_dispatcher.receive(ItemEvent.UNEQUIP_ITEM_EVENT, self._unequip_item_event_handler)

    def _unregister_receivers(self):
        pass

    def _load_item_templates(self, filename):
        item_templates = None
        with open(filename) as f:
            item_templates = yaml.safe_load(f)["item_data"]

        return item_templates

    def _use_item_effect(self, item, inventory_position):
        self._execute_effects(item.effects)
        if(item.consumable == True):
            data = { "item": item, "inventory_position": inventory_position }
            self.event_dispatcher.dispatch(InventoryEvent(InventoryEvent.REMOVE_ITEM_FROM_INVENTORY_EVENT, data))

    def _execute_equiped_item_stat_modifier(self, item):
        if(item.equiped == True):
            item_id = id(item)
            self._game_manager.player.add_modifier(item_id, item.modifier, item.modifier_value)

    def _remove_equiped_item_stat_modifier(self, item):
        if(item.equiped == False):
            item_id = id(item)
            self._game_manager.player.remove_modifier(item_id)

    def _execute_effects(self, effects):
        if(effects == None): return

        for effect_key in effects:
            if(effect_key == "heal"):
                max_heal = effects[effect_key]
                effect = Heal(max_heal, self._game_manager)
                effect.execute()
            elif(effect_key == "damage"):
                max_damage = effects[effect_key]
                effect = Damage(max_damage, self._game_manager)
                effect.execute()
            elif(effect_key == "attack_damage"):
                max_attack_power = effects[effect_key]
                effect = AttackPower(max_attack_power, self._game_manager)
                effect.execute()
            elif(effect_key == "defense"):
                max_defense = effects[effect_key]
                effect = Defense(max_defense, self._game_manager)
                effect.execute()
            else:
                print("There is no effect for this item. This could be an error.")

    def _handle_game_state_change(self, previous_state, new_state, data):
        pass

    # event handlers

    def _equip_item_event_handler(self, event):
        self._execute_equiped_item_stat_modifier(event.item)

    def _unequip_item_event_handler(self, event):
        self._remove_equiped_item_stat_modifier(event.item)

    def _use_item_event_handler(self, event):
        self._use_item_effect(event.item, event.inventory_position)
