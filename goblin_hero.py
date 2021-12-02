# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#                                                                     #
#   _________    ________    ________    _           _    __      _   #
#  |  _______|  |  ____  |  |  ____  |  | |         | |  |  \    | |  #
#  | |          | |    | |  | |    | |  | |         | |  |   \   | |  #
#  | |  _____   | |    | |  | |____| |  | |         | |  | |\ \  | |  #
#  | | |___  |  | |    | |  |  ____ |   | |         | |  | | \ \ | |  #
#  | |     | |  | |    | |  | |    | |  | |         | |  | |  \ \| |  #
#  | |_____| |  | |____| |  | |____| |  | |______   | |  | |   \   |  #
#  |_________|  |________|  |________|  |________|  |_|  |_|    \__|  #
#                                                                     #
#            _       _    ________    ________    ________            #
#           | |     | |  |  ______|  |  ____  |  |  ____  |           #
#           | |     | |  | |         | |    | |  | |    | |           #
#           | |_____| |  | |______   | |____| |  | |    | |           #
#           |  _____  |  |  ______|  |  _    _|  | |    | |           #
#           | |     | |  | |         | | \  \    | |    | |           #
#           | |     | |  | |______   | |  \  \   | |____| |           #
#           |_|     |_|  |________|  |_|   \__\  |________|           #
#                                                                     #
#                                                                     #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                     #
# A modern 8-bit JRPG written from scratch with the PyGame library.   #
# Author: Jackie P, aka TheDataElemental.                       #
# Contact: TheDataElemental at gmail dot com.                         #
# Project started 3/29/2021.                                          #
#                                                                     #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


# Hide pygame monolog popup
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

# Import builtins, pygame, classes, data and functions
from functions import *


# Start title screen
# pygame.mixer.music.load("Assets/Exports/Music/OceanBiomeDoodle1.wav")
# pygame.mixer.music.play(-1)
# title_screen()

# Play prototype intro sequence
# screen.blit(black_screen,(0,0))
# prototype_intro_text = "It was a snowy night at the outskirts of " + \
# "Forever Forest..."
# scroll_text(prototype_intro_text, False, None, False)

# Play prototype gameplay music
# pygame.mixer.music.load("Assets/Exports/Music/SnowBiomeDoodle2b.wav")
# pygame.mixer.music.set_volume(0.25)
# pygame.mixer.music.play(-1)

# Debug toggle
render_walls = True

# Start gameplay
overworld()


# TODO:
# bosses talk during fights
# possibility to fail to run away
# possibility for player / monster to miss an attack
# system for monster to run away if player level is too high
# tweak for balance
# critical hit chance
# make sure window can be properly closed at any time during gameplay
