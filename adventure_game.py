# constants

from random import randint

name = ""

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
        name = input("So tell me your name and your adventure shall begin!\n").strip()
        if name == "quit":
            exit()
        elif name == "Bill":
            print("\nWhats up homie :D")
        elif name == "mike":
            print("\nThe master returns!")
        elif name == "scott":
            print("\nIt you! great...")

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

#def player_attack_power():
    #player_attack = randint(1, 5)


#monster funtions
def monster_attack():
    global player_hitpoints

    player_hitpoints = player_hitpoints - monster_attack_power

    print(f"The monster has attacked you for {monster_attack_power} damage!")

def monster_defend():
    global player_attack_power, monster_hitpoints

    if(player_attack_power >= 3):
        player_attack_power = player_attack_power - monster_defense

    print("The monster defends against your attack!")

    return True

#def monster_attack_power():
#       monster_attack = randint(2, 6)

def monsters_action_chance():

    monster_action = randint(1, 10)

    if(monster_action <= 7):
        monster_attack()
    else:
        monster_defend()


#game functions
def is_someone_dead():
    global monster_hitpoints, player_hitpoints

    if(monster_hitpoints <= 0):
        print(f"{name} has slain the beast!")
        return True
    elif(player_hitpoints <= 0):
        print(f"{name} has been slain by the beast!")
        return True
    else:
        return False

def player_command(input_string):
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

print("Welcome intrepid adventurer! \nThis is the Adventure Game!(working title, dont laugh)")

user_name()

while(is_someone_dead() == False):
    round = round + 1

    print(f"\n\nRound {round}: monster - {monster_hitpoints}, player - {player_hitpoints} - last command {last_command}")

    input_string = input("I await your command: ")

    monsters_action_chance()

    result = player_command(input_string)

    if(result == True):
        last_command = input_string


    #when monster gets updated change this to any attack power decrease gets reset.
    if(monster_attack_power < 3):
        monster_attack_power = monster_attack_power + player_defense
    if(player_attack_power < 3):
        player_attack_power = player_attack_power + monster_defense
