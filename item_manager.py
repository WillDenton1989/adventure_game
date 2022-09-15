# the item manager.
import yaml
import player_manager
import event_manager

#fix this next time youre on this no longer works. make the items append into here like the level manager? use of items should def be event.
_items = {}

# public methods

def initialize():
    _load_items("data/items.yaml")
    event_manager.listen(event_manager.USE_ITEM_EVENT, _use_item_event_handler)

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
