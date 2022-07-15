# constants

name = ""

from random import randint

player_hitpoints = 10
monster_hitpoints = 10

player_attack_power = 3
monster_attack_power = 3

player_defense = 1
monster_defense = 1

last_command = None
round = 0


# game commands

def user_name():
    global name
    while not name:
        name = input("What is your name: ").strip()

def quit():
    print(f"Farewell {name}")
    exit()


#player funtions.
def player_attack(input_string):
    global monster_hitpoints, player_attack_power

    print("you wanted to attack ... ")
    monster_hitpoints = monster_hitpoints - player_attack_power
    print(f"... you did {player_attack_power} points of damage")

    return True

def player_defend(input_string):
    global monster_attack_power

    if(monster_attack_power >= 3):
        monster_attack_power = monster_attack_power - player_defense

    print("you defend against the incomming attack")

    return True


#monster funtions
def monster_attack():
    global monster_attack_power, player_hitpoints

    player_hitpoints = player_hitpoints - monster_attack_power
    print(f"The monster has attacked you for {monster_attack_power} damage!")

def monster_defend():
    global player_attack_power, monster_hitpoints

    if(player_attack_power >= 3):
        player_attack_power = player_attack_power - monster_defense

    print("The monster defends against your attack!")

    return True

def monsters_action_chance():

    monster_action = randint(1, 4)

    if(monster_action <= 2):
        monster_attack()
    else:
        monster_defend()


#game functions
def is_someone_dead():
    global monster_hitpoints, player_hitpoints

    if(monster_hitpoints <= 0):
        print("You have slain the beast!")
        return True
    elif(player_hitpoints <= 0):
        print("You were slain by the beast!")
        return True
    else:
        return False

def parse_command(input_string):
    if(input_string == "quit"):
        return quit()
    elif(input_string == "attack"):
        return player_attack(input_string)
    elif(input_string == "defend"):
        return player_defend(input_string)
    else:
        print(f"{name} I don't understand your command")
        return False




#in the beginning


user_name()

while(is_someone_dead() == False):
    round = round + 1

    print(f"\n\nRound {round}: monster - {monster_hitpoints}, player - {player_hitpoints} - last command {last_command}")

    input_string = input("I await your command: ")

    monsters_action_chance()

    result = parse_command(input_string)
    if(result == True):
        last_command = input_string


    #when monster gets updated change this to any attack power decrease gets reset.
    if(monster_attack_power < 3):
        monster_attack_power = monster_attack_power + player_defense
    if(player_attack_power < 3):
        player_attack_power = player_attack_power + monster_defense
