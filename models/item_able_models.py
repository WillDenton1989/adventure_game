# where the item_ables live

class Consumable:
    """for consuming items"""

    def __init__(self):
        # uses/charges
        pass

    def consume_item():
        # using an item will also apply its effects, maybe that needs another method.
        pass

    def deduct_uses():
        pass

    pass

class Equipable:
    """for equiping items"""

    def __init__(self):
        # effects when equiped.
        # effects lost when un_equiped.
    pass

    def equip():
        pass

    def un_equip():
        pass

    pass

class Useable:
    """for using items"""

    def __init__(self):
        # effects when used.
    pass

    def use():
        pass

    def remove_use():
        pass

    pass

class Droppable:
    """for dropping items"""

    def __init__(self):
        # effects when used.
    pass

    def drop_item():
        pass

    def drop_number_of_item():
        pass

    pass
