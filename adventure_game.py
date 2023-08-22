#!python3

from managers.game_manager import GameManager

# Runs the game

GAME_MANAGER = GameManager()
GameManager.game_intro_message()
GAME_MANAGER.start()
