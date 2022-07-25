# constants

from random import randint

name = None

player_hit_points = 15
monster_hit_points = 14

player_attack_power = randint(1, 4)
monster_attack_power = randint(2, 4)

player_input_string = None
round = 0

# game commands

def user_name():
    name = input("So tell me your name and your adventure shall begin!\n").strip()

    if name == "quit":
        exit()
    elif name == "Bill":
        print("\nWhats up homie :D")
    elif name == "Mike":
        print("\nThe master returns!")
    elif name == "Scott":
        print("\nIt's you! great...")
    elif name == "Gary":
        print("\nOwO it's Gary! UwU xD")
    elif name == "motherfucker":
        print("\nWhat aint no country i ever heard of. they speak english in what?")
    elif name == "boobs":
        print("\nMmmmmmm those are nice")
    else:
        print("\nHeh funny name.")
    return name

def quit():
    print(f"Farewell {name}")
    exit()

def controls():
    print("""\nType 'attack' or 'a' to try to damage the monster;
Type 'defend' or 'd' to try to defend against an attack;
Type 'quit' or 'q' to exit the adventure game.\n""")

#player funtions.

def player_command(player_input_string):

    if(player_input_string == "quit" or player_input_string == "q"):
        return quit()
    elif(player_input_string == "attack" or player_input_string == "a"):
        return basic_attack(monster_hit_points, player_attack_power)
    elif(player_input_string == "defend" or player_input_string == "d"):
        return basic_defend(monster_attack_power)
    else:
        print(f"{name} I don't understand your command")
    return False

#monster funtions

def monsters_action_chance():
    x = randint(1, 10)
    if(x <= 6):
        return 1
    else:
        return 2

def monster_command():
    if(monsters_action_chance() == 1):
        return basic_attack(player_hit_points, monster_attack_power)
    elif(monsters_action_chance() == 2):
        return basic_defend(player_attack_power)

#game functions

def is_someone_dead():

    if(monster_hit_points <= 0):
        print(f"{name} has slain the beast!")
        return True
    elif(player_hit_points <= 0):
        print(f"{name} has been slain by the beast!")
        return True
    else:
        return False

def basic_attack(original_hp, attack_damage):

    new_hp = original_hp - attack_damage

    return new_hp

def basic_defend(attack_damage):

    new_attack_damage = attack_damage % 2

    return new_attack_damage



#the actual code begins here. good luck

print("Welcome intrepid adventurer! \n\nThis is the Adventure Game!(working title, dont laugh)\n\n")
name = user_name()
print(f"\nAlright {name}. lets go!")

while(is_someone_dead() == False):

    round = round + 1
    #gather human input
    print(f"\n\nRound {round}: monster - {monster_hit_points}, player - {player_hit_points} - last command {player_input_string}")
    controls()
    player_input_string = input(f"I await your command {name}: ")

    #gather ai input
    #monsters_action_chance()

    #use combined inputs

    if(monster_command() == basic_attack(player_hit_points, monster_attack_power)):
        player_hit_points = monster_command()
        print(f"You have taken {monster_attack_power} damage!")

    if(player_command(player_input_string) == basic_attack(monster_hit_points, player_attack_power)):
        monster_hit_points = player_command(player_input_string)
        print(f"You have damaged the monster for {player_attack_power}!")



    player_attack_power = randint(1, 4)
    monster_attack_power = randint(2, 4)


print(f"\n\n{name} has finished the Adventure! So far...")
#this may or may not be the end?
