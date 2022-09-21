# the item manager.
import yaml
import player_manager
import event_manager

_items = {}

class Item:
    """builds the basics for items"""

    def __init__(self, name, display_name, type, effects, value):
        pass

    def drop_item():
        pass

    def use_item():
        pass
    pass
    
# public methods

def initialize():
    _load_items("data/items.yaml")

def item_from_key(key):
    global _items
    return _items[key]

# private methods

def _load_items(filename):
    with open(filename) as f:
        items = yaml.safe_load(f)

    _items.update(items)

# event handlers

def _use_item_event_handler(event_name, data):
    pass
