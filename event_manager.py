#where the events live.
import yaml

BATTLE_EVENT = "battle_event"

event_listeners = []

def publish_event(event_name, data):
    for event_listener in event_listeners:
        if(event_listener["event_name"] == event_name):
            event_listener["callback"](event_name, data)

def listen(event_name, callback):
    event_listeners.append({ "event_name": event_name, "callback": callback })

def battle_event(player, monster):
    game_functions.battle(player, monster, game_functions.attack, game_functions.defend, game_parser.parse_player_input, monster_module.enemy_npc_choice, game_commands.quit)

def finsih_line_event(player, finsih_line, moves):
    print(f"\nCongratulations {player['name']}!\nIt took you {moves} moves to escape the bleak and terrible dungeon!\n")
    pass#break

def loot_chest_event(player, loot_chest):
    #print("\nGreat chest ahead. Sadly there is no loot here.\n") #eventually will trigger the looting event.
    pass
