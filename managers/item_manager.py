import yaml
import event_manager
from managers.manager_base import ManagerBase
from models.effects.heal import Heal
from models.item import Item

class ItemManager(ManagerBase):
    def __init__(self, game_manager):
        ManagerBase.__init__(self)
        self._game_manager = game_manager
        self._item_templates = self._load_items("data/items.yaml")

    # public methods

    def item_from_key(self, key):
        template = self._item_templates[key]
        return Item(template["display_name"], template["type"], template["effects"], template["weight"], template["value"], template["consumable"], template["equipable"])

    # private methods

    def _register_listeners(self):
        event_manager.listen(event_manager.TRIGGER_CONSUME_ITEM_EFFECT_EVENT, self._trigger_item_effect_event_handler)

    def _unregister_listeners(self):
        pass

    def _load_items(self, filename):
        item_templates = None
        with open(filename) as f:
            item_templates = yaml.safe_load(f)["item_data"]

        return item_templates

    def _execute_effects(self, item_choice):
        effects = item_choice.effects
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
        print(damage_amount)

    def _increase_user_attack_damage(self, ad_amount):
        print(ad_amount)

    def _increase_user_defense(self, defense_amount):
        print(defense_amount)

    def _restore_user_mana(self, mana_amount):
        print(mana_amount)

    def _handle_game_state_change(self, previous_state, new_state, data):
        pass
        
    # event handlers

    def _trigger_item_effect_event_handler(self, event_name, data):
        self._execute_effects(data["item_choice"])
