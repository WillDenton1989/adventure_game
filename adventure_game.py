#!python3

from managers.game_manager import GameManager

def game_intro_message():
    print("\nWelcome intrepid adventurer! \n\nThis is the Adventure Game!(working title, dont laugh)\n\n")

# the cool running

game_intro_message()

GAME_MANAGER = GameManager()

GAME_MANAGER.start()

# is this the end?
