# data.py
# Load and generate data for Goblin Hero
# Author: Jackie P, aka TheDataElemental


# Import pygame, instances, classes, sounds, images and text
from images import *
from text import *
from sounds import *


# Generate fonts
small_font = pygame.font.Font("Assets/NESfont.ttf", 12)
text_font = pygame.font.Font("Assets/NESfont.ttf", 14)
menu_font = pygame.font.Font("Assets/NESfont.ttf", 16)
big_font = pygame.font.Font("Assets/NESfont.ttf", 20)
huge_font = pygame.font.Font("Assets/NESfont.ttf", 22)

# Initialize conditions
cursor_pos_x = 0
cursor_pos_y = 0
dead_monsters = []
earned_exp = 0
earned_gold = 0
battle_step_counter = 0
LEVEL_CAPS = (20, 50, 90, 150, 230, 350, 500, 700, 999)
steps_taken_into_level = 0

# Set color values for text
BLACK = (0,0,0)
WHITE = (255,255,255) 	# Standard text
GREEN = (81,162,0)		# Poison Element
BLUE = (97,162,255)		# Ice Element
RED = (178,16,48) 		# Flame Element
BROWN = (195, 113,0) 	# Earth Element
YELLOW = (235,211,32) 	# Light Element
PURPLE = (146,65,243) 	# Dark Element

# Dict of colors for monster names by element
element_colors = {'POISON': GREEN,
	'FLAME': RED,
	'ICE': BLUE,
	'EARTH': BROWN,
	'LIGHT': YELLOW,
	'DARK': PURPLE}

# Variables for text scrolling system
total_chars = 0
current_text_row = 1
current_page = 1
text_x_pos = 20
text_y_pos = 380
text_row_y_values = (380,400,420)

clock = pygame.time.Clock()
FPS = 60

# Overworld starting position
world_x = -256
world_y = -608

# Player position at center of screen
player_x = 224
player_y = 224

# Generate static text messages
fight_text = big_font.render('FIGHT', True, WHITE)
run_text = big_font.render('RUN', True, WHITE)
attack_text = big_font.render('ATTACK', True, WHITE)
item_text = big_font.render('ITEM', True, WHITE)
spell_text = big_font.render('SPELL', True, WHITE)
guard_text = big_font.render('GUARD', True, WHITE)

# Define command menu items
gear_menu_text = menu_font.render("GEAR", True, WHITE)
magic_menu_text = menu_font.render("MAGIC", True, WHITE)
map_menu_text = menu_font.render("MAP", True, WHITE)
stats_menu_text = menu_font.render("STATS", True, WHITE)
system_menu_text = menu_font.render("SYSTEM", True, WHITE)
exit_menu_text = menu_font.render("EXIT", True, WHITE)


# Code to allow player to close game window
# while True:
# 	events = pygame.event.get()
# 	for event in events:
# 		# Close game window
# 		if event.type == pygame.QUIT:
# 			sys.exit()
# 		pygame.display.flip()
