# this is where the item model shall live.

class Item:
    """builds the basics for items"""

    # type
    type = ["junk", "consumable", "weapon", "armor", "treasure", "gun"]

    # this is just the constructor, fml
    def __init__(self, display_name = None, type = 0, effect = None, weight = 1, value = 1, consumable = False, equipable = False):
        self.display_name = display_name
        self.type = type
        self.effect = effect
        self.weight = weight
        self.value = value
        self.consumable = consumable
        self.equipable = equipable


    def __str__(self):
        return f"{self.display_name}"

    def use_item(self):

        pass

    pass
