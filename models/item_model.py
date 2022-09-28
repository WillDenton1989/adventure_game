# this is where the item model shall live.

class Item:
    """builds the basics for items"""

    # type
    type = ["junk", "weapon", "armor", "equipment"]
    # category = ["junk", "consumable", "equipment"]

    # this is just the constructor, fml
    def __init__(self, display_name = None, weight = 1, type = 0, value = 1, consumable = False):
        self.display_name = display_name
        self.weight = weight
        self.type = type
        self.consumable = consumable

    def __str__(self):
        return f"{self.display_name}"

    def use_item(self, category):

        pass

    pass
