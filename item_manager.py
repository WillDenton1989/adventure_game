# the item manager.
import yaml
import player_manager

# public methods

def initialize():
    _load_player_inventory("data/items.yaml")

# private methods

def _load_player_inventory(filename):
    data = _load_items(filename)

    player_manager.update_player_inventory(data["player_inventory"])

def _load_items(filename):
    with open(filename) as f:
        items = yaml.safe_load(f)

    return items

def _use_item():
    pass

# event handlers
