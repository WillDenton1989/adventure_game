# where the item_ables live

class Consumable:
    """for consuming items"""

    def __init__(self):
        # uses/charges
        pass

    def consume_item(self):
        # using an item will also apply its effects, maybe that needs another method.
        pass

    def deduct_uses(self):
        pass

    pass

class Equipable:
    """for equiping items"""

    def __init__(self):
        # effects when equiped.
        # effects lost when un_equiped.
        pass

    def equip(self):
        pass

    def un_equip(self):
        pass

    pass

class Useable:
    """for using items"""

    def __init__(self):
        # effects when used.
    pass

    def use(self):
        pass

    def remove_use(self):
        pass

    pass

class Droppable:
    """for dropping items"""

    def __init__(self):
        # effects when used.
    pass

    def drop_item(self):
        pass

    def drop_number_of_item(self):
        pass

    pass
