# constants

name = ""

player_hitpoints = 10
monster_hitpoints = 10

player_attack_power = 2
monster_attack_power = 3

player_defense = 1


last_command = None

# game commands

def user_name():
    global name
    while not name:
        name = input("What is your name: ").strip()

def quit():
    print("Goodbye user")
    exit()

def player_attack(input_string):
    global monster_hitpoints, player_attack_power

    print("you wanted to attack ... ")
    monster_hitpoints = monster_hitpoints - player_attack_power
    print(f"... you did {player_attack_power} points of damage")

    return True

def defend(input_string):
    global monster_attack_power

    if monster_attack_power >= 3:
        monster_attack_power = monster_attack_power - player_defense

    print("you defend against the incomming attack")

    return True

def is_someone_dead():
    global monster_hitpoints, player_hitpoints

    if(monster_hitpoints <= 0):
        print("You killed the beast")
        return True
    elif(player_hitpoints <= 0):
        print("You were killed by the beast")
        return True
    else:
        return False

def monster_attack():
    global monster_attack_power, player_hitpoints

    player_hitpoints = player_hitpoints - monster_attack_power
    print(f"The monster has attacked you for {monster_attack_power} damage!")

def parse_command(input_string):
    if(input_string == "quit"):
        return quit()
    elif(input_string == "attack"):
        return player_attack(input_string)
    elif(input_string == "defend"):
        return defend(input_string)
    else:
        print(f"{name} I don't understand your command")
        return False

round = 0

#in the beginning


user_name()

while(is_someone_dead() == False):
    round = round + 1

    print(f"\n\nRound {round}: monster - {monster_hitpoints}, player - {player_hitpoints} - last command {last_command}")

    input_string = input("I await your command: ")

    result = parse_command(input_string)
    if(result == True):
        last_command = input_string

    monster_attack()
    #when monster gets updated change this to any attack power decrease gets reset.
    if(monster_attack_power < 3):
        monster_attack_power = monster_attack_power + player_defense
