# here is where the inventory models shall live!

class Inventory:
    """this will build a basic inventory"""

    def __init__(self):
        self.inventory_list = []

    def add_item(self, item):
        self.inventory_list.append(item)

    # def __str__(self):
    #     for item in items:
    #         print(f"{item}")
