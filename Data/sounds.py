# sounds.py
# Load sounds to be used by Goblin Hero
# Author: Jackie P, aka TheDataElemental


import pygame
pygame.mixer.init()


# Load sounds
battle_win_sound = \
	pygame.mixer.Sound('Assets/Exports/Sound/battle_win_2.wav')
	
take_damage_sound = \
	pygame.mixer.Sound('Assets/Exports/Sound/take_damage.wav')
	
attack_sound = pygame.mixer.Sound('Assets/Exports/Sound/attack.wav')

monster_take_damage_sound = \
	pygame.mixer.Sound('Assets/Exports/Sound/monster_take_damage.wav')
	
monster_attack_sound = \
	pygame.mixer.Sound('Assets/Exports/Sound/monster_attack.wav')
	
monster_appears_sound = \
	pygame.mixer.Sound('Assets/Exports/Sound/monster_appears.wav')
	
footsteps_sound = \
	pygame.mixer.Sound('Assets/Exports/Sound/footsteps.wav')
	
game_over_sound = \
	pygame.mixer.Sound('Assets/Exports/Sound/game_over.wav')
	
death_sound = \
	pygame.mixer.Sound('Assets/Exports/Sound/death.wav')
	
the_end_sound = pygame.mixer.Sound('Assets/Exports/Sound/the_end.wav')

welcome_sound = pygame.mixer.Sound('Assets/Exports/Sound/welcome.wav')

these_items_sound = \
	pygame.mixer.Sound('Assets/Exports/Sound/we_have_these_items.wav')
	
not_enough_gold_sound = \
	pygame.mixer.Sound('Assets/Exports/Sound/not_enough_gold.wav')
	
good_luck_sound = \
	pygame.mixer.Sound('Assets/Exports/Sound/good_luck.wav')
	
splash_screen_sound = \
	pygame.mixer.Sound('Assets/Exports/Sound/data_robo.wav')
splash_screen_sound.set_volume(0.25)

open_start_menu_sound = \
	pygame.mixer.Sound('Assets/Exports/Sound/open_start_menu.wav')
open_start_menu_sound.set_volume(0.25)

speech_8_sound = pygame.mixer.Sound\
	("Assets/Exports/Sound/speech_8.wav")
	
speech_16_sound = pygame.mixer.Sound\
	("Assets/Exports/Sound/speech_16.wav")
	
speech_24_sound = pygame.mixer.Sound\
	("Assets/Exports/Sound/speech_24.wav")
	
speech_32_sound = pygame.mixer.Sound\
	("Assets/Exports/Sound/speech_32.wav")
