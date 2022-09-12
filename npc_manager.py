#where the npcs are
from random import randint

def enemy_npc_choice():
    x = randint(1, 10)
    if(x <= 7):
        return "attack"
    else:
        return "defend"

def name_generator(type):
    y = 0# randint(0, 3)
    x = randint(0, 15)
    names = [
    "Bob",
    "Joe",
    "Jeff",
    "Bren",
    "Mike",
    "Dennis",
    "Tupok",
    "Biggie",
    "Huell",
    "Jerry",
    "Scott",
    "Clarence",
    "Dan",
    "Gary",
    "Kyle",
    "Theo"
    ]

    dwarf_names = [
        "Dain",
        "Gimli",
        "Kirk",
        "Scotty"
    ]

    if(type == "goblin"):
        return names[x]
    elif(type == "dwarf"):
        return dwarf_names[y]
    else:
        return names[x]

def monster_generator():
    x = randint(1, 6)
    npc_orc = {
        "name": "Ugluk the Orc",
        "hit_points": 8,
        "attack_power": 5,
        "defense": 1,
        "defense_scalar": .5,
        "battle_decision": None,
        "column": 8,
        "row": 8,
        "symbol": "O"
    }
    npc_goblin = {
        "name": "Gilbert the Goblin",
        "hit_points": 10,
        "attack_power": 4,
        "defense": -5,
        "defense_scalar": .5,
        "battle_decision": None,
        "column": 4,
        "row": 2,
        "symbol": "G"
    }
    npc_uruk = {
        "name": "Lurtz the Uruk",
        "hit_points": 20,
        "attack_power": 7,
        "defense": -3,
        "defense_scalar": 1,
        "battle_decision": None,
        "column": 8,
        "row": 1,
        "symbol": "U"
    }
    npc_troll = {
        "name": "Bob the cave Troll",
        "hit_points": 50,
        "attack_power": 9,
        "defense": -15,
        "defense_scalar": 0,
        "battle_decision": None,
        "column": 1,
        "row": 8,
        "symbol": "T"
    }
    npc_bandit = {
        "name": "Fred the Bandit",
        "hit_points": 10,
        "attack_power": 5,
        "defense": 1,
        "defense_scalar": 1,
        "battle_decision": None,
        "column": 6,
        "row": 6,
        "symbol": "B"
    }
    if(x == 1):
        return npc_orc
    elif(x == 2):
        return npc_goblin
    elif(x == 3):
        return npc_uruk
    elif(x == 4):
        return npc_troll
    else:
        return npc_bandit

def monster_catchphrase_generator(monster):
    print("\nAs your foe engages you in glorious combat they cry out...")
    if(monster["name"] == "Mike the goblin"):
        print("I'm a goblin? Why not something cool like an Elf?")
    elif(monster["name"] == "Gary the goblin"):
        print("It's Gary UwU XD")
    elif(monster["name"] == "Scott the goblin"):
        print("Is that 'THE' father linux?")
    else:
        print("We battle to the death!!")

enemies_dict = {
    "npc_orc": {
        "name": "Ugluk the Orc",
        "hit_points": 8,
        "attack_power": 5,
        "defense": 1,
        "defense_scalar": .5,
        "battle_decision": None,
        "column": 8,
        "row": 8,
        "symbol": "O"
    },
    "npc_goblin": {
        "name": "Gilbert the Goblin",
        "hit_points": 10,
        "attack_power": 4,
        "defense": -5,
        "defense_scalar": .5,
        "battle_decision": None,
        "column": 2,
        "row": 2,
        "symbol": "G"
    },
    "npc_uruk": {
        "name": "Lurtz the Uruk",
        "hit_points": 20,
        "attack_power": 7,
        "defense": -1,
        "defense_scalar": 1,
        "battle_decision": None,
        "column": 8,
        "row": 1,
        "symbol": "U"
    },
    "npc_troll": {
        "name": "Bob the cave Troll",
        "hit_points": 50,
        "attack_power": 9,
        "defense": -10,
        "defense_scalar": 0,
        "battle_decision": None,
        "column": 1,
        "row": 8,
        "symbol": "T"
    },
    "npc_bandit": {
        "name": "Fred the Bandit",
        "hit_points": 10,
        "attack_power": 5,
        "defense": 1,
        "defense_scalar": 1,
        "battle_decision": None,
        "column": 5,
        "row": 5,
        "symbol": "B"
    }
}
