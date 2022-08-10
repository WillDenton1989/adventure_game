#where the monsters are
from random import randint

def enemy_npc_choice():
    x = randint(1, 10)
    if(x <= 7):
        return "attack"
    else:
        return "defend"

def monster_generator():
    x = randint(1, 6)
    npc_orc = {
        "name": "Ugluk the Orc",
        "hit_points": 8,
        "attack_power": 5,
        "defense": 1,
        "defense_scalar": .5,
        "decision": None
    }
    npc_goblin = {
        "name": "Gilbert the Goblin",
        "hit_points": 10,
        "attack_power": 4,
        "defense": -5,
        "defense_scalar": .5,
        "decision": None
    }
    npc_uruk = {
        "name": "Lurtz the Uruk",
        "hit_points": 20,
        "attack_power": 7,
        "defense": -3,
        "defense_scalar": 1,
        "decision": None
    }
    npc_troll = {
        "name": "Bob the cave Troll",
        "hit_points": 50,
        "attack_power": 9,
        "defense": -15,
        "defense_scalar": 0,
        "decision": None
    }
    npc_bandit = {
        "name": "Bandit Fred the Dadfucker",
        "hit_points": 10,
        "attack_power": 5,
        "defense": 1,
        "defense_scalar": 1,
        "decision": None
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
    elif(monster["name"] == "Bandit Fred the Dadfucker"):
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
        "decision": None
    },
    "npc_goblin": {
        "name": "Gilbert the Goblin",
        "hit_points": 10,
        "attack_power": 4,
        "defense": -5,
        "defense_scalar": .5,
        "decision": None
    },
    "npc_uruk": {
        "name": "Lurtz the Uruk",
        "hit_points": 20,
        "attack_power": 7,
        "defense": -1,
        "defense_scalar": 1,
        "decision": None
    },
    "npc_troll": {
        "name": "Bob the cave Troll",
        "hit_points": 50,
        "attack_power": 9,
        "defense": -10,
        "defense_scalar": 0,
        "decision": None
    },
    "npc_bandit": {
        "name": "Bandit Fred the Dadfucker",
        "hit_points": 10,
        "attack_power": 5,
        "defense": 1,
        "defense_scalar": 1,
        "decision": None
    }
}
