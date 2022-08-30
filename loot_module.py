#where the loot lives
import game_commands
import game_parser

#CH = 9812
CH = 9691

loot_chest = {
    "symbol": chr(CH)
}

player_inventory = {
    "space_1": None,
    "space_2": None,
    "space_3": None,
    "space_4": None,
    "space_5": None
 }

def display_inventory(inventory, character):
    print(f"Hey {character['name']}, This is your stuff:")
    print(f"""    1) -{player_inventory['space_1']}
    2) -{player_inventory['space_2']}
    3) -{player_inventory['space_3']}
    4) -{player_inventory['space_4']}
    5) -{player_inventory['space_5']}""")

    inventory_input = input("\nPress the number of the corresponding item you wish to access.(1-5)\n")
    print(type(inventory_input))

def display_inventory_screen(inventory, character):
    while(True):
        display_inventory(inventory, character)
        break

#display_inventory_screen(player_inventory, game_commands.player)
