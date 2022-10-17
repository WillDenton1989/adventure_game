import yaml

from managers.manager_base import ManagerBase

from models.effects.heal import Heal
from models.events.inventory_event import InventoryEvent
from models.events.item_event import ItemEvent
from models.item import Item

class ItemManager(ManagerBase):
    def __init__(self, event_dispatcher, game_manager):
        ManagerBase.__init__(self, event_dispatcher)

        self._game_manager = game_manager
        self._item_templates = self._load_item_templates("data/items.yaml")

    def start(self):
        pass

    def process(self):
        pass

    # public methods

    def item_from_key(self, key):
        template = self._item_templates[key]
        return Item(template["display_name"], template["type"], template["effects"], template["weight"], template["value"], template["consumable"], template["equipable"])

    # private methods

    def _register_receivers(self):
        self.event_dispatcher.receive(ItemEvent.USE_ITEM_EVENT, self._use_item_event_handler)


    def _unregister_receivers(self):
        pass

    def _load_item_templates(self, filename):
        item_templates = None
        with open(filename) as f:
            item_templates = yaml.safe_load(f)["item_data"]

        return item_templates

    def _use_item(self, item, inventory_position):
        self._execute_effects(item.effects)
        if(item.consumable == True):
            data = { "item": item, "inventory_position": inventory_position }
            self.event_dispatcher.dispatch(InventoryEvent(InventoryEvent.REMOVE_ITEM_FROM_INVENTORY_EVENT, data))

    def _execute_effects(self, effects):
        if(effects == None): return

        for effect_key in effects:
            if(effect_key == "heal"):
                max_heal = effects[effect_key]
                effect = Heal(max_heal, self._game_manager)
                effect.execute()
            elif(effect_key == "damage"):
                damage_amount = effects[effect_key]
                self._damage_user(damage_amount)
            elif(effect_key == "attack_damage"):
                ad_amount = effects[effect_key]
                self._increase_user_attack_damage(ad_amount)
            elif(effect_key == "defense"):
                defense_amount = effects[effect_key]
                self._increase_user_defense(defense_amount)
            elif(effect_key == "mana"):
                mana_amount = effects[effect_key]
                self._restore_user_mana(mana_amount)
            else:
                print("There is no effect for this item. This could be an error.")

    def _damage_user(self, damage_amount):
        print(f"Damage amount: {damage_amount}")

    def _increase_user_attack_damage(self, ad_amount):
        print(f"Attack damage amount: {ad_amount}")

    def _increase_user_defense(self, defense_amount):
        print(f"Defense amount: {defense_amount}")

    def _restore_user_mana(self, mana_amount):
        print(f"Mana amount: {mana_amount}")

    def _handle_game_state_change(self, previous_state, new_state, data):
        pass

    # event handlers

    def _use_item_event_handler(self, event):
        self._use_item(event.item, event.inventory_position)
