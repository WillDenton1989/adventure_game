# the item manager.
import yaml
import player_manager
import event_manager
import game_manager
from models.item import Item
from models.effects.heal import Heal

_items = {}
_game_manager = None

# public methods

def initialize(game_manager):
    global _game_manager

    _load_items("data/items.yaml")
    event_manager.listen(event_manager.TRIGGER_CONSUME_ITEM_EFFECT_EVENT, _trigger_item_effect_event_handler)
    _game_manager = game_manager

def item_from_key(key):
    global _items
    return _items[key]

# private methods

def _load_items(filename):
    with open(filename) as f:
        items = yaml.safe_load(f)

    _items.update(items["item_data"])

def _execute_effects(item_choice):
    global _game_manager

    effects = item_choice.effects

    for effect_key in effects:
        if(effect_key == "heal"):
            max_heal = effects[effect_key]
            effect = Heal(max_heal, _game_manager)
            effect.execute()
        elif(effect_key == "damage"):
            damage_amount = effects[effect_key]
            _damage_user(damage_amount)
        elif(effect_key == "attack_damage"):
            ad_amount = effects[effect_key]
            _increase_user_attack_damage(ad_amount)
        elif(effect_key == "defense"):
            defense_amount = effects[effect_key]
            _increase_user_defense(defense_amount)
        elif(effect_key == "mana"):
            mana_amount = effects[effect_key]
            _restore_user_mana(mana_amount)
        else:
            print("There is no effect for this item. This could be an error.")

def _damage_user(damage_amount):
    user = _game_manager._player_manager.get_player_data
    hp = user["hit_points"]
    new_hp = hp - damage_amount
    return _game_manager._player_manager.update_player_data( {"hit_points" : new_hp} )

def _increase_user_attack_damage(ad_amount):
    print(ad_amount)

def _increase_user_defense(defense_amount):
    print(defense_amount)

def _restore_user_mana(mana_amount):
    print(mana_amount)

# event handlers

def _trigger_item_effect_event_handler(event_name, data):
    _execute_effects(data["item_choice"])
