#storage for now until i break the adventure game into modules.

player_hit_points = 10

def do_damage(original_hp, damage):
    print(f"original: {original_hp}")
    new_hp = original_hp - damage
    print(f"new hp: {new_hp}")
    return new_hp, True

player_hit_points, success = do_damage(player_hit_points, 3)

print(player_hit_points)
print(success)
