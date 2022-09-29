# the item manager.
import yaml
import player_manager
import event_manager
from models import item_model

_items = {}

# public methods

def initialize():
    _load_items("data/items.yaml")
    event_manager.listen(event_manager.TRIGGER_CONSUME_ITEM_EFFECT_EVENT, _trigger_item_effect_event_handler)

def item_from_key(key):
    global _items
    return _items[key]

# private methods

def _load_items(filename):
    with open(filename) as f:
        items = yaml.safe_load(f)

    _items.update(items["item_data"])

def _effects_parser(item_choice):
    # could take the list of available effects and just use that as a variable. but i would still need functions for the m so idk.
    effect = getattr(item_choice, "effect")

    for e in effect:
        if(e == "heal"):
            hp_amount = effect[e]
            _heal_user(hp_amount)
        elif(e == "damage"):
            damage_amount = effect[e]
            _damage_user(damage_amount)
        elif(e == "attack_damage"):
            ad_amount = effect[e]
            _increase_user_attack_damage(ad_amount)
        elif(e == "defense"):
            defense_amount = effect[e]
            _increase_user_defense(defense_amount)
        elif(e == "mana"):
            mana_amount = effect[e]
            _restore_user_mana(mana_amount)
        else:
            print("There is no effect for this item. This could be an error.")

def _heal_user(hp_amount):
    user = player_manager.get_player_data()
    max_hp = user["max_hit_points"]
    old_hp = user["hit_points"]
    new_hp = old_hp + hp_amount

    if(new_hp > max_hp):
        player_manager.change_player_data("hit_points", max_hp)
        print(f"{old_hp}, {max_hp}")
    else:
        player_manager.change_player_data("hit_points", new_hp)
        print(f"{old_hp}, {new_hp}")

def _damage_user(damage_amount):
    user = player_manager.get_player_data()
    hp = user["hit_points"]
    new_hp = hp - damage_amount
    return player_manager.change_player_data("hit_points", new_hp)

def _increase_user_attack_damage(ad_amount):
    print(ad_amount)

def _increase_user_defense(defense_amount):
    print(defense_amount)

def _restore_user_mana(mana_amount):
    print(mana_amount)

# event handlers

def _trigger_item_effect_event_handler(event_name, data):
    _effects_parser(data["item_choice"])
