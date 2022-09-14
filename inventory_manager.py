#where the inventory lives
import player_manager

# loot_chest = {}

player_inventory = {
    "space_1": None,
    "space_2": None,
    "space_3": None,
    "space_4": None,
    "space_5": None
 }

def display_inventory(inventory):
    print(f"""    1) -{inventory['space_1']}
    2) -{inventory['space_2']}
    3) -{inventory['space_3']}
    4) -{inventory['space_4']}
    5) -{inventory['space_5']}""")

    # inventory_input = input("\nPress the number of the corresponding item you wish to access.(1-5)\n")
    # print(type(inventory_input))

def display_inventory_screen(inventory, character):
    while(True):
        display_inventory(inventory, character)
        

#display_inventory_screen(player_inventory, get_player_data())
