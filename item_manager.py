# the item manager.
import yaml
import player_manager
import event_manager
from models import item_model

_items = {}

# public methods
# create healing potion

def initialize():
    _load_items("data/items.yaml")


def item_from_key(key):
    global _items
    # print(f"_items_key = {_items[key]}")
    return _items[key]

# private methods

def _load_items(filename):
    with open(filename) as f:
        items = yaml.safe_load(f)

    _items.update(items)

# event handlers

def _use_item_event_handler(event_name, data):
    pass
