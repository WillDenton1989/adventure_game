#storage for now until i break the adventure game into modules.

def do_damage(original_hp, damage):
    print(f"original: {original_hp}")
    new_hp = original_hp - damage
    print(f"new hp: {new_hp}")
    return new_hp, True

player_hit_points, success = do_damage(player_hit_points, 3)

print(player_hit_points)
print(success)

if(player_command(player_input_string) == basic_defend(monster_attack_power)):
    monster_attack_power, success = basic_defend(monster_attack_power)
    print("you defend againt the monster!")

if(monsters_action_chance() == basic_attack(player_hit_points, monster_attack_power)):
        player_hit_points, success = basic_attack(player_hit_points, monster_attack_power)
        print("the monster attacks!")

if(monsters_action_chance() == basic_defend(player_attack_power)):
    player_attack_power, success = basic_defend(player_attack_power)
    print("the monster defends against your attack!")

if(player_command(player_input_string) == basic_attack(monster_hit_points, player_attack_power)):
    monster_hit_points, success = basic_attack(monster_hit_points, player_attack_power)
    print("you attack the monster!")


player_attack_power = randint(1, 5)
monster_attack_power = randint(2, 4)
