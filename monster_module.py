#where the monsters are
from random import randint

#GL = 43961
GL = 9785
BN = 9792
DW = 9786

npc_goblin = {
    "name": "Gilbert the Goblin",
    "hit_points": 5,
    "attack_power": 4,
    "defense": 0,
    "defense_scalar": .5,
    "speed": 6,
    "battle_decision": None,
    "column": 2,
    "row": 2,
    "symbol": chr(GL)
}

npc_bandit = {
    "name": "Fred the Bandit",
    "hit_points": 10,
    "attack_power": 5,
    "defense": 1,
    "defense_scalar": 1,
    "speed": 5,
    "battle_decision": None,
    "column": 6,
    "row": 5,
    "symbol": chr(BN)
}

npc_dwarf = {
    "name": "Dain the Dwarf",
    "hit_points": 15,
    "attack_power": 5,
    "defense": 0,
    "defense_scalar": 1,
    "speed": 3,
    "battle_decision": None,
    "column": 10,
    "row": 1,
    "symbol": chr(DW)
}

def enemy_npc_choice():
    x = randint(1, 10)
    if(x <= 7):
        return "attack"
    else:
        return "defend"

def npc_battle_choice():
    x = randint(1, 100)
    if(x <= 50):
        return "normal_attack"
    elif(x > 50 and x <= 70):
        return "special_attack"
    else:
        return "guard"

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
    if(monster["name"] == "Ugluk the Orc"):
        print("Looks like meat's back on the menu boys!")
    elif(monster["name"] == "Lurtz the Uruk"):
        print("Have you seen a pair of Hobbits nearby?")
    elif(monster["name"] == "Bob the cave Troll"):
        print("Ugh. its a cave Troll")
    elif(monster["name"] == "Gilbert the Goblin"):
        print("Reeeeeeee!")
    elif(monster["name"] == "Fred the Bandit"):
        print("You're not a dad by any chance?")
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
